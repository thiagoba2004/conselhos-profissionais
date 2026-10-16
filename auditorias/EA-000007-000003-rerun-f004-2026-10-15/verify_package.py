"""Read-only package checks and provenance for the authorized F004 rerun."""
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = "38bfb1bdf247a0f06df383a2233443b8c487fc66"
GEN = "2af1258c4867da3bd59b0a3ff332f7e34f94bb6c"
GOV = "86998b2dcea6fb45ecb07f73e9330af26a6fdace"


def git(root, *args):
    return subprocess.check_output(["git", "-c", f"safe.directory={root.as_posix()}",
                                    "-C", str(root), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert git(ROOT, "branch", "--show-current").strip() == b"main"
    assert git(ROOT, "remote", "get-url", "origin").strip() == b"https://github.com/thiagoba2004/conselhos-profissionais.git"
    assert git(ROOT, "rev-parse", "--is-shallow-repository").strip() == b"false"
    git(ROOT, "merge-base", "--is-ancestor", BASE, "HEAD")
    files = [p for p in git(ROOT, "ls-tree", "-r", "--name-only", BASE).decode().splitlines()
             if p.startswith(("docs/", "comunicados/", "adaptadores/")) or p in
             ("AGENTS.md", "SITE_ARCHITECTURE.md", "SITE_STYLE_GUIDE.md",
              "MISSAO_E_ESCOPO.md", "INFORMATION_HANDLING_PROFILE.json",
              "estrategias/EA-000007-000001-constituicao-publica.md")]
    checks = []
    for p in files:
        old = git(ROOT, "show", f"{BASE}:{p}")
        # Git clean-filter bytes and physical bytes are different on CRLF worktrees.
        clean = git(ROOT, "hash-object", "--path=" + p, p).strip()
        expected = git(ROOT, "rev-parse", f"{BASE}:{p}").strip()
        assert clean == expected, p
        checks.append({"path": p, "git_sha256": sha(old), "git_blob": expected.decode(),
                       "worktree_sha256": sha((ROOT / p).read_bytes()), "unchanged": True})
    for p in ("REQUEST_LOG.jsonl", "STRATEGY_LOG.jsonl"):
        historical = git(ROOT, "show", f"{BASE}:{p}").replace(b"\r\n", b"\n")
        assert (ROOT / p).read_bytes().replace(b"\r\n", b"\n").startswith(historical)
    adapter = git(ROOT, "show", f"{BASE}:adaptadores/chatgpt/INSTRUCOES.md")
    original = git(ROOT, "show", "8644e96215c4f812b53b5b57dac06248d21ecef2:adaptadores/chatgpt/INSTRUCOES.md")
    begin = adapter.index(b"<!-- SCIV_BOOTSTRAP_BEGIN v1 -->")
    end = adapter.index(b"<!-- SCIV_BOOTSTRAP_END -->") + len(b"<!-- SCIV_BOOTSTRAP_END -->")
    # Provisioner adds one blank line after the managed block.
    assert adapter[:begin] + adapter[end:].lstrip(b"\r\n") == original
    state = json.loads((ROOT / "comunicados/SCIV_STATE.json").read_text(encoding="utf-8"))
    assert state["enabled"] is False and state["mode"] == "ON_DEMAND"
    sources = []
    for folder, commit, prefix in (("prj000007-f004-rerun-generator", GEN, "tools/"),
                                    ("prj000007-sciv-20261015-governance", GOV, "runtime/")):
        root = Path(os.environ["TEMP"]) / folder
        assert git(root, "rev-parse", "HEAD").decode().strip() == commit
        for p in git(root, "ls-tree", "-r", "--name-only", commit, "--", prefix).decode().splitlines():
            if p.endswith(".py"):
                raw = git(root, "show", f"{commit}:{p}")
                assert (root / p).read_bytes().replace(b"\r\n", b"\n") == raw.replace(b"\r\n", b"\n"), p
                sources.append({"commit": commit, "path": p, "git_sha256": sha(raw)})
    result = {"request_ref": "REQ-000007-20261015-008", "base_commit": BASE,
              "full_history": True, "initial_commit_count": 55,
              "append_only_prefix_preserved": True, "outside_adapter_block_preserved": True,
              "enabled": False, "protected_files": checks, "source_files": sources,
              "symlink_physical_verified": False,
              "classification": "S1_INTERNO_NAO_SENSIVEL_REVIEWED_PUBLICABLE"}
    (OUT / "verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verification": "PASS", "protected_files": len(checks), "source_files": len(sources)}))


if __name__ == "__main__":
    main()
