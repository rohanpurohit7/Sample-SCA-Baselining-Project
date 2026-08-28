# Sample System Security Plan

## 1. System Identification

System name: CoordinationHub  
System owner: Mission Collaboration Program Office  
Authorizing official: Sample AO  
Information system security officer: Sample ISSO  
Impact categorization: Moderate

## 2. System Environment

CoordinationHub is deployed in a cloud environment using a containerized API, static web front end, managed database, message queue, and registry. CI/CD performs build, test, scan, approval, and deployment stages.

## 3. Authorization Boundary

The authorization boundary is documented in `architecture/authorization-boundary.md`. The application API, web client, database, queue, registry, pipeline runner, logging, and monitoring components are in-boundary. External IdP and notification provider services are out-of-boundary and treated as inherited or external dependencies.

## 4. Control Implementation Summary

| Family | Status | Notes |
| --- | --- | --- |
| AC | Implemented with inheritance | IdP groups and application RBAC enforce access. |
| AU | Implemented | Application, scanner, and deployment logs are centralized. |
| CA | Implemented | SCA artifacts, POA&M, and continuous monitoring reports are maintained. |
| CM | Partially implemented | SIA process identified interface and database change risk. |
| IA | Inherited | Enterprise IdP provides MFA. |
| RA | Implemented | Scanner results feed risk assessment and POA&M. |
| SA | Implemented | DevSecOps stages include scanner gates and remediation checks. |
| SC | Partially implemented | Boundary controls require periodic validation after network changes. |
| SI | Implemented | Flaw remediation is tracked through CR and POA&M closure evidence. |

## 5. Continuous Monitoring

Continuous monitoring includes:

- SAST on every merge request.
- Dependency and SCA checks on every build.
- Container image scan before registry promotion.
- DAST before production release.
- IAST during integration test execution.
- Monthly POA&M aging and residual risk review.

## 6. Open Risks

After release R1.0.1, all high and medium sample findings are remediated. One low finding remains accepted as residual risk due to limited exploitability and compensating WAF logging.

## 7. Authorization Recommendation

Proceed with an authorization decision for a moderate-impact sample system with residual risk accepted at **Low**, contingent on continued monthly scanning and CR board review for future interface or database changes.

