#!/usr/bin/env python3
"""Deterministic score calculator for the Checker rubric."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


WEIGHTS = {
    "correctness": 30,
    "goal_fit": 15,
    "evidence": 15,
    "validation": 15,
    "maintainability": 10,
    "safety": 10,
    "communication": 5,
}


def usage() -> str:
    return (
        "Usage: checker_score.py scores.json\n\n"
        "scores.json example:\n"
        "{\n"
        '  "correctness": 27,\n'
        '  "goal_fit": 14,\n'
        '  "evidence": 13,\n'
        '  "validation": 12,\n'
        '  "maintainability": 9,\n'
        '  "safety": 10,\n'
        '  "communication": 5,\n'
        '  "flags": {\n'
        '    "p0_blocker": false,\n'
        '    "p1_blocker": false,\n'
        '    "high_risk_untested": false,\n'
        '    "unresolved_p2_findings": false,\n'
        '    "missing_primary_evidence": false\n'
        "  },\n"
        '  "independent_evidence_count": 2,\n'
        '  "relevant_validation": true,\n'
        '  "unverified_assumption_count": 0\n'
        "}\n"
    )


def score_value(data: dict[str, Any], key: str) -> float:
    raw = data.get(key, 0)
    if isinstance(raw, dict):
        raw = raw.get("score", 0)
    try:
        value = float(raw)
    except (TypeError, ValueError):
        raise ValueError(f"{key} must be a number or an object with a numeric score")
    max_value = WEIGHTS[key]
    if value < 0 or value > max_value:
        raise ValueError(f"{key} must be between 0 and {max_value}")
    return value


def verdict(score: float, flags: dict[str, bool], relevant_validation: bool) -> str:
    if flags.get("p0_blocker") or flags.get("p1_blocker") or score < 70:
        return "ABORT"
    if (
        score < 90
        or flags.get("high_risk_untested")
        or flags.get("unresolved_p2_findings")
        or flags.get("missing_primary_evidence")
        or not relevant_validation
    ):
        return "HOLD"
    return "GO"


def confidence(data: dict[str, Any], flags: dict[str, bool], final_score: float) -> str:
    evidence_count = int(data.get("independent_evidence_count", 0) or 0)
    relevant_validation = bool(data.get("relevant_validation", False))
    unverified = int(data.get("unverified_assumption_count", 0) or 0)

    if (
        final_score >= 90
        and evidence_count >= 2
        and relevant_validation
        and unverified == 0
        and not any(flags.values())
    ):
        return "High"
    if final_score >= 70 and evidence_count >= 1 and not flags.get("p0_blocker"):
        return "Medium"
    return "Low"


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] in {"-h", "--help"}:
        print(usage())
        return 0 if len(argv) == 2 else 2

    path = Path(argv[1])
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    raw_scores = {key: score_value(data, key) for key in WEIGHTS}
    raw_total = sum(raw_scores.values())

    flags = {
        "p0_blocker": False,
        "p1_blocker": False,
        "high_risk_untested": False,
        "unresolved_p2_findings": False,
        "missing_primary_evidence": False,
    }
    flags.update({k: bool(v) for k, v in data.get("flags", {}).items() if k in flags})

    cap = 100
    if flags["p0_blocker"]:
        cap = min(cap, 49)
    if flags["p1_blocker"]:
        cap = min(cap, 69)
    if flags["unresolved_p2_findings"]:
        cap = min(cap, 89)
    relevant_validation = bool(data.get("relevant_validation", False))
    unverified_assumptions = int(data.get("unverified_assumption_count", 0) or 0)

    if flags["high_risk_untested"]:
        cap = min(cap, 79)
    if unverified_assumptions > 0:
        cap = min(cap, 89)
    if not relevant_validation:
        cap = min(cap, 89)
    if flags["missing_primary_evidence"]:
        cap = min(cap, 84)

    final_score = min(raw_total, cap)
    result = {
        "raw_total": raw_total,
        "cap": cap,
        "score": final_score,
        "verdict": verdict(final_score, flags, relevant_validation),
        "confidence": confidence(data, flags, final_score),
        "scores": raw_scores,
        "flags": flags,
        "relevant_validation": relevant_validation,
        "unverified_assumption_count": unverified_assumptions,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except Exception as exc:
        print(f"checker_score.py: error: {exc}", file=sys.stderr)
        raise SystemExit(1)
