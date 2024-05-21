========================
OpenWISP 2 Documentation
========================

This repository aims to help out **new users and contributors** to get
start using and getting involved in `OpenWISP <http://openwisp.org>`_.

This repo at this stage is pretty much a work in progress, so
contributions, feedback and suggestions are very welcome.

How to build the docs
---------------------

Requirements: Python >= 3.9.

1. Fork this repository

2. Clone this repository using the following command::

.. code-block:: shell

    git clone https://github.com/<your-username>/openwisp2-docs.git

3. Install sphinx on your local machine using::

.. code-block:: shell

    pip install -r requirements.txt

4. Build documentation::

.. code-block:: shell

    # This command will generate the documentation in all formats - HTML, PDF and ePUB
    make build
    # The ``formats`` argument is a comma separated list of formats to build,
    # e.g. ``formats=html,pdf,epub``. The default is to build all available
    # formats, which currently are ``html``, ``pdf`` and ``epub``.
    make build formats=pdf,html
    # You can also build documentation for a specific version using the
    # VERSION argument
    make build VERSION=22.05
    # This command is a shortcut for generating only HTML documentation during
    # development, since building PDF and ePUB takes time. It also supports
    # the VERSION argument.
    make build_html

5. Open the generated HTML files in your browser.

To build the documentation using SSH remote URLs for OpenWISP
modules, set the ``DEV=1`` environment variable when running the build
commands. Example:

.. code-block:: shell

    DEV=1 make build

Need help?
----------

- If any help regarding installing and using `sphinx` and
  `reStructured Text` is required then please visit this
  `link <http://www.sphinx-doc.org/en/stable/tutorial.html>`_.

- Feel free to post any doubt or comment through our `support channels
  <http://openwisp.org/support.html>`_.
