"""Compare a separately fetched full Git store and record predecessor readback."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from verify_package import ROOT, OUT, BASE, git, sha


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    remote = Path(os.environ["TEMP"]) / "prj000007-f004-rerun-remote"
    commit = git(ROOT, "rev-parse", "HEAD").decode().strip()
    assert git(ROOT, "ls-remote", "origin", "refs/heads/main").decode().split()[0] == commit
    assert git(remote, "rev-parse", "refs/heads/main").decode().strip() == commit
    assert git(remote, "rev-parse", "--is-shallow-repository").strip() == b"false"
    git(remote, "merge-base", "--is-ancestor", BASE, commit)
    assert git(ROOT, "rev-parse", "HEAD^{tree}") == git(remote, "rev-parse", commit + "^{tree}")
    files = []
    for p in git(ROOT, "ls-tree", "-r", "--name-only", commit).decode().splitlines():
        local = git(ROOT, "show", f"{commit}:{p}")
        actual = git(remote, "show", f"{commit}:{p}")
        assert actual == local, p
        files.append({"path": p, "git_sha256": sha(actual), "remote_bytes_equal": True})
    assert git(remote, "rev-list", commit).splitlines() == git(ROOT, "rev-list", commit).splitlines()
    if args.check_only:
        print(json.dumps({"final_readback": "PASS", "commit": commit, "files": len(files),
                          "full_ancestry_equal": True}))
        return
    manifest = json.loads((OUT / "publication-manifest.json").read_text(encoding="utf-8"))
    for item in manifest["files"]:
        assert sha(git(remote, "show", f"{commit}:{item['path']}")) == item["new_git_sha256"]
    receipt = {"request_ref": "REQ-000007-20261015-008", "timestamp_utc": datetime.now(timezone.utc).isoformat(),
               "published_commit": commit, "remote_ref_observed": commit,
               "readback": "PASS_FULL_BARE_CLONE_ALL_TRACKED_BLOBS_TREE_AND_ANCESTRY",
               "full_history": True, "ancestor_checkpoint": BASE,
               "publication_manifest_sha256": sha((OUT / "publication-manifest.json").read_bytes()),
               "files": files, "enabled": False, "os_symlink_physical_verified": False,
               "operational_activation_blocked": True, "pages_changed": False,
               "initial_runtime_error_preserved": True, "final_tests": {"pass": 266, "fail": 0, "error": 0, "skip": 2},
               "scope": "SCIV_REPO_VERIFICADO_OFFLINE_WITH_PHYSICAL_SYMLINK_LIMITATION",
               "classification": "S1_INTERNO_NAO_SENSIVEL_REVIEWED_PUBLICABLE",
               "receipt_scope": "Predecessor evidence commit; receipt itself published in subsequent normal commit, checked separately."}
    write(OUT / "readback.json", receipt)
    state_path = ROOT / "PROJECT_STATE.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    sciv = state["sciv_rollout"]
    sciv.update(status="F004_REPOSITORY_VERIFIED_WITH_PHYSICAL_SYMLINK_LIMITATION_F005_HUMAN_PENDING",
                current_phase="F-000007-000003-005", last_completed_phase="F-000007-000003-004",
                last_completed_gate="SCIV_REPO_VERIFICADO", next_executor="HUMAN_G0",
                next_action="ACT-000007-000003-005", repository_gate_verified=True,
                blocker="PHYSICAL_SYMLINK_NOT_VERIFIED_OPERATIONAL_USE_BLOCKED;NATIVE_CONTEXT_AND_B8_NOT_VERIFIED",
                publication_status="RERUN_EVIDENCE_PUBLISHED_REMOTE_BYTES_VERIFIED",
                rerun_published_commit=commit,
                rerun_readback_ref="auditorias/EA-000007-000003-rerun-f004-2026-10-15/readback.json",
                repository_gate_scope="DOCUMENTARY_OFFLINE_ONLY;2_PHYSICAL_SYMLINK_SKIPS_NOT_APPROVED",
                next_logical_step="G0 reconcilia registro global por acao propria; titular decide contexto/configuracao F005. Resolver prova fisica de symlink antes de uso operacional; enabled=false.")
    write(state_path, state)
    matrix_path = ROOT / "estrategias/EA-000007-000003-actions.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    action = next(a for a in matrix["actions"] if a["action_key"] == "ACT-000007-000003-004")
    action.update(status="VERIFIED", local_result="ROUTE_B_SCIV_PASS_REMOTE_READBACK_VERIFIED_WITH_LIMITATIONS",
                  remote_readback_verified=True, blocker=None, decision_owner="TITULAR_HUMANO_G0",
                  verified_scope="REPOSITORY_OFFLINE_ONLY;PHYSICAL_SYMLINK_NOT_VERIFIED;NO_ACTIVATION",
                  operational_blocker="PHYSICAL_SYMLINK_AND_NATIVE_HUMAN_GATES_PENDING")
    action["evidence_refs"].append(sciv["rerun_readback_ref"])
    write(matrix_path, matrix)
    event = {"event_id": "EA007-SCIV-F004-READBACK-20261015-004", "date": "2026-10-15",
             "event_type": "PHASE_COMPLETED", "project_code": "PRJ-000007",
             "strategy_code": "EA-000007-000003", "strategy_id": "EA-000007-000003",
             "phase_code": "F-000007-000003-004", "phase_number": 4, "phase_total": 6,
             "status": "VERIFIED_REPOSITORY_OFFLINE_WITH_LIMITATIONS", "gate": "SCIV_REPO_VERIFICADO",
             "gate_satisfied": True, "request_ref": "REQ-000007-20261015-008",
             "published_commit": commit, "evidence_ref": sciv["rerun_readback_ref"],
             "tests": receipt["final_tests"], "initial_runtime_error": 1,
             "os_symlink_physical_verified": False, "enabled": False, "B8_accepted": False,
             "site_preserved": True, "next_phase": "F-000007-000003-005", "next_executor": "HUMAN_G0"}
    with (ROOT / "STRATEGY_LOG.jsonl").open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(event, ensure_ascii=False) + "\n")
    note = ("\n## Readback do rerun F004 — 15/10/2026\n\n"
            f"Commit {commit} publicado por push normal; copia remota completa, arvore, "
            f"ancestralidade e {len(files)} arquivos conferidos por bytes. F004 SCIV_REPO_VERIFICADO "
            "concluida somente no escopo repositorio/offline com ressalvas. 266 PASS / 2 SKIP; "
            "ERROR inicial de encoding preservado e retry UTF-8 aprovado. Dois testes fisicos de "
            "symlink NAO aprovados; uso operacional bloqueado. SCIV enabled=false, Site/Pages "
            "inalterados. F005 aguarda titular/G0; F006 nao executada. "
            "Recibo: auditorias/EA-000007-000003-rerun-f004-2026-10-15/readback.json.\n")
    for p in (ROOT / "ROADMAP.md", ROOT / "estrategias/EA-000007-000003-sciv-sob-demanda.md", OUT / "RELATORIO.md"):
        with p.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(note)
    print(json.dumps({"readback": "PASS", "commit": commit, "files": len(files), "receipt_written": True}))


if __name__ == "__main__":
    main()
