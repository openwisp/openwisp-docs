Connect OpenWRT to OpenWISP
===========================

This page will guide you through the installation of
`openwisp-config <https://github.com/openwisp/openwisp-config>`_ on a
device which supports `OpenWRT <https://openwrt.org/>`_.

**If you don't have a physical device available but you still want to try
out OpenWISP, you can use a Virtual Machine**.

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

1. Install OpenWISP
-------------------

Refer to the instructions described in
:ref:`Install the OpenWISP server application <install_server>`.

2. Flash OpenWRT on a device
----------------------------

If you have a physical OpenWRT compatible hardware, follow the
instructions in the `official OpenWRT flashing guide
<https://openwrt.org/docs/guide-user/installation/generic.flashing>`_.

If you don't have a physical device, you can
`install OpenWrt on a VirtualBox Virtual Machine
<https://openwrt.org/docs/guide-user/virtualization/virtualbox-vm>`_.

.. note::

    It's required to enable SSH access and connect the device or
    VM to the internet.

    Note that when using Virtualbox, both Adapter1 and Adapter2 use
    "Adapter Type: Intel PRO/1000 MT Desktop". Also, please do
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

Install openwisp-config on your OpenWRT system.
For this guide.

We recommend to install one of the latest stable builds from
`downloads.openwisp.io <http://downloads.openwisp.io/?prefix=openwisp-config/>`_,
copy the URL of the ipk file you want to download in your
clipboard and then run the following commands on your OpenWrt device:

.. code-block:: bash

    cd /tmp  # /tmp runs in memory
    wget <URL-you-just-copied>
    opkg update
    opkg install ./<file-just-downloaded>

Alternatively, you can also use the curl method instead of wget to install the ipk file:

.. code-block:: bash

    curl -o <some-file-name>.ipk <URL-you-just-copied>
    opkg install <some-file-name>.ipk


If you're running at least OpenWRT 19.07, you can install openwisp-config
from the official OpenWRT packages:

.. code-block:: bash

    opkg update
    opkg install openwisp-config

**We recommend installing from our latest builds or compiling your own
firmware image**. The OpenWrt packages are not always up to date.

If all the above methods fail you can:

- Download the ipk file on your system.
- Use SCP to transfer the file to the Openwrt system.
- Install using opkg.

Configuration
~~~~~~~~~~~~~

Once openwisp-config is installed, we need to configure
it to connect to our OpenWISP2
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

- ``url``: the hostname of your OpenWISP2 controller (for example, if
  you are hosting your OpenWISP server locally and you set the IP Address
  to "192.168.56.2", the url would be ``https://192.168.56.2``).
- ``verify_ssl``: set to ``'0'`` if your controller's SSL certificate is
  self-signed; in production you will need a valid SSL certificate to
  keep your instance secure
- ``shared_secret``: you can retrieve this from OpenWISP2 admin panel, in
  the Organization settings. The list of organizations is available at
  ``/admin/openwisp_users/organization/``.
- ``management_interface``: the name of the interface which OpenWISP
  can use to reach the device when it needs to,
  for more information **we highly recommend to read**:
  :ref:`how to make sure OpenWISP can reach your devices
  <openwisp_reach_devices>`.

.. note::

    When testing or developing using the Django development server
    directly from your computer, make sure the server listens on all
    interfaces (``./manage.py runserver 0.0.0.0:8000``) and then just
    point openwisp to use your local IP address
    (e.g. ``http://192.168.1.34:8000``)

Save the file and start openwisp-config:

.. code-block:: bash

    /etc/init.d/openwisp_config restart

Your OpenWRT instance should register itself to your openwisp2 controller.
Check the devices menu on the admin panel to make sure your OpenWRT
instance is registered.

Compile your own OpenWRT image
------------------------------

You may want to compile a custom OpenWRT image to save time in configuring
new devices. By compiling a custom image, you can pre-install
openwisp-config, including your configurations (e.g. ``url`` and
``shared_secret``), so that you won't have to go through the configuration
process again.

This will make you save a lot of time if you need to manage many devices!

A guide on `how to compile a custom OpenWRT image available in the
openwisp-config documentation
<https://github.com/openwisp/openwisp-config#compiling-a-custom-openwrt-image>`_.
