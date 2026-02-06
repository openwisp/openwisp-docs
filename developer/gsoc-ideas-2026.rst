GSoC Project Ideas 2026
=======================

.. tip::

    Do you want to apply with us?

    We have a page that describes how to increase your chances of success.
    **Please read it carefully.**

    :doc:`Read our Google Summer of Code guidelines
    <../developer/google-summer-of-code>`.

.. contents:: **Table of Contents**:
    :backlinks: none
    :depth: 3

General suggestions and warnings
--------------------------------

- **Project ideas describe the goals we want to achieve but may miss
  details that have to be defined during the project**: we expect
  applicants to do their own research, propose solutions and be ready to
  deal with uncertainty and solve challenges that will come up during the
  project
- **Code and prototypes are preferred over detailed documents and
  unreliable estimates**: rather than using your time to write a very long
  application document, we suggest to invest in writing a prototype (which
  means the code may be thrown out entirely) which will help you
  understand the challenges of the project you want to work on; your
  application should refer to the prototype or other Github contributions
  you made to OpenWISP that show you have the capability to succeed in the
  project idea you are applying for.
- **Applicants who have either shown to have or have shown to be fast
  learners for the required hard and soft skills by contributing to
  OpenWISP have a lot more chances of being accepted**: in order to get
  started contributing refer to the :doc:`OpenWISP Contributing Guidelines
  <../developer/contributing>`
- **Get trained in the projects you want to apply for**: once applicants
  have completed some basic training by :doc:`contributing to OpenWISP
  <../developer/contributing>` we highly suggest to start working on some
  aspects of the project they are interested in applying: all projects
  listed this year are improvements of existing modules so these modules
  already have a list of open issues which can be solved as part of your
  advanced training. It will also be possible to complete some of the
  tasks listed in the project idea right now before GSoC starts. We will
  list some easy tasks in the project idea for this purpose.

Project Ideas
-------------

Mass Commands
~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/2025/mass-commands.png

.. important::

    Languages and technologies used: **Python**, **Django**,
    **JavaScript**, **WebSockets**, **REST API**.

    **Mentors**: *Gagan Deep*, *Purhan Kaushik*, *Kapil Bansal*.

    **Project size**: 350 hours.

    **Difficulty rate**: medium.

This project idea aims to extend OpenWISP's remote device management
capabilities by enabling users to execute shell commands on multiple
devices simultaneously. Currently, OpenWISP supports executing commands on
a single device at a time. This project will introduce a bulk execution
feature while maintaining the existing security, rules, and limitations of
the single-device command execution feature.

The mass command operation will be accessible from two main entry points:

- An admin action on the device list page, allowing users to select
  multiple devices and send a shell command in bulk.
- A dedicated mass command admin section, where users can initiate bulk
  command execution with various targeting options:

  - All devices in the system (restricted to superusers).
  - All devices within a specific organization.
  - All devices within a specific device group.
  - All devices within a specific geographic location.
  - Specific selected devices.

The UI will guide users step-by-step, dynamically displaying relevant
fields based on the selected target scope. For example, if a user selects
"All devices in a specific organization", an auto-complete list of
organizations will be displayed next.

The system will provide real-time tracking of command execution results.
Inspired by OpenWISP Firmware Upgrader's mass upgrade feature, the UI will
receive live updates via WebSockets, displaying command output as soon as
it is received from the devices. Additionally:

- The device detail page will show executed commands under the "Recent
  Commands" tab.
- Commands that were part of a mass operation will be clearly marked, with
  a link to the corresponding mass command operation page.

To support API-based management, the REST API will be extended with the
following capabilities:

- Create new mass command operations.
- Retrieve mass command operations and their results (with pagination).
- Delete mass command operations.
- Modify the single-shell command API to reference the mass command
  operation ID if applicable.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

Applicants must demonstrate a solid understanding of Python, Django, HTML,
CSS, JavaScript, WebSockets, and `OpenWISP Controller
<https://github.com/openwisp/openwisp-controller>`__.

Expected outcomes
+++++++++++++++++

- Implementation of mass shell command execution in OpenWISP, replicating
  the rules and limitations of single-device execution.
- Development of an intuitive UI with the Django admin for selecting
  devices and tracking command results in real-time.
- Admin action for device list page.
- Enhancement of the device detail page to reflect mass command history
  for individual devices.
- Extension of the REST API to support mass command operations.
- Comprehensive automated tests covering the new feature.
- Updated documentation, including:

  - Feature description with usage instructions.
  - A short example usage video for YouTube that we can showcase on the
    website.

.. _gsoc-2026-x509-templates:

X.509 Certificate Generator Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/2025/x509-templates.webp

.. important::

    Languages and technologies used: **Python**, **Django**,
    **JavaScript**.

    **Mentors**: *Federico Capoano*, *Aryaman*, *Nitesh Sinha*.

    **Project size**: 175 hours.

    **Difficulty rate**: medium.

This GSoC project aims to enhance OpenWISP's certificate management
capabilities by enabling the generation of x509 certificates for
general-purpose use, beyond OpenVPN.

Currently, OpenWISP supports generating x509 certificates exclusively for
OpenVPN clients, where each VPN client template produces a certificate
signed by the CA linked to the corresponding VPN server. However, many
users require x509 certificates for other purposes, such as securing web
services, internal APIs, or device authentication outside of VPN usage.

The proposed solution introduces a new certificate template type that
allows users to generate x509 certificates using a selected Certificate
Authority (CA), while fully reusing the existing certificate
infrastructure provided by ``django-x509``.

Certificate template model and scope
++++++++++++++++++++++++++++++++++++

The new template type will reference an existing x509 certificate object,
which acts as a reusable blueprint for certificate generation.

The relation to the certificate object is optional:

- If a certificate template is specified, its non-unique properties are
  copied when generating per-device certificates
- If no certificate template is specified, certificate properties default
  to the selected CA's standard settings

The referenced certificate object is never issued or assigned to devices
directly and is used exclusively as a template.

No custom certificate profile system will be introduced. Only fields
already supported by ``django-x509`` may be used.

Device property integration
+++++++++++++++++++++++++++

Certificates generated from templates shall include device specific
properties resolved at generation time.

Supported device properties include:

- Device hostname
- Device MAC address
- Device UUID

These values may be included in:

- Standard subject fields supported by ``django-x509``, the hostname in
  particular shall be used as common name
- Custom x509 extensions stored in the existing ``extensions`` JSON field,
  using private OIDs

Device properties are resolved only when a template is assigned to a
device.

Certificates are automatically regenerated if the device's hostname or MAC
address fields are modified. This behavior must be explicitly stated in
the documentation; additionally, a UI notification of type
``generic_message`` must be triggered once the regeneration process is
complete.

Certificate lifecycle and ownership
+++++++++++++++++++++++++++++++++++

Certificates are generated when a certificate template is assigned to a
device, following the same lifecycle semantics as existing OpenVPN client
certificates.

- Assignment generates a new certificate
- Unassignment deletes the certificate
- Renewal regenerates the certificate
- No standalone certificates are generated without device assignment

Certificates are always associated with a CA, and revocation is handled
through the CA's existing Certificate Revocation List (CRL) mechanism. No
additional revocation logic will be introduced.

Storage, access, and security model
+++++++++++++++++++++++++++++++++++

Private keys and certificates are stored and protected using the existing
``django-x509`` mechanisms.

This project will not introduce:

- New encryption schemes
- New private key download endpoints
- New permission models

Existing OpenWISP access controls and organization scoping rules apply.

Configuration management integration
++++++++++++++++++++++++++++++++++++

Certificate details will be exposed to OpenWISP's configuration management
system as template variables, including:

- Certificate (PEM)
- Private key (PEM)
- Certificate UUID

Variable names will follow a UUID-based namespace to ensure uniqueness and
avoid conflicts with existing OpenWISP variables.

Certificate renewal triggers cache invalidation and configuration updates
to affected devices. No configuration updates are triggered unless a
certificate is renewed or regenerated.

API and admin interface
+++++++++++++++++++++++

The new certificate template type will be available through:

- Django admin
- Existing REST API template endpoints

No new API endpoints will be introduced. Existing RBAC and organization
scoping rules will apply.

Testing and documentation
+++++++++++++++++++++++++

The project requires:

- Automated tests covering certificate generation and lifecycle behavior
- Admin UI integration tests
- API tests
- Selenium browser tests
- Short video demonstration

Documentation updates include:

- A dedicated documentation page describing certificate templates
- Step-by-step usage instructions
- Clear explanation of supported options and limitations

Out of scope
++++++++++++

The following items are explicitly out of scope for this project:

- Subject Alternative Name (SAN) support
- OCSP integration
- Automated public CA issuance (e.g. Let's Encrypt)
- Custom cryptographic policy engines
- Changes to existing OpenVPN certificate behavior

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

Applicants must demonstrate a solid understanding of Python, Django, and
JavaScript.

Experience with `OpenWISP Controller
<https://github.com/openwisp/openwisp-controller>`__ and `django-x509
<https://github.com/openwisp/django-x509>`__ is essential. Contributions
or resolved issues in these repositories are considered strong evidence of
the required proficiency.

Add more timeseries database clients to OpenWISP Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/tsdb.png

.. important::

    Languages and technologies used: **Python**, **Django**, **InfluxDB**,
    **Elasticsearch**.

    **Mentors**: *Gagan Deep*, *Aryaman*, *Sankalp*.

    **Project size**: 350 hours.

    **Difficulty rate**: medium.

The goal of this project is to add more Time Series DB options to OpenWISP
while keeping good maintainability.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

The applicant must demonstrate good understanding of `OpenWISP Monitoring
<https://github.com/openwisp/openwisp-monitoring#openwisp-monitoring>`__,
and demonstrate basic knowledge of `NetJSON format
<https://netjson.org/>`_, **InfluxDB** and **Elasticsearch**.

Expected outcomes
+++++++++++++++++

- Complete the support to `Elasticsearch
  <https://github.com/elastic/elasticsearch>`_. `Support to Elasticsearch
  was added in 2020
  <https://github.com/openwisp/openwisp-monitoring/pull/164>`_ but was not
  completed.

  - The old pull request has to be updated on the current code base
  - The merge conflicts have to be resolved
  - All the tests must pass, new tests for new charts and metrics added to
    *InfluxDB* must be added (see `[feature] Chart mobile
    (LTE/5G/UMTS/GSM) signal strength #270
    <https://github.com/openwisp/openwisp-monitoring/pull/294>`_)
  - The usage shall be documented, we must make sure there's at least one
    dedicated CI build for **Elasticsearch**
  - We must allow to install and use **Elasticsearch** instead of
    **InfluxDB** from `ansible-openwisp2
    <https://github.com/openwisp/ansible-openwisp2>`_ and `docker-openwisp
    <https://github.com/openwisp/docker-openwisp/>`_
  - The requests to Elasticsearch shall be optimized as described in
    `[timeseries] Optimize elasticsearch #168
    <https://github.com/openwisp/openwisp-monitoring/issues/168>`_.

- `Add support for InfluxDB 2.0
  <https://github.com/openwisp/openwisp-monitoring/issues/274>`_ as a new
  timeseries backend, this way we can support both ``InfluxDB <= 1.8`` and
  ``InfluxDB >= 2.0``.

  - All the automated tests for **InfluxDB 1.8** must be replicated and
    must pass
  - The usage and setup shall be documented
  - We must make sure there's at least one dedicated CI build for
    Elasticsearch
  - We must allow choosing between **InfluxDB 1.8** and **InfluxDB 2.0**
    from `ansible-openwisp2
    <https://github.com/openwisp/ansible-openwisp2>`_ and `docker-openwisp
    <https://github.com/openwisp/docker-openwisp/>`_.

.. _gsoc-2026-vpn-deployer:

OpenWISP VPN Deployer Linux Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/2025/vpn-sync.webp

.. important::

    Languages and technologies used: **Linux**, **Python**, **Django**,
    **WebSockets**, **OpenVPN**, **WireGuard**, **WireGuard over VXLAN**,
    **ZeroTier**.

    **Mentors:** *Federico Capoano*, *Gagan Deep*, *Oliver Kraitschy*.

    **Project size:** 350 hours.

    **Difficulty level:** medium/hard.

This GSoC project aims to simplify the deployment and management of VPN
servers integrated with OpenWISP.

The goal is to develop an easy-to-install program that automates the
deployment of VPN servers synchronized with OpenWISP in real time. This
reduces manual intervention and ensures configuration consistency between
the VPN server objects in the OpenWISP database and the deployed VPN
instances.

Key Features
++++++++++++

The program will run on Linux-based servers and will:

- Be implemented in **Python** to ensure maintainability and
  extensibility, it should be a Python package installable via ``pip``.
- Use a **Makefile** to generate installation packages for major Linux
  distributions:

  - **DEB** (for Debian, Ubuntu, and related distributions)
  - **RPM** (for Red Hat, Fedora, and similar systems)

- Provide **Docker support** to run the VPN deployer as a containerized
  service, enabling easy deployment alongside docker-openwisp. We suggest
  running the deployer and VPN server(s) within the same container to keep
  the architecture simple, using host networking mode. Configuration
  management could be achieved via a configuration file (YAML is
  recommended for readability) mountable into the container. Contributors
  should verify these suggestions through research and propose the most
  suitable approach for their implementation.
- Establish a **WebSocket connection** with OpenWISP to listen for changes
  in VPN server configurations and synchronize local settings accordingly.
  The connection should handle reconnection automatically. We suggest
  retrying WebSocket connections indefinitely and using exponential
  backoff for HTTP requests, but contributors should propose a robust
  reconnection strategy.
- Keep the local list of peers updated whenever VPN clients are added,
  removed, or modified.
- Receive **real-time updates** via WebSocket when certificate revocation
  occurs, ensuring the **Certificate Revocation List (CRL)** is always
  current. The deployer needs to handle OpenVPN server reload when CRL
  updates are received. Initial research indicates that OpenVPN does not
  automatically reload CRL files when they change, and that sending a
  ``SIGUSR1`` signal to the OpenVPN process may reload the CRL without
  disconnecting existing clients. Contributors must verify this approach
  and propose the best solution based on their findings.
- Support the following VPN tunneling technologies (in order of
  implementation priority):

  1. **OpenVPN** (most complex due to CRL requirements)
  2. **WireGuard**
  3. **ZeroTier**
  4. **WireGuard over VXLAN** (VXLAN part is tricky)

- Provide a **command-line utility** to simplify the initial setup. This
  utility will:

  - Guide users step by step, making it accessible even to those with
    limited experience.
  - Support **non-interactive/scripted mode** for automation and Docker
    deployments (minimal implementation).
  - Allow users to select the VPN technology to be deployed.
  - Verify that the necessary system packages are installed and provide
    clear warnings if dependencies are missing. We suggest maintaining a
    mapping of required packages per distribution and VPN technology, as
    package names vary between Linux distributions (e.g., Debian
    ``openvpn`` vs. RHEL ``openvpn``), but contributors should propose
    their approach.
  - Store configuration in a YAML configuration file (mountable in Docker
    environments). Other formats may be considered if justified.
  - Assist in securely connecting and synchronizing with OpenWISP.

    .. note::

        The command-line utility must apply all necessary changes in the
        OpenWISP database via the **REST API**. If any required
        modifications cannot be performed with the current API, the
        contributor will be responsible for implementing the missing
        functionality.

    - To facilitate authentication, the utility will `guide users in
      retrieving their OpenWISP REST API token
      <https://github.com/openwisp/openwisp-users/issues/240>`_. A
      proposed approach is to provide a link to the OpenWISP admin
      interface, where users can generate and copy their API token easily.
      The WebSocket connection should authenticate using this API token.

- Support running **multiple instances**, where each instance manages a
  separate VPN server independently. Each instance could be identified by
  a dedicated configuration file or other suitable mechanism.
- Implement **structured logging** with dedicated log files for each
  instance, adhering to Linux logging best practices and supporting log
  rotation.
- Provide **comprehensive documentation** in ReStructuredText format,
  following OpenWISP conventions:

  - Documentation will be stored in a ``/docs`` directory, with a clear
    separation between user guides and developer documentation.
  - A **video demonstration** will be included, which can be published on
    YouTube to increase project visibility.

- Update the **OpenWISP documentation** to cover installation,
  configuration, and best practices.
- To support this project, **OpenWISP Controller** will need to be updated
  as follows:

  - Expose a **WebSocket endpoint** to allow the VPN synchronization
    program to receive real-time configuration updates.
  - **Automatically include the Certificate Revocation List (CRL)** in
    generated OpenVPN server configurations. The CRL content should be
    provided as a configuration variable (e.g., ``crl_content``, similar
    to x509 certificates), eliminating the need for manual CRL file
    management. The CRL file path should be determined as part of the
    implementation. When certificates are revoked, the system must trigger
    WebSocket notifications to connected VPN deployer instances to ensure
    immediate CRL updates. Additionally, the deployer should periodically
    poll the CRL checksum via HTTP API as a redundancy measure.
  - Define a **permission model** for the VPN deployer: the deployer
    requires a dedicated user account with organization manager role and
    permissions to add/change VPN servers within that organization.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

Applicants should have a solid understanding of:

- **Python** and **Django**.
- **WebSockets**.
- Experience with `OpenWISP Controller
  <https://github.com/openwisp/openwisp-controller>`__ is essential.
  Experience with `django-x509
  <https://github.com/openwisp/django-x509>`__ `netjsonconfig
  <https://github.com/openwisp/netjsonconfig>`__ is considered as a strong
  favorable point. Contributions in these repositories are considered
  strong evidence of the required proficiency.
- At least one of the supported VPN technologies (**OpenVPN, WireGuard,
  WireGuard over VXLAN, ZeroTier**).
- **System administration and Linux packaging** (preferred but not
  required).

Expected Outcomes
+++++++++++++++++

- A Python-based VPN synchronization tool.
- A command-line setup utility for easy first-time configuration.
- WebSocket-based synchronization between VPN servers and OpenWISP.
- Automated packaging for major Linux distributions (**DEB** and **RPM**).
- **Docker support** for running the VPN deployer as a containerized
  service, including integration with docker-openwisp.
- Structured logging with proper log rotation.
- Enhancements to **OpenWISP Controller**:

  - Support for WebSocket-based synchronization.
  - Automatic inclusion of **Certificate Revocation List (CRL)** in
    OpenVPN server configurations with variable-based CRL content.
  - WebSocket notifications triggered when certificates are revoked.
  - Any required REST API modifications.

- Automated tests to ensure reliability and stability:

  - **Unit tests** with mocks for both openwisp-controller and VPN server
    interactions to enable fast development and testing of individual
    components.
  - **Integration tests** using real openwisp-controller and VPN server
    instances to test core functionality: installation, configuration
    synchronization, and basic VPN server health checks. While initially
    minimal, these provide reliability and establish a foundation for
    expanded integration testing as the project matures and sees wider
    adoption.

- Comprehensive **documentation**, including setup guides and best
  practices.
- A **short tutorial video** demonstrating installation and usage.
