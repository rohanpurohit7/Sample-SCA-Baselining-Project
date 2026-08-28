# Security Test Plan

## Scope

Assess CoordinationHub release R1.0.1 against the tailored moderate baseline.

## Test Methods

| Test ID | Control Focus | Method | Expected Result |
| --- | --- | --- | --- |
| STP-001 | RA-5 | Run mock Veracode SAST | No open High findings |
| STP-002 | RA-5 SC-7 | Run mock Burp DAST | No exploitable High or Medium findings |
| STP-003 | AC-3 IA-2 | Run mock Contrast IAST | Authorization uses validated server-side principal |
| STP-004 | CM-6 SI-2 | Run mock Aqua container scan | Container is non-root and supported |
| STP-005 | CM-3 CM-4 | Review CR and SIA artifacts | Production changes link to impact analysis and POA&M where applicable |
| STP-006 | CA-5 | Review POA&M closure evidence | POA&M status matches scanner and CR evidence |

## Entry Criteria

- Build artifacts available.
- Scanner stage definitions available.
- POA&M register updated.
- CRs approved for release R1.0.1.

## Exit Criteria

- High and medium findings closed or risk accepted by AO.
- Residual risk documented.
- Test report and risk assessment updated.

