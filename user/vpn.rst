Setting Up the Management Network
=================================

In this section, we will explain how to ensure that your OpenWISP instance
can reach your network devices.

.. contents:: **Table of Contents**:
    :depth: 3
    :local:

Why OpenWISP Needs to Reach Your Devices
----------------------------------------

For OpenWISP to perform tasks such as :doc:`push operations
</controller/user/push-operations>`, :doc:`shell commands
</controller/user/shell-commands>`, :doc:`firmware upgrades
</firmware-upgrader/user/quickstart>`, and :doc:`periodically run active
checks </monitoring/user/checks>`, it **needs to be able to reach the
network devices**.

There are two main deployment scenarios for OpenWISP:

- :ref:`public_internet_deployment`
- :ref:`private_network`

.. _public_internet_deployment:

Public Internet Deployment
--------------------------

This is the most common scenario:

- The OpenWISP server is deployed in a data center exposed to the public
  internet. Thus, the server has a public IPv4 (and IPv6) address and
  usually a valid SSL certificate provided by Let's Encrypt or another
  commercial SSL provider.
- The network devices are geographically distributed across different
  locations (different cities, regions, or countries).

In this scenario, the OpenWISP application will not be able to reach the
devices unless a management tunnel is used.

Therefore, **having a management VPN solution is crucial**, not only to
allow OpenWISP to work properly but also to **perform debugging and
troubleshooting** when needed.

Requirements for this scenario:

- A VPN server must be installed so that the OpenWISP server can reach the
  VPN peers. For more information on how to do this via OpenWISP, please
  refer to the following sections:

      - :doc:`WireGuard </controller/user/wireguard>`
      - :doc:`WireGuard over VXLAN </controller/user/vxlan-wireguard>`
      - :doc:`OpenVPN </controller/user/openvpn>`

ZeroTier is also supported and documented as part of the VPN configuration in this section.

  If you prefer to use other tunneling solutions (L2TP, Softether, etc.)
  and know how to configure those solutions on your own, that's fine as
  well.

  If the OpenWISP server is connected to a network infrastructure that
  allows it to reach the devices via preexisting tunneling or Intranet
  solutions (e.g., MPLS, SD-WAN), then setting up a VPN server is not
  needed, as long as there's a dedicated interface on OpenWrt with an
  assigned IP address that is reachable from the OpenWISP server.

- The devices must be configured to join the management tunnel
  automatically, either via a preexisting configuration in the firmware or
  via a :ref:`default_templates`.
- The :doc:`/openwrt-config-agent/index` running on the network devices
  must be configured to specify the ``management_interface`` option, which
  must be set to the interface name assigned by the VPN tunnel. The agent
  will communicate the IP of the management interface to the OpenWISP
  Server, and OpenWISP will use the management IP to reach the device.

  For example, if the *management interface* is named ``tun0``, the
  openwisp-config configuration should look like the following:

.. code-block:: text

    # In /etc/config/openwisp on the device

    config controller 'http'
        # ... other configuration directives ...
        option management_interface 'tun0'

.. _private_network:

Private Network
---------------

In some cases, the OpenWISP instance is directly connected to the same
network where the devices it manages are operating.

Real-world examples:

- An office LAN where the OpenWISP instance and the network devices are in
  the same Layer 2 domain.
- A Layer 3 routed network, like that operated by an ISP, where each
  device already has an internal IP address that can be reached from the
  rest of the network.

In these cases, OpenWISP should be configured to accept requests using its
private IP address and should be configured to use the **Last IP** field
of the devices to reach them.

In this scenario, it's necessary to set the
:ref:`"OPENWISP_CONTROLLER_MANAGEMENT_IP_ONLY"
<openwisp_controller_management_ip_only>` setting to ``False``.
