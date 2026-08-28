# Change Request CR-005

Title: Remove default database password from image metadata  
Linked POA&M: POAM-005  
Release: R1.0.1  
Risk before: Low  
Risk after: Low  
Status: Accepted residual risk with monitoring

## Change Summary

Remove `DB_PASSWORD` from the Dockerfile. Use the platform secret manager at runtime.

## Verification

ECR mock scan no longer detects the static default secret in the patched Dockerfile.

