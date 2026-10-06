# TNRN Digital Hub — Plan & Status

Static, multi-page Bootstrap 5.3 website for the Tribal Nations Research Network.
Sources: `TNRN.docx`, `TNRNetwork.pdf`, images in `assets/`. Target: WCAG 2.2 Level AA.

## Decisions (2026-10-06)
- Static multi-page HTML + Bootstrap 5.3 (CDN) + Bootstrap Icons. No server required.
- Missing copy: short draft text written and marked with `data-draft` + `<!-- DRAFT -->` comments.
  Add `?review` to any page URL to outline every draft block.
- Images: assets folder only (PDF stock photos not used). Optimized copies are in `images/`; `assets/` is unchanged.
- Calendar and protocol links: accessible placeholders with `<!-- TODO -->` comments.

## Structure
| Page | File |
|---|---|
| Home (mission, hub ToC, framework, 6 R's, partners) | `index.html` |
| 01 Indigenous Research & Data Sovereignty | `data-sovereignty.html` |
| 02 Professional Development | `professional-development.html` |
| 03 Tribe-Engaged Research | `tribe-engaged-research.html` |
| 04 Resource Repository | `resources.html` |
| 05 Inter-Institutional Research Protocols | `protocols.html` |
| 06 Upcoming Activities & FAQ | `activities.html` |

Shared: `css/styles.css`, `js/main.js`, `images/`. The header and footer are repeated in every page,
so change them in all 7 files.

Local preview: `python3 -m http.server 8765` (also defined in `.claude/launch.json`).

## Status
- [x] Content extraction from docx/pdf; visual style from PDF (teal / slate / copper + 6 R's palette)
- [x] Image optimization (`images/`)
- [x] All 7 pages built
- [x] 2026-10-06: Home framework graphic replaced with `images/tnrn-framework-v2.jpg` (+ WebP); alt text describes the 5→1→2→3 cycle arrows
- [x] Accessibility verification: axe-core (WCAG 2.0/2.1/2.2 A+AA) shows 0 violations on all pages at 1280px and 375px;
      no horizontal scroll at 320px; targets ≥24px; skip link; visible focus; header is sticky only on wide screens (2.4.11);
      mobile menu closes with Escape; reduced-motion and forced-colors supported
- [ ] TNRN review of all draft copy (`?review` mode)
- [ ] Real contact details (footer; the PDF had Canva placeholder text)
- [ ] Protocol page URLs for each Tribe/institution (`protocols.html`)
- [ ] Events calendar content (`activities.html`; template in comment)
- [ ] Resource links (`resources.html`), Indigenous Scholars highlights, Tribal partnership stories
- [ ] Manual screen-reader pass (VoiceOver/NVDA) before launch
- [ ] Confirm logo usage permissions with each partner
