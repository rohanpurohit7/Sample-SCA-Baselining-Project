# Change Request CR-001

Title: Remediate SQL injection in message lookup  
Linked POA&M: POAM-001  
Release: R1.0.1  
Risk before: High  
Risk after: Low  
Status: Approved and deployed

## Change Summary

Replace dynamic SQL string concatenation with a prepared statement in the message lookup route.

## Security Impact

Affected control families:

- RA: vulnerability scanning and analysis.
- SA: developer testing and evaluation.
- SI: flaw remediation.

## Verification

Veracode mock rescan reports `VER-001` as fixed.

