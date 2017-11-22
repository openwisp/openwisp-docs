Values and Goals of the OpenWISP Community
==========================================

.. _what_is_openwisp:

What is OpenWISP?
-----------------

OpenWISP is a software platform designed to ease and automate the management of networks, with a special
focus on wireless networks, mainly public wifi, mesh networks, community networks and IoT scenarios.

OpenWISP 2, launched in December 2016 and gradually replacing OpenWISP 1, is the new generation of
the software which aims to build an ecosystem of applications and tools that make it easy for
developers to build custom networking applications in order to bring innovation in the communities
of the world that most need it.

History
-------

In the summer of 2008 the Province of Rome decided to start a free public Wi-Fi network to be spread
over its 5352 SQ KM territory including Rome and 120 other cities for a total of about 4.5 million inhabitants.

The main objective of the project, called ProvinciaWiFi (later renamed WiFi Metropolitano), was to
take a decisive step to reduce the existing digital divide by fostering and facilitating the use of ICT by citizens.

From the outset it was decided to commit the project to a completely open philosophy.

For this reason a clear choice towards open software and operating systems and the availability of
every modification, update and improvement to the community was made.
The same approach was adopted for the knowledge and the experience acquired within the project.

Core Values
-----------

1. Communication through electronic means is a human right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We believe that **communication through electronic means is a FUNDAMENTAL human right**.

According to Mozilla, `4 billion of people live without internet today
<https://blog.mozilla.org/blog/2017/07/31/mozilla-releases-research-results-zero-rating-not-serving-ramp-internet/>`_.

Having seen the great progress the internet has brought to our society, we are deeply convinced
that solving the issue of internet connectivity will help to alleviate the economic disparity
that at the beginning of the 21st century is so evident in our world.

For these reasons, **fighting digital divide, both primary (lack of infrastructure) and secondary
(lack of  know how) is our utmost priority**.

2. Net Neutrality
~~~~~~~~~~~~~~~~~

We believe `Net Neutrality <https://en.wikipedia.org/wiki/Net_neutrality>`_ to be beneficial to the
internet because it allows everyone to have a fair treatment (non discrimination) to their private communications.

The very virst public wifi networks that have been built with OpenWISP in Italy follow this
principle very strictly: **no content filtering of any type is allowed on these network, no
special privilege is given to any private network**.

For this reason **we are against including into our ecosystem and documentation any software tool
or tutorial that aims at implementing solutions that go against Net Neutrality**.

3. Privacy
~~~~~~~~~~

**We believe that privacy is very important for a healthy and well functioning society**.

The very virst public wifi networks that have been built with OpenWISP in Italy follow this
principle very strictly: **traffic logs are stored only for the period of time mandated by law
and personal data is never sold to third parties**.

For this reason **we are against including into our ecosystem and documentation any software tool
or tutorial that aims at implementing solutions that aim to collect user data with the aim of selling
it to third parties without the explicit consent of the user**.

4. Open Source, licenses and collaboration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We release all our software under Open Source licenses on `github.com/openwisp <https://github.com/openwisp>`_.

We mainly use two type of licenses:

- **GPLv3**: we use this license for the software modules which we think have a potentially high
  commercial value for ISPs and private companies, our aim in using this license is to avoid
  the inclusion of these tools and modules in propietary closed source solutions, which would result
  in private companies profitting from the work of our community without contributing back to it
- **BSD3** and **MIT**: we use these two very permissive licenses for experimental and innovative
  software modules which are very useful but do not deliver that kind of value which can be
  monetized easily. Therefore we hope that by allowing these modules to be included in proprietary
  solutions we will avoid having many organizations reinventing the wheel and we hope that a small
  percentage of the companies and individuals using them will contribute back even if not explicitly
  forced by the license

We beleive in transparency and also work towards in making this very place as more of a
**Community** than a **Top Down Organization** by warmly welcoming any new participant, contributor and user.

We want our community to be supportive, friendly and highly collaborative, with the aim of making
the software useful to the broadest possible audience - **as long as our core values are not distorted or ignored**.

We encourage anyone who shares our values to get in touch with us via our
`support channels <http://openwisp.org/support.html>`_ and :doc:`contribute to the project
<../developer/contributing>` however they can, according to their means and available free time.

5. Software reusability means long term sustainability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Long time contributors of OpenWISP experienced first hand the consequences of dealing with
unflexible monolithic applications which were hardly reusable outside of the narrow scope for
which they were designed.

We have seen countless projects born with great promises, developing their code from scratch and
then fading into oblivion, only to notice the same vicious cycle begin again some time later in
some other area of the globe.

For this reason, OpenWISP 2 has a strong focus on modularity and reusability.
The core OpenWISP 2 modules are licensed and built in a way that makes it possible for developers
not involved in OpenWISP to include these modules in their own applications (according to their licenses).

This is leading to the creation of an ecosystem of modern networking software tools which is
attracting developers from all over the world.

The mutual interest of the people who use, modify, share, resell and contribute to these modules is
our foundation for long term sustainability.

Goals
-----

- Help to solve the problem of lack of internet connectivity by making it easy to deploy and manage
  low cost network infrastructure all over the world
- Bring innovation in the networking software world by emphasizing automation, modularity, reusability,
  flexibility, extensibility and collaboration
- Create an ecosystem of software tools that can be used to create infinite OpenWISP derivatives
  that can be used to make human communication through electronic means easier and more affordable
- Alleviate the problem of vendor lock-in by attempting to support multiple operating systems and
  hardware vendors (although we now officially support only OpenWRT derivatives, but we do have
  2 experimental configuration backends for `Raspbian <https://github.com/openwisp/netjsonconfig/tree/raspbian>`_
  and `AirOS <https://github.com/openwisp/netjsonconfig/tree/airos>`_)
- Provide good documentation both for users and developers
- Create web interfaces that are easy to use even for people who have limited experience with
  computer networking concepts (**note**: we are very far from reaching this goal as of end of 2017)
