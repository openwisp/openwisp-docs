GSoC Project Ideas 2022
=======================

.. Tip:: Do you want to apply with us?

  We have a page that describes how to increase your chances of success.
  **Please read it carefully.**

  :doc:`Read our Google Summer of Code guidelines
  <../developer/google-summer-of-code>`.

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

General suggestions and warnings
--------------------------------

- **Project ideas describe the goals we want to achieve
  but may miss details that have to be defined during the project**:
  we expect students to do their own research, propose solutions and be
  ready to deal with uncertainty and solve challenges that
  will come up during the project

- **Code and prototypes are preferred over detailed
  documents and unreliable estimates**:
  rather than using your time to write a very long
  application document, we suggest to invest in writing a prototype
  (which means the code may be thrown out entirely) which will help you
  understand the challenges of the project you want to work on; your
  application should refer to the prototype or other Github contributions
  you made to OpenWISP that show you have the capability to succeed in the
  project idea you are applying for.

- **Students who have either shown to have or have shown to be
  fast learners for the required hard and soft skills by
  contributing to OpenWISP have a lot more chances of being accepted**:
  in order to get started contributing refer to the
  :doc:`OpenWISP Contributing Guidelines <../developer/contributing>`

- **Get trained in the projects you want to apply for**: once
  applicants have completed some basic training by
  :doc:`contributing to OpenWISP <../developer/contributing>`
  we highly suggest to start working on
  some aspects of the project they are
  interested in applying: all projects
  listed this year are improvements
  of existing modules so these modules
  already have a list of open issues
  which can be solved as part of your advanced training.
  It will also be possible to complete some of the tasks listed in
  the project idea right now before GSoC starts.
  We will list some easy tasks in the project idea for this purpose.

Project Ideas
-------------

Adding support for management of ZeroTier Tunnels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Important::

  Languages and technologies used:
  Mostly **OpenWRT**, **Python** and **Django**.

  **Mentors**: Gagan Deep (`pandafy <https://github.com/pandafy>`_).

`OpenWISP Controller <https://github.com/openwisp/openwisp-controller#openwisp-controller>`_
already supports configuring **OpenVPN**, **WireGuard** and
**VXLAN over WireGuard** tunnels. The goal of this project is to
add support for another VPN backend, i.e. `ZeroTier <https://www.zerotier.com>`_.

**Pre-requisites to work on this project**:

The contributor should be familiar with
`ZeroTier <https://www.zerotier.com/>`__,
`OpenWRT <https://openwrt.org>`_,
`netjsonconfig <https://netjsonconfig.openwisp.org/en/latest/>`_
`OpenWISP Controller <https://github.com/openwisp/openwisp-controller#openwisp-controller>`_
and `OpenWISP Network Topology <https://github.com/openwisp/openwisp-network-topology#openwisp-network-topology>`_


**Measurable outcomes**:

- Add support for ZeroTier in `netjsonconfig <https://netjsonconfig.openwisp.org/en/latest/>`_:

  - Add capability for generating ZeroTier configuration
    in OpenWrt backend.
  - Add a ZeroTier backend that generates network configuration
    accepted by REST API endpoints of the ZeroTier Controller.
  - Write documentation for generating ZeroTier configuration for
    OpenWrt and ZeroTier Controller.
  - GitHub Issues:

    - `netjsonconfig #207: [feature] Add support for ZeroTier tunnels to OpenWRT backend <https://github.com/openwisp/netjsonconfig/issues/207>`_
    - `netjsonconfig #208: [feature] Add ZeroTier backend <https://github.com/openwisp/netjsonconfig/issues/208>`_

- Add ZeroTier as a VPN backend in `OpenWISP Controller <https://github.com/openwisp/openwisp-controller#openwisp-controller>`_.

  - Add automatic generation of templates for ZeroTier VPN backend
    similar to OpenVPN and WireGuard VPN backends.
  - Integrate `ZeroTier Controller APIs <https://docs.zerotier.com/central/v1>`_
    in OpenWISP Controller to allow managing networks directly
    from OpenWISP.
  - Write documentation for using ZeroTier VPN backend and using applying
    a ZeroTier VPN template on a device.
  - GitHub Issues:

    - `openwisp-controller #604 : [feature] Add support for ZeroTier VPN backend <https://github.com/openwisp/openwisp-controller/issues/604>`_
    - `openwisp-controller #606 : [feature] Authorize member in ZeroTier network when a new device is added <https://github.com/openwisp/openwisp-controller/issues/606>`_
    - `openwisp-controller #605 : [feature] Allow managing ZeroTier networks from OpenWISP <https://github.com/openwisp/openwisp-controller/issues/605>`_

- Add a parser for `OpenWISP Network Topology <https://github.com/openwisp/openwisp-network-topology#openwisp-network-topology>`_
  that can parse ZeroTier peer information.

  - Write documentation for using this parser to generate topology
    from data received from multiple devices.
  - GitHub Issues:

    - `openwisp-network-topology #135: [feature] Add a parser for ZeroTier <https://github.com/openwisp/openwisp-network-topology/issues/135>`_

- Achieve at least 99% test coverage for the code added for this feature.
