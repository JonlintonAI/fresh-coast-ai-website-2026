# Editorial decisions: September 20, 2026

Source: Jonathan's September 20 feedback and follow-up in Codex.

## October 10, 2026 booking and professional services preview updates

- Add direct intro-call booking at `https://cal.com/jonlinton/intro`, following Jonathan's October 10 Cal.com builder instructions. Booking links open in a new tab with an accessible notice. The homepage hero is adapted to the current draft's layout. Scoping and general written-inquiry links retain their contact destination; assessment routes and form fields remain unchanged.
- Contact offers booking above the written inquiry form. Preserve the existing Netlify submission, honeypot, required states, field values, and contact-thank-you destination. Remove the promise to send suggested meeting times.
- Add `booking-confirmed.html` with `noindex,nofollow` and the same installed Google tags as contact-thank-you. There is no manual conversion event in the source to clone. Google Ads URL matching for the new path remains unverified; copying the global tag is not evidence that bookings count as conversions.
- Jonathan will configure the Cal.com post-booking redirect after the page is published. Do not change his Cal.com settings or report booking confirmation, email receipt, or Ads attribution as tested.
- Remove the unverified accounting-firm story and standard ROI figures from the professional-services page and its FAQ schema. Use only the approved Stanton case-study facts as the documented example. The same one-page correction is isolated in PR #11.
- Jonathan chose to keep PR #11 in preview. Neither these changes nor the broader draft are approved for production release.

## October 10, 2026 withdrawn internal application examples

Jonathan directed removal of the proposed internal testing and acquisition application examples after considering employer concerns. This supersedes the earlier request to add anonymized versions.

- Remove the examples and their related references from Home, Services, and About.
- Do not reuse these projects as website content, including anonymized descriptions or screenshots, without new explicit approval from Jonathan.
- The additions were local and uncommitted; they were not pushed or published.

## October 10, 2026 consolidated review draft

Jonathan requested a complete website draft incorporating the warmer revision and the reviewed contact-form feedback.

- Add visible required markers for Name, Email, Company, and the inquiry description. Keep Industry as optional free text and label both Industry and the interest selector optional.
- Harden the already-hidden honeypot wrapper with hidden and aria-hidden. Exclude its input from keyboard navigation and autocomplete while preserving its name and presence in the form payload.
- Change the final company-size band to 251+ to remove the overlap with 151–250.
- Add the supplied correct founder LinkedIn URL, https://www.linkedin.com/in/jonathan-linton/, to the homepage founder and About Person structured data. Do not associate the founder with /in/jonlinton.
- Keep September 2025, the warmer firm voice, the approved Stanton evidence, and the current pricing. The superseded Cultivate bundle is not restored.
- The draft remains a preview. Local/mock testing does not establish live Netlify spam filtering or email delivery. Production publication remains subject to Jonathan's approval.

## October 9, 2026 revision after preview review

Jonathan found the first preview less personal and agreed to a warmer revision for review.

- Firm attribution does not require third-person narration throughout. Use natural we/us language while FCAI owns delivery, methods, and client results.
- Restore the founder portrait near the top of About and a fuller first-person founder note. Its content draws on the existing About narrative; prior career results remain clearly separate from FCAI client work.
- Bring back the plainspoken point of view about team participation, skepticism, and human judgment. Keep the outcome-led services and approved client evidence.
- Restore more of the established ink-and-lake visual character, with human imagery on Home, About, and Contact.
- Concentrate commercial detail on How We Work. Pricing, security claim limits, form behavior, and the Stanton case study remain unchanged.
- This is a revised draft for preview only. Production publication still requires Jonathan's approval.

## October 9, 2026 core page preview

Jonathan approved implementing the October 9 copy draft as a full review preview and explicitly reserved production publication until after review.

- Core pages use firm voice and business outcomes, with process detail on How We Work. First person appears in the About founder note; approved client quotations retain their wording.
- Replace the generic invoice demo and unsupported savings examples with the approved Stanton story and CultureCon quotation. Prior career experience stays attributed to the founder.
- Retain the currently published $5,000–$55,000 project range in this preview. New assessment, implementation, and advisory price bands have not been selected. Do not invent them or publish placeholders.
- Security copy describes the requirements to address during scoping. It does not assert BAA availability, insurance coverage, compliance certification, or verified retention/deletion controls.
- Remove departure slogans, repeated no-retainer messaging, the 12-month exclusion, and the bundle discount/automatic 90-day support pitch. Support is defined in the scope.
- Keep industry positioning open and preserve existing industry and local resources. Shared navigation follows the new core-page order; legacy service section anchors remain valid.
- Contact field names, required states, existing interest values, Netlify submission, and thank-you routing remain compatible. Display labels describe the business need. Two additional interest values cover reporting/information access and workflow improvement; no repository script routes on those values.
- This update supersedes conflicting older copy guidance below. It authorizes a preview, not a production deployment.

## October 8, 2026 update

Jonathan requested removal of the Personal AI Systems offering and correction of the documentation result. These decisions supersede the September 20 personal AI approval below:

- Remove the personal AI offering from the homepage, Services page, site summary, and article links. Keep the ownership field note focused on team workflows.
- The documentation result is 25 hours to 12 hours per workflow, a 52% reduction. Use the baseline and result in public copy. Do not reuse the older 40-hour baseline or the claim of a reduction above 70%.
- This records the requested content decisions, not production deployment status.

## October 8, 2026: named Stanton case study

Jonathan supplied `2026-10-08-stanton-case-study-named-final.pdf`, described it as FCAI's first named case study, and approved the proposed website implementation with “Lets do it!” This supersedes the September 20 pending-case-study status below for the supplied narrative, attribution, quote, and illustrative digest.

- The final PDF is the content source. The public download at `case-studies/stanton-company-kpi-digest.pdf` incorporates Jonathan's subsequent firm-voice and general-CTA corrections; preserve the supplied original in Downloads.
- Lead with weekly visibility across every account and the internal team's rollout and operation. Do not invent ROI, percentage savings, client counts, or measured benefits.
- The quote is from Emily Michels, Director of Operations, Stanton & Company. Preserve its wording and attribution.
- The digest table contains fictional example accounts and sample values. Keep its “Illustrative, sample data” label adjacent to it.
- Use FCAI or Fresh Coast AI as the subject of delivery throughout the HTML page and downloadable PDF, including the byline and author metadata. Jonathan explicitly corrected “Jon rebuilt it” to “FCAI rebuilt it” and rejected “Jon did” or “I did” framing.
- The closing invitation is “Let's talk about your business.” Remove the pitch about reproducing Stanton's workflow or asking whether the same pattern fits another team.
- Add a dedicated HTML story, homepage feature, site navigation and Services links, and a secondary PDF download. The Google tag receives editorial click events only; this does not add a conversion action or verify analytics reporting in the account.
- Website implementation is staged for preview. This record does not authorize or claim production deployment.

## Public language
- Use “No required retainer.” Project fees, optional monthly advisory, separately scoped prepaid support blocks, and third-party software costs are different things.
- Readiness Assessment: 2–4 weeks. Proof of concept: 2–4 weeks. Rollout: 1–3 months. Full Journey: 3–5 months. Agree each schedule at scoping; do not describe all engagements as 6–10 weeks or add the ranges as a guaranteed schedule.
- Public founding date: September 2025. Do not infer a founding date from the current calendar year or copyright.
- Personal AI systems offering approved in this conversation. Publish as a service, not as evidence of client results. No client names, new numeric pricing, or guaranteed savings.
- Remove Living Canvas from the trusted-by row because Jonathan says it is closed. Preserve CultureCon, Trusted Electric, Stanton & Co, and Edie Ford. Preserve approved testimonials as written.
- Additional client work is not approved for public attribution. Do not add names, logos, scope, or results without explicit permission. The personal AI offering does not name a client.
- New field note: “Owning an AI System Means Being Able to Change It.” This is a point-of-view article with an explicitly illustrative example, not a client case study or measured outcome. Date the new article on publication; do not refresh old article dates to imply new writing.
- Remove the static last-shipped footer rather than maintaining a second, easily stale publication clock.

## September 20 history: Stanton case study pending approval (superseded October 8)
Logo permission does not approve a case study. Do not publish a teaser suggesting results have already been approved.

Prepare the story only from approved project material: the original problem, scope, workflow before and after, what the client can operate themselves, and remaining limitations. Separate demo or pilot evidence from live use.

Before publication, obtain approval for the exact narrative, client attribution, screenshots (with private details removed), any quote, and every outcome. A metric needs its baseline, measurement window, source, and client sign-off. Without measured results, write a factual implementation story without invented savings.

Once the final draft is approved, publish it as the first case study, link it from the homepage and blog, and retain that approval with the source material.
