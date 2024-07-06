Values and Goals of OpenWISP
============================

.. contents::
    :depth: 1
    :local:

.. _what_is_openwisp:

What is OpenWISP?
-----------------

OpenWISP is a robust and versatile software platform designed to simplify and automate
network management, with a strong emphasis on wireless networks. It's widely used in
various scenarios, including public Wi-Fi hotspots, mesh networks, community networks,
and IoT applications.

In December 2016, OpenWISP 2 was launched, marking the next generation of our software.
This version, built with Python and Django, replaced the original version developed with
Ruby on Rails. The OpenWISP community has since cultivated an ecosystem of applications
and tools that empower developers to create custom networking solutions. Our mission is
to drive innovation and promote freedom in the realm of network infrastructure
automation.

History
-------

Refer to `History of OpenWISP <http://openwisp.org/history.html>`_.

Core Values
-----------

1. Communication through Electronic Means is a Human Right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We believe that **communication through electronic means is a fundamental human right**.

According to Mozilla, `4 billion people live without internet access today
<https://blog.mozilla.org/blog/2017/07/31/mozilla-releases-research-results-zero-rating-not-serving-ramp-internet/>`_.

Having witnessed the significant progress the internet has brought to our society, we
are deeply convinced that addressing the issue of internet connectivity will help to
alleviate the economic disparity that is so evident at the beginning of the 21st
century.

For these reasons, **fighting the digital divide, both primary (lack of infrastructure)
and secondary (lack of know-how), is our utmost priority**.

2. Net Neutrality
~~~~~~~~~~~~~~~~~

We believe `Net Neutrality <https://en.wikipedia.org/wiki/Net_neutrality>`_ is
beneficial to the internet because it ensures fair treatment (non-discrimination) of
private communications.

The very first public Wi-Fi networks built with OpenWISP in Italy adhere strictly to
this principle: no content filtering of any type is allowed on these networks, and no
special privileges are given to any private entities.

For this reason, we are opposed to including in our ecosystem and documentation any
software tools or tutorials that aim to implement solutions contrary to Net Neutrality.

3. Privacy
~~~~~~~~~~

**Privacy is fundamental to a healthy and functional society**.

The initial public WiFi networks built with OpenWISP in Italy adhere strictly to this
principle: traffic logs are stored only for the duration mandated by law, and personal
data is never sold to third parties.

Therefore, we oppose the inclusion in our ecosystem and documentation of any software
tool or tutorial that aims to intrude upon user privacy by collecting and selling their
data to third parties for profit.

4. Open Source, Licenses, and Collaboration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We release all our software under Open Source licenses on `GitHub
<https://github.com/openwisp>`_.

We primarily use two types of licenses:

- **GPLv3**: Used for software modules we consider to have significant commercial value
  for ISPs and private companies. This license aims to prevent these tools from being
  included in proprietary closed-source solutions, ensuring that private entities do not
  profit from our community's work without contributing back.
- **BSD3** and **MIT**: These highly permissive licenses are used for experimental and
  innovative software modules that are valuable but less monetizable. By allowing these
  modules to be included in proprietary solutions, we aim to reduce duplication of
  effort and encourage contributions from organizations and individuals.

We advocate for transparency and a community-driven approach, welcoming all new
participants, contributors, and users.

Our community values support, friendliness, and collaboration, aiming to make our
software as useful as possible to a wide audience, **while upholding our core values**.

We encourage those who share our values to reach out to us through our `support channels
<http://openwisp.org/support.html>`_ and :doc:`contribute to the project
<../developer/contributing>` in any way they can, according to their means and available
time.

5. Software Reusability for Long-Term Sustainability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Long-time contributors to **OpenWISP have firsthand experience with the pitfalls of
dealing with inflexible monolithic applications** that are difficult to reuse beyond
their original design scope.

**We've witnessed numerous projects emerge with great promise, only to develop their
code from scratch and eventually fade into obscurity**. This recurring cycle represents
a tremendous waste of human effort, energy, and resources.

For this reason, **OpenWISP 2 places a strong emphasis on modularity and reusability**,
drawing inspiration from **best practices established in the Unix world** as outlined in
`The Art of Unix Programming <http://www.catb.org/esr/writings/taoup/html/>`_ by `Eric
S. Raymond <https://en.wikipedia.org/wiki/Eric_S._Raymond>`_.

The core modules of OpenWISP 2 are licensed and designed to facilitate inclusion by
developers outside the OpenWISP community in their own applications (subject to
licensing terms).

This approach fosters an ecosystem of modern networking software tools that attracts
developers from around the globe.

The shared interest of users, modifiers, sharers, resellers, and contributors of these
modules forms the bedrock of **long-term sustainability**.

Goals
-----

- Help solve the problem of lack of internet connectivity by simplifying the deployment
  and management of low-cost network infrastructure worldwide.
- Drive innovation in the networking software realm through automation, modularity,
  reusability, flexibility, extensibility, and collaboration.
- Foster an ecosystem of software tools capable of generating numerous OpenWISP
  derivatives, enhancing the accessibility and affordability of electronic
  communication.
- Mitigate vendor lock-in by striving to support multiple operating systems and hardware
  vendors. While our official support is currently limited to OpenWrt derivatives, we
  have experimental configuration backends for `Raspbian
  <https://github.com/openwisp/netjsonconfig/tree/raspbian>`_ and `AirOS
  <https://github.com/openwisp/netjsonconfig/tree/airos>`_, demonstrating feasibility
  for supporting multiple systems.
- Provide comprehensive documentation for both users and developers.
- Develop user-friendly web interfaces accessible to a broad audience.
