Threat Model
============

This high-level model follows the scope defined in
:doc:`disclosing-vulnerabilities` and the components described in
:doc:`/general/architecture`. It is not an exhaustive assessment of every
module or deployment.

.. contents:: **Table of Contents**:
    :backlinks: none
    :depth: 2

Assets to Protect
-----------------

- Private organization data, user accounts, and authentication tokens.
- Device configurations, firmware, and access to managed networks.
- Device and enrollment secrets, SSH credentials, VPN keys, and
  certificate authority private keys.
- The availability and integrity of network management, monitoring, and
  authentication services.
- Project repositories, release artifacts, websites, and the accounts and
  automation used to publish them.

Potential Attackers
-------------------

Consider unauthenticated clients, malicious or compromised user accounts,
compromised managed devices, and attackers with access to network traffic.
Compromised maintainer accounts or publishing systems can also put users
at risk through malicious releases or downloads.

Restricted registration and trusted operators can reduce exposure, but do
not remove the need to consider stolen credentials or compromised devices.

Trust Boundaries
----------------

Users and Organizations
~~~~~~~~~~~~~~~~~~~~~~~

Organization membership and assigned permissions define access to private
resources. A user must not gain unauthorized access to another
organization's data or operations. Shared resources and intentionally
public information are distinct from private organization data.

Superusers have instance-wide privileges: organization separation does not
protect tenants from a trusted instance administrator. See
:doc:`/users/user/basic-concepts` for roles and shared objects.

Clients, Devices, and the Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Web interfaces, APIs, and device endpoints receive input from outside the
server. Authentication does not make that input trustworthy or authorize
every operation. A compromised device or user account must not gain
unrelated privileges through submitted data.

OpenWISP intentionally gives authorized administrators powerful device
management capabilities, including configuration changes and, where
enabled, command execution and firmware upgrades. These capabilities are
not a sandbox for untrusted administrators. Their credentials and
permissions must be protected, and access must remain within the caller's
authorized scope.

Device enrollment is another boundary: an organization enrollment secret
allows new devices to register, while registered devices use their own
credentials. Protect both types of credentials. See
:doc:`/openwrt-config-agent/user/automatic-registration`.

Limit credentials to the devices, organizations, and operations that need
them, and revoke or rotate them after compromise. A stolen device
credential and an organization enrollment secret have different impacts:
the latter can allow unauthorized enrollment of additional devices.

The server also connects to devices and other services.
Attacker-controlled addresses or connection settings can cause
unauthorized requests to internal services or expose management
credentials to an unintended destination. Validate connection destinations
and remote identities, and restrict network access according to the
deployment's management needs.

Availability and Shared Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Excessive requests, device enrollment, telemetry submissions, or expensive
operations can exhaust shared resources and disrupt other organizations.
Authenticated users and compromised devices can cause this as well as
unauthenticated clients. Assess resource limits, request rates, and
workload isolation at both the application and deployment levels.

Deployment and Publishing Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The deployment administrator controls the server, database, installed
code, and service credentials. Application permissions do not protect
against an attacker who already controls that infrastructure.

Project release and website infrastructure forms a separate trust
boundary. Compromise of publishing access can distribute malicious code or
redirect downloads without a defect in the OpenWISP application. The
team's response is covered in :doc:`incident-response-plan`.

OpenWISP release tags are immutable, protecting existing tags from being
changed to point to different code. This does not prevent an attacker with
compromised publishing access from publishing a malicious new release.

Malicious dependencies or compromised build workflows can also introduce
malicious code into releases. Immutable tags alone do not establish that
the referenced code, dependencies, or build artifacts are safe. Review
dependency and workflow changes, limit build credentials and permissions,
and verify the origin and integrity of release artifacts.

Two-factor authentication (2FA) is mandatory for OpenWISP GitHub
organization members and package-publishing accounts wherever supported
(e.g., PyPI and Ansible Galaxy).

Operator Responsibilities
-------------------------

Operators are responsible for securing their deployments, including:

- Keeping OpenWISP and its dependencies updated and following
  :doc:`advisories`.
- Protecting administrative accounts, limiting privileges, and replacing
  default credentials.
- Using valid TLS certificates and keeping certificate verification
  enabled on device agents.
- Securing device management connectivity and protecting enrollment
  secrets, private keys, and other service credentials.
- Maintaining protected backups and a recovery process.

Custom applications and integrations can introduce additional trust
boundaries that their developers must assess. These responsibilities do
not exclude reporting defects in OpenWISP itself.

Evaluating a Suspected Boundary Violation
-----------------------------------------

Describe the attacker's initial access, the boundary crossed, and the
additional data or capabilities obtained. Authorized administration and
intended access to public information are not vulnerabilities by
themselves. An input validation defect, unauthorized access, or privilege
escalation still requires assessment even when the attacker already has an
account. Follow :ref:`security_report_evaluation` and
:ref:`security_issue_priority` for the shared assessment criteria.
