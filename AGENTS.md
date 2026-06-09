# Fresh Coast AI Website Instructions

## Project

- This repo is the Fresh Coast AI public website.
- GitHub repo: `JonlintonAI/fresh-coast-ai-website-2026`.
- Production branch: `main`.
- Production site: `https://www.freshcoast.ai`.
- Netlify project: `zippy-gecko-f58d8d`.
- Netlify site id: `cfe3b403-681a-4794-a9d1-a2c4abbe1f7a`.
- Local preferred path: `/Users/jonathanlinton/Documents/FCAI Website 2026`.

## Deployment

- The site deploys from GitHub to Netlify from `main`.
- Do not push directly to `main` unless the user explicitly asks to push live.
- For normal changes, prefer a `codex/` branch and a pull request.
- If the user explicitly says to push live, commit intentionally and push to `main`.
- After deploy, verify public pages at `https://www.freshcoast.ai`.
- If cached content appears stale, purge Netlify's CDN cache for the site.

## Site Architecture

- This is a static HTML site.
- Core national pages should speak to businesses broadly:
  - `index.html`
  - `about.html`
  - `services.html`
  - `how-we-work.html`
  - `contact.html`
- Local SEO catcher pages should keep local framing, local keywords, schema, and NAP:
  - `milwaukee-ai-consulting.html`
  - `madison-ai-consulting.html`
  - `green-bay-fox-valley-ai-consulting.html`
  - `wisconsin-ai-consulting.html`
- Industry pages should use national service-area language unless a local example is specific and intentional.

## Positioning

- National layer: Fresh Coast AI works with teams wherever they are.
- Milwaukee is the home base, not the audience boundary.
- Preferred service-area language: "working with teams wherever they are," "in person when it matters," and "remote when it doesn't."
- Keep the broad category targets separate from geo targets:
  - Core pages: AI adoption consultant, AI readiness, AI governance, AI implementation.
  - Location pages: city or state AI consulting terms.

## Content Guardrails

- Never use the phrase "zero service disruptions."
- Do not claim "zero compliance incidents," "zero IT dependency," "100% retention," or similar absolutes unless the user explicitly confirms the proof.
- Do not reference "guiding a complete website rebuild."
- Do not invent facts, metrics, clients, client quotes, or personal/family details.
- Avoid em dashes in site copy. Use periods, commas, colons, or parentheses.
- Avoid filler words in generated or touched site copy: leverage, utilize, robust, comprehensive, seamless, holistic, paradigm, synergy, empower, game-changer, pivotal, tapestry, landscape.
- Keep the voice direct, warm, plain, and specific.

## Known Content Decisions

- Current displayed clients include CultureCon, Trusted Electric, and Living Canvas Foundation.
- Trusted Electric website-related language on the homepage is real client/testimonial material. If full consistency around the website-rebuild theme is requested, consider renaming the workflow card before altering the quote.
- The optional Bourdain line for the About page should not be added unless the user explicitly confirms it.
- Do not create new metro/location pages without user direction.

## Verification

- Use `rg` for content scans.
- Run `git diff --check` before committing.
- For frontend checks, preview locally with a static server, for example:
  - `python3 -m http.server 5178`
- Check mobile responsiveness around `390px` width when changing layout or long copy.
- Check for broken visible images after changing page structure, logos, or image references.

## Useful Commands

```bash
git status --short --branch
git diff --check
rg -ni "zero service disruptions|complete website rebuild|zero compliance incidents|zero IT dependency|100% retention" .
rg -n "Midwest|Milwaukee businesses|serving businesses nationwide|work with businesses across|Milwaukee-based but work anywhere" index.html about.html services.html how-we-work.html contact.html
curl -sI https://freshcoast.ai/contact-thank-you.html | head -n 5
curl -sI https://www.freshcoast.ai/contact-thank-you.html | head -n 5
```

## Related Context

- Read `docs/site-context.md` before making strategic content, SEO, Netlify, Google Ads, or analytics changes.
