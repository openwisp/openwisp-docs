:orphan:

Roadmap
=======

Installation & Usability
------------------------

- Make OpenWISP easier to install and configure for newcomers by
  simplifying the installation process and reducing the learning curve.
- Address feedback that OpenWISP feels heavy and hard to use by:

  - Providing a simplified installer for users managing small networks
    (e.g., up to 50 devices).
  - Streamlining the interface and default behavior to feel lighter and
    more approachable.

- Improve the user experience based on the UX study conducted by Ura
  Design.
- Notify users via the UI when a new version of OpenWISP is available.
- Simplify the upgrade process:

  - Explore the feasibility of guided upgrades via the UI.
  - Automatically back up everything before upgrading.
  - Automatically restore if the upgrade fails.

Firmware Tools
--------------

- Provide tools for all OpenWrt-supported targets:

  - Pre-built OpenWrt firmware images that are ready to use and configured
    to connect to ``demo.openwisp.io``.
  - Pre-built OpenWrt image builders for all targets that allow users to
    quickly generate custom firmware images.

- Automate the compilation and publishing of firmware images and image
  builder in order to ease maintenance and keeping up with new OpenWrt
  releases.

Documentation
-------------

- Create more detailed, step-by-step tutorials for:

  - Hotspot setup.
  - PPPoE configuration.
  - Hooking custom actions on specific events, eg: open a Jira ticket
    whenever a device goes into critical state.

Agent Improvements
------------------

- Eliminate the need for users to manually configure the management
  interface in the OpenWISP agent, particularly during demo/testing.
- The agent should automatically detect the management tunnel and
  determine the correct IP address to use for operations like:

  - Ping (checksum)
  - Remote shell
  - Active checks

Monitoring Logic Enhancements
-----------------------------

- If a device is sending checksum requests and monitoring data, but the
  tunnel is down:

  - Show device as “PROBLEM” instead of “CRITICAL”.

- A device should only be in the “CRITICAL” state if:

  - It is unreachable *and* not receiving any monitoring data.

- Add a new metric to track the presence of monitoring requests from the
  device.
- Modify the logic for critical metrics to allow combining multiple
  metrics using logical AND conditions.

Management Tunnel Notifications
-------------------------------

- If no management tunnel is working, the agent should report this to the
  administrator.
- Notify the user, but avoid spamming them with repeated alerts.
- Consider alternative ways to communicate tunnel issues clearly without
  excessive notifications.

Notification Preferences
------------------------

- Improve notification settings and customization (GSoC 2024).

IP Intelligence
---------------

- In the controller:

  - Collect and store WHOIS information for `last_ip` if it is a public
    IP.
  - Display a summary in the UI and allow expanding to view more detailed
    WHOIS data. (GSoC 2025)

Geo App Improvements
--------------------

- Add support for fuzzy locations based on IP geolocation.
- UI should explain how these are generated and show suggestions to:

  - Edit to precise location.
  - Disable the feature if undesired.

- Allow this feature to be disabled globally and per-organization. (GSoC
  2025)

Syslog & Event Hooks
--------------------

- Add support for collecting syslog entries.
- Allow triggering alerts or actions based on syslog data.

SNMP Monitoring
---------------

- Finalize and polish SNMP monitoring support for OpenWrt and AirOS.
- Build upon the GSoC 2021 work, which is incomplete but provides a
  foundation.

Wireless Support
----------------

- Implement full support for 802.11k and 802.11v (band steering, load
  balancing).
- Offer features equivalent to the OpenWrt LuCI interface directly in the
  OpenWISP device page in a user-friendly format.

Configuration Editor
--------------------

- Rebuild the configuration editor to:

  - Improve usability.
  - Display the full device configuration in a readable format.
  - Visually differentiate: - Pre-existing device configuration. -
    Device-specific configuration in OpenWISP. - Template-based
    configuration in OpenWISP.

- Enable devices to send their full configuration to OpenWISP.
- OpenWISP must identify and exclude duplicate data already stored in
  device or template config.
- The editor should clearly indicate what config comes from where.
- Add full support for inserting variables in all field types, not just
  strings.
- Support defining configuration context using non-string types (e.g.,
  lists).

Firmware Upgrade UX
-------------------

- Add support for upgrading all devices in a specific group (currently
  only per device or per org). (GSoC 2025)
- Improve the visual feedback of firmware upgrades to show real-time
  progress without requiring page reloads. (GSoC 2025)

Mesh Networking
---------------

- Improve mesh network support by enabling synchronized configuration
  updates for groups of devices.
- This ensures that changes like radio channel adjustments don’t break the
  mesh during rollout.
- Use monitoring data to build real-time mesh topology maps by identifying
  connected mesh interfaces.

Dashboard & Visualization
-------------------------

- Add general time-series charts with filters on the dashboard:

  - Total traffic over time.
  - Device count trends (online, offline, etc).

- Complete the rewrite of `netjsongraph.js` (GSoC 2019 branch):

  - Integrate it into OpenWISP.
  - Replace current minimal map with an advanced viewer similar to:
    https://regensburg.freifunk.net/meshviewer/

- Support toggling between geographic and logical network views.

Indoor Maps
-----------

- Implement full indoor map support to:

  - View devices per floor inside buildings.
  - Drill down from geographic/logical views into indoor view.
  - Zoom out back from indoor to geo/logical views. (GSoC 2025)

Monitoring Improvements
-----------------------

- Address open issues scheduled for Monitoring 0.3 release:
  https://github.com/openwisp/openwisp-monitoring/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22OpenWISP+Monitoring+0.3+Release%22

Networking Features
-------------------

- Add support for ZeroTier.
- Add support for Hotspot 2.0 and WiFi Offloading in OpenWISP RADIUS.
- Add support for:

  - Deep Packet Inspection (DPI) and layer-7 firewall rules.
  - WPA Enterprise EAP-TLS (OpenWISP RADIUS).
  - pfSense
  - Vyatta
  - TR-069 / TR-369
  - NETCONF
  - CAPWAP

- Complete support for managing Ubiquiti AirOS original firmware.
