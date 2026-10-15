# Editorial decisions: October 15, 2026

Jonathan approved the reviewed trust and assessment cleanup for implementation and preview review, then explicitly authorized production deployment on October 15, 2026. Account settings changes and real form submissions or bookings remain outside that authorization.

This record supersedes conflicting booking, assessment, healthcare, About, and release-status statements in the September 20 record, including its October 9 and 10 updates. Historical entries are preserved as history.

## Production and preview status

- At the start of this work, GitHub main was d6e99c1, the October 10 merge of PR #12. PR #10 and PR #12 are merged; their core-page refresh and inline booking page are already published.
- This cleanup is released through [PR #13](https://github.com/JonlintonAI/fresh-coast-ai-website-2026/pull/13), based on that main commit. Production deployment is authorized. The PR release record will contain the merge commit and post-deployment verification; approval alone is not proof of publication.
- Intro-call links lead to /book in the same tab. The direct Cal.com fallback remains available on that page.
- The existing Google tag, Ads configuration, Cal.com embed, query forwarding, and bookingSuccessfulV2 callback are preserved. Do not add a manual Ads conversion snippet.
- PR #11 remains open. Its intended professional-services story correction is already in main. Closing it without merging is recommended; closure has not been performed.

## Healthcare and unpublished content

- Withdraw the healthcare page with 301 redirects to /services and remove its sitemap entry.
- Remove unsupported healthcare client and capability references from the location pages and Professional Services. Assessment industry options can remain when selection makes no experience claim.
- Return 404 for /blog/pending/*.
- Remove the three internal SEO reports and opportunity-brief template from published files. Verified private archive copies were retained outside this repository. No repository-history rewrite or deletion of old Netlify deployments was performed.
- Do not add healthcare, HIPAA, BAA, Part 11, or GCP claims without new explicit approval from Jonathan.

## Assessment

- Keep the 14 questions, scoring thresholds, seven dimension scores, on-screen results, and booking link.
- Use "Book an intro call" consistently for the assessment navigation, results, and footer booking links, including their accessibility labels.
- A Clinical Research / CRO industry option is deferred until Jonathan confirms that niche. The existing Healthcare & Medical Practices and Other options remain available; no industry choice is evidence of completed client work.
- Remove both assessment submissions and email capture. Redirect /assessment-thank-you and its .html variant to /assessment.
- Qualify the score as self-reported guidance, not an audit, benchmark, or deployment approval. Industry selection does not affect the score or establish industry experience.
- No replacement completion-tracking event is added. The existing sitewide Google tag remains.
- The reviewed source contains no assessment-summary sending mechanism. The October 12 mailbox evidence found no lead-shaped notifications or summary emails in the searched mailbox, but documents coverage gaps. It does not establish zero submissions or that no outside service ever sent email.
- Existing Netlify records and notification settings are unchanged. Historical submission counts, spam counts, notification scopes, and outgoing integrations remain unverified in the dashboard.

## About and industry evidence

- Remove the unsupported quantified result and employer-specific experience bullets from About. Keep general professional background, the SAP experience, Myanmar narrative, and approved client evidence.
- No current-employer results, figures, or project descriptions may be added without new explicit approval.
- Remove the unsupported example-story sections from Property Management, Manufacturing, Staffing, and Trades rather than relabeling them as client evidence. Remove Property Management's payback sentence from both visible copy and FAQ structured data.
- Preserve current service pricing. Financial figures belonging to withdrawn illustrative stories are removed with those stories. Broader pricing alignment, platform claims, delivery-time claims, and industry rewrites are deferred.
- The assessment CTA follow-up does not change pricing. A replacement public pricing position has not been selected or approved.

## Contact and privacy

- Preserve the contact form's fields, required states, Netlify form name, honeypot, and contact-thank-you destination.
- Add bounded waiting, accessible inline status, autocomplete, and stronger field contrast. Retain entered values after errors and do not retry automatically.
- A timeout or network error does not prove the server failed to receive a message. Recovery copy must say receipt could not be confirmed.
- Privacy copy describes browser-based assessment scoring, Netlify Forms, the Google tag, and Cal.com's embed. It does not claim all technical visit data stays in the browser.
- The privacy date is October 15, 2026, matching the authorized release date. Legal review has not been recorded.

## Verification and release prerequisites

- Local verification on October 15 passed: 13 changed page templates at 1280px and 390px, assessment totals of 14, 35, 36, 53, 54, and 70, neutral healthcare/custom/empty industry messages, and mocked contact success, HTTP 500, network rejection, and a real 15-second deadline. Errors retained every field; duplicate submission and late-success handling were checked. No live form submission or booking was made. Third-party measurement requests were intercepted during browser tests.
- Source validation passed for all JSON-LD, inline script syntax, sitemap XML, preserved form attributes and fields, preserved Google tags and booking code, and unchanged approved case-study files. Contact placeholder contrast is 4.94:1 on white; field-border contrast is 3.22:1 on white.
- Local and mocked browser checks can verify score rendering, lack of assessment submissions, contact recovery, success navigation, and layout. They do not verify live email delivery, Netlify spam handling, or Ads attribution.
- Verify redirects and removed-file responses on the hosted preview, then repeat after an approved production release.
- Google Ads was inspected read-only on October 15 before release. All six conversion actions were listed, including two removed actions. The three enabled website actions use www.freshcoast.ai/contact-thank-you (starts with), www.freshcoast.ai/booking-confirmed (contains), and freshcoast.ai/contact (starts with); the fourth enabled action is Google hosted. None of the enabled actions depends on /assessment-thank-you. No Ads settings were changed. Existing tracking-status warnings remain; this URL-dependency check does not establish attribution.
- A production booking through the inline embed, its confirmation redirect, notifications, and conversion request remains unverified. The documented October 10 test predates the embed merge and does not establish that full production path.
- Confirm Cal.com availability with Jonathan's intended hours. Any real booking and cancellation require separate authorization.
- Repository privacy and access to old deploy previews remain separate settings decisions. Current source removal does not recall old copies.
- Full assessment accessibility work, broader industry and blog claims, navigation consistency, pricing posture, and contact-field restructuring remain outside this change set.
