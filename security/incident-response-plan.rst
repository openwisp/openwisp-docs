Incident Response Plan
======================

.. note::

    This is internal guidance for the OpenWISP Security Incident Response
    Team; to report a suspected vulnerability, see
    :doc:`disclosing-vulnerabilities`.

.. contents:: **Table of Contents**:
    :backlinks: none
    :depth: 2

Handling a Software Vulnerability
---------------------------------

1. **Receive the report privately.** Acknowledge it and request missing
   information where needed.
2. **Assess the issue.** Reproduce it safely, determine the security
   impact, and identify affected components and versions. Explain the
   outcome to the reporter.
3. **Coordinate the response.** For a valid issue, collaborate privately
   through the relevant GitHub advisory workflow and prioritize by actual
   impact.
4. **Prepare a fix.** Develop and review the fix, add appropriate
   regression tests, and identify mitigations where a release cannot be
   immediate. Keep pre-release fixes confidential where feasible.
5. **Release the fix.** Follow the :ref:`security_supported_versions`
   policy, coordinate affected components, and provide clear upgrade or
   mitigation instructions.
6. **Disclose and announce.** Publish the advisory, request a CVE where
   appropriate, update :doc:`advisories`, and announce it on the OpenWISP
   mailing list following :ref:`security_announcements`. An early warning
   can precede the fix under the :ref:`security_coordinated_disclosure`
   exception.

Handling a Compromised Account, Service, or Release
---------------------------------------------------

A compromise requires more than a software fix. If someone steals a
package-publishing token and uploads a malicious release, fixing
application code does not remove the attacker's access or make that
release safe. An attacker could also change download links by taking over
a project website account even when the software has no vulnerability.

The security response team uses the following checklist on a best-effort
basis:

1. **Stop further harm.** Revoke the stolen token or affected account
   sessions, restrict the compromised service, and pause publishing if
   release integrity is uncertain. Use an unaffected account or channel
   when the usual one cannot be trusted.
2. **Check what was affected.** Preserve available logs and record
   relevant times, releases, and downloads. Keep evidence private and
   avoid erasing it during cleanup where possible, without delaying urgent
   containment.
3. **Restore trusted operation.** Remove unauthorized access, rotate
   affected credentials, and rebuild or restore from verified sources.
   Remove or clearly flag malicious artifacts and verify the publishing
   path before resuming releases.
4. **Tell users what to do.** If users may have received unsafe downloads
   or exposed credentials, publish concrete guidance: which versions or
   downloads to avoid, what to replace, and whether credentials need
   rotation. Use the project website and mailing list as appropriate; do
   not wait for a software patch or CVE when neither is relevant.
