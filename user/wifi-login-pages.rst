WiFi Login Pages
================

.. note::
  For a demonstration of how this module is used,
  please refer to the following demo tutorial:
  :doc:`WiFi Hotspot, Captive Portal (Public WiFi),
  Social Login <../tutorials/hotspot>`.

Screenshots
-----------

.. raw:: html

   <p align="center">
     <img src="https://github.com/openwisp/openwisp-wifi-login-pages/raw/media/docs/login-desktop.png" alt="">
   </p>
   <p align="center">
     <img src="https://github.com/openwisp/openwisp-wifi-login-pages/raw/media/docs/sign-up-desktop.png" alt="">
   </p>
   <p align="center">
     <img src="https://github.com/openwisp/openwisp-wifi-login-pages/raw/media/docs/verify-mobile-phone-desktop.png" alt="">
   </p>
   <p align="center">
     <img src="https://github.com/openwisp/openwisp-wifi-login-pages/raw/media/docs/login-mobile.png" alt="">
   </p>
   <p align="center">
     <img src="https://github.com/openwisp/openwisp-wifi-login-pages/raw/media/docs/signup-mobile.png" alt="">
   </p>

Overview
--------

OpenWISP WiFi login pages provides unified and consistent user
experience for public/private WiFi services.

In short, this app replaces the classic captive/login page of a WiFi
service by integrating the `OpenWISP Radius API`_ to provide the
following features:

-  Mobile first design (responsive UI)
-  Sign up
-  Optional support for mobile phone verification: verify phone number
   by inserting token sent via SMS, resend the SMS token
-  Login to the WiFi  service (by getting a radius user token from
   OpenWISP Radius and sending a POST to the captive portal login URL
   behind the scenes)
-  Session status information
-  Logout from the WiFi service (by sending a POST to the captive portal
   logout URL behind the scenes)
-  Change password
-  Reset password (password forgot)
-  Support for `Social Login`_ and `SAML`_
-  Optional social login buttons (Facebook, Google, X/Twitter)
-  Contact box showing the support email and/or phone number,
   as well as additional links specified via configuration
-  Navigation menu (header and footer) with the possibility of specifying
   if links should be shown to every user or only authenticated or
   unauthenticated users
-  Support for multiple organizations with the possibility of
   customizing the theme via CSS for each organization
-  Support for multiple languages
-  Possibility to change any text used in the pages
-  Configurable Terms of Services and Privacy Policy for each
   organization
-  Possibility of automatically logging in users who signed in previously
   (if the captive portal browser of their operating system supports
   cookies)
-  Support for `credit/debit card verification and paid subscription
   plans`_

.. _OpenWISP Radius API: https://openwisp-radius.readthedocs.io/
.. _Social Login: https://github.com/openwisp/openwisp-wifi-login-pages/tree/1.0#configuring-social-login
.. _SAML: https://github.com/openwisp/openwisp-wifi-login-pages/tree/1.0#configuring-saml-login--logout
.. _credit/debit card verification and paid subscription plans: https://github.com/openwisp/openwisp-wifi-login-pages/tree/1.0#signup-with-payment-flow

For more information please see the
`OpenWISP WiFi Login Pages documentation <https://github.com/openwisp/openwisp-wifi-login-pages/tree/1.0>`_.
