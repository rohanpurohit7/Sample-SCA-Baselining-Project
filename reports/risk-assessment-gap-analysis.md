# Risk Assessment and Gap Analysis

## Risk Assessment

| Risk ID | Source | Initial Risk | Current Risk | Disposition |
| --- | --- | --- | --- | --- |
| RISK-001 | SQL injection | High | Low | Remediated |
| RISK-002 | Stored XSS | Medium | Low | Remediated |
| RISK-003 | Authorization bypass | Medium | Low | Remediated |
| RISK-004 | Container hardening weakness | High | Low | Remediated |
| RISK-005 | Static secret pattern | Low | Low | Accepted with monitoring |
| RISK-006 | New partner interface authorization | Medium | Low target | Pending CR-006 evidence |

## Gap Analysis

| Control Area | Gap | Remediation |
| --- | --- | --- |
| CM-4 Impact Analyses | Interface changes were not originally tied to scanner replay criteria. | SIA-001 now requires scanner replay before production. |
| RA-5 Vulnerability Monitoring | Baseline scanner results were stored, but trend reporting was manual. | `scripts/generate_release_report.py` summarizes fixed LMH counts. |
| AC-3 Access Enforcement | Header-based role trust was present in vulnerable baseline. | Patched release uses validated principal and MFA claim. |
| SI-2 Flaw Remediation | POA&M closure evidence needed clearer CR traceability. | Each POA&M now links to a CR and verification evidence. |

## Residual Risk Determination

Residual risk for R1.0.1 is acceptable at **Low** because high and medium findings are closed, remaining low findings are monitored, and future interface/database changes require SIA review.

