Contributing guidelines
=======================

We are glad and thankful that you want to contribute to OpenWISP.

Please read these guidelines carefully, it will help you and us to save
precious time later.

Introduce yourself
~~~~~~~~~~~~~~~~~~

It won't hurt to join `our main communication channel
<https://gitter.im/openwisp/general>`_ and introduce yourself,
although to coordinate with one another on technical matters we use
`the development channel <https://gitter.im/openwisp/development>`_.
Use these two channels share feedback, share your OpenWISP
derivative work, ask questions or announce your intentions.

Look for open issues
~~~~~~~~~~~~~~~~~~~~

Check out these two kanban boards:

- `OpenWISP Contributor's Board
  <https://github.com/orgs/openwisp/projects/3>`_: lists
  issues that are suited to newcomers.

- `OpenWISP Priorities for next releases
  <https://github.com/orgs/openwisp/projects/4>`_, lists
  issues that are more urgently needed by the community and is
  frequently used and reviewed by more seasoned contributors.

If there's anything you don't understand regarding the
board or a specific github issue, don't hesitate to ask questions in our
`general chat <https://gitter.im/openwisp/general>`_.

**You don't need to wait for the issue to be assigned to you.**
Just check if there is anyone else actively working on it
(eg: an open pull request with recent activity).
If nobody else is actively working on it, **just announce your intention
to work on it by leaving a comment in the issue**.

Setup
~~~~~

Once you have chosen an issue to work on, read the ``README`` of the
repository of the module you want to contribute to, follow the setup
instructions, each module has its own specific instructions which we
highly advise to read carefully.

How to commit your changes properly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our main development branch is master, it's our central development
branch.

You should open a pull request on github. The pull request will
be merged only once the CI build completes successfully
(automated tests, code coverage check, QA checks, etc.)
and after project maintainers have reviewed and tested it.

You can run QA checks locally by running ``./run-qa-checks`` in the
top level directory of the repository you're working on.
Every OpenWISP module should have this script
(if a module doesn't have it, please open an issue on github).

1. Branch naming guidelines
---------------------------

Create a new branch for your patch, use a self-descriptive name, eg:

::

  git pull origin master
  # if there's an issue your patch addresses
  git checkout -b issues/48-issue-title-shortened

  # if there is no issue for your branch, (we suggest creating one anyway)
  # use a descriptive name
  git checkout -b autoregistration

2. Commit message style guidelines
----------------------------------

**Please follow our commit message style conventions**.

If the issue is present on Github, use following commit style:

::

    [module/file/feature] Short description #<issue-number>

    Long description here.
    Fixes #<issue-number>

Here's a real world commit message example from `one of our modules
<https://github.com/openwisp/django-netjsonconfig/commit/7a5dad9f97e708b89149c2765f8298c5a94b652b>`_:

::

    [admin] Fixed VPN context in preview #57

    Fortunately it was just a frontend JS issue.
    The preview instance was getting the UUID of the Device
    object instead of the Config object, and that prevented
    the system from finding the associated VPN and fill the
    context VPN keys correctly.

    Fixes #57

Moreover, keep in mind the following guidelines:

- commits should be descriptive in nature, the message should
  explain the nature of the change
- make sure to follow the code style used in the module
  you are contributing to
- before committing and pushing the changes, test the code both manually
  and automatically with the automated test suite if applicable
- after pushing your branch code, make a pull-request of that
  corresponding change of yours which should contain a descriptive
  message and mention the issue number as suggested in the example above
- make sure to send one pull request for each feature. Whenever changes
  are requested during reviews, please send new commits (do not amend
  previous commits), if multiple commits are present in a single pull
  request, they will be squashed in a single commit by the maintainers
  before merging
- in case of big features in which multiple related features/changes needs
  to be implemented, multiple commits (one commit per feature)
  in a single PR are acceptable.

3. Pull-Request guidelines
--------------------------

After pushing your changes to your fork, prepare a new Pull Request
(from now on we will shorten it often to just *PR*):

- from your forked repository of the project select your branch and
  click "New Pull Request"
- check the changes tab and review the changes again to ensure everything
  is correct
- write a concise description of the PR, if an issue exists for
- after submitting your PR, check back again whether your PR has passed
  our required tests and style checks
- if the tests fail for some reason, try to fix them and if you get
  stuck seek our help on `our communication channels
  <http://openwisp.org/support.html>`_
- if the tests pass, maintainers will review the PR and may ask
  you to improve details or changes, please be patient: creating a good
  quality open source project takes a bit of sweat and effort; ensure
  to follow up with this type of operations
- once everything is fine with us we'll merge your PR

4. Avoiding unnecessary changes
-------------------------------

Keep your contribution focused and change the least amount
of lines of code as possible needed to reach the goal you're working on.

**Avoid changes unrelated** to the feature/bugfix/change
you're working on.

**Avoid changes related to white-space** (spaces, tabs, blank lines) by
setting your editor as follows:

- always add a blank line at the end of the file
- clear empty lines containing only spaces or tabs
- show white space (this will help you to spot unnecessary white space)

Coding Style Conventions
~~~~~~~~~~~~~~~~~~~~~~~~

1. Python code conventions
--------------------------

OpenWISP follows `PEP 8 -- Style Guide for Python Code
<https://www.python.org/dev/peps/pep-0008/>`_ and several
other style conventions which can be enforced by using the
following tools:

- ``openwisp-qa-format``: this command is shipped in
  `openwisp-utils <https://github.com/openwisp/openwisp-utils#openwisp-qa-format>`_,
  a dependency used in every OpenWISP python module,
  it formats the Python code according to the
  OpenWISP style conventions, it's based on popular tools like:
  `isort <http://isort.readthedocs.io/en/latest/>`_ and
  `black <https://black.readthedocs.io/en/stable/>`_
  (**please do not run black directly** but always call
  ``openwisp-qa-format``)
- ``./run-qa-checks``: it's a script present in the top level directory
  of each OpenWISP module and performs all the QA checks that are specific
  to each module. It mainly calls the ``openwisp-qa-check`` command,
  which performs several common QA checks used across all OpenWISP modules
  to ensure consistency (including `flake8 <http://flake8.pycqa.org/en/latest/>`_),
  for more info consult the documentation of
  `openwisp-qa-check <https://github.com/openwisp/openwisp-utils#openwisp-qa-format>`_


Keep in mind that the QA checks defined in the ``run-qa-checks`` script
are also executed in the CI builds, which will fail if any QA check fails.

To fix QA check failures, run ``openwisp-qa-format`` and apply manual
fixes if needed until ``./run-qa-checks`` runs without errors.

.. note::

  If you want to learn more about our usage of python and django,
  we suggest reading :doc:`Hacking OpenWISP: Python and Django
  <../developer/hacking-openwisp-python-django>`

2. Javascript code conventions
------------------------------

- OpenWISP follows standard JavaScript coding style conventions that are
  generally accepted or the ones that are specified in `.jslintrc files
  <https://github.com/openwisp/django-freeradius/blob/master/.jslintrc>`_;
  find out more about `JSlint here <https://www.jslint.com/help.html>`_
- please follow this `JavaScript Style Guide and Coding Conventions
  <https://www.w3schools.com/js/js_conventions.asp>`_ link for proper
  explanation and wonderful examples

3. OpenWRT related conventions
----------------------------------

OpenWISP follows the standard OpenWRT coding style conventions of OpenWRT:

- `Working with Patches
  <https://wiki.openwrt.org/doc/devel/patches>`_
- `Naming patches
  <https://wiki.openwrt.org/doc/devel/patches#naming_patches>`_
- `Adding new files
  <https://wiki.openwrt.org/doc/devel/patches#naming_patches>`_.

Thank You
~~~~~~~~~

If you follow these guidelines closely your contribution will have a
very positive impact on the OpenWISP project.

Thanks a lot for your patience.
