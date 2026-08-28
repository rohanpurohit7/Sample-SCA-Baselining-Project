# Mock Security Scanner Stages

| Stage | Tool | Target | Gate |
| --- | --- | --- | --- |
| sast | Veracode | Java source and dependencies | No open High findings |
| dast | Burp Suite | Deployed test endpoint | No exploitable High or Medium findings |
| iast | Contrast | Integration test runtime | No authentication or authorization bypass |
| container | Aqua | Built container image | No critical/high image or runtime policy issue |
| registry | ECR Image Scan | Promoted release image | No unapproved secrets or high CVEs |
| code-quality | CodeQL-style mock scan | Source repository | No unsafe data flow findings |

## Mock Result Progression

- R1.0.0 baseline: 2 High, 2 Medium, 1 Low.
- R1.0.1 remediation: 0 High, 0 Medium, 1 accepted Low.

