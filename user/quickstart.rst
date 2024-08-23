Quick Start Guide
=================

.. contents:: **Get started with OpenWISP!**
    :depth: 3
    :local:

Try the Demo
------------

Before installing OpenWISP, we recommend trying out the :doc:`OpenWISP
Demo system </tutorials/demo>`. This will give you a great overview of how
the system works.

Once you have explored the demo, you can install your own instance by
following the instructions below.

.. _install_server:

Install OpenWISP
----------------

For production usage, we recommend :doc:`Deploying OpenWISP with the
Ansible OpenWISP role </ansible/user/quickstart>`.

Alternatively, you can use :doc:`Docker OpenWISP
</docker/user/quickstart>`.

Make Sure OpenWISP Can Reach Your Devices
-----------------------------------------

For smooth operations, please :doc:`Setup a Management Network
</user/vpn>`.

Configure Your OpenWrt Devices
------------------------------

Follow the guide to :doc:`Configure Your OpenWrt Devices
<./configure-device>`.

If you don't have a physical OpenWrt-compatible device, you can install
OpenWrt in a VirtualBox VM. The guide above covers how to do this.

Learn More
----------

Once you have everything set up, we recommend exploring other sections of
this documentation to make the most out of OpenWISP.

Depending on your use case, you might be interested in different features:

- **Automating Configuration Provisioning**: If your primary interest is
  automating the provisioning of configurations for OpenWrt devices, check
  out the :doc:`Controller module </controller/index>`.
- **Device Monitoring**: For those who need monitoring information from
  their devices, the :doc:`Monitoring module </monitoring/index>` will be
  particularly useful.
- **WiFi Connectivity and Security**: If you're focused on providing WiFi
  Hotspot connectivity or WPA Enterprise WiFi, take a look at the
  :doc:`RADIUS </user/radius>` and :doc:`WiFi Login Pages
  </wifi-login-pages/index>` modules.

Additionally, we offer tutorials for the most common scenarios:

- :doc:`Open and/or WPA Protected WiFi Access Point SSID
  <../tutorials/wifi-access-point>`
- :doc:`WiFi Hotspot, Captive Portal (Public WiFi), Social Login
  <../tutorials/hotspot>`
- :doc:`Setting Up WPA Enterprise (EAP-TTLS-PAP) Authentication
  <../tutorials/wpa-enterprise-eap-ttls-pap>`
- :doc:`Setting Up a Wireless Mesh Network <../tutorials/mesh>`

Explore these resources to fully leverage the capabilities of OpenWISP!

Seek Help
---------

Reach out to the `Community Support Channels
<http://openwisp.org/support.html>`_.
