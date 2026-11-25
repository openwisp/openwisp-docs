Contributing guidelines
=======================

We are glad and thankful that you want to contribute to OpenWISP.

.. warning::

    AI assisted contributions which shift the burden of understanding,
    implementation, testing, and review entirely onto maintainers are not
    acceptable. Please read the :ref:`Anti AI Spam Policy
    <anti_spam_policy>` before opening a pull request.

**Table of Contents:**

.. contents::
    :depth: 2
    :local:

Introduce yourself
------------------

We strongly recommend joining `the development channel
<https://matrix.to/#/#openwisp_development:gitter.im>`_ to ask technical
questions and coordinate contributions. You are also welcome to introduce
yourself in `our main communication channel
<https://matrix.to/#/#openwisp_general:gitter.im>`_, share feedback, or
tell us about your OpenWISP derivative work.

.. _openwisp_look_for_open_issues:

Look for "validated" issues
---------------------------

Not all issues are suited to new contributors.

Check out these two kanban boards:

- `OpenWISP Contributor's Board
  <https://github.com/orgs/openwisp/projects/42/views/1>`_: lists issues
  that are suited to newcomers.
- `OpenWISP Priorities for next releases
  <https://github.com/orgs/openwisp/projects/37/views/1>`_, lists issues
  that are more urgently needed by the community and is frequently used
  and reviewed by more seasoned contributors.

If there's anything you don't understand regarding the board or a specific
github issue, don't hesitate to ask questions in our `dev channel
<https://matrix.to/#/#openwisp_development:gitter.im>`_.

Contributors who are neither members of the OpenWISP organization nor
repository collaborators must verify that **the issue has been validated
by maintainers** before opening a pull request.

You are welcome to open bug reports, but **wait until a maintainer has
validated the issue before opening a pull request for it**.

In OpenWISP, **an issue is considered validated when all of the following
conditions are met**:

- it is open
- it belongs to a repository in the OpenWISP organization
- it has at least one label other than ``invalid`` or ``wontfix``
- it is added to either the `OpenWISP Contributor's Board
  <https://github.com/orgs/openwisp/projects/42/views/1>`_ or the
  `OpenWISP Priorities for next releases
  <https://github.com/orgs/openwisp/projects/37/views/1>`_ board

**Some issues are not suited to beginners**. These are clearly marked with
a prominent warning at the beginning and must be avoided by beginners.

**If the issue has already been validated by a maintainer, you don't need
to wait for it to be assigned to you before working on it.** Just check if
there is anyone else actively working on it (e.g.: an open pull request
with recent activity). If nobody else is actively working on it, **just
announce your intention to work on it by leaving a comment in the issue**.

.. warning::

    For contributors who are neither members of the OpenWISP organization
    nor repository collaborators, pull requests that do not target a
    validated issue are automatically flagged as invalid and closed after
    24 hours.

Priorities for the next release
-------------------------------

When we are close to releasing a new major version of OpenWISP, we will
encourage all contributors to focus on the **To Do** column of the
`OpenWISP Priorities for next releases
<https://github.com/orgs/openwisp/projects/37/views/1>`_ board.

Newcomers can filter by `Good first issue
<https://github.com/orgs/openwisp/projects/37/views/1?sliceBy%5BcolumnId%5D=Labels&sliceBy%5Bvalue%5D=good+first+issue>`_.

Setup
-----

Once you have chosen an issue, follow the developer installation
instructions in the documentation of the module you want to contribute to.

.. important::

    For a complete list of the OpenWISP modules, refer to
    :doc:`/general/architecture`.

Submitting changes
------------------

1. Branch naming guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a descriptively named branch from an up-to-date ``master``, e.g.:

.. code-block::

    git checkout master
    git pull origin master
    git checkout -b issues/48-issue-title-shortened

.. _openwisp_commit_message_style_guidelines:

2. Commit message conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    The required commit message format is enforced by automated checks in
    the CI builds. Use ``openwisp-commit --check`` to check the latest
    commit message, as described in :ref:`Commit message checks
    <utils_commit_message_checks>`.

When working on issues picked from the boards mentioned in the beginning
of this document, please use the following commit message conventions:

.. code-block::

    [feature/change/fix/chores] Short description #<issue-number>

    Long description here.
    Closes #<issue-number>

Here's a real world commit message example from `one of our modules
<https://github.com/openwisp/openwisp-controller/commit/4eec3234864b5102b575c71a043513ef038975a0>`_:

.. code-block::

    [fix] Fixed perennial "modified" state #213

    The status of Config objects will only be updated if
    the checksum changes, whether it's because of a
    change in the config, device or any related templates.

    Closes #213

Moreover, keep the following guidelines in mind:

- write all commit messages in clear, descriptive, past-tense language
- add an explanatory commit body for substantial changes, new features, or
  non-obvious bug fixes; the subject of ``[feature]``, ``[change]``,
  ``[change!]``, ``[deps]``, and ``[fix]`` commits, including scoped
  variants, is automatically included in the changelog, so write it in
  clear, user-friendly, past-tense language
- make sure to follow the code style used in the module you are
  contributing to
- before committing and pushing the changes, test the code both manually
  and automatically with the automated test suite if applicable

3. Pull-Request guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~

Send one pull request (PR) for each focused change. For bigger PRs
involving multiple related features or changes, multiple commits (one per
feature or change) are acceptable.

After pushing your changes to your fork, prepare a PR:

- from your forked repository of the project select your branch and click
  "New Pull Request"
- check the changes tab and review the changes again to ensure everything
  is correct
- write a concise description of the PR and link its validated issue using
  ``Fixes #ISSUE_NUMBER``, ``Closes #ISSUE_NUMBER``, or ``Related to
  #ISSUE_NUMBER``. To link an issue in another OpenWISP repository, use
  ``Fixes openwisp/repository#ISSUE_NUMBER`` or ``Fixes
  https://github.com/openwisp/repository/issues/ISSUE_NUMBER``
- after submitting your PR, check back again whether your PR has passed
  our required tests and style checks
- if the tests fail for some reason, try to fix them and if you get stuck
  seek our help on `our communication channels
  <http://openwisp.org/support/>`_
- if the tests pass, maintainers will review the PR; respond to their
  feedback and push requested changes as new commits (do not amend
  previous commits)
- once the checks pass and maintainers approve the PR, we will merge it,
  squashing multiple commits into one

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

Each repository defines style conventions appropriate to its languages and
tools. Run ``./run-qa-checks`` from the repository's top-level directory
to verify your changes. This script runs the relevant automated QA checks,
and CI rejects pull requests that do not pass them.

We recommend running ``openwisp-pre-push-hook --install`` in the
repository to run ``./run-qa-checks --pre-push`` automatically before each
push and block the push if the checks fail.

Follow the repository's ``AGENTS.md`` file for formatting guidance and any
required automatic formatting tools.

Thank You
---------

If you follow these guidelines closely your contribution will have a very
positive impact on the OpenWISP project.

Thanks a lot for your patience.
