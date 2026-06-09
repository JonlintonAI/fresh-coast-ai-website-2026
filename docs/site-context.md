# Fresh Coast AI Website Context

Last updated: 2026-06-09.

## Current State

Fresh Coast AI is a static HTML website deployed from GitHub to Netlify.

- Repo: `https://github.com/JonlintonAI/fresh-coast-ai-website-2026`
- Production branch: `main`
- Live site: `https://www.freshcoast.ai`
- Netlify project name: `zippy-gecko-f58d8d`
- Netlify site id: `cfe3b403-681a-4794-a9d1-a2c4abbe1f7a`
- Preferred local path: `/Users/jonathanlinton/Documents/FCAI Website 2026`

The project used to live at:

`/Users/jonathanlinton/Documents/New project 2/fresh-coast-ai-website-2026`

## Deployment Notes

The active production site deploys from GitHub `main` to Netlify. The repo folder is linked locally to the Netlify project.

The most recent major production push was commit `1336e1e`, `Refresh national positioning and about copy`.

After that push, the Netlify CDN cache was purged successfully through the direct purge API with HTTP status `202`.

## Domain And Canonical Setup

The primary production domain is:

`https://www.freshcoast.ai`

The apex domain should redirect to `www`:

`https://freshcoast.ai/<path>` to `https://www.freshcoast.ai/<path>`

This matters for Google Ads and Search Console. Google Ads conversion matching was tied to `www.freshcoast.ai`, so the site was switched from apex-primary to `www`-primary.

Canonicals, `og:url`, `og:image`, sitemap URLs, and robots sitemap references should use `https://www.freshcoast.ai`.

## Google Ads Tracking Context

The active lead conversion has been investigated several times.

Key conclusions:

- The sitewide Google tag should stay in place.
- Do not add a manual `gtag('event', 'conversion')` snippet unless Google Ads is intentionally changed to a tag-based conversion action.
- The thank-you page is currently part of a URL-based automatic page-load conversion flow.
- Synthetic `gclid` tests do not prove real attribution because Google validates against real ad clicks.
- Tag Assistant or a real ad click is the right way to validate attribution.

Important tag ids:

- Global tag: `GT-TQSC2BPG`
- Google Ads id: `AW-18008252065`

## LinkedIn Verification

LinkedIn site verification was added as a hidden text file:

`linkedin-site-verification.txt`

Content:

`linkedin-site-verification=d5df9fc5-5a5d-4eab-a26b-3159cf5443f9`

## Positioning

The site now uses a national brand layer with local SEO catcher pages underneath.

Core pages should not frame the audience as only Milwaukee or Midwest businesses. Milwaukee is the home base. The audience is broader.

Preferred service-area language:

- "working with teams wherever they are"
- "in person when it matters"
- "remote when it doesn't"

Local catcher pages should keep local language, local keywords, schema, and NAP. Do not thin or genericize those pages.

## About Page Direction

The About page was rewritten around this idea:

"Technology only works when people do."

The tone is human, honest, and plainspoken. It should not read like a generic AI consultancy bio.

Do not add the optional Bourdain line unless the user explicitly confirms it.

## Content Guardrails

Do not use:

- "zero service disruptions"
- "guiding a complete website rebuild"
- unverifiable absolutes such as "zero compliance incidents," "zero IT dependency," or "100% retention"
- invented metrics, clients, quotes, or personal/family details

Avoid em dashes and filler words in generated or touched copy:

- leverage
- utilize
- robust
- comprehensive
- seamless
- holistic
- paradigm
- synergy
- empower
- game-changer
- pivotal
- tapestry
- landscape, when used as a metaphor

Voice standard: direct, warm, plain, and specific.

## Clients And Logos

The main page currently displays:

- CultureCon
- Trusted Electric
- Living Canvas Foundation

Earlier placeholder or unverified client names were removed.

## Homepage Website-Rebuild Theme

The About page no longer includes the old track-record bullet about guiding a complete website rebuild.

The homepage still contains:

- A workflow card titled "Website & digital presence"
- A real Trusted Electric testimonial that says "We rebuilt my website."

Those are materially different from the removed About claim and are legitimate. If the user wants full consistency around the website-rebuild theme, the first recommended change is to rename the workflow card to something like "Digital ops & estimating" while preserving the real testimonial quote unless the user approves quote editing.

## Netlify Forms

Netlify forms have been part of the site workflow. Do not change form actions, form names, or thank-you redirects casually. The contact form redirects to `contact-thank-you.html`.

If form notifications fail, check Netlify Forms configuration and project linkage before changing site code.

## Local Workflow

This is a static site. A simple local preview is enough:

```bash
python3 -m http.server 5178
```

Then preview with:

`http://127.0.0.1:5178/index.html`

For production verification, use curl against `https://www.freshcoast.ai`.

## Fresh Chat Starter Prompt

Use this when starting a new Codex thread:

```text
Work in /Users/jonathanlinton/Documents/FCAI Website 2026.
Read AGENTS.md and docs/site-context.md first.
Then help me with the Fresh Coast AI website.
```
