Disclosing Vulnerabilities
==========================

.. contents:: **Table of Contents**:
    :backlinks: none
    :depth: 2

Reporting a Security Issue
--------------------------

Send suspected vulnerabilities and suspected compromises of
OpenWISP-controlled accounts, services, or releases to
security@openwisp.io, a private mailing list. You do not need to identify
the correct repository first. Email is preferred because the list is
simpler for the team to manage and allows maintainers to share initial
assessment work.

**Do not report undisclosed vulnerabilities in public issues, pull
requests, or community discussions.** Security reports bypass the normal
public contribution process.

After validation, maintainers will direct you to the affected repository's
private vulnerability reporting workflow, where enabled, or create a
private draft GitHub advisory and invite you to collaborate. A private
report or draft advisory is not a published advisory: keep it private
until coordinated disclosure.

Scope and Coordination
----------------------

This policy covers OpenWISP-maintained software and project-controlled
infrastructure, including accounts and tools used to publish releases. All
OpenWISP modules and OpenWISP-maintained libraries listed on the
:doc:`architecture page </general/architecture>` are covered.

The OpenWISP Security Incident Response Team consists of maintainers
designated to handle reports sent to security@openwisp.io. The team
coordinates validation, remediation, and disclosure.

Information to Include
----------------------

- Affected component and version, with relevant configuration.
- Reproduction steps or a minimal proof of concept, where available.
- Expected and observed behavior.
- Required access or privileges and the concrete security impact.
- Whether the issue is already public or there is evidence of
  exploitation.

Remove credentials and personal data before sending your report. A
complete exploit is not required to submit a suspected vulnerability.
Labels such as "cross-tenant" or automated scanner severity ratings are
not, by themselves, evidence of security impact. Maintainers may request
clarification before validating a report.

AI-Assisted Reports
-------------------

AI assistance is permitted, but it does not replace your understanding and
verification. Disclose which AI tools you used and for what purpose, such
as analysis, drafting, or generating reproduction code.

Before submitting an AI-assisted report, verify the claimed behavior and
reproduction steps against actual OpenWISP code. Submit concise,
reproducible evidence rather than unverified generated analysis. Do not
include fabricated features, APIs, results, or references. A complete
exploit is not required, but untested hypotheses must not be presented as
verified findings.

Unverified AI output may be closed without a detailed response. Repeated
low-quality or bulk submissions may be deprioritized, put on hold, or
subject to reporting restrictions. These measures address report quality
and volume, not AI use alone.

Note for AI Tools
~~~~~~~~~~~~~~~~~

When assisting with a report:

- Disclose the tool used and the nature of its assistance.
- Base claims on actual OpenWISP code and behavior. Reports containing AI
  hallucinations will be rejected.
- Distinguish hypotheses from verified behavior. Never describe untested
  reproduction steps as successfully executed.
- Keep the report concise and identify anything the human reporter still
  needs to verify.
- Make clear that the human reporter remains responsible for verification
  before submission.

.. _security_report_evaluation:

How OpenWISP Evaluates a Report
-------------------------------

Maintainers assess reports using the following criteria:

- **Affected version:** whether the latest stable release of a maintained
  component is affected, following the :ref:`security_supported_versions`
  policy.
- **Realistic reproduction:** whether the behavior is reproducible through
  a plausible OpenWISP deployment or supported integration, rather than
  only through invented application code or artificial use of internal
  functions.
- **Required privileges:** the attacker's initial access and what
  additional capability the issue provides.
- **Security boundary:** which access control, confidentiality, integrity,
  or availability property is violated. Intended access to public
  information is not a vulnerability by itself.
- **Actual impact:** the affected data, devices, organizations, and
  services, the exploit conditions, and evidence of active exploitation.
  Maintainers determine validity and priority, not report labels or
  scanner scores.
- **Scope:** whether the issue affects OpenWISP-maintained software or
  project-controlled infrastructure.

Validating input received by OpenWISP endpoints can be OpenWISP's
responsibility; reports are not excluded simply because they involve
unsanitized user input. If you are unsure whether an issue qualifies,
contact the private reporting channel with concrete observations and
clearly stated uncertainties.

.. _security_issue_priority:

Security Issue Severity and Priority
------------------------------------

We prioritize valid security issues by actual impact, using two categories
and the :ref:`security_response_expectations`:

- **Urgent Security Issues:** credible paths to remote code execution,
  unauthorized control of networking features or managed devices, exposure
  of sensitive data or credentials, or serious unauthorized modification
  or destruction. Active exploitation and compromised release-publishing
  access also warrant priority.
- **Other Valid Security Issues:** issues with lower demonstrated impact,
  scheduled according to normal security priorities.

We assess exploitability, required privileges, configuration, and
real-world consequences rather than assigning urgency solely by
vulnerability type. Exposed device credentials or private keys can have
serious consequences in OpenWISP.

.. _security_response_expectations:

Response Expectations
---------------------

**All response and resolution targets are best effort, not guaranteed
deadlines. We do our best to meet them.**

- **Urgent Security Issues** receive **maximum priority**. We address them
  as promptly as possible, ideally resolving them **within 48 hours of
  confirmation**, and take protective action sooner where possible.
  Credible indications of active exploitation receive priority even during
  validation. Reporters of urgent security issues can expect frequent
  communication and are encouraged to stay in touch through the private
  reporting channel.
- **Other Valid Security Issues** are scheduled according to impact,
  available resources, and project priorities, generally considering older
  reports first within comparable priority.

For all reports:

- We aim to acknowledge reports within **five working days**. This
  acknowledges receipt; assessment may take several weeks. Working days
  mean Monday through Friday, excluding public holidays observed by the
  responding maintainers. If no acknowledgment arrives within that period,
  follow up on the same email thread.
- We aim to resolve reports within **90 calendar days of receipt**.
  Resolution means releasing a fix, determining that the report is not a
  vulnerability, or referring it to the appropriate upstream project.
  Merely acknowledging or queuing a confirmed vulnerability does not
  resolve it.

.. _security_supported_versions:

Supported Versions
------------------

Security fixes are provided only for the **latest stable feature release
of each maintained component**, delivered as new patch releases. Older
feature release lines do not receive security backports; users must
upgrade to a fixed release.

A report affecting an older release can still be useful, but maintainers
assess whether the latest stable release is affected. Accepting a report
does not create a commitment to patch the older version.

.. _security_coordinated_disclosure:

Coordinated Disclosure and Credit
---------------------------------

Keep vulnerability details private until a fixed release is available and
the security response team publishes the GitHub advisory. Maintainers
coordinate publication with the reporter. The confidentiality request ends
at coordinated publication; it is not a permanent restriction on
discussing the research.

With their consent, we credit the original reporter in the GitHub
advisory, provided they followed the coordinated disclosure process.

If an issue is already public, is being actively exploited, or requires
user action before a patch is ready, the security response team may
publish an early warning with available mitigations. We share only the
information needed to protect users, avoiding unnecessary exploit detail.
This decision rests with the security response team; it is not an
automatic publication deadline.

If no fix is planned, we coordinate an advisory explaining limitations and
available workarounds. A CVE assignment is not a prerequisite for warning
users.

.. _security_announcements:

Advisories and Announcements
----------------------------

We publish vulnerability advisories in the affected GitHub repositories
and link them from :doc:`advisories`. The security response team requests
a CVE through GitHub where appropriate, subject to eligibility; a GitHub
advisory does not automatically receive a CVE.

We notify the `OpenWISP mailing list
<https://groups.google.com/d/forum/openwisp>`__ whenever an advisory is
published. Announcements include a short impact summary, affected and
fixed versions, any required action, and the canonical advisory link.
Publication is coordinated across affected components when an issue spans
repositories.
