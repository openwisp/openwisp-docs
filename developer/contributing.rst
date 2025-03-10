Contributing guidelines
=======================

We are glad and thankful that you want to contribute to OpenWISP.

.. important::

    Please read these guidelines carefully, it will help to save precious
    time for everyone involved.

**Table of Contents:**

.. contents::
    :depth: 2
    :local:

Introduce yourself
------------------

It won't hurt to join `our main communication channel
<https://matrix.to/#/#openwisp_general:gitter.im>`_ and introduce
yourself, although to coordinate with one another on technical matters we
use `the development channel
<https://matrix.to/#/#openwisp_development:gitter.im>`_. Use these two
channels share feedback, share your OpenWISP derivative work, ask
questions or announce your intentions.

Look for open issues
--------------------

Check out these two kanban boards:

- `OpenWISP Contributor's Board
  <https://github.com/orgs/openwisp/projects/42/views/1>`_: lists issues
  that are suited to newcomers.
- `OpenWISP Priorities for next releases
  <https://github.com/orgs/openwisp/projects/37/views/1>`_, lists issues
  that are more urgently needed by the community and is frequently used
  and reviewed by more seasoned contributors.

If there's anything you don't understand regarding the board or a specific
github issue, don't hesitate to ask questions in our `general chat
<https://matrix.to/#/#openwisp_general:gitter.im>`_.

**You don't need to wait for the issue to be assigned to you.** Just check
if there is anyone else actively working on it (e.g.: an open pull request
with recent activity). If nobody else is actively working on it, **just
announce your intention to work on it by leaving a comment in the issue**.

Priorities for the next release
-------------------------------

When we are close to releasing a new major version of OpenWISP, we will
encourage all contributors to focus on the **To Do** column of the
`OpenWISP Priorities for next releases
<https://github.com/orgs/openwisp/projects/37/views/1>`_ board and filter
the issues according to their expertise:

- **Newcomer**: filter by `Good first issue
  <https://github.com/orgs/openwisp/projects/37/views/1?sliceBy%5BcolumnId%5D=Labels&sliceBy%5Bvalue%5D=good+first+issue>`_
  or `Hacktoberfest
  <https://github.com/orgs/openwisp/projects/37/views/1?sliceBy%5BcolumnId%5D=Labels&sliceBy%5Bvalue%5D=hacktoberfest>`_.
- **Expert**: filter by `Important
  <https://github.com/orgs/openwisp/projects/37/views/1?sliceBy%5BcolumnId%5D=Labels&sliceBy%5Bvalue%5D=important>`_.

Setup
-----

Once you have chosen an issue to work on, read the documentation section
of the module you want to contribute to, follow the setup instructions,
each module has its own specific developer installation instructions which
we highly advise to read carefully.

.. important::

    For a complete list of the OpenWISP modules, refer to
    :doc:`/general/architecture`.

How to commit your changes properly
-----------------------------------

Our main development branch is master, it's our central development
branch.

You should open a pull request on github. The pull request will be merged
only once the CI build completes successfully (automated tests, code
coverage check, QA checks, etc.) and after project maintainers have
reviewed and tested it.

You can run QA checks locally by running ``./run-qa-checks`` in the top
level directory of the repository you're working on. Every OpenWISP module
should have this script (if a module doesn't have it, please open an issue
on github).

1. Branch naming guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new branch for your patch, use a self-descriptive name, e.g.:

.. code-block::

    git pull origin master
    # if there's an issue your patch addresses
    git checkout -b issues/48-issue-title-shortened

    # if there is no issue for your branch, (we suggest creating one anyway)
    # use a descriptive name
    git checkout -b autoregistration

.. _openwisp_commit_message_style_guidelines:

2. Commit message style guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Please follow our commit message style conventions**.

If the issue is present on Github, use following commit style:

.. code-block::

    [module/file/feature] Short description #<issue-number>

    Long description here.
    Fixes #<issue-number>

Here's a real world commit message example from `one of our modules
<https://github.com/openwisp/django-netjsonconfig/commit/7a5dad9f97e708b89149c2765f8298c5a94b652b>`_:

.. code-block::

    [admin] Fixed VPN context in preview #57

    Fortunately it was just a frontend JS issue.
    The preview instance was getting the UUID of the Device
    object instead of the Config object, and that prevented
    the system from finding the associated VPN and fill the
    context VPN keys correctly.

    Fixes #57

Moreover, keep in mind the following guidelines:

- commits should be descriptive in nature, the message should explain the
  nature of the change
- make sure to follow the code style used in the module you are
  contributing to
- before committing and pushing the changes, test the code both manually
  and automatically with the automated test suite if applicable
- after pushing your branch code, make a pull-request of that
  corresponding change of yours which should contain a descriptive message
  and mention the issue number as suggested in the example above
- make sure to send one pull request for each feature. Whenever changes
  are requested during reviews, please send new commits (do not amend
  previous commits), if multiple commits are present in a single pull
  request, they will be squashed in a single commit by the maintainers
  before merging
- in case of big features in which multiple related features/changes needs
  to be implemented, multiple commits (one commit per feature) in a single
  PR are acceptable.

3. Pull-Request guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~

After pushing your changes to your fork, prepare a new Pull Request (from
now on we will shorten it often to just *PR*):

- from your forked repository of the project select your branch and click
  "New Pull Request"
- check the changes tab and review the changes again to ensure everything
  is correct
- write a concise description of the PR, if an issue exists for
- after submitting your PR, check back again whether your PR has passed
  our required tests and style checks
- if the tests fail for some reason, try to fix them and if you get stuck
  seek our help on `our communication channels
  <http://openwisp.org/support.html>`_
- if the tests pass, maintainers will review the PR and may ask you to
  improve details or changes, please be patient: creating a good quality
  open source project takes a bit of sweat and effort; ensure to follow up
  with this type of operations
- once everything is fine with us we'll merge your PR

4. Avoiding unnecessary changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keep your contribution focused and change the least amount of lines of
code as possible needed to reach the goal you're working on.

**Avoid changes unrelated** to the feature/fix/change you're working on.

**Avoid changes related to white-space** (spaces, tabs, blank lines) by
setting your editor as follows:

- always add a blank line at the end of the file
- clear empty lines containing only spaces or tabs
- show white space (this will help you to spot unnecessary white space)

Coding Style Conventions
------------------------

1. Python code conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenWISP follows `PEP 8 -- Style Guide for Python Code
<https://www.python.org/dev/peps/pep-0008/>`_ and several other style
conventions which can be enforced by using the following tools:

- ``openwisp-qa-format``: this command is shipped in :doc:`openwisp-utils
  </utils/developer/qa-checks>`, a dependency used in every OpenWISP
  python module, it formats the Python code according to the OpenWISP
  style conventions, it's based on popular tools like: `isort
  <http://isort.readthedocs.io/en/latest/>`_ and `black
  <https://black.readthedocs.io/en/stable/>`_ (**please do not run black
  directly** but always call ``openwisp-qa-format``)
- ``./run-qa-checks``: it's a script present in the top level directory of
  each OpenWISP module and performs all the QA checks that are specific to
  each module. It mainly calls the ``openwisp-qa-check`` command, which
  performs several common QA checks used across all OpenWISP modules to
  ensure consistency (including `flake8
  <http://flake8.pycqa.org/en/latest/>`_), for more info consult the
  documentation of :doc:`openwisp-qa-check </utils/developer/qa-checks>`.

.. important::

    QA checks defined in the ``run-qa-checks`` script are also executed in
    CI builds. These builds will fail if any QA check fails.

    To resolve QA check failures, run ``openwisp-qa-format`` and apply
    manual fixes if necessary, until ``./run-qa-checks`` completes without
    errors.

.. note::

    If you want to learn more about our usage of python and django, we
    suggest reading :doc:`../developer/hacking-openwisp-python-django`.

2. CSS and Javascript code conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenWISP follows CSS and JavaScript coding conventions enforced by the
`Prettier <https://prettier.io>`_ code formatting tool.

The Prettier formatter is used by the :doc:`openwisp-qa-format
</utils/developer/qa-checks>` tool and by the `./run-qa-checks` script
located in the top-level directory of each repository.

.. important::

    QA checks defined in the ``run-qa-checks`` script are also executed in
    CI builds. These builds will fail if any QA check fails.

    To resolve QA check failures, run ``openwisp-qa-format`` and apply
    manual fixes if necessary, until ``./run-qa-checks`` completes without
    errors.

3. OpenWrt related conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenWISP follows the standard OpenWrt coding style conventions of OpenWrt:

- `Working with Patches <https://wiki.openwrt.org/doc/devel/patches>`_
- `Naming patches
  <https://wiki.openwrt.org/doc/devel/patches#naming_patches>`_
- `Adding new files
  <https://wiki.openwrt.org/doc/devel/patches#naming_patches>`_.

Thank You
---------

If you follow these guidelines closely your contribution will have a very
positive impact on the OpenWISP project.

Thanks a lot for your patience.
