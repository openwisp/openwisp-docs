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

4. You can build the documentation using the following command

.. code-block:: shell

    # This command will generate the documentation in all formats - HTML, PDF and ePUB
    make build
    # The ``formats`` argument is a comma separated list of formats to build,
    # e.g. ``formats=html,pdf,epub``. The default is to build all available
    # formats, which currently are ``html``, ``pdf`` and ``epub``.
    make build formats=pdf,html
    # This command is a shortcut for generating only HTML documentation during
    # development, since building PDF and ePUB takes time. It also supports
    # the VERSION argument.
    make build_html

.. note::

    Please refer the "`build options" <#build-options>`_section of this
    configuration for a complete reference of the available options.

5. Open the generated HTML files in your browser.

Build options
-------------

Building different formats
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the ``make build`` command will generate documentation in all
supported output formats: HTML, PDF, and ePUB.

If you want to generate the documentation in specific formats,
you can specify the ``FORMATS`` argument. The ``FORMATS`` argument
accepts a comma-separated list of formats to generate.
The supported formats are:

- ``html``: HTML documentation
- ``pdf``: PDF documentation
- ``epub``: ePUB documentation

For example, to generate only HTML and PDF documentation, you can run:

.. code-block:: shell

    make build FORMATS=html,pdf

To generate all supported formats, just omit the ``FORMATS`` argument:

.. code-block:: shell

    make build

.. code-block:: shell

    # This command will only generate HTML
    make build FORMATS=html

Building specific version
~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the ``make build`` command will generate documentation for
all the versions defined in ``config.yml``.

If you want to generate the documentation for a specific version,
you can do so by using the ``VERSION`` argument. ``VERSION`` accepts any
version that is specified in the ``config.yml`` file.

For example, if you want to generate documentation for the
``dev`` version, you can run:

.. code-block:: shell

    make build VERSION=dev

This is useful if you only want to generate documentation for the
version you are currently working on, or if you want to generate
documentation for a specific version without having to rebuild all
the other versions as well.

Overriding a module of a version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``make build`` command is programmed to generate the documentation
for the modules that are defined in the ``config.yml`` file. Sometimes,
it may be necessary to override the branch/remote of a module defined in the
``config.yml`` file to build the documentation for a specific version
or to test a specific commit/branch of a module.

You can do so by using the ``MODULES`` argument. ``MODULES`` accepts a
comma separated string where each item is of the following format:

.. code-block:: text

    version=<openwisp-version>,repository=<repo-owner>/<repo-name>,branch=<branch-name>

E.g. if you want to build the documentation for the ``dev`` version, but want
to use the ``feature`` branch of openwisp-controller of your fork, then
the command will be:

.. code-block:: shell

    make build MODULES="version=dev:repository=<your-username>/openwisp-controller:branch=feature"

The ``MODULES`` argument allows you to override the default settings
for a single module, or multiple modules, defined in the
``config.yml`` file.

You can use the ``MODULES`` argument to add modules to a version that
is not defined in the ``config.yml`` file.

Building with SSH remotes
~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the OpenWISP modules are cloned over HTTPS. This may pose
a hurdle if you wish to make changes to the cloned modules and push
them to the remote URL. To use SSH remotes, you can set the environment
variable ``DEV=1``. This will instruct the build to clone the modules
using SSH instead of HTTPS. For example:

.. code-block:: shell

    DEV=1 make build

Building for production
~~~~~~~~~~~~~~~~~~~~~~~

If you want to build the documentation for the production environment,
i.e. for deploying on `https://openwisp.io/docs`, set the environment
variable ``PRODUCTION=1``. This will generate the documentation in
all the formats:

.. code-block:: shell

    PRODUCTION=1 make build

Need help?
----------

- If any help regarding installing and using `sphinx` and
  `reStructured Text` is required then please visit this
  `link <http://www.sphinx-doc.org/en/stable/tutorial.html>`_.

- Feel free to post any doubt or comment through our `support channels
  <http://openwisp.org/support.html>`_.
