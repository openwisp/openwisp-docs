Configuration Templates
=======================

This page aims to introduce you to some OpenWRT Configuration Templates.

What are Configuration Templates?
---------------------------------

Configuration templates contain configuration data. Typically, the data is
used for configuring servers. Configuration templates are usually
pre-defined with data that is regularly used by users.

NetJSON
-------

NetJSON is a data interchange format based on JavaScript Object Notation
(JSON) designed to describe the basic building blocks of layer2 and layer3
networks. You can find more information about NetJSON on `its website
<http://netjson.org>`_.

netjsonconfig
-------------

netjsonconfig is a python library that converts `NetJSON
<http://netjson.org>`_ DeviceConfiguration objects into real router
configurations that can be installed on systems like `OpenWRT
<http://openwrt.org/>`_, `LEDE <https://www.lede-project.org/>`_ or
`OpenWisp Firmware <https://github.com/openwisp/OpenWISP-Firmware>`_.

Example templates for OpenWRT
-----------------------------

Render method
^^^^^^^^^^^^^

``OpenWrt.render(files=True)``
  
  *Converts the configuration dictionary into the corresponding configuration
  format*

    **Parameters**: **files** – whether to include “additional files” in the
    output or not; defaults to ``True``
    **Returns**: string with output

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

Generate method
^^^^^^^^^^^^^^^

``OpenWrt.generate()``

  *Returns a ``BytesIO`` instance representing an in-memory tar.gz archive
  containing the native router configuration.*

    **Returns**: in-memory tar.gz archive, instance of ``BytesIO``

Example:

.. code-block:: python

    >>> import tarfile
    >>> from netjsonconfig import OpenWrt
    >>>
    >>> o = OpenWrt({
    ...     "interfaces": [
    ...         {
    ...             "name": "eth0",
    ...             "type": "ethernet",
    ...             "addresses": [
    ...                 {
    ...                     "proto": "dhcp",
    ...                     "family": "ipv4"
    ...                 }
    ...             ]
    ...         }
    ...     ]
    ... })
    >>> stream = o.generate()
    >>> print(stream)
    <_io.BytesIO object at 0x7fd2287fb410>
    >>> tar = tarfile.open(fileobj=stream, mode='r:gz')
    >>> print(tar.getmembers())
    [<TarInfo 'etc/config/network' at 0x7fd228790250>]

Write method
^^^^^^^^^^^^

``OpenWrt.write(name, path='./')``
  Like ``generate`` but writes to disk.

    **Parameters**:

    - **name**: file name, the tar.gz extension will be
      added automatically
    - **path**: directory where the file will be written
      to, defaults to ``./``
      
    **Returns**: None

Example:

.. code-block:: python

    >>> import tarfile
    >>> from netjsonconfig import OpenWrt
    >>>
    >>> o = OpenWrt({
    ...     "interfaces": [
    ...         {
    ...             "name": "eth0",
    ...             "type": "ethernet",
    ...             "addresses": [
    ...                 {
    ...                     "proto": "dhcp",
    ...                     "family": "ipv4"
    ...                 }
    ...             ]
    ...         }
    ...     ]
    ... })
    >>> o.write('dhcp-router', path='/tmp/')
