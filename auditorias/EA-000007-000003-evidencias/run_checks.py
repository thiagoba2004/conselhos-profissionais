"""Offline F004 checks. Canonical dependencies must be supplied explicitly.

No credential access or network is intended. Upstream suites use synthetic
stores, temporary files and local Git repositories. Results never attest UI.
"""
import argparse
import contextlib
import hashlib
import importlib.metadata
import io
import json
from pathlib import Path
import socket
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("suite", choices=("local", "generator", "runtime", "gates"))
    parser.add_argument("--generator", type=Path, required=True)
    parser.add_argument("--governance", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(OUT))
    sys.path.insert(0, str(args.generator / "tools"))
    sys.path.insert(0, str(args.governance / "runtime"))
    # Explicit block in this process; child commands are pre-inspected local
    # fixture/Git commands, and are not covered by this Python socket guard.
    def no_network(*args, **kwargs):
        raise RuntimeError("NETWORK_FORBIDDEN_IN_OFFLINE_CHECKS")
    socket.create_connection = no_network
    socket.socket.connect = no_network
    if args.suite == "gates":
        import project_creation_gate
        import validate_execution_action_plan
        import executor_action_gate
        local = json.loads((ROOT / "governanca/EXECUTOR_ACTION_CATALOG.json").read_text(encoding="utf-8"))
        result = {
            "routing": [executor_action_gate.evaluate(action, "CODEX", project_code="PRJ-000007", local=local)
                        for action in ("CODE_REFACTOR", "TEST_EXECUTION")],
            "action_matrix": validate_execution_action_plan.validate(ROOT, "EA-000007-000003"),
            "generator_sciv": project_creation_gate.inspect(ROOT, route="B", gate="sciv")}
    else:
        names = {"local": ["test_sciv_local"],
                 "generator": ["test_sciv_bootstrap", "test_project_creation_gate",
                               "test_validate_execution_action_plan", "test_legacy_bootstrap_gate"],
                 "runtime": ["test_sciv_mailbox", "test_sciv_essential", "test_sciv_archive",
                             "test_sciv_security", "test_sciv_publication", "test_sciv_per_project"]}[args.suite]
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            suite = unittest.defaultTestLoader.loadTestsFromNames(names)
            tests = unittest.TextTestRunner(stream=output, verbosity=2).run(suite)
        result = {"suite": args.suite, "run": tests.testsRun,
                  "pass": tests.testsRun - len(tests.failures) - len(tests.errors) - len(tests.skipped),
                  "fail": len(tests.failures), "error": len(tests.errors), "skip": len(tests.skipped),
                  "skipped": [(str(test), reason) for test, reason in tests.skipped],
                  "failures": [(str(test), detail) for test, detail in tests.failures],
                  "errors": [(str(test), detail) for test, detail in tests.errors],
                  "limitation": "Offline fixtures only; no independent attestation, native UI or live PEP."}
        # Raw upstream logs stay outside the public repository.
        (args.generator.parent / f"prj000007-sciv-{args.suite}.log").write_text(output.getvalue(), encoding="utf-8")
    result["python"] = sys.version.split()[0]
    if args.suite == "runtime":
        result["dependency_versions"] = {name: importlib.metadata.version(name)
                                         for name in ("jsonschema", "attrs", "referencing", "rpds-py", "jsonschema-specifications")}
    (OUT / f"{args.suite}-results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return int(bool(result.get("fail") or result.get("error")))


if __name__ == "__main__":
    raise SystemExit(main())
