import argparse
import csv
import hashlib
import json
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = ROOT / "artifacts" / "cadence"
POAM_FILE = ROOT / "poam" / "poam-register.csv"
SCAN_FILES = [
    ROOT / "scanners" / "mock-scan-results.json",
    ROOT / "scanners" / "mock-rescan-results-r1.0.1.json",
]

CADENCE_SOURCES = {
    "weekly": [
        "architecture/authorization-boundary.md",
        "architecture/inventory.csv",
        "controls/control-tailoring.md",
        "controls/ssp.md",
        "scanners/mock-scan-results.json",
        "scanners/mock-rescan-results-r1.0.1.json",
        "poam/poam-register.csv",
        "reports/security-test-report.md",
        "reports/risk-assessment-gap-analysis.md",
        "reports/release-r1.0.1-lmh-summary.md",
    ],
    "monthly": [
        "architecture/authorization-boundary.md",
        "architecture/inventory.csv",
        "controls/control-tailoring.md",
        "controls/ssp.md",
        "scanners/mock-scan-results.json",
        "scanners/mock-rescan-results-r1.0.1.json",
        "poam/poam-register.csv",
        "reports/security-impact-analysis.md",
        "reports/security-test-plan.md",
        "reports/security-test-report.md",
        "reports/risk-assessment-gap-analysis.md",
        "reports/release-r1.0.1-lmh-summary.md",
    ],
    "release": [
        "change-requests/CR-001-sql-injection.md",
        "change-requests/CR-002-xss.md",
        "change-requests/CR-003-authz.md",
        "change-requests/CR-004-container-hardening.md",
        "change-requests/CR-005-secret-handling.md",
        "change-requests/CR-006-sia-partner-interface.md",
        "poam/poam-register.csv",
        "scanners/mock-rescan-results-r1.0.1.json",
        "reports/security-test-report.md",
        "reports/release-r1.0.1-lmh-summary.md",
    ],
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_poams() -> list[dict[str, str]]:
    with POAM_FILE.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_findings() -> list[dict[str, str]]:
    findings = []
    for path in SCAN_FILES:
        data = json.loads(path.read_text(encoding="utf-8"))
        for finding in data["scanner_results"]:
            row = dict(finding)
            row["release"] = data["release"]
            row["source_file"] = path.relative_to(ROOT).as_posix()
            row["control_refs"] = ";".join(row.get("control_refs", []))
            findings.append(row)
    return findings


def copy_sources(package_dir: Path, sources: list[str]) -> list[dict[str, object]]:
    copied = []
    evidence_dir = package_dir / "evidence"
    for source in sources:
        source_path = ROOT / source
        if not source_path.exists():
            copied.append({"path": source, "missing": True})
            continue
        target_path = evidence_dir / source
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        copied.append(
            {
                "path": source,
                "missing": False,
                "bytes": source_path.stat().st_size,
                "sha256": sha256(source_path),
            }
        )
    return copied


def write_poam_summary(package_dir: Path, poams: list[dict[str, str]]) -> dict[str, int]:
    counts = Counter(f"{row['severity']}:{row['status']}" for row in poams)
    summary_path = package_dir / "poam-status-summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["severity", "status", "count"])
        for key, count in sorted(counts.items()):
            severity, status = key.split(":", 1)
            writer.writerow([severity, status, count])
    return dict(counts)


def write_scanner_summary(package_dir: Path, findings: list[dict[str, str]]) -> dict[str, int]:
    counts = Counter(f"{row['severity']}:{row['status']}" for row in findings)
    summary_path = package_dir / "scanner-findings-summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["release", "scanner", "finding_id", "severity", "status", "linked_poam", "linked_cr", "source_file"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in findings:
            writer.writerow(row)
    return dict(counts)


def write_gate(package_dir: Path, poams: list[dict[str, str]]) -> dict[str, object]:
    open_by_severity = defaultdict(list)
    for row in poams:
        if row["status"] not in {"Closed", "Accepted"}:
            open_by_severity[row["severity"]].append(row["poam_id"])

    blocking = open_by_severity["High"] + open_by_severity["Medium"]
    decision = "BLOCK" if blocking else "ALLOW"
    gate_path = package_dir / "release-gate-decision.md"
    gate_path.write_text(
        "\n".join(
            [
                "# Release Gate Decision",
                "",
                f"Decision: {decision}",
                "",
                f"Open high POA&Ms: {', '.join(open_by_severity['High']) or 'None'}",
                f"Open medium POA&Ms: {', '.join(open_by_severity['Medium']) or 'None'}",
                f"Open low POA&Ms: {', '.join(open_by_severity['Low']) or 'None'}",
                "",
                "Gate rule: open high or medium findings block release until closed or formally accepted.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return {"decision": decision, "blocking_poams": blocking}


def write_index(package_dir: Path, cadence: str, copied: list[dict[str, object]]) -> None:
    rows = [
        "# Evidence Index",
        "",
        f"Cadence: {cadence}",
        "",
        "| Source Artifact | Included | SHA-256 |",
        "| --- | --- | --- |",
    ]
    for item in copied:
        rows.append(
            f"| {item['path']} | {'No' if item['missing'] else 'Yes'} | {item.get('sha256', 'missing')} |"
        )
    rows.append("")
    (package_dir / "evidence-index.md").write_text("\n".join(rows), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate scheduled SCA evidence artifacts.")
    parser.add_argument("--cadence", choices=sorted(CADENCE_SOURCES), default="weekly")
    args = parser.parse_args()

    generated_at = datetime.now(timezone.utc)
    package_dir = ARTIFACT_ROOT / f"{generated_at:%Y%m%dT%H%M%SZ}-{args.cadence}"
    package_dir.mkdir(parents=True, exist_ok=True)

    poams = load_poams()
    findings = load_findings()
    copied = copy_sources(package_dir, CADENCE_SOURCES[args.cadence])
    poam_counts = write_poam_summary(package_dir, poams)
    scanner_counts = write_scanner_summary(package_dir, findings)
    gate = write_gate(package_dir, poams)
    write_index(package_dir, args.cadence, copied)

    manifest = {
        "system": "CoordinationHub",
        "cadence": args.cadence,
        "generated_at_utc": generated_at.isoformat(),
        "package": package_dir.relative_to(ROOT).as_posix(),
        "release_gate": gate,
        "poam_status_counts": poam_counts,
        "scanner_status_counts": scanner_counts,
        "source_artifacts": copied,
        "generated_artifacts": [
            "artifact-manifest.json",
            "poam-status-summary.csv",
            "scanner-findings-summary.csv",
            "release-gate-decision.md",
            "evidence-index.md",
        ],
    }
    (package_dir / "artifact-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Generated {args.cadence} cadence package: {package_dir.relative_to(ROOT)}")
    print(f"Release gate decision: {gate['decision']}")


if __name__ == "__main__":
    main()
