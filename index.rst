OpenWISP 2 Documentation
========================

OpenWISP is a software suite aimed at reducing the friction when
managing networks and devices providing network access. Ease of
deploying new infrastructure and ease of managing existing
infrastructure are the goals.

OpenWISP comes with a web portal, the _controller_ or _server_, and
software running on the infrastructure, the _daemon_. The daemon
periodically checks that the configuration for your device
is updated and updates it when necessary.

We rely on NetJSON as the format to write the configuration
for your devices but this is then converted to the configuration
that your device can read. Using NetJSON abstracts from
the vendor device configuration and helps you swap out devices
from different vendors or simply dealing with incompatible
configuration files.

Contents:

.. toctree::
   :maxdepth: 2

   user/quickstart
   user/configure-device
   general/values
   general/help-us
   general/technologies
   general/glossary
   general/press
   general/code-of-conduct
   developer/contributing
   developer/hacking-openwisp-python-django
   developer/google-summer-of-code
   developer/google-code-in

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
