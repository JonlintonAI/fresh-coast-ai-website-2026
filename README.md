# Fresh Coast AI — Website (May 2026 redesign)

Static HTML site for [freshcoast.ai](https://freshcoast.ai). Served via Netlify.

## Structure

```
.
├── index.html                  # Homepage (May 2026 redesign)
├── about.html                  # About / founder story
├── how-we-work.html            # Process + pricing
├── services.html               # Service tiers
├── contact.html                # Free consultation form
├── assessment.html             # AI Readiness self-assessment
├── deliverables.html           # Sample deliverables landing
├── deliverables/               # Detail pages per deliverable (6)
├── industries/                 # Industry-specific pages (6)
├── blog/                       # Blog index + 11 posts (+ pending drafts)
├── milwaukee-ai-consulting.html        # Local SEO landing pages
├── madison-ai-consulting.html
├── green-bay-fox-valley-ai-consulting.html
├── wisconsin-ai-consulting.html
├── privacy.html · terms.html · 404.html
├── contact-thank-you.html · assessment-thank-you.html
├── brand-2026.css              # Site-wide design overrides (May 2026)
├── sitemap.xml · robots.txt · _redirects
└── (images, fonts, favicons, PDFs)
```

## Design system

- **Fonts**: DM Serif Display, Outfit, JetBrains Mono (loaded via Google Fonts)
- **Color tokens** (defined in each page's inline `<style>` and overridden by `brand-2026.css`):
  - `--ink: #0B1A2B` (deep ink blue)
  - `--lake: #2B7A9E` (signature blue)
  - `--wave: #48B5D2` (light blue accent)
  - `--sand: #D97757` (terracotta, replaced yellow as of May 2026)
- `brand-2026.css` is a site-wide override stylesheet that propagates the May 2026 redesign across every interior page.

## Tracking

- **Google tag**: `GT-TQSC2BPG` (every production page)
- **Google Ads**: `AW-18008252065` (every production page)
- **Manual conversion event snippets**: removed. Lead tracking should be handled by Google Tag / Ads configuration, not page-level conversion calls.

## Forms

Powered by Netlify Forms.

- `contact` — full consultation form
- `assessment-results` — anonymous score data on assessment completion
- `assessment-leads` — email leads from assessment

## Deploy

Drag-and-drop the folder onto [app.netlify.com/drop](https://app.netlify.com/drop) or push to a Netlify-connected git branch.

## Source-of-truth files

- **Live site as of May 2026**: this repo
- **Pre-redesign archive**: `Claude Website` folder (kept locally, not in this repo)
- **SEO/GEO audit**: `Claude Outputs/2026-05-04-seo-geo-audit-new-website.md`
