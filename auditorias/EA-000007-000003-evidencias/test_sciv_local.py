"""Offline fixtures for the exact local provisioning surface; no real mailbox IO."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import sciv_local as local


class ProvisionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "fixture"
        self.stage = self.base / "stage"
        self.root.mkdir()
        self.stage.mkdir()
        self.original = b"original\r\n"
        self.entries = []
        for relative in sorted(local.PATHS):
            data = b"disabled fixture\n"
            dest = self.stage / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            old = None
            if relative == local.ADAPTER:
                target = self.root / relative
                target.parent.mkdir(parents=True)
                target.write_bytes(self.original)
                old = local.digest(self.original)
            self.entries.append({"path": relative, "old_sha256": old,
                                 "new_sha256": local.digest(data)})
        raw = json.dumps({"base_commit": local.BASE, "files": self.entries}).encode()
        (self.stage / "manifest.json").write_bytes(raw)
        self.sha = local.digest(raw)
        def git(root, *args):
            if args[0] == "branch":
                return b"main\n"
            if args[0] == "remote":
                return b"https://github.com/thiagoba2004/conselhos-profissionais.git\n"
            return (local.BASE + "\n").encode()
        self.mock = patch.object(local, "git", side_effect=git)
        self.mock.start()
        self.addCleanup(self.mock.stop)

    def apply(self, **kwargs):
        return local.apply(self.root, self.stage, self.sha, **kwargs)

    def test_apply_and_retry_idempotent(self):
        self.assertEqual(self.apply()["writes"], 6)
        self.assertEqual(self.apply()["writes"], 0)

    def test_partial_interruption_reconciles_without_overwrite(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            with self.assertRaisesRegex(RuntimeError, "INTERRUPTION"):
                self.apply(fail_after=2)
        self.assertEqual(json.loads(output.getvalue())["status"], "PARTIALLY_APPLIED")
        self.assertEqual(self.apply()["writes"], 4)
        self.assertEqual(self.apply()["writes"], 0)

    def test_divergence_denies_before_first_write(self):
        (self.root / local.ADAPTER).write_bytes(b"third-party")
        with self.assertRaisesRegex(ValueError, "OLD_BYTES"):
            self.apply()
        self.assertFalse((self.root / "comunicados").exists())

    def test_stage_corruption_denied(self):
        (self.stage / local.ADAPTER).write_bytes(b"corrupt")
        with self.assertRaisesRegex(ValueError, "STAGE_CHANGED"):
            self.apply()
        self.assertEqual((self.root / local.ADAPTER).read_bytes(), self.original)

    def test_manifest_corruption_denied(self):
        (self.stage / "manifest.json").write_bytes(b"{}")
        with self.assertRaisesRegex(ValueError, "MANIFEST_CHANGED"):
            self.apply()

    def test_unexpected_environment_denied(self):
        for answer in (b"unexpected head", b"unexpected branch", b"unexpected repo"):
            with self.subTest(answer=answer), patch.object(local, "git", return_value=answer):
                with self.assertRaisesRegex(ValueError, "UNEXPECTED_ENVIRONMENT"):
                    self.apply()

    def test_traversal_absolute_unknown_paths_denied(self):
        for path in ("../escape", "/escape", "C:/escape", "docs/index.md",
                     "comunicados/../escape", "comunicados\\SCIV_STATE.json"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                local.safe(self.root, path)

    def test_real_hardlink_denied(self):
        target = self.root / local.ADAPTER
        os.link(target, self.base / "alias")
        self.assertEqual(target.stat().st_nlink, 2)
        with self.assertRaisesRegex(ValueError, "HARDLINK"):
            self.apply()

    def test_real_symlink_denied(self):
        target = self.root / "comunicados"
        outside = self.base / "outside"
        outside.mkdir()
        try:
            target.symlink_to(outside, target_is_directory=True)
        except OSError as error:
            if getattr(error, "winerror", None) == 1314:
                self.skipTest("SKIP_ENV_NOT_SUPPORTED: Windows symlink privilege 1314")
            raise
        with self.assertRaisesRegex(ValueError, "LINK_OR_REPARSE"):
            self.apply()
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(os.name == "nt", "Windows junction only")
    def test_real_junction_denied(self):
        outside = self.base / "outside"
        outside.mkdir()
        target = self.root / "comunicados"
        # Both absolute paths are fixed children of this TemporaryDirectory.
        result = subprocess.run(["cmd.exe", "/c", "mklink", "/J", str(target), str(outside)],
                                capture_output=True)
        if result.returncode:
            self.skipTest("SKIP_ENV_NOT_SUPPORTED: junction creation denied")
        try:
            with self.assertRaisesRegex(ValueError, "LINK_OR_REPARSE"):
                self.apply()
            self.assertEqual(list(outside.iterdir()), [])
        finally:
            target.rmdir()  # Remove only the verified junction, never recurse.

    def test_controlled_reparse_denied(self):
        real = Path.lstat
        def altered(path, *args, **kwargs):
            info = real(path, *args, **kwargs)
            if path == self.root / local.ADAPTER:
                class Reparse:
                    st_mode = info.st_mode
                    st_file_attributes = 0x400
                return Reparse()
            return info
        with patch.object(Path, "lstat", altered):
            with self.assertRaisesRegex(ValueError, "LINK_OR_REPARSE"):
                self.apply()

    def test_preservation_mixed_newlines_and_negative(self):
        original = "Missão\r\n**Bootstrap:** teste\n".encode()
        proposed = local.BEGIN + b"\nmanaged\n" + local.END + b"\n\n" + original
        local.preserve(original, proposed)
        with self.assertRaisesRegex(ValueError, "OUTSIDE_BYTES"):
            local.preserve(original, proposed + b"changed")


if __name__ == "__main__":
    unittest.main()
