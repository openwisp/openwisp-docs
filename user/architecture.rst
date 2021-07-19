Architecture
============

The following image summarizes the OpenWISP architecture.

.. image:: /assets/design/meta-openwisp-architecture.jpg
   :align: center
   :alt: OpenWISP Architecture Meta Level

A `larger version of the architecture image <https://miro.com/app/board/o9J_kvt3edQ=/?moveToWidget=3074457361507412175&cot=14>`_ and more detailed architectures of the modules can be found on Miro.

- Server Side:
   - OpenWISP (You have 2 main options):
       - Ansible-OpenWISP2 (Recommended): Primary method to install
         OpenWISP. Find `ansible-openwisp2 architecture details on GitHub <https://github.com/openwisp/ansible-openwisp2#architecture>`_.
       - Docker-OpenWISP (In-Alpha): The future for installation of
         OpenWISP. Find `docker-openwisp architecture details on GitHub <https://github.com/openwisp/docker-openwisp#architecture>`_.
   - WiFi Login Pages (Optional): Configurable captive page for
     public/private WiFi services providing login, sign up etc.
     It can work with various captive portals like Coova-chilli, pfSense,
     OPNSense. Useful for implementing public WiFi services with captive
     portal authentication or WPA enterprise.
     Read more about `WiFi login pages features on GitHub <https://github.com/openwisp/openwisp-wifi-login-pages>`_.
     You can use the `ansible script to install login pages on your server <https://github.com/openwisp/ansible-openwisp-wifi-login-pages>`_.
- Network Device Side:
   - OpenWISP Config: Package that helps OpenWRT devices to connect
     with OpenWISP. Read more about `openwisp-config features on GitHub <https://github.com/openwisp/openwisp-config>`_.
     You can use the ansible script to `generate OpenWRT images with openwisp-config for your fleet <https://github.com/openwisp/ansible-openwisp2-imagegenerator>`_ or `install openwisp-config on a single device
     <../user/configure-device.html#install-openwisp-config>`_.
- Other relevant Repositories:
    - openwisp-docs: User, developer and contributor documentation for OpenWISP, hosted on `openwisp.io/docs <https://openwisp.io/docs/>`_.
    - openwisp-website: Home page for introducing OpenWISP, hosted on `openwisp.org <https://openwisp.org/>`_.
