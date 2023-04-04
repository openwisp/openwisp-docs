OpenWISP Demo
=============

.. image:: ../images/demo/demo.png
    :target: ../_images/demo.png

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

Accessing the demo system
-------------------------

- **URL**: `demo.openwisp.io <https://demo.openwisp.io/>`_
- **Username**: demo
- **Password**: tester123

The content of the demo organization is reset every day at 1:00 UTC.

The password of the demo user is reset every minute.

For security reasons, the demo user is
not allowed to use the following features:

* delete existing devices
* sending custom shell commands to devices
* sending password change commands to devices
* uploading new firmware builds
* launch firmware upgrade operations
* create new users or change the details of the demo organization
* changing the details of RADIUS groups

If you want to test the features above you can request
a free 30 days trial, the form to request the free trial
will pop up while using the demo system.

Firmware instructions (flashing OpenWISP Firmware)
--------------------------------------------------

We host an OpenWrt based firmware which ships all the packages
that are commonly used in OpenWISP installations.

This firmware will help you get up to speed and test the main features
of the OpenWISP cloud quickly.

If for some reason your prefer to use the firmware you already have,
read the
:ref:`the alternative instructions <alternative_firmware_instructions>`.

1. Downloading the firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open `downloads.openwisp.io <http://downloads.openwisp.io/?prefix=firmware/22.03/ath79/>`_
and select the target architecture and image for your device.

At the moment we are generating the firmware only for ath79,
but we will be adding more targets over time.

If your device is missing, let us know via the
`support channels <https://openwisp.org/support.html>`__,
in the meantime you can use
:ref:`the alternative instructions <alternative_firmware_instructions>`.

2. Flashing the firmware
~~~~~~~~~~~~~~~~~~~~~~~~

You can `Flash the firmware via web UI
<https://openwrt.org/docs/guide-user/installation/generic.sysupgrade>`_,
or via `other means available on OpenWrt
<https://openwrt.org/docs/guide-user/installation/generic.flashing>`_.

Make sure not to keep settings
(supply the ``-n`` command line option to sysupgrade, for the web UI
there is a specific checkbox).

.. _alternative_firmware_instructions:

Alternative firmware instructions
---------------------------------

If your device is missing from our list of available firmware images
or if you have a custom firmware you do not want to lose, you can
get the basic features working by downloading and installing the
following packages on your device:

- openwisp-config
- openwisp-monitoring (and its dependency netjson-monitoring)

The easiest thing is to use the following commands:

.. code-block::

    opkg update
    opkg install openwisp-config
    opkg install openwisp-monitoring

However, if you want to install more recent versions of the packages
you can use download the packages from
`downloads.openwisp.io <http://downloads.openwisp.io/>`__ on your
device and install them, eg:

.. code-block::

    opkg update
    cd /tmp

    # WARNING: the URL may change overtime, so verify the right URL
    # from downloads.openwisp.io

    wget https://downloads.openwisp.io/openwisp-config/latest/openwisp-config_1.1.0a-1_all.ipk
    wget https://downloads.openwisp.io/openwisp-monitoring/latest/netjson-monitoring_0.1.1-1_all.ipk
    wget https://downloads.openwisp.io/openwisp-monitoring/latest/openwisp-monitoring_0.1.1-1_all.ipk
    opkg install openwisp-config_1.1.0a-1_all.ipk
    opkg install netjson-monitoring_0.1.1-1_all.ipk
    opkg install netjson-monitoring_0.1.1-1_all.ipk
    opkg install openwisp-monitoring_0.1.1-1_all.ipk

.. note::
  If ``wget`` doesn't work (eg: SSL issues), you can use ``curl``,
  or alternatively you can download the packages on your machine
  and from there upload them to your device via ``scp``.

Once the packages are installed, copy the following contents to
``/etc/config/openwisp``:

.. code-block::

  config controller 'http'
      option url 'https://cloud.openwisp.io'
      # the following shared secret is for the demo organization
      option shared_secret 'nzXTd7qpXKPNdrWZDsYoMxbGpOrEVjeD'
      option management_interface 'tun0'

Once the configuration has been changed, you will need to restart
the agent:

.. code-block::

    service openwisp_config restart

Connecting your device to OpenWISP
----------------------------------

.. image:: ../images/demo/lan-ports.jpg

Once your device is flashed, connect an ethernet cable from your LAN into
one of the available LAN ports.

DHCP client mode
~~~~~~~~~~~~~~~~

Assuming your LAN is equipped with a DHCP server (usually your
main ISP router), after booting up, the device will be assigned an
IP address from the LAN DHCP server, at this point the device
should be able to reach the internet and hence register to the
OpenWISP demo system.

Static address mode
~~~~~~~~~~~~~~~~~~~

If your LAN does not have a DHCP server you will need to configure the
a static ip address and gateway address to the LAN interface.

Registration
~~~~~~~~~~~~

.. image:: ../images/demo/device-list-registered.png
    :target: ../_images/device-list-registered.png

Once the previous steps are executed correctly and the device can
reach the internet, the device will register and you will be able to find
it in the list of available
devices of the demo organization, most likely you will be able to find
it by its mac address as in the screenshot above
(or by its name if you changed its name from "OpenWrt" to something else).

At this point the device should have already downloaded and applied
the configuration, in a few minutes the management tunnel will be
up and the device will start collecting monitoring information

Monitoring charts and status
----------------------------

After a few minutes, you should start noticing OpenWISP is collecting
metrics from your device, the UI will show the information similar to
the screenshots below.

Health status
~~~~~~~~~~~~~

.. image:: ../images/demo/health-status.png
    :target: ../_images/health-status.png

Device Status
~~~~~~~~~~~~~

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-1.png
    :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-1.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-2.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-2.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-3.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-3.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-4.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/device-status-4.png

Charts
~~~~~~

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/uptime.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/uptime.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/packet-loss.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/packet-loss.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/rtt.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/rtt.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/traffic.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/traffic.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/wifi-clients.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/wifi-clients.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/cpu-load.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/cpu-load.png

The following charts are displayed only for devices
with mobile connections (eg: 3G, LTE).

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/access-technology.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/access-technology.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/signal-strength.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/signal-strength.png

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/signal-quality.png
   :target: https://raw.githubusercontent.com/openwisp/openwisp-monitoring/docs/docs/signal-quality.png

Find out more information about the
:doc:`Monitoring module of OpenWISP <../user/monitoring>`.

Get help
--------

If you need help, you can write to the
`support channels <https://openwisp.org/support.html>`__ or just click
directly on "Contact support" as indicated in the screenshot below.

.. image:: ../images/demo/contact-support.png
    :target: ../_images/contact-support.png

Next steps
----------

- Try the :doc:`WiFi Hotspot & Captive Portal (Public WiFi) <./hotspot>`
  features
