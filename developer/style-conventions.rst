Style Conventions
=================

We are thankful that you took your time to contribute to this community.

This document is about what style conventions you should follow
and keep in mind while programming in different languages and contributing to
the codebase of this organisation.

Steps to Commit your Code or Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our main development branch is master it's our central development
branch.

Your code should be pushed from a different branch and then it is
merged into master after proper review from the project maintainers.

1. Create a new branch
----------------------

Create a new branch for your patch, use a self-descriptive name, eg:

::

  git pull origin master
  # if there's an issue for your patch
  git checkout -b issues/48
  # if you prefer a descriptive name
  git checkout -b autoregistration

2. Commit and push
------------------

Please follow our commit message style, eg:

::

    [module/file/feature] Short description #issue

    Long description here.
    Fixes #issue

Here's a real world example from `one of our modules
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


Python Code conventions
~~~~~~~~~~~~~~~~~~~~~~~

- For proper python coding conventions one should read `PEP 8 -- Style Guide for
  Python Code <https://www.python.org/dev/peps/pep-0008/>`_.

- OpenWISP uses `flake8 <https://pypi.python.org/pypi/flake8>`_ as it's style guide
  enforcement tool or source code checker.

- Please make sure you follow this code style while making changes to any
  of the OpenWISP's Python file.

- To know more about flake visit `this page. <http://flake8.pycqa.org/en/latest/>`_.


Javascript Code Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- OpenWISP follows standard JavaScript coding style conventions that are generally
  accepted or the ones that are mentioned in
  `JSlint <https://github.com/openwisp/django-freeradius/blob/master/.jslintrc>`_ file.
  To know more about JSlint please see `this <https://www.jslint.com/help.html>`_.

- Proper structure and indentations should be maintained in code and descriptive
  function and variable name should be used so that code is more readable and
  self explanatory.

- Please follow this `JavaScript Style Guide and Coding Conventions
  <https://www.w3schools.com/js/js_conventions.asp>`_ link for proper
  explanation and wonderful examples.


Openwrt Related Code Convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- OpenWISP follows the standard OpenWRT coding style conventions as stated by
  OpenWRT.

- If you want ot work with patches in OpenWRT please refer the following link for yourself
  to get started `Working with Patches <https://wiki.openwrt.org/doc/devel/patches>`_.

- For reference on how to name the patches in OpenWRT please visit the given link
  `Naming patches <https://wiki.openwrt.org/doc/devel/patches#naming_patches>`_.

- For adding new files to your patch please refer this link on how to structure your files
  and patches `Adding new files <https://wiki.openwrt.org/doc/devel/patches#naming_patches>`_.

Thanks for your effort to read the above guidelines. We are happy that you took
your time out to contribute to this community.
