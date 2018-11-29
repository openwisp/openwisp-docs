Template Configurations 
============================

   What are Configuration Templates?

Configuration templates are files with prebuilt configuration data to achieve a specific task. This files come default while setting up such services. Prebuilt configuration templates save the users from writing this configurations from scratch hence improving working speed. This templates also make it possible for those who do not have a basic understanding as to how the configurations are set up to make use of such services. 
	
NetJSON, which is a data interchange format based upon the popular JSON[ JavaScript Object Notation ] has the aim of creating an ecosystem of interoperable software that enable developers write network – centric applications faster and better, requires some configurations. This could be a turnoff for some, most especially those who are just getting started with the service.             
Hence, the NetJSON team saw the need to build an additional tool to reduce the problems people face when it comes to writing configurations. Please refer to Official NetJSON page for a full information on it at the https://netjson.org page
 
	
This desire thus gave birth to the creation of Netsjonconfig –  The official configuration engine of OpenWISP2 . 
Netjsconfig is a python library which converts Netjson Device Configuration objects into real router configurations that can be installed on several machines such as OpenWRT, LEDE  or OpenWisp Firmware. Netjsonconfig’s Multiple Template Inheritance helps reduce the pain that comes precompiled with writing configurations by reducing repetition to the barest minimum. It also has several cool features such as Command Line Utility, Validations, File inclusions e.t.c. Please refer to NetJSON documentation page for a full information on it at the https://http://netjsonconfig.openwisp.org/en/latest/ page              	           

Below are three examples configurations for OpenWRT

Render method
-------------

Using the render method.

Code example:

.. code-block:: python

    from netjsonconfig import OpenWrt

    o = OpenWrt({
        "interfaces": [
            {
                "name": "eth0.1",
                "type": "ethernet",
                "addresses": [
                    {
                        "address": "192.168.1.2",
                        "gateway": "192.168.1.1",
                        "mask": 24,
                        "proto": "static",
                        "family": "ipv4"
                    },
                    {
                        "address": "192.168.2.1",
                        "mask": 24,
                        "proto": "static",
                        "family": "ipv4"
                    },
                    {
                        "address": "fd87::2",
                        "gateway": "fd87::1",
                        "mask": 64,
                        "proto": "static",
                        "family": "ipv6"
                    }
                ]
            }
        ]
    })
    print(o.render())

Device Configuration 
======================
Using the JSON method  

Code example:

.. code-block:: python

    >>> from netjsonconfig import OpenWrt
    >>>
    >>> router = OpenWrt({
    ...     "general": {
    ...         "hostname": "HomeRouter"
    ...     }
    ... })
    >>> print(router.json(indent=4))
    {
        "type": "DeviceConfiguration",
        "general": {
            "hostname": "HomeRouter"
        }
    } 

Wireless access point
======================

The following *configuration dictionary* represent one of the most
common wireless access point configuration:

.. code-block:: python

    {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "myWiFi",
                    "wmm": True,  # 802.11e
                    "isolate": True  # client isolation
                }
            }
        ]
    }

Please refer to  `netjson OpenWrt Backend
for a full explanation on netjson template configuration and sample configurations
<http://netjsonconfig.openwisp.org/en/latest/backends/openwrt.html>`_. 