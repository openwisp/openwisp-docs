How to Edit Django Settings
===========================

**Table of Contents:**

.. contents::
    :depth: 2
    :local:

What is an OpenWISP Module?
---------------------------

The OpenWISP server application is composed of a number of modules called
`Django apps
<https://docs.djangoproject.com/en/4.2/intro/reusable-apps/>`_.

`Django <https://djangoproject.com/>`_ is the underlying Python web
framework on top of which OpenWISP is built.

Some of the Django apps used by OpenWISP are developed and maintained by
OpenWISP, other apps are developed and maintained by either Django or
third party organizations, but most of these apps are configurable and
customizable in different shapes or forms.

The most common way to modify the behavior of a Django app is by editing
the `project settings.py file
<https://docs.djangoproject.com/en/4.2/topics/settings/>`_, a file which
holds all the global configuration of the application.

The Django based modules of OpenWISP are highly configurable and over time
you may need to edit their settings, these settings are documented in the
respective section of each module on this website, a reference is also
provided for convenience at the end of this page.

If you are looking for a reference which lists and describes all the
OpenWISP modules please refer to :doc:`/general/architecture`.

Editing Settings with Ansible-OpenWISP2
---------------------------------------

The official ansible OpenWISP role provides many :doc:`role variables
</ansible/user/role-variables>` which offer a convenient way to edit the
most widely used settings of OpenWISP.

However, not all the possible settings have a corresponding variable
because doing so would be very costly to maintain and make the code more
complicated, for that reason the role provides a way to add any python
instruction to define and manipulate settings via the
``openwisp2_extra_django_settings_instructions`` variable, eg:

.. code-block::

    # in the playbook variables add:
    openwisp2_extra_django_settings_instructions:
      - |
        OPENWISP_NETWORK_TOPOLOGY_NODE_EXPIRATION = 14

        OPENWISP_MONITORING_METRICS = {
            'ping': {
                'alert_settings': {'tolerance': 60}
            },
            'config_applied': {
                'alert_settings': {'tolerance': 60}
            },
            'disk': {
                'alert_settings': {'tolerance': 60}
            },
            'memory': {
                'alert_settings': {'tolerance': 60}
            },
            'cpu': {
                'alert_settings': {
                    'threshold': 95,
                    'tolerance': 60
                }
            },
        }

This allows for great flexibility in configuring and extending OpenWISP:
the possibility of running python code in the settings allows for
limitless adaptation and customization.

Editing Settings with Docker-OpenWISP
-------------------------------------

Similarly to the ansible role, the dockerized version of OpenWISP provides
mainly two ways of changing settings:

1. The most widely used setting have a :doc:`dedicated environment
   variable </docker/user/settings>`.
2. For more advanced use cases, it's possible :doc:`to provide an entirely
   custom django settings file </docker/user/customization>`.

OpenWISP Settings Reference
---------------------------

- :doc:`OpenWISP Controller Settings </controller/user/settings>`
- :doc:`OpenWISP Monitoring Settings </monitoring/user/settings>`
- :doc:`OpenWISP Firmware Upgrader Settings
  </firmware-upgrader/user/settings>`
- :doc:`OpenWISP Network Topology Settings
  </network-topology/user/settings>`
- :doc:`OpenWISP Users Settings </users/user/settings>`
- :doc:`OpenWISP Notifications Settings </notifications/user/settings>`
- :doc:`OpenWISP Utils Settings </utils/user/settings>`
