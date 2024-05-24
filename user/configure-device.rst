Connect OpenWRT to OpenWISP
===========================

This page will guide you through the installation of
`openwisp-config <https://github.com/openwisp/openwisp-config>`_ on a
device which supports `OpenWRT <https://openwrt.org/>`_.

**If you don't have a physical device available but you still want to try
out OpenWISP, you can use a Virtual Machine.**

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

1. Install OpenWISP
-------------------

Refer to the instructions described in
:ref:`Install the OpenWISP server application <install_server>`.

2. Flash OpenWRT on a device
----------------------------

If you have a network device which is compatible with OpenWRT, follow the
instructions in the `official OpenWRT flashing guide
<https://openwrt.org/docs/guide-user/installation/generic.flashing>`_.

If you don't have a physical device, you can
`install OpenWrt on a VirtualBox Virtual Machine
<https://openwrt.org/docs/guide-user/virtualization/virtualbox-vm>`_.

.. note::

    It's required to enable SSH access and connect the device or
    VM to the internet.

    Note that when using Virtualbox, both Adapter1 and Adapter2 use
    "Adapter Type: Intel PRO/1000 MT Desktop". Do
    not use the same IP Address that you used for the local OpenWISP
    website you hosted before. That suggested change applies only when
    you boot into the OpenWRT device as per the description of the
    above link (for example, if you set 192.168.56.2 as the IP Address
    of your local OpenWISP website, please use another IP such as
    192.168.56.3 for the IP Address of the OpenWRT device).

3. Install openwisp-config
--------------------------

Installation
~~~~~~~~~~~~

To install openwisp-config on your OpenWRT system follow the steps below:

Install one of the latest stable builds from
`downloads.openwisp.io <http://downloads.openwisp.io/?prefix=openwisp-config/>`_,
copy the URL of the IPK file you want to download onto your
clipboard, then run the following commands on your OpenWrt device:

.. code-block:: bash

    cd /tmp  # /tmp runs in memory
    wget <URL-you-just-copied>
    opkg update
    opkg install ./<file-just-downloaded>

If you're running at least OpenWRT 19.07, you can install openwisp-config
from the official OpenWRT packages:

.. code-block:: bash

    opkg update
    opkg install openwisp-config

**We recommend installing from our latest builds or compiling your own
firmware image** as the OpenWrt packages are not always up to date.

Configuration
~~~~~~~~~~~~~

Once openwisp-config is installed, you will need to configure
it to connect to our OpenWISP2
controller. To do that, edit the config file located at
``/etc/config/openwisp``.

You will see the default config file, as shown below.
If your instance lacks some of the lines shown in the example below,
please add them.

.. code-block:: text

    # For more information about the config options please see the README
    # or https://github.com/openwisp/openwisp-config#configuration-options

    config controller 'http'
        #option url 'https://openwisp2.mynetwork.com'
        #option interval '120'
        #option verify_ssl '1'
        #option shared_secret ''
        #option consistent_key '1'
        #option mac_interface 'eth0'
        #option management_interface 'tun0'
        #option merge_config '1'
        #option test_config '1'
        #option test_script '/usr/sbin/mytest'
        #option hardware_id_script '/usr/sbin/read_hw_id'
        #option hardware_id_key '1'
        option uuid ''
        option key ''
        # curl options
        #option connect_timeout '15'
        #option max_time '30'
        #option capath '/etc/ssl/certs'
        #option cacert '/etc/ssl/certs/ca-certificates.crt'
        # hooks
        #option pre_reload_hook '/usr/sbin/my_pre_reload_hook'
        #option post_reload_hook '/usr/sbin/my_post_reload_hook'

Uncomment and change the following fields:

- ``url``: the hostname of your OpenWISP controller. For example, if you
  are hosting your OpenWISP server locally and you set the IP Address to
  "192.168.56.2", the url would be ``https://192.168.56.2``.
- ``verify_ssl``: set to ``'0'`` if your controller's SSL certificate is
  self-signed; in production you will need a valid SSL certificate to
  keep your instance secure
- ``shared_secret``: you can retrieve this from the  OpenWISP2 admin
  panel, in the Organization settings. The list of organizations is
  available at ``/admin/openwisp_users/organization/``.
- ``management_interface``: this is the interface which OpenWISP uses to
  reach the device when it needs to. For more information
  **we highly recommend reading**:
  :ref:`how to make sure OpenWISP can reach your devices
  <openwisp_reach_devices>`.

.. note::

    When testing or developing using the Django development server
    directly from your computer, make sure the server listens on all
    interfaces (``./manage.py runserver 0.0.0.0:8000``) and then just
    point openwisp-config to use your local IP address
    (e.g. ``http://192.168.1.34:8000``)

Save the file and start openwisp-config:

.. code-block:: bash

    /etc/init.d/openwisp_config restart

Your OpenWRT instance should register itself to your OpenWISP controller.
Check the devices menu on the admin panel to make sure your OpenWRT
device is registered.

Compile your own OpenWRT image
------------------------------

You may want to compile a custom OpenWRT image to save time when
configuring new devices. By compiling a custom image, you can pre-install
openwisp-config, including your configurations (e.g. ``url`` and
``shared_secret``). This ensures that you will not have to go through
the configuration process again. This will make you save a lot of time if
you need to manage many devices!

A guide on `how to compile a custom OpenWRT image available in the
openwisp-config documentation
<https://github.com/openwisp/openwisp-config#compiling-a-custom-openwrt-image>`_.
