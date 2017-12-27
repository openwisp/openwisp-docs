Installing LEDE and connecting it to OpenWISP2
==============================================

This page will guide you through the installation of
`openwisp-config <https://github.com/openwisp/openwisp-config>`_ on a device
which supports `OpenWRT <https://openwrt.org/>`_ or `LEDE <https://lede-project.org>`_.

For simplicity, we will be installing it in a Virtual Machine running
`LEDE <https://lede-project.org>`_, an OpenWRT-based Linux OS.

1. Install OpenWISP2
--------------------

You can install OpenWISP2 by using ansible, as shown by the guide in
`this page <https://github.com/openwisp/ansible-openwisp2#usage-tutorial>`_

2. Install LEDE
---------------

.. note::
    **You may skip this part if you plan on installing openwisp-config on an
    actual device.**

Download ``combined-ext4.img.gz`` from `this
page <https://downloads.lede-project.org/snapshots/targets/x86/64>`__. The
other images may not work well.

Extract the downloaded file and convert the image file to a VirtualBox disk:

.. code-block:: bash

    VBoxManage convertfromraw --format VDI lede-x86-64-combined-ext4.img lede-x86-64-combined-ext4.vdi

If you encounter an error about ``VERR_ID_INVALID_SIZE``, you need to pad the
image with the following command:

.. code-block:: bash

    dd if=lede-x86-64-combined-ext4.img of=lede-padded.img bs=128000 conv=sync

And then try to convert the padded image using the previous command.

Next, open up VirtualBox and create a VM. Load up the VDI and then start the
machine. If done correctly, it should boot to a GRUB menu and then proceed with
initialization. When the text stops scrolling, simply press Enter to activate
the terminal.

.. note::

    Continue with the procedures in
    `this guide <https://lede-project.org/docs/user-guide/virtualbox-vm>`_.
    It's required to enable SSH access and connect the VM to the internet.

3. Install openwisp-config on your LEDE instance
------------------------------------------------

Installation
~~~~~~~~~~~~

.. note::

    An installation guide is also available
    `here <https://github.com/openwisp/openwisp-config#install-precompiled-package>`__.

Run the following commands on your device:

.. code-block:: bash

    opkg update
    opkg install <URL>

Replace ``<URL>`` with the link to one of the latest build, available
`here <http://downloads.openwisp.org/openwisp-config/latest/>`__. For this
guide, let's choose the ``openssl`` package, but any of them should work the
same.

Configuration
~~~~~~~~~~~~~

Once it's installed, we need to configure it to connect to our OpenWISP2
controller. To do that, edit the config file located at
``/etc/config/openwisp``.

You will see the default config file, something like the following:

::

    # For more information about these config options please see the README
    # or https://github.com/openwisp/openwisp-config#configuration-options

    config controller 'http'
        #option url 'https://openwisp2.mynetwork.com'
        #option interval '120'
        #option verify_ssl '1'
        #option shared_secret ''
        #option consistent_key '1'
        #option mac_interface 'eth0'
        #option merge_config '1'
        #option test_config '1'
        #option test_script '/usr/sbin/mytest'
        option uuid ''
        option key ''
        list unmanaged 'system.@led'
        list unmanaged 'network.loopback'
        list unmanaged 'network.@switch'
        list unmanaged 'network.@switch_vlan'
        # curl options
        #option connect_timeout '15'
        #option max_time '30'
        #option capath '/etc/ssl/certs'

Uncomment and change the following fields:

- ``url``: The hostname of your OpenWISP2 controller
- ``verify_ssl``: Set to ``0`` if your controller's SSL certificate is
  self-signed
- ``shared_secret``: Get it from OpenWISP2's admin panel, located at the
  Organization settings. The list of organizations is available at
  ``/admin/openwisp_users/organization/``.

Save the file and start openwisp-config:

.. code-block:: bash

    /etc/init.d/openwisp_config start

Your LEDE instance should register itself to your openwisp2 controller. Check
the devices menu on the admin panel to make sure your LEDE instance is
registered.

Compiling your own LEDE/OpenWRT image
-------------------------------------

You may want to compile a custom LEDE/OpenWRT image to save time on configuring
new devices. By compiling a custom image, you can pre-install openwisp-config,
including your configurations (e.g. ``shared_secret``), so that you wouldn't have
to go through the configuration process again. This will be very useful if you
want to manage many devices.

A guide on how to do it is available
`here <https://github.com/openwisp/openwisp-config#compiling-a-custom-lede--openwrt-image>`_.