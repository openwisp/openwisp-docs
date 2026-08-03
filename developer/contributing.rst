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

It won't hurt to join `our main communication channel
<https://matrix.to/#/#openwisp_general:gitter.im>`_ and introduce
yourself, although to coordinate with one another on technical matters we
use `the development channel
<https://matrix.to/#/#openwisp_development:gitter.im>`_. Use these two
channels share feedback, share your OpenWISP derivative work, ask
questions or announce your intentions.

.. _openwisp_look_for_open_issues:

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
github issue, don't hesitate to ask questions in our `dev channel
<https://matrix.to/#/#openwisp_development:gitter.im>`_.

New or occasional contributors must verify that **the issue has been
validated by maintainers** before opening a pull request.

This also applies to issues you opened yourself: **wait until a maintainer
has acknowledged and validated the issue before opening a pull request for
it**.

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

2. Commit message conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    The commit message conventions described in this section are enforced
    by automated checks in the CI builds and can be easily followed by
    using the ``openwisp-commit`` tool described in :ref:`Commit message
    checks <utils_commit_message_checks>`.

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

- commits should be descriptive in nature, the message should explain the
  nature of the change
- add an explanatory commit body for substantial changes, new features, or
  non-obvious bug fixes; the subject of ``[feature]``, ``[change]``,
  ``[change!]``, ``[deps]``, and ``[fix]`` commits, including scoped
  variants, is automatically included in the changelog, so write it in
  clear, user-friendly, past-tense language
- make sure to follow the code style used in the module you are
  contributing to
- before committing and pushing the changes, test the code both manually
  and automatically with the automated test suite if applicable
- after pushing your branch code, make a pull-request of that
  corresponding change of yours which should contain a descriptive message
  and mention the issue number as suggested in the example above
- make sure to send one pull request for each change. Whenever changes are
  requested during reviews, please send new commits (do not amend previous
  commits), if multiple commits are present in a single pull request, they
  will be squashed in a single commit by the maintainers before merging
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
- if the tests pass, maintainers will review the PR and may ask you to
  improve details or changes, please be patient: creating a good quality
  open source project takes a bit of sweat and effort; ensure to follow up
  with this type of operations
- once everything is fine with us we'll merge your PR

For external contributors, automation validates the linked issue. Owners,
organization members, and repository collaborators are exempt. If the
issue link is missing or does not refer to a validated issue, the PR
receives the ``invalid`` label and one comment explaining the problem.
Updating the PR description with a valid link removes the label. If the PR
remains invalid, it is closed 24 hours after that comment. This does not
change the stale-PR policy: ordinary stale PRs are not automatically
closed.

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

Follow the repository's ``AGENTS.md`` file for formatting guidance and any
required automatic formatting tools.

Thank You
---------

If you follow these guidelines closely your contribution will have a very
positive impact on the OpenWISP project.

Thanks a lot for your patience.
