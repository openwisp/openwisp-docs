Configure Your OpenWrt Devices
==============================

This page will guide you through installing the
:doc:`/openwrt-config-agent/index` on a device that supports `OpenWrt
<https://openwrt.org/>`_.

.. hint::

    **No physical device? No problem!** You can try OpenWISP using a
    Virtual Machine.

.. contents:: **Table of Contents**:
    :depth: 3
    :local:

Prerequisites
-------------

Ensure you have already :ref:`Installed the OpenWISP Server Application
<install_server>` and :doc:`Configured a Management Network </user/vpn>`.

Flash OpenWrt on Your Device
----------------------------

If you have a compatible network device, follow the `official OpenWrt
flashing guide
<https://openwrt.org/docs/guide-user/installation/generic.flashing>`_.

If you don't have a physical device, you can `install OpenWrt on a
VirtualBox Virtual Machine
<https://openwrt.org/docs/guide-user/virtualization/virtualbox-vm>`_.

.. note::

    Enable SSH access and connect the device or VM to the internet.

    When using VirtualBox, both Adapter1 and Adapter2 should use "Adapter
    Type: Intel PRO/1000 MT Desktop". Use a different IP address for the
    OpenWrt device than the one used for the local OpenWISP website (e.g.,
    if your OpenWISP site uses 192.168.56.2, use 192.168.56.3 for the
    OpenWrt device).

Install the Config Agent
------------------------

Refer to the :doc:`Config Agent Quick Start Guide
</openwrt-config-agent/user/quickstart>`.

Install the Monitoring Agent
----------------------------

Refer to the :doc:`Monitoring Agent Quick Start Guide
</openwrt-monitoring-agent/user/quickstart>`.

Compile Your Own OpenWrt Image
------------------------------

.. note::

    This section is for advanced users.

Compiling a custom OpenWrt image can save time when configuring new
devices. By doing this, you can pre-install openwisp-config and include
your configurations (e.g., ``url`` and ``shared_secret``). This way, you
won't have to configure each new device manually, which is particularly
useful if you manage many devices.

Refer to the :doc:`guide on compiling a custom OpenWrt image
</openwrt-config-agent/user/compiling>` for detailed instructions.
