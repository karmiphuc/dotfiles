#!/usr/bin/env python3
"""Fixture tests for checker_score.py."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import uuid
from pathlib import Path


SCRIPT = Path(__file__).with_name("checker_score.py")


BASE = {
    "correctness": 30,
    "goal_fit": 15,
    "evidence": 15,
    "validation": 15,
    "maintainability": 10,
    "safety": 10,
    "communication": 5,
    "flags": {
        "p0_blocker": False,
        "p1_blocker": False,
        "high_risk_untested": False,
        "unresolved_p2_findings": False,
        "missing_primary_evidence": False,
    },
    "independent_evidence_count": 2,
    "relevant_validation": True,
    "unverified_assumption_count": 0,
}


def temp_parent() -> Path:
    candidates = []
    if os.environ.get("CHECKER_TEST_TMP"):
        candidates.append(Path(os.environ["CHECKER_TEST_TMP"]))
    candidates.append(Path(__file__).resolve().parent)
    candidates.append(Path.cwd())

    for candidate in candidates:
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            probe = candidate / ".checker-score-write-test"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
            return candidate
        except OSError:
            continue
    raise RuntimeError("no writable temporary directory found")


def run_case(case: dict) -> dict:
    path = temp_parent() / f".checker-score-case-{uuid.uuid4().hex}.json"
    try:
        path.write_text(json.dumps(case), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(proc.stdout)
    finally:
        try:
            path.unlink()
        except OSError:
            pass


def merged(**overrides) -> dict:
    case = json.loads(json.dumps(BASE))
    for key, value in overrides.items():
        if key == "flags":
            case["flags"].update(value)
        else:
            case[key] = value
    return case


def assert_case(name: str, case: dict, verdict: str, score: float) -> None:
    result = run_case(case)
    assert result["verdict"] == verdict, (name, result)
    assert result["score"] == score, (name, result)


def main() -> int:
    assert_case("go", merged(), "GO", 100.0)
    assert_case("hold_missing_validation", merged(relevant_validation=False), "HOLD", 89)
    assert_case(
        "hold_unresolved_p2",
        merged(flags={"unresolved_p2_findings": True}),
        "HOLD",
        89,
    )
    assert_case(
        "hold_unverified_assumption",
        merged(unverified_assumption_count=1),
        "HOLD",
        89,
    )
    assert_case(
        "hold_missing_primary_evidence",
        merged(flags={"missing_primary_evidence": True}),
        "HOLD",
        84,
    )
    assert_case(
        "hold_high_risk_untested",
        merged(flags={"high_risk_untested": True}),
        "HOLD",
        79,
    )
    assert_case("abort_p1", merged(flags={"p1_blocker": True}), "ABORT", 69)
    assert_case("abort_p0", merged(flags={"p0_blocker": True}), "ABORT", 49)
    print("checker_score fixtures passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
