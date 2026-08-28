# NIST SP 800-53 Rev. 5 Control Tailoring

## Baseline

Selected baseline: **Moderate**

Tailoring approach:

- Include controls that directly support application, cloud, container, and DevSecOps risk.
- Mark cloud provider, identity provider, and enterprise governance controls as inherited where appropriate.
- Mark controls as system-specific when implemented by the application team.
- Document compensating measures where scanner coverage or manual review is used.

## Tailored Control Set

| Family | Control | Allocation | Implementation Summary |
| --- | --- | --- | --- |
| AC | AC-2 Account Management | Hybrid | Application roles are mapped to IdP groups; account lifecycle inherited from IdP. |
| AC | AC-3 Access Enforcement | System-specific | API enforces role-based authorization on message and task routes. |
| AC | AC-4 Information Flow Enforcement | System-specific | Public API, private DB, and queue access are segmented by security groups and service roles. |
| AU | AU-2 Event Logging | System-specific | API, pipeline, database, and scanner events are centrally logged. |
| AU | AU-6 Audit Record Review | Hybrid | SIEM alerts and weekly AppSec review verify anomalous activity. |
| CA | CA-2 Control Assessments | System-specific | SCA test plan and report are maintained under `reports/`. |
| CA | CA-5 Plan of Action and Milestones | System-specific | POA&M register is tracked under `poam/poam-register.csv`. |
| CA | CA-7 Continuous Monitoring | Hybrid | Scanner stages execute per release and monthly. |
| CM | CM-2 Baseline Configuration | System-specific | Container image, Kubernetes manifests, and IaC are versioned. |
| CM | CM-3 Configuration Change Control | System-specific | CR records gate production deployments. |
| CM | CM-4 Impact Analyses | System-specific | SIA report required for interface, schema, or trust-boundary changes. |
| CM | CM-6 Configuration Settings | Hybrid | CIS container and cloud checks are reviewed by DevSecOps. |
| IA | IA-2 Identification and Authentication | Inherited | Enterprise IdP handles MFA and identity proofing. |
| RA | RA-3 Risk Assessment | System-specific | Risk assessment and gap analysis are updated after each assessment cycle. |
| RA | RA-5 Vulnerability Monitoring and Scanning | System-specific | Veracode, Burp Suite, Contrast, Aqua, and image scans are mocked in `scanners/`. |
| SA | SA-11 Developer Testing and Evaluation | System-specific | Unit, SAST, DAST, IAST, dependency, and container checks run in pipeline. |
| SC | SC-7 Boundary Protection | Hybrid | WAF, private subnets, and security groups isolate tiers. |
| SC | SC-8 Transmission Confidentiality and Integrity | System-specific | TLS required for external and internal service traffic. |
| SI | SI-2 Flaw Remediation | System-specific | Findings are remediated through POA&M-linked CRs. |
| SI | SI-4 System Monitoring | Hybrid | Runtime events are monitored by cloud logs and IAST telemetry. |

