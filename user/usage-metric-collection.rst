Collection of Usage Metrics
===========================

The ``openwisp-utils`` module includes an optional
sub-app ``openwisp_utils.measurements``.

This sub-app allows the collection of the following information:

- OpenWISP Version
- List of enabled OpenWISP modules and their version
- Operating System identifier, e.g.:
  Linux version, Kernel version, target platform (e.g. x86)
- Installation method, if available, e.g. `ansible-openwisp2
  <https://github.com/openwisp/ansible-openwisp2>`_
  or `docker-openwisp <https://github.com/openwisp/docker-openwisp>`_

The data above is collected in the following events:

- **Install**: when OpenWISP is installed the first time
- **Upgrade**: when any OpenWISP module is upgraded
- **Heartbeat**: once every 24 hours

We collect data on OpenWISP usage to gauge user engagement, satisfaction,
and upgrade patterns. This informs our development decisions, ensuring
continuous improvement aligned with user needs.

To enhance our understanding and management of this data, we have
integrated `Clean Insights <https://cleaninsights.org/>`_, a privacy-preserving
analytics tool. Clean Insights allows us to responsibly gather and analyze
usage metrics without compromising user privacy. It provides us with the
means to make data-driven decisions while respecting our users'
rights and trust.

We have taken great care to ensure no
sensitive or personal data is being tracked.
