RADIUS
======

**Source code**: `github.com/openwisp/openwisp-radius
<https://github.com/openwisp/openwisp-radius>`_.

OpenWISP RADIUS is available since OpenWISP 22.05 and
provides many features aimed at public WiFi services.

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

Deploy instructions
-------------------

See :ref:`Enabling the RADIUS module on the
OpenWISP ansible role documentation
<ansible_enabling_radius_module>`.

Alternatively you can set it up manually by following these guides:

- `Freeradius Setup for Captive Portal authentication
  <https://openwisp-radius.readthedocs.io/en/stable/developer/freeradius.html>`_
- `Freeradius Setup for WPA Enterprise (EAP-TTLS-PAP) authentication
  <https://openwisp-radius.readthedocs.io/en/stable/developer/freeradius_wpa_enterprise.html>`_

This module is also available in
:doc:`docker-openwisp </docker/index>`
although its usage is not recommended for production usage yet,
unless the reader is willing to invest effort in adapting the docker
images and configurations to overcome any roadblocks encountered.

Find out more about OpenWISP RADIUS
-----------------------------------

For more information about the features offered by OpenWISP RADIUS,
we refer to the its documentation:

- `Registration of new users <https://openwisp-radius.readthedocs.io/en/stable/user/registration.html>`_
- `SMS verification <https://openwisp-radius.readthedocs.io/en/stable/user/settings.html#openwisp-radius-sms-verification-enabled>`_
- `Importing users <https://openwisp-radius.readthedocs.io/en/stable/user/importing_users.html>`_
- `Generating users <https://openwisp-radius.readthedocs.io/en/stable/user/generating_users.html>`_
- `Social Login <https://openwisp-radius.readthedocs.io/en/stable/user/social_login.html>`_
- `Single Sign-On (SAML) <https://openwisp-radius.readthedocs.io/en/stable/user/saml.html>`_
- `Enforcing session limits <https://openwisp-radius.readthedocs.io/en/stable/user/enforcing_limits.html>`_
- `REST API <https://openwisp-radius.readthedocs.io/en/stable/user/api.html>`_
- `Django Settings <https://openwisp-radius.readthedocs.io/en/stable/user/settings.html>`_
