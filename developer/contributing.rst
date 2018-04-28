Contributing guidelines
=======================

We are glad and thankful that you want to contribute to OpenWISP.

Please read these guidelines carefully, it will help you and us
to save precious time later.

Setting things up
~~~~~~~~~~~~~~~~~~

Please follow up the instructions in the README of the repository to
which you want to contribute to, so that you can set up the project.

Finding Something to Work
~~~~~~~~~~~~~~~~~~~~~~~~~

Visit any repository and then to try to explore the project's codebase.
Use it and give us your opinion about any change that might be helpful
to you as well as to us. If you find any bug or error or something
that is worth mentioning please create an **issue** regarding that
bug or error.

If you are unable to find anything on your own to be worked upon,
don't worry we got your back. Visit that project's **Issues** tab and
explore those issues that might interests you, comment on the issue
thread and we'll help you get along with that.

We also use an agile development tool, namely Taiga. You may head over
to the `project page <https://tree.taiga.io/project/nemesisdesign-openwisp>`_
and explorer some issues and epics over there too. If you have certain
interesting ideas, you may contribute those in Taiga.

If neither of the above works for you, please get in touch with us
via `our communication channels <http://openwisp.org/support.html>`_.

Steps to Commit your Code or Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our main development branch is master, it's our central development
branch.

Your code should be pushed from a different branch and then it is
merged into master after proper review from the project maintainers.

1. Branch naming guidelines
---------------------------

Create a new branch for your patch, use a self-descriptive name, eg:

::

  git pull origin master
  # if there's an issue for your patch
  git checkout -b issues/48
  # if you prefer a descriptive name
  git checkout -b autoregistration

2. Commit message style guidelines
----------------------------------

Please follow our commit message style, eg:

If the issue is present on Taiga, use following commit style:

::

    [module/file/feature] Short description TG-[Taiga issue number] #closed

    Long description here.

If the issue is present on Github, use following commit style:

::

    [module/file/feature] Short description #issue-number

    Long description here.
    Fixes #issue-number

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

3. Create pull-request
----------------------

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
  you to improve details or changes, please be patient: creating
  a good quality open source project takes a bit of sweat and effort;
  ensure to follow up with this type of operations
- once everything is fine with us we'll merge your PR

4. Avoiding unnecessary changes
-------------------------------

- While making changes to the required files, then saving it and comitting it,
  different contributors often find that there occur same changes that they have
  not made and those changes gets committed with the desired change that the person
  wants to make.

- These unnecessary changes should be evaluated first and then the commit should
  be made.

- These changes generally occur due to different settings and customizations
  of your editor that you are working with. These changes are produced on their own
  as soon as you save a file. Examples are - Introducing new lines, removing and
  adding spaces, etc.

- To avoid such changes please check your editor settings first. If this sort of
  behaviour persists please use any command line editor like VIM, etc.

Coding Style Conventions
~~~~~~~~~~~~~~~~~~~~~~~~

1. Python Code conventions
--------------------------

- For proper python coding conventions one should read `PEP 8 -- Style Guide for
  Python Code <https://www.python.org/dev/peps/pep-0008/>`_.

- OpenWISP uses `flake8 <https://pypi.python.org/pypi/flake8>`_ as it's style guide
  enforcement tool or source code checker.

- Please make sure you follow this code style while making changes to any
  of the OpenWISP's Python file.

- To know more about flake visit `this page. <http://flake8.pycqa.org/en/latest/>`_

- OpenWISP also uses `isort <https://pypi.python.org/pypi/isort>`_ to manage its codebase
  in a definite order. To know more about its use, please head over to this
  `page <http://isort.readthedocs.io/en/latest/>`_.

2. Javascript Code Conventions
------------------------------

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

3. OpenWRT Related Code Convention
----------------------------------

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
