# Google Ads Import Instructions

## Why CSV Instead of Browser?
The LastPass extension keeps stealing focus every time Google Ads navigates, blocking me from clicking the "Done" button. These CSV files give you the same result in about 2 minutes.

## What's Included

| File | What It Does |
|------|-------------|
| `01-ad-groups.csv` | Creates 2 new ad groups: "AI Strategy Session" and "AI Implementation & Build" |
| `02-keywords.csv` | Adds 13 phrase-match keywords across both ad groups |
| `03-negative-keywords.csv` | Adds 27 campaign-level negative keywords to block wasted spend |
| `04-responsive-search-ads.csv` | Creates 2 RSA ads with 15 headlines + 4 descriptions each |

## Option A: Google Ads Editor (Recommended, ~2 min)

1. Download Google Ads Editor from ads.google.com/home/tools/ads-editor/
2. Open it, sign in with jonlinton@gmail.com
3. Download your account (Get recent changes)
4. For each CSV file, go to **Account > Import > From file**
5. Import in this order: ad groups first, then keywords, then negative keywords, then ads
6. Click **Post** to push changes live

## Option B: Google Ads Web UI Bulk Upload (~3 min)

1. Go to ads.google.com > Campaign #1
2. Click **Tools** in the left nav > **Bulk actions** > **Uploads**
3. Click **+** to create a new upload
4. Upload each CSV file in order
5. Review the preview and click **Apply**

## Manual Step: Location Targeting

After importing, expand your location targeting:

1. Go to **Campaign settings** > **Locations**
2. Remove "Milwaukee" DMA if it's the only target
3. Add these states: **Wisconsin, Illinois, Michigan, Minnesota, Indiana, Iowa, Ohio**
4. Keep "Presence: People in or regularly in your targeted locations"

## Manual Step: Pause "Ad group 1"

The original "Ad group 1" has spent $343 with poor conversion rates. Consider pausing it:

1. Go to **Ad groups**
2. Click the green dot next to "Ad group 1"
3. Select **Paused**

## Summary of Changes

### New Ad Groups
- **AI Strategy Session**: 7 keywords targeting people looking for AI strategy help
- **AI Implementation & Build**: 6 keywords targeting people ready to build AI workflows

### New RSA Ads (one per ad group)
- 15 headlines each (30 char max) emphasizing: ownership, fixed-fee, vendor-neutral, $1K strategy session, 4-week timeline
- 4 descriptions each (90 char max) reinforcing the "built to end" positioning

### Negative Keywords (campaign-level)
- Blocks: jobs/careers, software/SaaS, training/courses, competitors (dynatrace), free tools, AI platforms (chatgpt/openai)

### Location Targeting
- Expand from Milwaukee to 7 Midwest states (WI, IL, MI, MN, IN, IA, OH)
