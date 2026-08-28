# Sample SCA Baselining Project

This repository is a self-contained mock Security Control Assessment (SCA) baselining package for a cloud-hosted communication and coordination application named **CoordinationHub**.

It demonstrates:

- Cloud authorization boundary definition and mocked asset inventory.
- NIST SP 800-53 Rev. 5 control tailoring for a moderate-impact sample system.
- A sample System Security Plan (SSP).
- Mock scanner integrations for Veracode, Burp Suite, Contrast, Aqua, and ECR/container image scanning.
- Vulnerable code examples and patched versions linked to change requests (CRs).
- POA&M generation, remediation, risk reduction, and residual risk reporting.
- Security Impact Analysis (SIA), security test plan, security test report, risk assessment, and gap analysis.

This is a training/sample package only. It is not an official authorization package.

## Repository Layout

```text
app/
  vulnerable/          Example vulnerable service code
  patched/             Remediated service code
architecture/          Boundary, inventory, and cloud data flow docs
controls/              NIST 800-53 control tailoring and SSP traceability
scanners/              Mock scanner outputs and scanner stage definitions
poam/                  POA&M register, remediation plan, and risk reduction report
change-requests/       CR records for patched findings and SIA-driven changes
reports/               Security test, risk, SIA, release, and gap analysis reports
pipeline/              Mock DevSecOps workflow stages
scripts/               Local report validation/generation helpers
```

## Quick Start

Run the local summary generator:

```powershell
python scripts/generate_release_report.py
```

Expected output:

```text
Release R1.0.1 fixed 5 POA&Ms: High=2 Medium=2 Low=1
Residual risk: Low / Acceptable with AO approval
```

## NIST Reference Notes

Primary references used for this sample:

- NIST SP 800-53 Rev. 5, including updates through Release 5.2.0.
- NIST SP 800-37 Rev. 2 for RMF framing, continuous monitoring, authorization, and change impact concepts.
- NIST SP 800-18 Rev. 1 is referenced historically for SSP format concepts, but it was withdrawn on June 30, 2026 and superseded by SP 800-18 Rev. 2.
