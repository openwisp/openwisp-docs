WiFi Hotspot & Captive Portal
=============================

A common use case in which OpenWISP is widely employed is
**Public Wi-Fi**.

In this tutorial we will explain some technical details of the most
common **WiFi Hotspot** deployments and how to test the most
important functionalities
of this use case on the :doc:`OpenWISP Demo System <./demo>`.

Testing the Hotspot Functionality on Demo
-----------------------------------------

The firmware image provided for the :doc:`OpenWISP Demo System <./demo>`
includes a captive portal software package called
`Coova-Chilli <https://coova.github.io/CoovaChilli/>`_, which
supports the
`RADIUS protocol <https://networkradius.com/doc/current/introduction/RADIUS.html>`_,
a standard protocol used for AAA
(Accounting, Authorization and Authentication), which means a way
of authenticating, authorizing and rate limiting network usage supported
by a lot of networking hardware equipment and software.

Enable Captive Portal Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you flashed the firmware and registered your device as explained
in the :doc:`OpenWISP Demo Page <./demo>`, you can proceed to
assign the captive portal template to your device:

- go to the device list
- open the device details
- click on the configuration tab
- select the "Captive Portal Demo" template
- hit "Save"

Make sure the OpenVPN management tunnel is working or otherwise
the captive portal software will not be able to talk to the demo
`FreeRADIUS <https://freeradius.org/>`_ server instance.

Shortly after the configuration is applied successfully,
the Public WiFi SSID will be broadcasted by the device.

Accessing the Public WiFI Hotspot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect one of your laptop or phone devices to the SSID
"OpenWISP Public WiFi Demo", if all is working well your operating
system should open a browser window showing the captive page as in
the screenshot below.

.. image:: ../images/demo/wifi-login-pages-public-wifi-hotspot.jpeg
   :target: ../_images/wifi-login-pages-public-wifi-hotspot.jpeg
   :width: 300
   :align: center

At this point you can try to sign in using the same credentials to
access the demo system (``demo``/``tester123``).

.. note::
  Trying to surf the internet without authenticating will not work.

Once you have logged in you will see a status page like in the following
screenshots:

.. image:: ../images/demo/hotspot-status.jpeg
  :target: ../_images/hotspot-status.jpeg
  :width: 300
  :align: center

This page communicates that the user can now use the internet,
it also provides the following features:

- it shows a list of the sessions of the user,
  each session showing the start time, the stop time, the duration,
  the traffic consumed (download and upload) and the mac address of
  the device which has accessed the WiFi service.
- It allows to change password of the account.
- When SMS verification is enabled, it allows to change the phone
  number (will require to verify the number again via SMS, **this
  feature is not enabled on the demo system**).
- It allows to perform log out (more on why this is useful below).

On some mobile operating system, the mini browser
automatically closes when switching windows
(eg: opening the real browser to surf the internet),
which can be problematic if the user needs to use one of the
features of the status page listed above.

To alleviate this pain, once the WiFi session is started, OpenWISP
will send an email to the user with a magic link which will allow
to access the status page of WiFi Login Pages without entering
the credentials again, this link has temporary validity.

.. note::
  For more technical information and implementation details
  about the magic link feature,
  Consult the
  `openwisp-users documentation <https://github.com/openwisp/openwisp-users#2-openwisp_usersapiauthenticationsesameauthentication>`_
  (which discloses and links
  to the documentation of the underlying open source
  library used to implement this feature).

.. image:: ../images/demo/public-wifi-session-started.jpeg
  :target: ../_images/public-wifi-session-started.jpeg
  :width: 300
  :align: center

However, when using the demo account, the email will be sent to the
email of the demo account, so if you want to try this feature, you
will have to sign up for your own account or use the social login
feature (both described below in this page).

Logging out
~~~~~~~~~~~

Most public WiFi services do not allow users to browse indefinitely but
have limitations in place.

Some services allow to surf only for a limited amount of time per day,
some services allow to to consume only a certain amount of traffic
per day, others employ a mix of both (as soon as the either the
daily time or traffic limit is reached, the session is closed).

For this reason, users which use the service often and who intend
to use the service again later on in the same day, in order to
avoid consuming the time of their session may want to close
the session using the log out button.

Session limits
~~~~~~~~~~~~~~

.. image:: ../images/demo/session-limit-exceeded.jpeg
  :target: ../_images/session-limit-exceeded.jpeg
  :width: 300
  :align: center

The default session limits built in the default OpenWISP RADIUS
configuration are 300 MB daily traffic or 3 hours of daily surfing.

To find out more about this topic please read:
`Enforcing session limits
<https://openwisp-radius.readthedocs.io/en/stable/user/enforcing_limits.html>`_.
