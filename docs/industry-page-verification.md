# Industry page handoff and preview checks

This November 22 revision supersedes the industry selection, clinical research copy, accounting dropdown change, and verification checklist in the November 19 instructions. The site branch contains the copy to review.

## Scope

Feature Marketing & PR Agencies, Real Estate, Clinical Research, and Professional Services, in that order. Visitors can find all four on the homepage, in the Milwaukee and Wisconsin industry grids, and in both industry footer styles. Keep Manufacturing, Staffing, and Trades accessible at their existing URLs and in the sitemap for existing visitors. Use the four featured industries in the industry section of `llms.txt`.

Clinical Research covers scheduling, staff and room coverage, changes to visits, and coordinator handoffs. Describe proposed work and who approves the schedule. The insurance statement covers the existence of coverage. Policy types, limits, certifications, clinical decisions, and named-client claims are outside the copy. Professional Services covers client projects, proposals, documents, and reporting. Keep the optional industry dropdown, including its existing accounting and financial services choice, and the free self-assessment.

## Checks before publication

Use the actual Netlify preview URL for the revision under review. Check the rendered site on desktop and a 390-pixel phone. Record the revision, URL, and any failing route.

1. Open the homepage, both active location pages, and both footer styles. Follow each of the four featured links. Confirm the titles, order, HTTP 200 responses, and final destinations. Check the footer on the assessment, contact thank-you page, and booking confirmation. The retired assessment thank-you route should still redirect to the assessment.
2. Open both `/industries/property-management` and `/industries/property-management.html` without following redirects. Each must return HTTP 301 directly to `/industries/real-estate`, which must return HTTP 200. Check the trailing-slash entry as well. Search published pages, the sitemap, and `llms.txt` for links to the old route.
3. Run `python3 docs/check-stanton-logo.py` in the checkout and repeat with `--base-url https://YOUR-PREVIEW-HOST`. The homepage and agency testimonial must use the root-relative PNG, preserve Emily Michels’s words and attribution, and load the actual image. In a browser, scroll each figure into view, confirm its displayed height and width are positive, and inspect it on desktop and mobile. Follow the agency case-study link to the named case study.
4. On all seven reachable industry pages, inspect the title, H1, search and social descriptions, canonical URL, and page text. Check the CTA fee against How We Work. Architecture quoted separately, the intro call and the self-assessment must be clear. Review unqualified performance claims in headings as well as paragraphs. Check that Clinical Research and Professional Services stay within the scope above.
5. Parse every industry JSON-LD script separately. Compare every FAQ question and answer against its visible card after normalizing whitespace. Check breadcrumb destinations, canonical, and Open Graph URL against that page’s route. Inspect the XML sitemap for exactly one entry per reachable industry page.
6. From an industry page, follow the self-assessment link, choose the accounting and financial services option, answer all fourteen questions, and verify the visible score. Repeat with the industry blank and identical answers. The scores should match. Check the intro-call button opens the booking page.
7. On mobile, open the navigation, follow a link, inspect the four homepage links and both location grids, and check for horizontal overflow. Submit the preview for business-owner review before publishing to the production branch.
