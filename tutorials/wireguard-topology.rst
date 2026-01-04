WireGuard Topology
==================

.. contents:: **Table of Contents**:
    :depth: 3
    :local:

Introduction
------------

In this tutorial, we will explain how to create a **WireGuard topology template** in OpenWISP.
This allows you to automate the deployment of **management VPNs** and visualize the resulting network structure in the topology dashboard.

Prerequisites
-------------

Before starting, ensure you have:

- An active **OpenWISP instance** with the **Controller** and **Network Topology** modules enabled.
- At least one device connected and managed by OpenWISP.
- A basic understanding of **configuration templates** and **variables**.

Creating a WireGuard Template
-----------------------------

In this section, we will explain how to automate the provisioning of WireGuard interfaces using a configuration template.
This template ensures that all assigned devices maintain a consistent and secure VPN configuration.

1. From the OpenWISP navigation menu, go to **Configurations** and then **Templates**.
2. Click on **Add template**.
3. Fill in the basic information:
   - **Name**: Enter a descriptive name like "Management VPN (WireGuard)".
   - **Organization**: Select the appropriate organization.
   - **Type**: Select **Generic**.
   - **Backend**: Select **OpenWrt**.
4. Scroll down to the **Configuration** section and click on **Advanced mode (raw JSON)**.
5. Paste the following configuration, which defines the **WireGuard interface** and its peer:

.. code-block:: json

    {
        "interfaces": [
            {
                "name": "wg0",
                "type": "wireguard",
                "wireguard": {
                    "private_key": "{{ wg0_private_key }}",
                    "listen_port": 51820,
                    "peers": [
                        {
                            "public_key": "VPN_SERVER_PUBLIC_KEY",
                            "endpoint": "vpn.example.com",
                            "port": 51820,
                            "allowed_ips": [
                                "10.0.0.0/24"
                            ],
                            "persistent_keepalive": 25
                        }
                    ]
                },
                "addresses": [
                    {
                        "address": "{{ wg0_address }}",
                        "mask": 24
                    }
                ]
            }
        ]
    }

.. note::

    In the example above:
    - ``{{ wg0_private_key }}`` and ``{{ wg0_address }}`` are **configuration variables** used to ensure each device has a unique identity and IP.
    - ``VPN_SERVER_PUBLIC_KEY`` and ``vpn.example.com`` are placeholders for your VPN server's details.

6. Click **Back to normal mode** to validate the JSON and then click **Save** to create the template.

Enabling Topology Visualization
-------------------------------

Once the template is ready, you can enable **topology collection** by following these steps:

1. From the navigation menu, go to **Network Topology** and then **Topologies**.
2. Click on **Add topology**.
3. Fill in the basic details:
   - **Name**: Enter a name like "WireGuard Management Topology".
   - **Organization**: Select the same organization used for the template.
   - **Strategy**: Select **Network Topology Collector**.
4. Ensure the **Protocol** is set to **WireGuard**.
5. Click **Save** to enable the topology collection.

Assigning the Template to Devices
---------------------------------

Follow these steps to apply the WireGuard configuration to your devices:

1. From the navigation menu, go to **Controller** and then **Devices**.
2. Click on the name of the device you want to configure.
3. Navigate to the **Configuration** tab.
4. In the **Templates** field, select the "Management VPN (WireGuard)" template.
5. Click **Save and continue editing**.
6. OpenWISP will now schedule a configuration push to the device.

Verifying the Topology
----------------------

After the configuration is applied, you can verify the status of the WireGuard tunnel on the device using the ``wg show`` command.
The resulting network graph will be visible in the **Network Topology** section of the OpenWISP dashboard, providing a real-time view of your management network.

See Also
--------

For more information on configuration templates, the WireGuard VPN backend, and the network topology module, please refer to the user documentation of the respective modules.
