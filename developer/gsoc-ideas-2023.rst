:orphan:

GSoC Project Ideas 2023
=======================

.. tip::

    Do you want to apply with us?

    We have a page that describes how to increase your chances of success.
    **Please read it carefully.**

    :doc:`Read our Google Summer of Code guidelines
    <../developer/google-summer-of-code>`.

.. contents:: **Table of Contents**:
    :backlinks: none
    :depth: 3

General suggestions and warnings
--------------------------------

- **Project ideas describe the goals we want to achieve but may miss
  details that have to be defined during the project**: we expect
  applicants to do their own research, propose solutions and be ready to
  deal with uncertainty and solve challenges that will come up during the
  project
- **Code and prototypes are preferred over detailed documents and
  unreliable estimates**: rather than using your time to write a very long
  application document, we suggest to invest in writing a prototype (which
  means the code may be thrown out entirely) which will help you
  understand the challenges of the project you want to work on; your
  application should refer to the prototype or other Github contributions
  you made to OpenWISP that show you have the capability to succeed in the
  project idea you are applying for.
- **Applicants who have either shown to have or have shown to be fast
  learners for the required hard and soft skills by contributing to
  OpenWISP have a lot more chances of being accepted**: in order to get
  started contributing refer to the :doc:`OpenWISP Contributing Guidelines
  <../developer/contributing>`
- **Get trained in the projects you want to apply for**: once applicants
  have completed some basic training by :doc:`contributing to OpenWISP
  <../developer/contributing>` we highly suggest to start working on some
  aspects of the project they are interested in applying: all projects
  listed this year are improvements of existing modules so these modules
  already have a list of open issues which can be solved as part of your
  advanced training. It will also be possible to complete some of the
  tasks listed in the project idea right now before GSoC starts. We will
  list some easy tasks in the project idea for this purpose.

Project Ideas
-------------

Adding support for automatic management of ZeroTier Tunnels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/zerotier_logo_black.png

.. important::

    Languages and technologies used: Mostly **OpenWrt**, **Python**,
    **Django**, **ZeroTier**.

    **Mentors**: *Gagan Deep* (`pandafy <https://github.com/pandafy>`_),
    *Federico Capoano*.

    **Project size**: 350 hours.

    **Difficulty rate**: hard.

`OpenWISP Controller
<https://github.com/openwisp/openwisp-controller#openwisp-controller>`_
already supports configuring **OpenVPN**, **WireGuard** and **VXLAN over
WireGuard** tunnels. The goal of this project is to add support for
another VPN backend: `ZeroTier <https://www.zerotier.com>`_.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

The contributor must demonstrate good understanding of the following
OpenWISP modules:

- `netjsonconfig <https://netjsonconfig.openwisp.org/en/latest/>`_
- `OpenWISP Controller
  <https://github.com/openwisp/openwisp-controller#openwisp-controller>`_
- `OpenWISP Network Topology
  <https://github.com/openwisp/openwisp-network-topology#openwisp-network-topology>`_

Any merged patches on any of those modules is considered an important plus
point.

The contributor must also demonstrate familiarity with `ZeroTier
<https://www.zerotier.com/>`__, and `OpenWrt <https://openwrt.org>`_,
moreover, they should be willing to increase their experience with these
technologies and show enthusiasm toward learning and implementing IT
network automation.

Expected outcomes
+++++++++++++++++

- Add support for ZeroTier in `netjsonconfig
  <https://netjsonconfig.openwisp.org/en/latest/>`_:

  - Add capability for generating ZeroTier configuration in OpenWrt
    backend.
  - Add a ZeroTier backend that generates network configuration accepted
    by REST API endpoints of the ZeroTier Controller.
  - Write documentation for generating configuration for OpenWrt and
    ZeroTier Controller using netjsonconfig.
  - GitHub Issues:

    - `netjsonconfig #207: [feature] Add support for ZeroTier tunnels to
      OpenWrt backend
      <https://github.com/openwisp/netjsonconfig/issues/207>`_
    - `netjsonconfig #208: [feature] Add ZeroTier backend
      <https://github.com/openwisp/netjsonconfig/issues/208>`_

- Add ZeroTier as a VPN backend in `OpenWISP Controller
  <https://github.com/openwisp/openwisp-controller#openwisp-controller>`_.

  - Add automatic generation of templates for ZeroTier VPN backend similar
    to OpenVPN and WireGuard VPN backends.
  - Integrate `ZeroTier Controller APIs
    <https://docs.zerotier.com/central/v1>`_ in OpenWISP Controller to
    allow managing networks directly from OpenWISP.
  - Write a step by step documentation which explains how to set up and
    use the new ZeroTier VPN backend with a device.
  - GitHub Issues:

    - `openwisp-controller #604 : [feature] Add support for ZeroTier VPN
      backend
      <https://github.com/openwisp/openwisp-controller/issues/604>`_
    - `openwisp-controller #606 : [feature] Authorize member in ZeroTier
      network when a new device is added
      <https://github.com/openwisp/openwisp-controller/issues/606>`_
    - `openwisp-controller #605 : [feature] Allow managing ZeroTier
      networks from OpenWISP
      <https://github.com/openwisp/openwisp-controller/issues/605>`_

- Add a parser in `OpenWISP Network Topology
  <https://github.com/openwisp/openwisp-network-topology#openwisp-network-topology>`_
  that can parse ZeroTier peer information.

  - Write documentation for using this parser to generate topology from
    data received from multiple devices.
  - GitHub Issues:

    - `openwisp-network-topology #135: [feature] Add a parser for ZeroTier
      <https://github.com/openwisp/openwisp-network-topology/issues/135>`_

- Achieve at least 99% test coverage for the code added for this feature.

Improve UX and Flexibility of the Firmware Upgrader Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/2023/firmware.jpg

.. important::

    Languages and technologies used: **Python**, **Django**, **OpenWrt**.

    **Mentors**: *Federico Capoano* (more mentors TBA).

    **Project size**: 175 hours.

    **Difficulty rate**: easy/medium.

The goal of this project is to improve the Firmware Upgrader module to
make its mass upgrade operation feature more versatile and to improve the
user experience by showing progress in real time.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

The applicant must demonstrate good understanding of Python, Django,
Javascript and `OpenWISP Controller
<https://github.com/openwisp/openwisp-controller#openwisp-controller>`__.

They must demonstrate also a basic understanding of `OpenWISP Firmware
Upgrader
<https://github.com/openwisp/openwisp-firmware-upgrader#openwisp-firmware-upgrader>`__,
OpenWrt and UI development.

Prior experience with OpenWrt is not extremely required but welcome.

Expected outcomes
+++++++++++++++++

The applicant must open pull-requests for the following issues which must
be merged by the final closing date of the program:

- `[feature] Allow cancellation of stuck "in-progress" upgrades
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/208>`_
- `[feature:UI] Show upgrade progress in real time in the UI
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/224>`_
- `[feature] Allow to perform mass upgrade of devices by their group
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/213>`_
- `[feature] Allow to perform mass upgrade of devices by their location
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/225>`_

Each issue contains the details which the applicant needs to know in order
to complete the project successfully.

At each step of code changing the test coverage must be maintained stable
and the documentation in the README must be kept up to date.

Training Issues
+++++++++++++++

The applicant may warm up in the application phase by working on the
following issues:

- `[bug] FileNotFoundError when trying to delete an image which links a
  non existing file
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/140>`_
- `[change] Improve endpoints to download firmware images
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/69>`_
- `[feature] Allow management of UpgradeOperation objects in the admin
  <https://github.com/openwisp/openwisp-firmware-upgrader/issues/145>`_

Improve UX of the Notifications Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/2023/notification-preferences.png

.. important::

    Languages and technologies used: **Python**, **Django**,
    **JavaScript**, **HTML**, **CSS**

    **Mentors**: *Gagan Deep* (`pandafy <https://github.com/pandafy>`_)
    (more mentors TBA).

    **Project size**: 175 hours.

    **Difficulty rate**: medium.

The goal of this project is to improve the user experience for managing of
the notification module in regards to managing notification preferences
and batching of email notifications.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

The applicant must demonstrate good understanding of `OpenWISP
Notifications
<https://github.com/openwisp/openwisp-notifications#openwisp-notifications>`__,
it's integration in `OpenWISP Controller
<https://github.com/openwisp/openwisp-controller#openwisp-controller>`_
and `OpenWISP Monitoring
<https://github.com/openwisp/openwisp-monitoring#openwisp-monitoring>`_.

The applicant must demonstrate at least basic UI/UX development skills and
eagerness to learn more about this subject.

Expected outcomes
+++++++++++++++++

The applicant must open pull-requests for the following issues which must
be merged by the final closing date of the program:

- `[feature] Batch email notifications to prevent email flooding
  <https://github.com/openwisp/openwisp-notifications/issues/132>`_: this
  issue has priority because when this happens it causes most users to
  want to disable email notifications.
- `[feature] Allow to disable notifications for all organizations or keep
  everything disabled except notifications for specific organizations
  <https://github.com/openwisp/openwisp-notifications/issues/148>`_.
- `[feature] Add REST API to manage notification preferences of other
  users <https://github.com/openwisp/openwisp-notifications/issues/255>`_.
- `[feature] Add a dedicated view for managing notification preferences
  <https://github.com/openwisp/openwisp-notifications/issues/110>`_.
- `[feature] Add link to manage notification preferences to email
  notifications
  <https://github.com/openwisp/openwisp-notifications/issues/256>`_.

Each issue contains the details which the applicant needs to know in order
to complete the project successfully.

At each step of code changing the test coverage must be maintained stable
and the documentation in the README must be kept up to date.

Applicants are expected to gain more understanding of the UI changes
requested with the help of *wireframes* which must be included in the
application; experience in wireframing is considered an important factor,
alternatively mentors will guide applicants in learning more about the
subject. Willingness and eagerness to learn more about this subject, as
well as UI/UX development are paramount.

Training Issues
+++++++++++++++

The applicant may warm up in the application phase by working on the
following issues:

- `[feature] Add dedicated notification type for internal errors
  <https://github.com/openwisp/openwisp-notifications/issues/254>`_
- `[change] Allow relative paths
  <https://github.com/openwisp/openwisp-notifications/issues/249>`_

Add more timeseries database clients to OpenWISP Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/gsoc/ideas/tsdb.png

.. important::

    Languages and technologies used: **Python**, **Django**, **InfluxDB**,
    **Elasticsearch**.

    **Mentors**: *Federico Capoano*, *Gagan Deep* (more mentors TBA).

    **Project size**: 175 hours.

    **Difficulty rate**: medium.

The goal of this project is to add more Time Series DB options to OpenWISP
while keeping good maintainability.

Prerequisites to work on this project
+++++++++++++++++++++++++++++++++++++

The applicant must demonstrate good understanding of `OpenWISP Monitoring
<https://github.com/openwisp/openwisp-monitoring#openwisp-monitoring>`__,
and demonstrate basic knowledge of `NetJSON format
<https://netjson.org/>`_, **InfluxDB** and **Elasticsearch**.

Expected outcomes
+++++++++++++++++

- Complete the support to `Elasticsearch
  <https://github.com/elastic/elasticsearch>`_. `Support to Elasticsearch
  was added in 2020
  <https://github.com/openwisp/openwisp-monitoring/pull/164>`_ but was not
  completed.

  - The old pull request has to be updated on the current code base
  - The merge conflicts have to be resolved
  - All the tests must pass, new tests for new charts and metrics added to
    *InfluxDB* must be added (see `[feature] Chart mobile
    (LTE/5G/UMTS/GSM) signal strength #270
    <https://github.com/openwisp/openwisp-monitoring/pull/294>`_)
  - The usage shall be documented, we must make sure there's at least one
    dedicated CI build for **Elasticsearch**
  - We must allow to install and use **Elasticsearch** instead of
    **InfluxDB** from `ansible-openwisp2
    <https://github.com/openwisp/ansible-openwisp2>`_ and `docker-openwisp
    <https://github.com/openwisp/docker-openwisp/>`_
  - The requests to Elasticsearch shall be optimized as described in
    `[timeseries] Optimize elasticsearch #168
    <https://github.com/openwisp/openwisp-monitoring/issues/168>`_.

- `Add support for InfluxDB 2.0
  <https://github.com/openwisp/openwisp-monitoring/issues/274>`_ as a new
  timeseries backend, this way we can support both ``InfluxDB <= 1.8`` and
  ``InfluxDB >= 2.0``.

  - All the automated tests for **InfluxDB 1.8** must be replicated and
    must pass
  - The usage and setup shall be documented
  - We must make sure there's at least one dedicated CI build for
    Elasticsearch
  - We must allow choosing between **InfluxDB 1.8** and **InfluxDB 2.0**
    from `ansible-openwisp2
    <https://github.com/openwisp/ansible-openwisp2>`_ and `docker-openwisp
    <https://github.com/openwisp/docker-openwisp/>`_.
