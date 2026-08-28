# Authorization Boundary

## System Name

CoordinationHub

## Purpose

CoordinationHub is a sample cloud application used by mission teams to coordinate tasks, exchange operational messages, and track decisions.

## Impact Level

FIPS 199 categorization: **Moderate**

- Confidentiality: Moderate
- Integrity: Moderate
- Availability: Moderate

## Boundary Description

The authorization boundary includes:

- Public web application load balancer.
- Containerized API service hosted in managed Kubernetes.
- Private application database.
- Managed message queue for asynchronous notifications.
- ECR-style container registry.
- Centralized logging and monitoring services.
- CI/CD pipeline stages that build, scan, approve, and deploy application releases.

The boundary excludes:

- User endpoint devices.
- External identity provider.
- Third-party email/SMS notification provider.
- Enterprise ticketing system used for final CR board approvals.

## Data Flow

1. Users authenticate through the external identity provider.
2. The web client calls the CoordinationHub API through a cloud load balancer.
3. The API reads and writes coordination messages in the private database.
4. Notification events are placed on the managed queue.
5. Logs and security telemetry are forwarded to the cloud logging account.
6. CI/CD publishes container images to the registry after SAST, DAST, IAST, SCA, and container checks complete.

## Boundary Assumptions

- The identity provider is inherited as a common control.
- Cloud provider physical and environmental controls are inherited.
- The application team owns application, container, pipeline, and database configuration controls.

