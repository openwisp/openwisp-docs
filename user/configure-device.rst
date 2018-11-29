Connect OpenWRT to OpenWISP2
============================

This page will guide you through the installation of
`openwisp-config <https://github.com/openwisp/openwisp-config>`_ on a
device which supports `OpenWRT <https://openwrt.org/>`_.

If you don't have a physical device available but you still want to try
out OpenWISP, you can use a Virtual Machine.

1. Install OpenWISP2
--------------------

Refer to the  `OpenWISP 2 installation tutorial
<https://github.com/openwisp/ansible-openwisp2#usage-tutorial>`_

2. Install OpenWRT on VirtualBox
--------------------------------

.. note::
    **You can skip this part if you plan on installing openwisp-config on
    a physical device.**

Download ``combined-ext4.img.gz`` from `this
page <https://downloads.openwrt.org/releases/18.06.1/targets/x86/64/>`__.
The other images may not work well.

Extract the downloaded file and convert the image file to a `VirtualBox
<https://www.virtualbox.org/>`_ disk:

.. code-block:: bash

    VBoxManage convertfromraw --format VDI
    openwrt-18.06.1-x86-64-combined-ext4.img
    openwrt-18.06.1-x86-64-combined-ext4.vdi

If you encounter an error about ``VERR_ID_INVALID_SIZE``, you need to
pad the image with the following command:

.. code-block:: bash

    dd if=openwrt-18.06.1-x86-64-combined-ext4.img
    of=openwrt-18.06.1-x86-64-padded.img bs=128000 conv=sync

And then try to convert the padded image using the previous command.

Next, open up VirtualBox and create a VM. Load up the VDI and then start
the machine. If done correctly, it should boot to a GRUB menu and then
proceed with initialization. When the text stops scrolling, simply press
Enter to activate the terminal.

.. note::

    Continue with the procedures in

    `the OpenWRT virtualbox guide <https://openwrt.org/docs/guide-user/virtualization/virtualbox-vm>`_.
    It's required to enable SSH access and connect the VM to the internet.

    Note that both Adapter1 and Adapter2 use
    "Adapter Type: Intel PRO/1000 MT Desktop". Also, please do
    not use the same IP Address that you used for the local OpenWISP
    website you hosted before. That suggested change applies only when
    you boot into the OpenWRT device as per the description of the
    above link (for example, if you set 192.168.56.2 as the IP Address
    of your local OpenWISP website, please use another IP such as
    192.168.56.3 for the IP Address of the OpenWRT device).


3. Install openwisp-config on your OpenWRT instance
---------------------------------------------------

Installation
~~~~~~~~~~~~

Run the following commands on your device:

.. code-block:: bash

    opkg update
    opkg install <URL>

Replace ``<URL>`` with the link to one of the latest build,
available on `downloads.openwisp.io <http://downloads.openwisp.io/openwisp-config/latest/>`__.
For this guide, let's choose the ``openssl`` variant.

Configuration
~~~~~~~~~~~~~

Once it's installed, we need to configure it to connect to our OpenWISP2
controller. To do that, edit the config file located at
``/etc/config/openwisp``.

You will see the default config file, something like the following
(if your instance lacks some of the lines in the following,
please add them):

::

    # For more information about the config options please see the README
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
        #option uuid ''
        #option key ''
        list unmanaged 'system.@led'
        list unmanaged 'network.loopback'
        list unmanaged 'network.@switch'
        list unmanaged 'network.@switch_vlan'
        # curl options
        #option connect_timeout '15'
        #option max_time '30'
        #option capath '/etc/ssl/certs'

Uncomment and change the following fields:

- ``url``: the hostname of your OpenWISP2 controller (for example, if
  you are hosting your OpenWISP server locally and you set the IP Address
  to "192.168.56.2", the url would be ``https://192.168.56.2/``).
- ``verify_ssl``: set to ``0`` if your controller's SSL certificate is
  self-signed; in production you will need a valid SSL certificate to
  keep your instance secure
- ``shared_secret``: you can retrieve this from OpenWISP2 admin panel, in
  the Organization settings. The list of organizations is available at
  ``/admin/openwisp_users/organization/``.

Save the file and start openwisp-config:

.. code-block:: bash

    /etc/init.d/openwisp_config start

Your OpenWRT instance should register itself to your openwisp2 controller.
Check the devices menu on the admin panel to make sure your OpenWRT
instance is registered.

Compile your own OpenWRT image
------------------------------

You may want to compile a custom OpenWRT image to save time on configuring
new devices. By compiling a custom image, you can pre-install
openwisp-config, including your configurations (e.g. ``url`` and
``shared_secret``), so that you won't have to go through the configuration
process again.

This will make you save a lot of time if you need to manage many devices!

A guide on `how to compile a custom OpenWRT image available in the
openwisp-config documentation
<https://github.com/openwisp/openwisp-config#compiling-a-custom-openwrt-image>`_.

A guide on :doc:`template configurations and sample configurations 
is available at the Template Configurations section of this documentation  <./template>`.


 