"""Build the TNRN promotional summary for the Idaho CREWS website.

Outputs (from the same content, so they stay in sync):
  tnrn-summary.html          standalone page (inline CSS, embedded images)
  tnrn-summary-snippet.html  paste-in block for an existing page (scoped CSS, embedded images,
                             headings start at h2 so it fits under the host page's h1)

Run from anywhere:  python3 promo/build_promo.py
Edit the CONTENT / CSS below, then re-run. Images come from promo/images/.
"""
import base64
import pathlib

HERE = pathlib.Path(__file__).parent
HUB_URL = "https://ui-iids.github.io/tnrn-digital-hub/"


def img(name):
    data = base64.b64encode((HERE / "images" / f"{name}.webp").read_bytes()).decode()
    return f"data:image/webp;base64,{data}"


# Colors match the Digital Hub and are verified for WCAG 2.2 AA:
#   white on #08332b 13.8:1 | white on #0a4f42 9.5:1 | #08332b on #ffc56b 8.9:1
#   #1f2a2e on #fbf8f3 13.9:1 | #4a5560 on #fff 7.5:1 | #8a4b22 on #fff 6.8:1
CSS = """
.tnrn-promo {
  --tp-deep: #08332b; --tp-dark: #0a4f42; --tp-teal: #0e6b58; --tp-tint: #e9f4f0;
  --tp-cream: #fbf8f3; --tp-ink: #1f2a2e; --tp-slate: #4a5560; --tp-clay: #8a4b22;
  --tp-gold: #ffc56b; --tp-sun: #e07a1f; --tp-focus: #0a4f42;
  --tp-display: "Barlow Condensed", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --tp-body: "Source Sans 3", "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
  color: var(--tp-ink);
  background: var(--tp-cream);
  font-family: var(--tp-body);
  font-size: 1.125rem;
  line-height: 1.6;
  overflow-wrap: break-word;
}
.tnrn-promo *, .tnrn-promo *::before, .tnrn-promo *::after { box-sizing: border-box; }
.tnrn-promo h1, .tnrn-promo h2, .tnrn-promo h3, .tnrn-promo h4 {
  font-family: var(--tp-display); font-weight: 700; line-height: 1.1;
  letter-spacing: .01em; margin: 0 0 .75rem; color: inherit;
}
.tnrn-promo p { margin: 0 0 1rem; }
.tnrn-promo ul { margin: 0; padding: 0; list-style: none; }
.tnrn-promo img { max-width: 100%; height: auto; display: block; }
.tnrn-promo a { color: var(--tp-dark); text-decoration: underline; text-underline-offset: .18em; }
.tnrn-promo a:hover { color: var(--tp-clay); text-decoration-thickness: 2px; }
.tnrn-promo a:focus-visible {
  outline: 3px solid var(--tp-focus); outline-offset: 3px; border-radius: 4px;
}
.tnrn-promo .tp-on-dark { --tp-focus: var(--tp-gold); }
.tnrn-promo .tp-wrap { max-width: 1140px; margin: 0 auto; padding: 0 1rem; }
.tnrn-promo .tp-section { padding: 3.5rem 0; }
.tnrn-promo .tp-eyebrow {
  font-family: var(--tp-body); font-size: .9rem; font-weight: 700; letter-spacing: .16em;
  text-transform: uppercase; color: var(--tp-clay); margin-bottom: .5rem;
}
.tnrn-promo .tp-lede { color: var(--tp-slate); max-width: 44rem; }

/* Hero */
.tnrn-promo .tp-hero {
  color: #fff; padding: 3.5rem 0;
  background-color: var(--tp-deep);
  background-image:
    url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='56' height='56' viewBox='0 0 56 56'%3e%3cpath d='M28 6 L36 28 L28 50 L20 28 Z' fill='none' stroke='%23ffffff' stroke-opacity='.07' stroke-width='2'/%3e%3c/svg%3e"),
    radial-gradient(ellipse at 85% 30%, rgba(26,166,183,.35), transparent 60%),
    radial-gradient(ellipse at 10% 100%, rgba(224,122,31,.22), transparent 55%);
}
.tnrn-promo .tp-hero-grid { display: grid; gap: 2rem; align-items: center; }
.tnrn-promo .tp-hero .tp-eyebrow { color: var(--tp-gold); }
.tnrn-promo .tp-hero-title { font-size: clamp(2.4rem, 6vw, 3.75rem); }
.tnrn-promo .tp-hero p { color: #f1f7f5; max-width: 40rem; }
.tnrn-promo .tp-hero .tp-big { font-size: 1.3rem; }
.tnrn-promo .tp-emblem { width: 100%; max-width: 340px; margin: 0 auto; filter: drop-shadow(0 14px 30px rgba(0,0,0,.35)); }
.tnrn-promo .tp-band {
  height: 10px;
  background: linear-gradient(90deg, #0b3f7a 0 14%, #1aa6b7 14% 28%, #2e7d32 28% 42%,
    #ffd54f 42% 57%, #f7941d 57% 71%, #d84315 71% 85%, #7a1f12 85% 100%);
}

/* Buttons */
.tnrn-promo .tp-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: .5rem;
  min-height: 48px; padding: .75rem 1.5rem; border-radius: .6rem;
  font-weight: 700; font-size: 1.1rem; text-decoration: none; border: 2px solid transparent;
}
.tnrn-promo .tp-btn-gold { background: var(--tp-gold); color: var(--tp-deep); }
.tnrn-promo .tp-btn-gold:hover { background: #ffd998; color: var(--tp-deep); }
.tnrn-promo .tp-btn-teal { background: var(--tp-teal); color: #fff; }
.tnrn-promo .tp-btn-teal:hover { background: var(--tp-deep); color: #fff; }
.tnrn-promo .tp-actions { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1.5rem; }

/* Goals */
.tnrn-promo .tp-goals { display: grid; gap: 1rem; margin-top: 1.5rem; }
.tnrn-promo .tp-goal {
  background: var(--tp-dark); color: #fff; border-radius: .75rem; padding: 1.5rem;
  border-left: 6px solid var(--tp-gold);
}
.tnrn-promo .tp-goal-title { font-size: 1.6rem; margin: 0; }

/* Cards */
.tnrn-promo .tp-cards { display: grid; gap: 1rem; margin-top: 1.75rem; }
.tnrn-promo .tp-card {
  background: #fff; border: 1px solid #d9e6e1; border-top: 6px solid var(--tp-teal);
  border-radius: .75rem; padding: 1.4rem 1.5rem;
}
.tnrn-promo .tp-card-title { font-size: 1.45rem; color: var(--tp-dark); }
.tnrn-promo .tp-card p { color: var(--tp-slate); margin: 0; font-size: 1.05rem; }

/* 6 R's */
.tnrn-promo .tp-white { background: #fff; }
.tnrn-promo .tp-split { display: grid; gap: 2rem; align-items: center; }
.tnrn-promo .tp-rs { display: grid; grid-template-columns: repeat(2, 1fr); gap: .65rem; }
.tnrn-promo .tp-rs li {
  background: var(--tp-cream); border: 1px solid #d9e6e1; border-left: 6px solid var(--tp-sun);
  border-radius: .5rem; padding: .7rem 1rem;
  font-family: var(--tp-display); font-size: 1.3rem; font-weight: 700; color: var(--tp-deep);
}

/* Hub list */
.tnrn-promo .tp-tint { background: var(--tp-tint); }
.tnrn-promo .tp-hub { display: grid; gap: .75rem; margin-top: 1.5rem; counter-reset: hub; }
.tnrn-promo .tp-hub li {
  counter-increment: hub; display: flex; align-items: center; gap: 1rem;
  background: #fff; border: 1px solid #cfe0da; border-radius: .6rem; padding: .85rem 1rem;
  font-weight: 600;
}
.tnrn-promo .tp-hub li::before {
  content: counter(hub, decimal-leading-zero);
  font-family: var(--tp-display); font-size: 1.6rem; font-weight: 700; color: var(--tp-teal);
  min-width: 2.25rem;
}

/* Partners */
.tnrn-promo .tp-partners { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1.5rem; }
.tnrn-promo .tp-partners li {
  background: #fff; border: 1px solid #d9e6e1; border-radius: .75rem; padding: 1rem;
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  gap: .6rem; text-align: center;
}
.tnrn-promo .tp-partners img { max-height: 80px; width: auto; }
.tnrn-promo .tp-partners span { font-size: .98rem; font-weight: 600; color: var(--tp-slate); line-height: 1.3; }

/* CTA */
.tnrn-promo .tp-cta { color: #fff; text-align: center; background: var(--tp-deep); padding: 3rem 0; }
.tnrn-promo .tp-cta p { color: #f1f7f5; max-width: 40rem; margin-left: auto; margin-right: auto; }
.tnrn-promo .tp-cta .tp-actions { justify-content: center; }

@media (min-width: 640px) {
  .tnrn-promo .tp-cards { grid-template-columns: repeat(2, 1fr); }
  .tnrn-promo .tp-goals { grid-template-columns: repeat(2, 1fr); }
  .tnrn-promo .tp-partners { grid-template-columns: repeat(3, 1fr); }
  .tnrn-promo .tp-hub { grid-template-columns: repeat(2, 1fr); }
  .tnrn-promo .tp-rs { grid-template-columns: repeat(3, 1fr); }
}
@media (min-width: 960px) {
  .tnrn-promo .tp-hero-grid { grid-template-columns: 1.5fr 1fr; }
  .tnrn-promo .tp-split { grid-template-columns: 1fr 1.2fr; }
  .tnrn-promo .tp-cards { grid-template-columns: repeat(3, 1fr); }
  .tnrn-promo .tp-partners { grid-template-columns: repeat(6, 1fr); }
  .tnrn-promo .tp-hub { grid-template-columns: repeat(3, 1fr); }
}
@media (prefers-reduced-motion: reduce) {
  .tnrn-promo *, .tnrn-promo *::before, .tnrn-promo *::after { transition: none !important; animation: none !important; }
}
@media (forced-colors: active) {
  .tnrn-promo .tp-card, .tnrn-promo .tp-goal, .tnrn-promo .tp-partners li, .tnrn-promo .tp-hub li { border: 1px solid CanvasText; }
}
"""

PINPOINT = '<script src="https://pinpoint.nkn.uidaho.edu/embed.js" data-project="EN5sGA_bUls0IUqB" async></script>'

EMBLEM_ALT = ("Tribal Nations Research Network seal: a carved wooden medallion with a tree whose "
              "branches hold feathers and patterned leaves, the shape of Idaho in its trunk, and "
              "mountains and a river on either side. A banner reads TNRN, Building Tribe-Driven Research.")

PARTNERS = [
    ("logo-cda", "Coeur d&rsquo;Alene Tribe", 160, 160),
    ("logo-sbt", "Shoshone-Bannock Tribes of Fort Hall", 160, 160),
    ("logo-ui", "University of Idaho", 145, 160),
    ("logo-isu", "Idaho State University", 107, 160),
    ("logo-bsu", "Boise State University", 180, 134),
    ("logo-icrews", "Idaho I-CREWS", 160, 160),
]


def content(h1, h2, h3):
    """h1/h2/h3 are the tag names for the three heading levels used."""
    partners = "\n".join(
        f'          <li><img src="{img(n)}" alt="" width="{w}" height="{h}" loading="lazy"><span>{label}</span></li>'
        for n, label, w, h in PARTNERS
    )
    hub_link = (f'<a class="tp-btn tp-btn-gold" href="{HUB_URL}">'
                'Visit the TNRN Digital Hub</a>')
    return f"""
  <section class="tp-hero tp-on-dark" aria-labelledby="tnrn-promo-title">
    <div class="tp-wrap tp-hero-grid">
      <div>
        <p class="tp-eyebrow">Part of Idaho I-CREWS</p>
        <{h1} id="tnrn-promo-title" class="tp-hero-title">Tribal Nations Research Network</{h1}>
        <p class="tp-big">Recentering knowledge exchange between Tribes and Idaho universities, in support of Tribes&rsquo; sovereignty and self-determination.</p>
        <p>Critical to that effort is the inclusion of Indigenous ways of knowing into higher education and research. The network focuses on collaboration between Tribes and universities through the development of research originated by Tribal nations.</p>
        <div class="tp-actions">{hub_link}</div>
      </div>
      <img class="tp-emblem" src="{img('tnrn-seal')}" width="440" height="435" alt="{EMBLEM_ALT}">
    </div>
  </section>
  <div class="tp-band" aria-hidden="true"></div>

  <section class="tp-section" aria-labelledby="tnrn-promo-goals">
    <div class="tp-wrap">
      <p class="tp-eyebrow">Our Goals</p>
      <{h2} id="tnrn-promo-goals" style="font-size:clamp(1.9rem,4vw,2.6rem)">Two commitments at the center</{h2}>
      <ul class="tp-goals tp-on-dark">
        <li class="tp-goal"><{h3} class="tp-goal-title">Build Tribe-centered research capacity</{h3}></li>
        <li class="tp-goal"><{h3} class="tp-goal-title">Build Idaho education institutions&rsquo; capacity to center Tribe-driven research</{h3}></li>
      </ul>

      <ul class="tp-cards">
        <li class="tp-card">
          <{h3} class="tp-card-title">Researchers</{h3}>
          <p>Tribal nation researchers, faculty, and student researchers, including Indigenous students, working together.</p>
        </li>
        <li class="tp-card">
          <{h3} class="tp-card-title">Training System</{h3}>
          <p>Building Tribal administrative and institutional capacity through a professional development framework sustained within institutions.</p>
        </li>
        <li class="tp-card">
          <{h3} class="tp-card-title">Inter-Institutional Capacity</{h3}>
          <p>Shared systems, procedures, and agreements, plus a sustainable training model and an inter-institutional website that lasts beyond I-CREWS.</p>
        </li>
        <li class="tp-card">
          <{h3} class="tp-card-title">SEED Grants</{h3}>
          <p>Piloting collaborative research practices, including Coeur d&rsquo;Alene Tribe projects on temperature and snowpack scenarios and a Coeur d&rsquo;Alene Basin integrated archival framework.</p>
        </li>
        <li class="tp-card">
          <{h3} class="tp-card-title">Relational Research</{h3}>
          <p>Research rooted in relationship, respect, responsibility, and reciprocity that serves communities well beyond a grant cycle.</p>
        </li>
      </ul>
    </div>
  </section>

  <section class="tp-section tp-white" aria-labelledby="tnrn-promo-6rs">
    <div class="tp-wrap tp-split">
      <div>
        <p class="tp-eyebrow">Featured Series</p>
        <{h2} id="tnrn-promo-6rs" style="font-size:clamp(1.9rem,4vw,2.6rem)">The 6 R&rsquo;s of Indigenous Research</{h2}>
        <p class="tp-lede">A workshop series on ethical Native-engaged research, grounded in six interconnected values.</p>
      </div>
      <ul class="tp-rs">
        <li>Respect</li><li>Relationality</li><li>Responsibility</li>
        <li>Representation</li><li>Relevance</li><li>Reciprocity</li>
      </ul>
    </div>
  </section>

  <section class="tp-section tp-tint" aria-labelledby="tnrn-promo-hub">
    <div class="tp-wrap">
      <p class="tp-eyebrow">TNRN Digital Hub</p>
      <{h2} id="tnrn-promo-hub" style="font-size:clamp(1.9rem,4vw,2.6rem)">One place for Tribes, researchers, and institutions</{h2}>
      <p class="tp-lede">The Digital Hub brings together guidance, learning, and connections for responsible research with Tribal nations.</p>
      <ul class="tp-hub">
        <li>Indigenous Research &amp; Data Sovereignty</li>
        <li>Professional Development</li>
        <li>Tribe-Engaged Research</li>
        <li>Resource Repository</li>
        <li>Inter-Institutional Research Protocols</li>
        <li>Upcoming Activities</li>
      </ul>
    </div>
  </section>

  <section class="tp-section" aria-labelledby="tnrn-promo-partners">
    <div class="tp-wrap">
      <p class="tp-eyebrow">Our Network</p>
      <{h2} id="tnrn-promo-partners" style="font-size:clamp(1.9rem,4vw,2.6rem)">Partners</{h2}>
      <p class="tp-lede">Tribal nations and Idaho universities working together.</p>
      <ul class="tp-partners">
{partners}
      </ul>
    </div>
  </section>

  <section class="tp-cta tp-on-dark" aria-labelledby="tnrn-promo-cta">
    <div class="tp-wrap">
      <{h2} id="tnrn-promo-cta" style="font-size:clamp(1.9rem,4vw,2.6rem)">Research that serves communities for generations</{h2}>
      <p>Explore resources on Indigenous data sovereignty, professional development, and research protocols across our partner Tribes and institutions.</p>
      <div class="tp-actions">{hub_link}</div>
    </div>
  </section>
  <div class="tp-band" aria-hidden="true"></div>
"""


FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700'
         '&amp;family=Source+Sans+3:wght@400;600;700&amp;display=swap" rel="stylesheet">')

standalone = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tribal Nations Research Network | Idaho I-CREWS</title>
<meta name="description" content="The Tribal Nations Research Network recenters knowledge exchange between Tribes and Idaho universities in support of Tribal sovereignty and self-determination.">
{FONTS}
<style>
html, body {{ margin: 0; background: #fbf8f3; }}
.tp-skip {{ position: absolute; left: 1rem; top: -100px; z-index: 10; padding: .75rem 1.25rem;
  background: #08332b; color: #fff; font: 700 1rem system-ui, sans-serif; border-radius: 0 0 .5rem .5rem; }}
.tp-skip:focus {{ top: 0; outline: 3px solid #ffc56b; outline-offset: 2px; }}
{CSS}
</style>
</head>
<body>
<a class="tp-skip" href="#tnrn-promo-main">Skip to main content</a>
<main id="tnrn-promo-main" class="tnrn-promo" tabindex="-1">
{content("h1", "h2", "h3")}
</main>
{PINPOINT}
</body>
</html>
"""

snippet = f"""<!-- ============================================================
  TNRN promotional block for the Idaho CREWS website.
  Paste this whole block into a page or HTML/CMS block.
  - All styles are scoped to .tnrn-promo and will not affect the rest of the page.
  - Headings start at h2, so the host page should already have an h1.
  - Images are embedded (data URIs). If your CMS strips them, upload the files
    in promo/images/ and replace each src with the uploaded URL.
  - The font <link> is optional; without it the block uses system fonts.
  - The Pinpoint <script> at the end only runs on domains registered to the TNRN
    Pinpoint project. Ask the TNRN team to register this site's domain, or remove the script.
  Generated by promo/build_promo.py. Edit that script and re-run instead of editing this file.
============================================================= -->
{FONTS}
<style>
{CSS}
</style>
<div class="tnrn-promo">
{content("h2", "h3", "h4")}
</div>
{PINPOINT}
"""

(HERE / "tnrn-summary.html").write_text(standalone)
(HERE / "tnrn-summary-snippet.html").write_text(snippet)
for f in ("tnrn-summary.html", "tnrn-summary-snippet.html"):
    print(f, round((HERE / f).stat().st_size / 1024), "KB")
