Roadmap to 2030
===============

This document describes the strategic evolution of the OpenWISP project
through 2030. Our objective is to consolidate OpenWISP as the most
versatile, enterprise grade, open source network management system and
controller available.

As networking environments continue to become increasingly heterogeneous,
the focus shifts toward reducing the barrier to entry while expanding the
technical reach of the platform.

The primary objectives for the 2026 to 2030 period are:

1. **Frictionless deployment**: Move toward a day one ready approach by
   simplifying installation workflows and providing clear, sensible
   default configurations that work out of the box.
2. **Refined user experience**: Improve the interface of core modules so
   that frequent operations such as device onboarding, configuration,
   monitoring, and firmware upgrades are intuitive and accessible,
   including for users with limited technical background.
3. **Community driven feature parity**: Address long standing feature
   requests from the community and reduce functional gaps compared to
   proprietary network management solutions.
4. **Ecosystem agnosticism**: Expand support beyond OpenWrt by improving
   compatibility with other operating systems and by adopting standard
   protocols such as NETCONF and YANG, as well as TR-069 and TR-369. This
   will allow OpenWISP to manage a wider range of hardware and software
   platforms, becoming useful to a larger audience.

Read on for a detailed description of the technical goals.

.. note::

    If you are interested in a specific task or would like to help shape
    the future of open source networking, please refer to:

    - :doc:`help-us`
    - :doc:`../developer/contributing`

**Table of Contents:**

.. contents::
    :depth: 2
    :local:

Installation & Usability
------------------------

Simplify the deployment and initial configuration process to lower the
entry barrier for new users.

- **Simplified Deployment**: Package Python dependencies into a unified
  archive or executable to enable single-command installation.
- **Cloud Readiness**: Provide optimized, preconfigured VM images for
  rapid deployment across major cloud providers.
- **Edge/Local Instance**: Develop a lightweight OpenWISP variant
  optimized for self-hosting on low-cost hardware, featuring:

  - Support for resource-efficient time-series databases as an alternative
    to InfluxDB.
  - SQLite and SpatiaLite support for local storage.
  - Integrated FreeRADIUS and captive portal configuration template.
  - Layer 2 auto-discovery for seamless device onboarding.

- **User Experience Studies**:

  - Implement UI/UX enhancements based on the `UX study conducted by Ura
    Design funded by the Open Tech Fund
    <https://www.figma.com/board/vAFwUleMy68NMdjslZsKWg/OpenWISP-UX-Research?node-id=0-1&t=z7w8qg3k7KYb2KZC-1>`_.
  - Conduct more UX studies and surveys as OpenWISP improves to keep
    finding the common pain points.

- **Facilitate Upgrades**:

  - Notify users through the web interface when new OpenWISP versions are
    available.
  - Evaluate guided upgrades through the web interface.
  - Verify requirements are met before attempting the upgrade (Python
    version, other system dependencies).
  - Automatically create a full backup before upgrading.
  - Automatically restore the backup if the upgrade fails.

- **Facilitate the setup of VPN automations**: See `OpenWISP VPN Deployer
  Linux Package GSoC 2025 Project Idea
  <https://openwisp.io/docs/dev/developer/gsoc-ideas-2025.html#openwisp-vpn-deployer-linux-package>`_
  for more information.

Agent Improvements
------------------

- **Automated Management Interface Detection**: Remove the requirement for
  manual configuration of the management interface in the OpenWISP agent.
  The agent will automatically identify the management tunnel and
  determine the appropriate IP address for core operations, including:

  - Connectivity monitoring (ping/checksum)
  - Remote shell access
  - Active monitoring checks

  See also: `GitHub Issue openwisp-config#208
  <https://github.com/openwisp/openwisp-config/issues/208>`_

- **Full Configuration Reporting**: Enable the agent to send the complete
  device configuration to OpenWISP, providing a comprehensive view of the
  current state directly in the controller.
- **Local Change Synchronization**: Implement automatic detection of local
  configuration changes. The agent will sync these updates back to the
  controller to ensure the central database remains accurate and local
  modifications are not overwritten.
- **Layer 2 Device Onboarding**: Enable automatic discovery and enrollment
  of network devices within the same broadcast domain. This allows
  OpenWISP to:

  - Detect new hardware as soon as it is connected to the local network.
  - Adopt and configure devices without requiring connection to a cloud
    controller.
  - Simplify local deployments by removing the need for manual IP
    discovery or static configuration.

Firmware Tools
--------------

- **Pre-configured Firmware Images**: Provide ready-to-use OpenWrt images
  for all supported targets, pre-configured to enroll into the
  :doc:`OpenWISP Demo System <../tutorials/demo>`, which would allow
  testing most OpenWISP features quickly.
- **Custom Image Builders**: Supply image builders for all targets to
  allow users to generate custom firmware locally.
- **Automated Build Pipeline**: Automate the compilation and publishing of
  firmware images and builders to ensure timely updates for new OpenWrt
  releases and reduce maintenance overhead.

Configuration Editor
--------------------

- **Enhanced Configuration Visibility**: Update the editor to manage full
  device configurations without overwhelming the interface. Implement a
  high-level overview with drill-down capabilities for specific details.
- **Data Deduplication**: Automatically identify and filter configuration
  data already stored in templates or existing device settings to prevent
  redundant entries in the database.
- **Unified Editor Interface**: Redesign the editor to display the
  complete device state with clear visual distinctions between:

  - Current local device settings.
  - Device-specific overrides stored in OpenWISP.
  - Inherited settings from OpenWISP configuration templates.

- **Expanded Variable Support**: Enable the use of variables across all
  field types beyond standard string values.
- **Rich Context Support**: Allow the definition of configuration contexts
  using non-string data types, such as lists and objects.
- **Improved Validation Feedback**: Overhaul backend error reporting to
  provide clear, actionable messages when configuration validation fails.

Documentation
-------------

**Step-by-Step Tutorials**: Develop comprehensive guides for common
deployment scenarios, including:

- Hotspot and captive portal setup.
- PPPoE configuration.
- Event-driven automation and custom hooks, such as:

  - Triggering HTTP requests when a device enters a critical state.
  - Executing HTTP requests upon receiving RADIUS accounting stop packets.

Dashboard & Visualization
-------------------------

- **Time-Series Analytics**: Add interactive dashboard charts with
  filtering capabilities to track Device status trends (online, offline,
  and total counts).
- **Advanced Network Viewer**: Replace the current map with a feature-rich
  viewer similar to `Freifunk MeshViewer
  <https://regensburg.freifunk.net/meshviewer/>`_, supporting toggling
  between geographic and logical network views.

Indoor Maps
-----------

.. note::

    These subjects have been worked on during Google Summer of Code 2025;
    see the project board `[GSoC25] General Map: Indoor, Mobile, Linkable
    URLs <https://github.com/orgs/openwisp/projects/47>`_.

- **Building and Floor Support**: Implement indoor mapping capabilities
  to:

  - View device placement per floor within buildings.
  - Provide seamless navigation between geographic, logical, and indoor
    views.

IP Intelligence
---------------

.. note::

    These subjects have been worked on during Google Summer of Code 2025;
    see the project board `[GSoC25] WHOIS Information and IP Address-Based
    Geolocation <https://github.com/orgs/openwisp/projects/44/views/1>`_.

- **WHOIS Data Collection**: Automatically collect and store WHOIS
  information for the device ``last_ip`` when a public IP is detected.
- **UI Integration**: Display a summary of WHOIS data in the interface
  with the option to expand for full technical details.

Geo App Improvements
--------------------

.. note::

    These subjects have been worked on during Google Summer of Code 2025;
    see the project board `[GSoC25] WHOIS Information and IP Address-Based
    Geolocation <https://github.com/orgs/openwisp/projects/44/views/1>`_.

- **IP-Based Geolocation**: Support approximate device locations derived
  from IP geolocation data.
- **Location Management**: The UI will clarify how approximate locations
  are generated and provide options to:

  - Manually refine the coordinates to a precise location.
  - Disable the feature for specific devices if not required.

- **Global & Multitenant Controls**: Allow geolocation features to be
  toggled globally or at the per-organization level.

Syslog & Event Hooks
--------------------

- **Centralized Log Collection**: Enable the collection and storage of
  syslog entries from OpenWrt-managed devices.
- **Log Management API**: Provide an API endpoint for querying and
  searching collected logs.
- **On-Demand Device Logs**: Add a dedicated tab to the device details
  page to load and inspect logs for specific hardware.
- **Real-Time Log Viewer**: Implement a global interface for viewing live
  log streams across all managed devices.
- **Log-Based Automation**: Allow the system to trigger alerts or custom
  actions based on specific log content or patterns.

Wireless Support
----------------

- **Optimized Roaming**: Implement support for 802.11k and 802.11v to
  facilitate band steering and network load balancing.
- **Integrated Wireless Management**: Provide a user-friendly interface
  within the OpenWISP device page that offers management parity with the
  OpenWrt LuCI wireless configuration.

Firmware Upgrade UX
-------------------

.. note::

    Part of these subjects have been worked on during Google Summer of
    Code 2025; see the project board `[GSoC25] Firmware Upgrader UX
    improvements <https://github.com/orgs/openwisp/projects/43/views/3>`_.

- **Group Upgrades**: Extend firmware upgrade capabilities to allow
  targeting specific device groups, in addition to per-device or
  per-organization options.
- **Real-Time Progress Tracking**: Enhance visual feedback to provide live
  status updates during firmware upgrades without requiring page
  refreshes.
- **Persistent Upgrade Tasks**: Implement support for continuous upgrades
  that remain queued for offline devices, executing automatically once
  they reconnect.
- **Automated Firmware Image Identification**

  - **Removal of Predefined Image Types**: Eliminates the need for
    maintainers and users to manually define and maintain firmware image
    identifiers or types.
  - **Automatic Server-Side Extraction**: The server automatically
    extracts the firmware image identifier from uploaded files to
    determine device compatibility. If automatic detection fails, the user
    will be notified and asked to provide the required information
    manually.
  - **Automatic Device Matching**: Uses the hardware identifier reported
    by ``openwisp-config`` to automatically associate devices with
    compatible firmware images. The existing behavior will continue to
    work and will be adjusted only if necessary.
  - **Improved User Experience**: Removes the need for users to customize
    the hardware definition list when using custom hardware or standard
    OpenWrt firmware images that are not yet defined in OpenWISP.
  - **Reduced Maintenance Overhead**: Avoids the need for administrators
    to track internal OpenWrt or vendor-specific image identifiers, which
    frequently change over time.

Monitoring Improvements
-----------------------

- **Database Compatibility**: Implement support for `InfluxDB 2.0
  <https://github.com/openwisp/openwisp-monitoring/issues/274>`_.
- **SNMP Support Finalization**: Complete and refine SNMP monitoring
  support for OpenWrt and Ubiquiti AirOS devices. Review and integrate
  existing code from GSoC 2021 to provide a stable monitoring baseline.
- **Rapid Health Diagnostics**: When a device status reports a "PROBLEM,"
  provide an immediate drill-down view to identify the specific root
  cause. Ensure full feature parity for these diagnostic insights via the
  REST API.
- **Asynchronous core refactoring**: Refactor core Django components to
  support asynchronous execution. This transition enables the use of the
  ``gevent`` execution pool within the Celery distributed task queue. By
  moving away from synchronous, blocking operations, OpenWISP can achieve
  higher concurrency and throughput, allowing it to manage a much larger
  number of concurrent device operations while reducing overall CPU and
  memory usage.
- **Adaptive task orchestration**: Implement an intelligent and adaptive
  Celery worker and consumer model that automatically adjusts concurrency
  based on available hardware resources.
- **Priority aware scheduling**: Introduce a scheduler that supports multi
  queue topologies with explicit priority handling. This ensures that time
  sensitive tasks, such as configuration changes and reactive network
  operations, are not delayed by resource intensive background workloads,
  such as those generated by the monitoring module.

Networking Features
-------------------

- **Bulk Command Execution**: Implement the ability to dispatch commands
  to multiple devices simultaneously, including status tracking and result
  logging for each target. Maintain REST-API feature parity.
- **Interactive Web Shell**: Develop a browser-based interactive terminal
  to allow direct command-line access to managed devices through the
  OpenWISP interface.
- **Expanded VPN Protocol Support**: Add support for IPsec and SoftEther.
- **Advanced Traffic & Access Control**:

  - Deep Packet Inspection (DPI) and Layer 7 firewall rules.
  - WPA-Enterprise EAP-TLS integration via OpenWISP RADIUS.

- **Platform & Protocol Expansion**:

  - Support for pfSense and Vyatta.
  - Management support for TR-069 / TR-369, NETCONF, and CAPWAP.
  - Integration with proprietary vendor firmwares, including Ubiquiti and
    MikroTik.

Mesh Networking
---------------

- **Atomic Group Updates**: Improve mesh stability by synchronizing
  configuration changes across groups. This prevents connectivity loss
  during rollouts (e.g., coordinated radio channel adjustments).
- **Dynamic Topology Mapping**: Utilize monitoring data from mesh
  interfaces to generate real-time topology maps of the active network.
