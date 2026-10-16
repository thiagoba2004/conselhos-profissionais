"""Normalize tracking JSON and build an exact review manifest, without Git mutation."""
import json
import re
from pathlib import Path
import subprocess
from verify_package import ROOT, OUT, BASE, sha, git, main as verify


def main():
    for name in ("PROJECT_STATE.json", "estrategias/EA-000007-000003-actions.json"):
        p = ROOT / name
        p.write_text(json.dumps(json.loads(p.read_text(encoding="utf-8")), ensure_ascii=False,
                                indent=2) + "\n", encoding="utf-8")
    verify()
    tracked = git(ROOT, "diff", "--name-only", BASE).decode().splitlines()
    untracked = git(ROOT, "ls-files", "--others", "--exclude-standard").decode().splitlines()
    paths = sorted(set(tracked + [p for p in untracked if "__pycache__" not in p
                                 and not p.startswith(".codex-rerun/")]))
    manifest_path = OUT / "publication-manifest.json"
    entries = []
    for p in paths:
        if p == manifest_path.relative_to(ROOT).as_posix():
            continue
        assert not p.startswith(("docs/", "comunicados/", "adaptadores/", ".github/")), p
        data = (ROOT / p).read_bytes()
        clean = data.replace(b"\r\n", b"\n")
        assert not re.search(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|github_pat_[A-Za-z0-9_]{30,}", data), p
        old = subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:{p}"], capture_output=True)
        entries.append({"path": p, "effect": "UPDATE" if old.returncode == 0 else "CREATE",
                        "old_git_sha256": sha(old.stdout) if old.returncode == 0 else None,
                        "new_git_sha256": sha(clean), "new_worktree_sha256": sha(data),
                        "classification": "S1_INTERNO_NAO_SENSIVEL_REVIEWED_PUBLICABLE"})
    manifest_path.write_text(json.dumps({"request_ref": "REQ-000007-20261015-008",
        "base_commit": BASE, "publication": "NORMAL_PUSH_NO_FORCE",
        "scope": "F004 evidence, tracking, historical publication receipts; reviewed publicable",
        "review": "Human-authorized technical artifacts; no secrets or private case data found; not a full historic security audit",
        "recovery": "New corrective commit; preserve full history and receipts",
        "self_hash_excluded": True, "files": entries}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"manifest_files": len(entries), "status": "PREPARED"}))


if __name__ == "__main__":
    main()
