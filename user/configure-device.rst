Configure Your OpenWrt Device
=============================

This page will guide you through installing the OpenWISP agents on a
device that supports `OpenWrt <https://openwrt.org/>`_.

.. hint::

    **No physical device? No problem!** You can try OpenWISP using a
    `Virtual Machine
    <https://openwrt.org/docs/guide-user/virtualization/virtualbox-vm>`_.

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

Install the OpenWISP OpenWrt Agents
-----------------------------------

We recommend installing the latest versions of the OpenWISP packages.
Download them onto your device from `downloads.openwisp.io
<http://downloads.openwisp.io/>`__ and then install them as follows:

.. code-block::

    cd /tmp

    # WARNING: the URL may change over time, so verify the correct URL
    # from downloads.openwisp.io

    wget https://downloads.openwisp.io/openwisp-config/latest/openwisp-config_1.1.0-1_all.ipk
    wget https://downloads.openwisp.io/openwisp-monitoring/latest/netjson-monitoring_0.2.0-1_all.ipk
    wget https://downloads.openwisp.io/openwisp-monitoring/latest/openwisp-monitoring_0.2.0-1_all.ipk
    opkg install openwisp-config_1.1.0a-1_all.ipk
    opkg install netjson-monitoring_0.2.0a-1_all.ipk
    opkg install openwisp-monitoring_0.2.0a-1_all.ipk

.. note::

    If ``wget`` doesn't work (e.g., SSL issues), you can use ``curl`` or
    alternatively download the packages onto your machine and upload them
    to your device via ``scp``.

Once the agents are installed on your OpenWrt device, let's ensure they
can connect to OpenWISP successfully.

Edit the config file located at ``/etc/config/openwisp``, which should
look like the following sample:

::

    # For more information about the config options, please see the README
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

Uncomment and update the following lines:

- ``url``: Set this to the hostname of your OpenWISP instance (e.g., if
  your OpenWISP server is at "192.168.56.2", set the URL to
  ``https://192.168.56.2``).
- ``verify_ssl``: Set to ``'0'`` if your controller's SSL certificate is
  self-signed; in production, use a valid SSL certificate to ensure
  security.
- ``shared_secret``: Retrieve this from the OpenWISP dashboard in the
  Organization settings. The list of organizations is available at
  ``/admin/openwisp_users/organization/``.
- ``management_interface``: Refer to :doc:`/user/vpn`.

.. hint::

    For more details on the configuration options, refer to :doc:`OpenWrt
    Config Agent Settings </openwrt-config-agent/user/settings>`.

.. note::

    When testing or developing using the Django development server
    directly from your computer, make sure the server listens on all
    interfaces (``./manage.py runserver 0.0.0.0:8000``) and then point
    OpenWISP to use your local IP address (e.g.
    ``http://192.168.1.34:8000``).

Save the file and restart the agent:

.. code-block:: bash

    /etc/init.d/openwisp_config restart

.. note::

    No changes are needed for the monitoring agent at this stage. The
    default settings work for most cases, and the agent restarts itself
    when the config agent is restarted.

    For more details on its configuration options, refer to :doc:`OpenWrt
    Monitoring Agent Settings </openwrt-monitoring-agent/user/settings>`.

Your OpenWrt device should now be able to register with OpenWISP.

If not, refer to the following **troubleshooting** guides:

- :doc:`Troubleshooting issues with the OpenWrt Config Agent
  </openwrt-config-agent/user/debugging>`
- :doc:`Troubleshooting issues with the OpenWrt Monitoring Agent
  </openwrt-monitoring-agent/user/debugging>`
- :doc:`Troubleshooting issues with the OpenWISP Server (Ansible role)
  </ansible/user/troubleshooting>`

.. seealso::

    - :doc:`Config Agent Quick Start Guide
      </openwrt-config-agent/user/quickstart>`
    - :doc:`OpenWrt Config Agent Settings
      </openwrt-config-agent/user/settings>`
    - :doc:`Monitoring Agent Quick Start Guide
      </openwrt-monitoring-agent/user/quickstart>`
    - :doc:`OpenWrt Monitoring Agent Settings
      </openwrt-monitoring-agent/user/settings>`

Compiling Your Own OpenWrt Image
--------------------------------

.. warning::

    This section is for advanced users.

Compiling a custom OpenWrt image can save time when configuring new
devices. By doing this, you can preinstall the agents and include your
configurations (e.g., ``url`` and ``shared_secret``) in the default image.

This way, you won't have to configure each new device manually, which is
particularly useful if you provision and manage many devices.

Refer to the :doc:`guide on compiling a custom OpenWrt image
</openwrt-config-agent/user/compiling>` for more information.
