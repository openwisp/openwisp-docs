Security Advisories
===================

Published OpenWISP security advisories and historical security fixes are
listed below, most recent first. Follow the links for details and upgrade
guidance.

- **2026-09-15, OpenWISP RADIUS (GHSA-pfx3-4m53-g475):** `SMS verification
  bypasses destination and IP restrictions
  <https://github.com/openwisp/openwisp-radius/security/advisories/GHSA-pfx3-4m53-g475>`_.
- **2026-06-15, OpenWISP IPAM (GHSA-x287-5c68-36wp):** `Broken
  object-level authorization allows exporting another organization's
  subnet and IP addresses
  <https://github.com/openwisp/openwisp-ipam/security/advisories/GHSA-x287-5c68-36wp>`_.
- **2024-08-20, OpenWISP WiFi Login Pages:** `Replaced the compromised
  polyfill.io script source to prevent malicious JavaScript delivery
  <https://groups.google.com/g/openwisp/c/4nfhep0lFIg>`_.
- **2022-06-28, OpenWISP Users 1.0.2:** `Updated django-allauth to fix
  social-account linking CSRF and password-reset rate-limit bypasses
  <https://github.com/openwisp/openwisp-users/blob/1.0.2/CHANGES.rst#version-102-2022-06-28>`_.
- **2021-07-01, Ansible OpenWISP and Docker OpenWISP:** `Fixed nginx alias
  path traversal exposing files outside the static and media directories
  <https://groups.google.com/g/openwisp/c/jnyGtkH0eIY>`_.
- **2021-04-09, OpenWISP Controller:** `Fixed internal HTTP endpoints
  exposing other organizations' UUIDs and sensitive information
  <https://groups.google.com/g/openwisp/c/lxcwmV5onm0>`_.

Announcements are also sent to the `OpenWISP mailing list
<https://groups.google.com/d/forum/openwisp>`_. To report a new suspected
vulnerability privately, follow the instructions in
:doc:`disclosing-vulnerabilities`.
