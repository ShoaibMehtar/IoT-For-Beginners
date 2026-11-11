"""Static site generator for qventus.qa.

Usage (from the qventus-website folder):  python3 _build/build.py
Writes the HTML pages, sitemap.xml and robots.txt next to the assets folder.
"""
import json
import os
import sys
from html import escape
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *  # noqa: E402,F403

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVC = {s["slug"]: s for s in SERVICES}
PRJ = {p["id"]: p for p in PROJECTS}

# ---------------------------------------------------------------- icons (24px stroke icons)
ICON_PATHS = {
    "building": "M4 21V5l8-3v19M12 21V9l8 3v9M2 21h20M7 7h2M7 11h2M7 15h2M15 14h2M15 18h2",
    "bed": "M2 19V7M2 15h20v4M22 15v-2.5A2.5 2.5 0 0 0 19.5 10H11v5M6.5 12.5a1.5 1.5 0 1 0 0-.01",
    "health": "M12 21s-8-4.5-8-11a5 5 0 0 1 8-4 5 5 0 0 1 8 4c0 6.5-8 11-8 11zM12 8.5v5M9.5 11h5",
    "factory": "M2 21V10l6 4v-4l6 4V6l8-3v18zM2 21h20M17 10v3",
    "server": "M4 3h16v5H4zM4 10h16v5H4zM4 17h16v4H4zM7.5 5.5h.01M7.5 12.5h.01M7.5 19h.01",
    "anchor": "M12 3a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM12 7v14M5 13H2a10 10 0 0 0 20 0h-3M8.5 10h7",
    "rig": "M6 21l6-18 6 18M8 15h8M9.6 10h4.8M3 21h18M12 3v18",
    "gov": "M3 21h18M5 21v-10M9.5 21v-10M14.5 21v-10M19 21v-10M2 10l10-6 10 6z",
    "food": "M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 0-3 2-3 6s1 4 3 4v8V3",
    "warehouse": "M2 21V8l10-5 10 5v13M6 21v-9h12v9M6 15h12M6 18h12",
    "plane": "M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z",
    "edu": "M2 9l10-5 10 5-10 5zM6 11v5c3 2 9 2 12 0v-5M22 9v6",
    "chiller": "M3 5h18v13H3zM3 18v3M21 18v3M7.5 11.5m-3 0a3 3 0 1 0 6 0 3 3 0 1 0-6 0M13 8h5M13 11.5h5M13 15h5",
    "tower": "M6 21l2-13h8l2 13zM4.5 8h15M9 5h6v3M7.6 13h8.8M7 17.5h10M10 2.5h4",
    "ahu": "M2 7h20v10H2zM8 12m-3 0a3 3 0 1 0 6 0 3 3 0 1 0-6 0M14 9.5v5M17 9.5v5M20 9.5v5",
    "fcu": "M3 5h18v6H3zM6 8h12M6.5 14c0 2 2 2 2 4.5M12 14c0 2 0 2 0 4.5M17.5 14c0 2-2 2-2 4.5",
    "package": "M3 8h18v12H3zM3 8l3-4h12l3 4M9 14m-3 0a3 3 0 1 0 6 0 3 3 0 1 0-6 0M15 12h3M15 16h3",
    "rooftop": "M2 21h20M4 21V11h16v10M7 11V7h10v4M8 16h8M12 3v4",
    "vrf": "M3 4h8v7H3zM13 4h8v4h-8zM13 10.5h8v4h-8zM13 17h8v4h-8zM7 11v8h6M7 12.5h6",
    "thermo": "M14 14.8V4.5a2.5 2.5 0 0 0-5 0v10.3a4.5 4.5 0 1 0 5 0zM11.5 9v7.5M17.5 6h3M17.5 10h3",
    "snow": "M12 2v20M4.9 4.9l14.2 14.2M2 12h20M4.9 19.1L19.1 4.9M9 3.5l3 2 3-2M9 20.5l3-2 3 2",
    "blast": "M4 3h16v18H4zM4 10h16M7 6.5h2M7 13.5h2M13 15l2.5 2.5L18 15M15.5 13v4.5",
    "fan": "M12 12m-2 0a2 2 0 1 0 4 0 2 2 0 1 0-4 0M12 10c0-4 1-7 4-7s2 5-2 7M14 12c4 0 7 1 7 4s-5 2-7-2M12 14c0 4-1 7-4 7s-2-5 2-7M10 12c-4 0-7-1-7-4s5-2 7 2",
    "monitor": "M3 4h18v12H3zM8 20h8M12 16v4M6 12l3-3 3 2 4-5 2 2",
    "chart": "M3 3v18h18M7 15l4-4 3 3 5-6M16 8h3v3",
    "bolt": "M13 2L4 14h7l-1 8 9-12h-7z",
    "smart": "M4 21V9l8-6 8 6v12zM9 21v-6h6v6M8.5 11a5 5 0 0 1 7 0M10.3 13a2.4 2.4 0 0 1 3.4 0",
    "check": "M20 6L9 17l-5-5",
    "arrow": "M5 12h14M13 6l6 6-6 6",
    "phone": "M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z",
    "mail": "M3 5h18v14H3zM3 6l9 7 9-7",
    "pin": "M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12zM12 9m-2.5 0a2.5 2.5 0 1 0 5 0 2.5 2.5 0 1 0-5 0",
    "clock": "M12 12m-9 0a9 9 0 1 0 18 0 9 9 0 1 0-18 0M12 7v5l3 2",
    "alert": "M12 3l10 18H2zM12 10v5M12 18h.01",
    "home": "M3 11l9-8 9 8M5 9.5V21h14V9.5M10 21v-6h4v6",
    "drawing": "M3 21h18M5 21V5h14v16M8 9h8M8 13h5M8 17h8M14 13l2 2",
    "wrench": "M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z",
    "filter": "M3 4h18l-7 8.5V19l-4 2v-8.5z",
    "gear": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 0 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 0 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 0 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 0 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z",
    "container": "M2 7h20v12H2zM6 7v12M10 7v12M14 7v12M18 7v12M2 4h20",
    "event": "M3 21V9l9-6 9 6v12M3 21h18M8 21v-6h8v6M12 3v4",
    "people": "M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM2 21v-1a6 6 0 0 1 12 0v1M16 3.1a4 4 0 0 1 0 7.8M22 21v-1a6 6 0 0 0-4-5.6",
}
WA_PATH = "M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8 8 0 0 1-2.4-1.5 9 9 0 0 1-1.6-2c-.2-.3 0-.5.1-.6l.5-.5.3-.5a.5.5 0 0 0 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.4 13.4 0 0 0 5.2 4.6c.7.3 1.3.5 1.7.6a4.2 4.2 0 0 0 1.9.1 3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.1-.3-.2-.6-.3zM12 21.8a9.9 9.9 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.9L.1 24l6.3-1.6a11.8 11.8 0 0 0 5.6 1.4A11.8 11.8 0 0 0 20.4 3.6z"


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{ICON_PATHS[name]}"/></svg>')


def wa_icon():
    return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{WA_PATH}"/></svg>'


CHEV = '<svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M1 1l4 4 4-4"/></svg>'

LOGO = ('<a class="logo" href="{r}index.html" aria-label="Q Ventus — home">'
        '<svg class="q" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="4" aria-hidden="true">'
        '<circle cx="18" cy="18" r="14.5"/><path d="M19 34.5h19" stroke-linecap="round"/></svg>'
        '<span class="word">VENTUS</span>'
        '<svg class="wind" viewBox="0 0 40 32" fill="none" stroke="#4fa3f7" stroke-width="2.6" stroke-linecap="round" aria-hidden="true">'
        '<path d="M3 9h22a4.5 4.5 0 1 0-4.5-4.5"/><path d="M3 16h29a4.5 4.5 0 1 1-4.5 4.5"/><path d="M3 23h16a4 4 0 1 1-4 4"/></svg></a>')


def wa_link(text="Hello Q Ventus, I would like to discuss an HVAC requirement."):
    return f"https://wa.me/{WHATSAPP}?text={quote(text)}"


# ---------------------------------------------------------------- layout
def nav_html(r, active):
    def col(title, items):
        links = "".join(f'<a href="{r}services/{s}.html">{escape(label)}</a>' for label, s in items)
        return f"<div><h4>{title}</h4>{links}</div>"

    hvac = [(SVC[s]["name"].replace(" & Emergency Support", ""), s) for s in
            ["commercial-hvac", "industrial-hvac", "offshore-hvac", "marine-hvac", "commercial-refrigeration", "hvac-design-engineering", "preventive-maintenance"]]
    hvac.append(("Emergency Breakdown Support", "preventive-maintenance.html#emergency"[:-len(".html#emergency")]))
    systems = [(SVC[s]["name"], s) for s in ["chiller-services", "cold-rooms", "air-quality-filtration", "mechanical-overhauling", "residential-hvac"]]
    support = [(SVC[s]["name"], s) for s in ["offshore-containers", "event-support", "technical-manpower"]]
    mega = (col("HVAC Engineering", hvac) + col("Specialized Systems", systems) +
            col("Industrial Support", support)[:-6] + f'<a class="all" href="{r}services.html">ALL SERVICES →</a></div>')
    # Emergency link should land on the anchor
    mega = mega.replace(f'{r}services/preventive-maintenance.html">Emergency', f'{r}services/preventive-maintenance.html#emergency">Emergency')

    def a(href, label, key):
        cls = ' class="active"' if active == key else ""
        cur = ' aria-current="page"' if active == key else ""
        return f'<a href="{r}{href}"{cls}{cur}>{label}</a>'

    dd_cls = "dd active" if active == "services" else "dd"
    return (f'<nav class="nav" id="site-nav" aria-label="Main">'
            f'{a("index.html", "Home", "home")}{a("about.html", "About", "about")}'
            f'<div class="{dd_cls}"><button type="button" aria-expanded="false" aria-haspopup="true">Services {CHEV}</button>'
            f'<div class="mega">{mega}</div></div>'
            f'{a("projects.html", "Projects", "projects")}{a("index.html#industries", "Industries", "industries")}'
            f'{a("contact.html", "Contact", "contact")}'
            f'<a class="btn btn-primary mobile-cta" href="{r}contact.html">Request a Site Survey</a></nav>')


def header(r, active):
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <div class="tb-left"><span class="em">24/7 EMERGENCY</span><a href="tel:{PHONE_1_LINK}">{PHONE_1}</a><a class="hide-sm" href="mailto:{EMAIL}">{EMAIL}</a></div>
  <div class="tb-right"><span class="iso">ISO 9001 · ISO 45001 · ISO 14001</span><span>{ADDRESS.split(',')[2].strip()}, Qatar</span></div>
</div></div>
<header class="site-header"><div class="container">
  {LOGO.format(r=r)}
  {nav_html(r, active)}
  <div style="display:flex;align-items:center;gap:10px">
    <a class="btn btn-dark btn-sm header-cta" href="{r}contact.html">Request a Site Survey</a>
    <button class="burger" type="button" aria-label="Open menu" aria-controls="site-nav" aria-expanded="false"><span></span></button>
  </div>
</div></header>"""


def footer(r):
    def links(slugs):
        return "".join(f'<li><a href="{r}services/{s}.html">{escape(SVC[s]["name"])}</a></li>' for s in slugs)
    isos = "".join(f"<span>{i[0]}</span>" for i in ISO)
    return f"""<footer class="site-footer"><div class="container">
  <div class="top">
    <div class="about">{LOGO.format(r=r)}
      <p>A professional HVAC engineering company trusted to design, maintain and optimise mission-critical cooling systems for commercial, industrial, marine and offshore facilities.</p>
      <div class="isos">{isos}</div></div>
    <div><h4>HVAC Engineering</h4><ul>{links(["commercial-hvac", "industrial-hvac", "offshore-hvac", "marine-hvac", "commercial-refrigeration", "hvac-design-engineering"])}</ul></div>
    <div><h4>Systems &amp; Support</h4><ul>{links(["chiller-services", "cold-rooms", "preventive-maintenance", "offshore-containers", "event-support", "technical-manpower"])}</ul></div>
    <div><h4>Company</h4><ul><li><a href="{r}about.html">About Q Ventus</a></li><li><a href="{r}projects.html">Featured Projects</a></li><li><a href="{r}services.html">All Services</a></li><li><a href="{r}index.html#industries">Industries</a></li><li><a href="{r}contact.html">Contact</a></li></ul></div>
    <div><h4>Get in Touch</h4><ul>
      <li><a href="tel:{PHONE_1_LINK}">{PHONE_1}</a></li><li><a href="tel:{PHONE_2_LINK}">{PHONE_2}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{escape(ADDRESS)}</li>
      <li><a href="{wa_link()}" target="_blank" rel="noopener">WhatsApp us →</a></li></ul></div>
  </div>
  <div class="bottom"><span>© <span id="year">2026</span> Q Ventus. All rights reserved.</span><span class="mono">ENGINEERING HVAC FOR CRITICAL INFRASTRUCTURE · DOHA, QATAR</span></div>
</div></footer>
<a class="wa-float" href="{wa_link()}" target="_blank" rel="noopener" aria-label="Chat with Q Ventus on WhatsApp">{wa_icon()}</a>"""


def org_schema():
    return {
        "@context": "https://schema.org", "@type": "HVACBusiness", "name": COMPANY,
        "url": SITE_URL + "/", "logo": SITE_URL + "/assets/img/og-image.jpg", "email": EMAIL,
        "telephone": PHONE_1_LINK, "image": SITE_URL + "/assets/img/og-image.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": "Office 81, Zone E, Al Mirqab Mall", "addressLocality": "Doha", "addressCountry": "QA"},
        "areaServed": "Qatar",
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "08:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "13:00"},
        ],
    }


def page(path, title, desc, body, active="", schema=None):
    depth = path.count("/")
    r = "../" * depth
    canonical = SITE_URL + "/" + ("" if path == "index.html" else path)
    full_title = title if "Q Ventus" in title else f"{title} | Q Ventus"
    ld = ""
    for s in (schema or []):
        ld += f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n'
    html = f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0b1b2b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Q Ventus">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;700&family=Josefin+Sans:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ld}</head>
<body>
{header(r, active)}
<main id="main">
{body.replace("{r}", r)}
</main>
{footer(r)}
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
"""
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    PAGES.append(path)


PAGES = []


# ---------------------------------------------------------------- reusable blocks
def eyebrow(t):
    return f'<div class="eyebrow">{t}</div>'


def btn(href, label, cls="btn-primary", arrow=True):
    return f'<a class="btn {cls}" href="{href}">{label}{icon("arrow") if arrow else ""}</a>'


def page_hero(crumbs, h1, lead, img=None, extra=""):
    bg = f'<div class="hero-bg" style="background-image:url({{r}}assets/img/{img}.jpg)"></div>' if img else ""
    cr = ' <span class="sep">/</span> '.join(f'<a href="{{r}}{h}">{escape(t)}</a>' if h else f"<span>{escape(t)}</span>" for t, h in crumbs)
    return f"""<section class="page-hero blueprint">{bg}<div class="container">
<nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>
<h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div></section>"""


def stats_block():
    items = "".join(f'<div class="stat"><div class="num"><span data-count="{n}">{n}</span><sup>{s}</sup></div><div class="lbl">{l}</div></div>' for n, s, l in STATS)
    return f'<div class="stats"><div class="container">{items}</div></div>'


def clients_block():
    tiles = "".join(f'<div class="client"><img src="{{r}}assets/img/clients/{f}" alt="{escape(n)}" loading="lazy"></div>' for f, n in CLIENTS)
    tiles += '<div class="client more"><strong>60+</strong><span>Corporate clients</span></div>'
    return f'<div class="clients reveal">{tiles}</div>'


def groups_block():
    out = []
    for key, code, name, desc in GROUPS:
        if key == "systems":
            items = "".join(f'<li><a href="{{r}}services/{s}.html">{escape(l)}</a></li>' for l, s in SYSTEM_LINKS)
        else:
            items = "".join(f'<li><a href="{{r}}services/{s["slug"]}.html">{escape(s["name"])}</a></li>' for s in SERVICES if s["group"] == key)
            if key == "hvac":
                items += '<li><a href="{r}services/preventive-maintenance.html#emergency">Emergency Breakdown Support</a></li>'
        out.append(f'<div class="group reveal"><span class="code">{code}</span><h3>{name}</h3><p>{desc}</p><ul>{items}</ul></div>')
    return f'<div class="groups">{"".join(out)}</div>'


def caps_block():
    cells = "".join(f'<div class="cap"><span class="id">EQ-{i:02d}</span>{icon(ic)}<h3>{escape(t)}</h3><p>{escape(d)}</p></div>'
                    for i, (ic, t, d) in enumerate(CAPABILITIES, 1))
    return f'<div class="caps reveal">{cells}</div>'


def industries_block():
    cells = "".join(f'<div class="ind">{icon(ic)}<div><small>IND-{i:02d}</small>{escape(t)}</div></div>' for i, (ic, t) in enumerate(INDUSTRIES, 1))
    return f'<div class="industries reveal">{cells}</div>'


def why_block():
    cells = "".join(f'<div class="why-item"><span class="n">{i:02d}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></div>' for i, (t, d) in enumerate(WHY, 1))
    return f'<div class="why reveal">{cells}</div>'


def certs_block():
    cells = "".join(f'<div class="cert"><div class="seal">ISO</div><h3>{n}</h3><span class="std">{t}</span><p>{d}</p></div>' for n, t, d in ISO)
    cells += ('<div class="cert"><div class="seal">QP·QG</div><h3>Offshore Safety</h3><span class="std">QP &amp; QG approved training</span>'
              '<p>Offshore personnel certified and trained to Qatar Petroleum and Qatargas safety standards.</p></div>')
    return f'<div class="certs reveal">{cells}</div>'


def project_cards(limit=None):
    cards = []
    for p in PROJECTS[:limit]:
        k = "".join(f"<div><strong>{escape(a)}</strong><span>{escape(b)}</span></div>" for a, b in p["kpis"][:3])
        cards.append(f'<a class="pcard reveal" href="{{r}}projects.html#{p["id"]}"><div class="img"><img src="{{r}}assets/img/{p["img"]}.jpg" alt="" loading="lazy"><span class="num">PROJECT {p["n"]}</span></div>'
                     f'<div class="body"><span class="pind">{escape(p["industry"])}</span><h3>{escape(p["title"])}</h3><p>{escape(p["short"])}</p><div class="kpi">{k}</div></div></a>')
    return f'<div class="projects">{"".join(cards)}</div>'


def cta_band(title="Is HVAC reliability critical to your operation?", text="Talk to our engineers about a site survey, a maintenance programme or an urgent breakdown."):
    return f"""<section class="cta-band blueprint dark"><div class="container">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="actions">{btn("{r}contact.html", "Request a Site Survey")}<a class="btn btn-ghost" href="{wa_link()}" target="_blank" rel="noopener">WhatsApp an Engineer</a></div>
</div></section>"""


SCHEMATIC = """<svg class="schematic" viewBox="0 0 520 430" role="img" aria-label="Diagram of a chilled water system: cooling tower, chiller, pump and air handling unit serving building zones">
<defs><marker id="ar" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="#4fa3f7"/></marker></defs>
<g font-family="JetBrains Mono, monospace" font-size="10" fill="#8ea3b9" letter-spacing=".06em">
<rect x="6" y="6" width="508" height="418" fill="none" stroke="rgba(143,176,211,.25)"/>
<path d="M6 20h14M20 6v14M514 20h-14M500 6v14M6 410h14M20 424v-14" stroke="#6cc24a" stroke-width="1.5"/>
<!-- condenser water -->
<path class="flow" d="M78 128V196" stroke="#6cc24a" stroke-width="2.5" fill="none"/>
<path class="flow ret" d="M146 128V196" stroke="#6cc24a" stroke-width="2.5" fill="none"/>
<!-- chilled water supply / return -->
<path class="flow" d="M196 230H330" stroke="#4fa3f7" stroke-width="3" fill="none"/>
<path class="flow" d="M405 272V340H285M245 340H112V290" stroke="#5b87bf" stroke-width="3" fill="none"/>
<!-- supply air to zones -->
<path class="flow" d="M405 186V140" stroke="#4fa3f7" stroke-width="2" fill="none" marker-end="url(#ar)"/>
<!-- cooling tower -->
<g stroke="#8fb0d3" stroke-width="1.5" fill="rgba(79,163,247,.05)"><path d="M48 128l10-78h108l10 78z"/><path d="M58 50h108"/></g>
<g class="fan"><circle cx="112" cy="34" r="12" fill="none" stroke="#4fa3f7" stroke-width="1.5"/><path d="M112 22v24M100 34h24" stroke="#4fa3f7" stroke-width="1.5"/></g>
<text x="40" y="150" fill="#dbe6f1">CT-01</text><text x="40" y="163">COOLING TOWER</text>
<!-- chiller -->
<rect x="40" y="196" width="156" height="94" fill="rgba(79,163,247,.06)" stroke="#8fb0d3" stroke-width="1.5"/>
<circle cx="80" cy="243" r="20" fill="none" stroke="#8fb0d3" stroke-width="1.5"/><path d="M70 243h20M80 233v20" stroke="#8fb0d3"/>
<path d="M120 220h60M120 236h60M120 252h60M120 268h60" stroke="rgba(143,176,211,.5)"/>
<text x="40" y="312" fill="#dbe6f1">CH-01</text><text x="86" y="312">WATER-COOLED CHILLER</text>
<!-- pump -->
<circle cx="265" cy="340" r="20" fill="rgba(108,194,74,.08)" stroke="#6cc24a" stroke-width="1.5"/><path d="M256 340l14-9v18z" fill="#6cc24a"/>
<text x="240" y="380" fill="#dbe6f1">P-01</text><text x="240" y="393">CHW PUMP</text>
<!-- AHU -->
<rect x="330" y="186" width="150" height="86" fill="rgba(79,163,247,.06)" stroke="#8fb0d3" stroke-width="1.5"/>
<path d="M340 200v58M350 200v58M360 200v58" stroke="rgba(143,176,211,.5)"/>
<g class="fan"><circle cx="440" cy="229" r="22" fill="none" stroke="#4fa3f7" stroke-width="1.5"/><path d="M440 207v44M418 229h44M424 213l32 32M456 213l-32 32" stroke="#4fa3f7" stroke-width="1"/></g>
<text x="330" y="290" fill="#dbe6f1">AHU-01</text><text x="384" y="290">25 TR</text>
<!-- zones -->
<g stroke="#8fb0d3" stroke-width="1.2" fill="rgba(79,163,247,.04)"><rect x="300" y="44" width="62" height="78"/><rect x="368" y="44" width="62" height="78"/><rect x="436" y="44" width="62" height="78"/></g>
<text x="310" y="88">ZONE A</text><text x="378" y="88">ZONE B</text><text x="446" y="88">ZONE C</text>
<text x="300" y="36" fill="#6cc24a">24.0°C · 50%RH</text>
<!-- readouts -->
<rect x="206" y="206" width="112" height="18" fill="#07131f"/><text x="212" y="219" fill="#4fa3f7">CHWS 6.7°C ▸</text>
<rect x="296" y="346" width="112" height="18" fill="#07131f"/><text x="302" y="359" fill="#8fb0d3">◂ CHWR 12.2°C</text>
<text x="90" y="182" fill="#6cc24a">CW 29.4°C</text>
<!-- title block -->
<g transform="translate(350 362)"><rect width="158" height="54" fill="#07131f" stroke="rgba(143,176,211,.35)"/><path d="M0 18h158M0 36h158M64 18v36" stroke="rgba(143,176,211,.25)"/>
<text x="8" y="13" fill="#dbe6f1">Q VENTUS · ENGINEERING</text><text x="8" y="31">CHW LOOP</text><text x="70" y="31">DWG M-101</text><text x="8" y="49">STATUS</text><text x="70" y="49" fill="#6cc24a">● ONLINE</text></g>
</g></svg>"""


# ---------------------------------------------------------------- pages
def build_home():
    sectors = "".join(f"<span>{s}</span>" for s in ["Commercial", "Industrial", "Offshore", "Marine"])
    pillars = "".join(f"<li>{icon('check')}{t}</li>" for t in ["Engineering-led design", "Commercial & industrial HVAC", "Offshore & marine capability", "Long-term maintenance partnerships", "Safety-driven operations", "ISO-certified management systems"])
    innov = "".join(f'<div>{icon(ic)}<h3>{t}</h3><p>{d}</p></div>' for ic, t, d in INNOVATION)
    body = f"""
<section class="hero blueprint">
  <div class="hero-bg" style="background-image:url({{r}}assets/img/rooftop-hvac-aerial.jpg)"></div>
  <div class="container">
    <div>
      <div class="eyebrow">Q Ventus · HVAC Engineering · Qatar</div>
      <h1>Engineering HVAC Solutions <span class="accent">for Critical Infrastructure</span></h1>
      <div class="sectors">{sectors}</div>
      <p class="lead">When cooling failure isn't an option, facilities across Qatar call Q Ventus. We engineer, commission and maintain mission-critical HVAC and refrigeration systems — onshore, offshore and at sea.</p>
      <div class="actions">{btn("{r}contact.html", "Request a Site Survey")}{btn("{r}services.html", "Explore Services", "btn-ghost", False)}</div>
    </div>
    <div class="schematic-wrap">{SCHEMATIC}</div>
  </div>
  {stats_block()}
</section>

<section class="section-sm">
  <div class="container">
    <div class="section-head"><div>{eyebrow("Trusted By")}<h2>Relied on by leaders in energy, hospitality and healthcare</h2></div>
    <p>From offshore drilling contractors to international hotel groups, our client portfolio reflects the trust placed in our engineering.</p></div>
    {clients_block()}
  </div>
</section>

<section class="section bg-paper" id="about">
  <div class="container split">
    <div class="frame reveal"><img src="{{r}}assets/img/engineering-drawings.jpg" alt="Q Ventus engineers reviewing HVAC drawings" loading="lazy">
      <div class="tag"><strong>15+ years</strong><span>HVAC engineering expertise</span></div></div>
    <div class="reveal">
      {eyebrow("01 — About Q Ventus")}
      <h2>Engineering Excellence for Critical Environments</h2>
      <p class="lead">Q Ventus is an HVAC engineering company specialising in systems where reliability is not optional — commercial buildings, industrial facilities, offshore platforms and marine vessels.</p>
      <p>Our engineers and certified technicians design, install, commission and maintain cooling, ventilation and refrigeration systems to exacting technical and safety standards. We build long-term partnerships with our clients, supporting their plant through its entire lifecycle with preventive maintenance and rapid emergency response.</p>
      <ul class="pillars">{pillars}</ul>
      {btn("{r}about.html", "More About Us", "btn-dark")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><div>{eyebrow("02 — Services")}<h2>Engineering services, organised around what you need</h2></div>
    <p>From heat load calculation to 24/7 breakdown response, every service is delivered by one accountable engineering team.</p></div>
    {groups_block()}
  </div>
</section>

<section class="section blueprint dark">
  <div class="container">
    <div class="section-head"><div>{eyebrow("03 — Capabilities")}<h2>Our expertise includes</h2></div>
    <p>The systems our engineers specify, install, commission and maintain every day — from chiller plants to marine chilled water systems.</p></div>
    {caps_block()}
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="section-head"><div>{eyebrow("04 — Featured Engineering Projects")}<h2>Engineering success stories</h2></div>
    <p>Real projects, real constraints: live operations, harsh environments and zero tolerance for downtime.</p></div>
    {project_cards()}
  </div>
</section>

<section class="section" id="industries">
  <div class="container">
    <div class="section-head"><div>{eyebrow("05 — Industries")}<h2>Industries we serve</h2></div>
    <p>We focus on facilities where HVAC performance directly affects safety, operations, product or reputation.</p></div>
    {industries_block()}
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="section-head"><div>{eyebrow("06 — Why Q Ventus")}<h2>The company you call when HVAC reliability is critical</h2></div>
    <p>Eight reasons operators across Qatar trust us with their most important systems.</p></div>
    {why_block()}
  </div>
</section>

<section class="section blueprint dark">
  <div class="container innov">
    <div class="reveal">{eyebrow("07 — Innovation")}<h2>Engineering Tomorrow's HVAC</h2>
      <p class="lead">Q Ventus is investing in intelligent HVAC technologies — remote monitoring, predictive maintenance, energy optimization and smart building solutions — to improve equipment reliability and operational efficiency.</p>
      <p>Our goal is simple: find problems before they become breakdowns, and run plant at the lowest energy cost that still meets the duty.</p></div>
    <div class="innov-list reveal">{innov}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><div>{eyebrow("08 — Certifications")}<h2>Certified management systems</h2></div>
    <p>Quality, safety and environmental management certified to international standards.</p></div>
    {certs_block()}
  </div>
</section>
{cta_band()}
"""
    schema = [org_schema(), {"@context": "https://schema.org", "@type": "WebSite", "name": COMPANY, "url": SITE_URL + "/"}]
    page("index.html", "Q Ventus | HVAC Engineering for Critical Infrastructure in Qatar",
         "Q Ventus is an HVAC engineering company in Doha, Qatar, delivering commercial, industrial, offshore and marine HVAC, commercial refrigeration and preventive maintenance. ISO 9001, 45001 & 14001 certified.",
         body, "home", schema)


def build_about():
    body = page_hero([("Home", "index.html"), ("About", None)], "Your Trusted HVAC Engineering Partner",
                     "Q Ventus is a professional HVAC engineering company trusted to design, maintain and optimise mission-critical cooling systems for commercial, industrial, marine and offshore facilities.", "site-team")
    body += f"""
<section class="section"><div class="container split">
  <div class="reveal">{eyebrow("Who we are")}<h2>Not simply an air conditioning contractor</h2>
    <p class="lead">We exist for the facilities where HVAC reliability is critical: hotels that cannot lose guest comfort, hospitals with clinical requirements, cold stores that cannot lose stock, and offshore modules that must stay pressurized.</p>
    <p>Our services span onshore and offshore sectors — HVAC design and engineering, installation, commissioning, preventive maintenance and emergency support — tailored to the specific needs of each client. In the offshore sector our technicians are certified and trained to Qatar Petroleum standards, with strong expertise in cabin air conditioning engineering and installation.</p>
    <p>Behind every project is a diverse team of engineers, technicians, supervisors and managers. We invest in them through fair wages, training and safety systems — because skilled, safe people are what make engineering reliable.</p></div>
  <div class="frame reveal"><img src="{{r}}assets/img/technicians.jpg" alt="Q Ventus technical team" loading="lazy"><div class="tag"><strong>~50</strong><span>Engineers &amp; technicians deployed for FIFA 2022</span></div></div>
</div></section>
<section class="blueprint dark" style="padding:0">{stats_block()}</section>
<section class="section bg-paper"><div class="container">
  <div class="section-head"><div>{eyebrow("How we work")}<h2>Engineering-led, from survey to long-term support</h2></div><p>One accountable team across the full lifecycle of your system.</p></div>
  <ol class="steps reveal" style="max-width:760px">
    <li><strong>Assess</strong>Site survey, condition assessment and understanding of your operational risk.</li>
    <li><strong>Engineer</strong>Heat load calculations, system design, equipment selection and shop drawings.</li>
    <li><strong>Deliver</strong>Phased installation planned around live operations, with temporary cooling where needed.</li>
    <li><strong>Commission</strong>Testing, balancing and performance verification against the design duty.</li>
    <li><strong>Support</strong>Preventive maintenance programmes, AMC contracts and rapid emergency response.</li>
  </ol>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><div>{eyebrow("Why Q Ventus")}<h2>What sets us apart</h2></div><p>Concise reasons clients choose us for critical work.</p></div>
  {why_block()}
</div></section>
<section class="section bg-paper"><div class="container">
  <div class="section-head"><div>{eyebrow("Certifications")}<h2>Certified to international standards</h2></div><p>Our management systems are certified for quality, health &amp; safety and the environment.</p></div>
  {certs_block()}
</div></section>
<section class="section-sm"><div class="container">
  <div class="section-head"><div>{eyebrow("Trusted By")}<h2>Our clients</h2></div><p>Our client portfolio is one of our biggest strengths.</p></div>
  {clients_block()}
</div></section>
{cta_band()}"""
    page("about.html", "About Q Ventus — HVAC Engineering Company in Doha, Qatar",
         "About Q Ventus: an engineering-led HVAC company in Doha serving commercial, industrial, offshore and marine facilities with design, installation, commissioning and maintenance.",
         body, "about", [org_schema()])


def build_services_hub():
    def cards(keys):
        out = ""
        for s in SERVICES:
            if s["group"] in keys:
                out += (f'<a class="pcard reveal" href="{{r}}services/{s["slug"]}.html"><div class="img"><img src="{{r}}assets/img/{s["img"]}.jpg" alt="" loading="lazy"></div>'
                        f'<div class="body"><h3>{escape(s["name"])}</h3><p>{escape(s["card"])}</p><span class="pind" style="margin:0">View service →</span></div></a>')
        return out
    body = page_hero([("Home", "index.html"), ("Services", None)], "HVAC Engineering Services",
                     "Grouped the way engineers think: core HVAC engineering, the specialised systems we know inside out, and the industrial support that keeps projects moving.", "commercial-rooftop-plant",
                     '<div class="jump"><a href="#hvac">G-01 HVAC Engineering</a><a href="#systems">G-02 Specialized Systems</a><a href="#support">G-03 Industrial Support</a></div>')
    for key, code, name, desc in GROUPS:
        bg = " bg-paper" if key == "systems" else ""
        body += f"""<section class="section{bg}" id="{key}" style="scroll-margin-top:80px"><div class="container">
<div class="section-head"><div>{eyebrow(code)}<h2>{name}</h2></div><p>{desc}</p></div>
<div class="projects" style="grid-template-columns:repeat(3,1fr)">{cards([key])}</div></div></section>"""
    body += f"""<section class="section-sm bg-paper"><div class="container">
<div class="section-head"><div>{eyebrow("Also available")}<h2>Residential &amp; villa HVAC</h2></div>
<p>We also serve villas, compounds and apartment buildings. <a href="{{r}}services/residential-hvac.html">View residential services →</a></p></div></div></section>
{cta_band("Not sure which service you need?", "Describe the problem and our engineers will recommend the right approach.")}"""
    body = body.replace('style="grid-template-columns:repeat(3,1fr)"', 'class="svc-cards"')
    body = body.replace('<div class="projects" class="svc-cards">', '<div class="projects svc-cards">')
    page("services.html", "HVAC Engineering Services in Qatar",
         "Q Ventus services: commercial, industrial, offshore and marine HVAC, commercial refrigeration, HVAC design, preventive maintenance, chiller services, cold rooms, offshore containers and technical manpower.",
         body, "services")


def build_service(s):
    chips = "".join(f'<span class="chip">{escape(c)}</span>' for c in s["chips"])
    hero = page_hero([("Home", "index.html"), ("Services", "services.html"), (s["name"], None)], escape(s["h1"]), escape(s["lead"]), s["img"],
                     f'<div class="spec-strip">{chips}</div>')
    main = f'<img class="svc-img" src="{{r}}assets/img/{s["img"]}.jpg" alt="{escape(s["name"])} — Q Ventus" loading="lazy">'
    main += f'<h2>Overview</h2>' + "".join(f"<p>{escape(p)}</p>" for p in s["body"]) if s["body"] else ""
    if not s["body"]:
        main = f'<img class="svc-img" src="{{r}}assets/img/{s["img"]}.jpg" alt="{escape(s["name"])} — Q Ventus" loading="lazy">'
    for anchor, h, t in s.get("blocks", []):
        main += f'<h2 id="{anchor}">{escape(h)}</h2><p>{escape(t)}</p>'
    if s.get("cols"):
        main += '<h2>What we provide</h2><div class="case-grid" style="margin-top:20px">'
        for i, (h, items) in enumerate(s["cols"]):
            if len(items) == 1:
                inner = f"<p>{escape(items[0])}</p>"
            else:
                inner = "<ul>" + "".join(f"<li>{escape(x)}</li>" for x in items) + "</ul>"
            main += f'<div class="case-col c2"><div class="lab">{escape(h)}</div>{inner}</div>'
        main += "</div>"
    if s.get("containers"):
        main += '<h2>Container range</h2><div class="cont-grid">'
        for img, h, dl in s["containers"]:
            d = "".join(f"<dt>{escape(a)}</dt><dd>{escape(b)}</dd>" for a, b in dl)
            main += f'<div class="cont"><img src="{{r}}assets/img/{img}.jpg" alt="{escape(h)}" loading="lazy"><div><h3>{escape(h)}</h3><dl>{d}</dl></div></div>'
        main += "</div>"
    if s["scope"]:
        label = "Scope of services" if s["group"] != "support" else "Key features"
        main += f'<h2>{label}</h2><ul class="scope">' + "".join(f"<li>{icon('check')}{escape(x)}</li>" for x in s["scope"]) + "</ul>"
    if s.get("table"):
        main += '<h2>At a glance</h2><table class="spec-table">' + "".join(f"<tr><th>{escape(a)}</th><td>{escape(b)}</td></tr>" for a, b in s["table"]) + "</table>"
    if s.get("process"):
        main += '<h2>Our engineering process</h2><ol class="steps">' + "".join(f"<li><strong>{escape(a)}</strong>{escape(b)}</li>" for a, b in s["process"]) + "</ol>"
    if s.get("extra") == "emergency":
        main += f"""<h2 id="emergency" style="scroll-margin-top:100px">Emergency breakdown support</h2>
<p>Breakdowns don't wait for office hours. Our rapid-response technicians are available around the clock for chillers, AHUs, refrigeration, offshore and marine systems. Call the emergency line and an engineer will triage the fault with you immediately.</p>
<div class="cinfo" style="margin-top:18px"><div class="row em">{icon('alert')}<div><h4>24/7 Emergency line</h4><p><a href="tel:{PHONE_1_LINK}">{PHONE_1}</a> · <a href="{wa_link('URGENT: HVAC breakdown — please call me.')}" target="_blank" rel="noopener">WhatsApp</a></p></div></div></div>"""
    if s.get("project"):
        p = PRJ[s["project"]]
        main += (f'<h2>Featured project</h2><div class="case-value"><strong>{escape(p["title"])}</strong>'
                 f'<p>{escape(p["short"])} <a href="{{r}}projects.html#{p["id"]}" style="color:#6cc24a">Read the full project →</a></p></div>')

    same = [x for x in SERVICES if x["group"] == s["group"]] if s["group"] != "secondary" else [x for x in SERVICES if x["group"] == "hvac"]
    side_links = "".join(f'<li><a href="{{r}}services/{x["slug"]}.html"{" class=\"cur\"" if x["slug"] == s["slug"] else ""}>{escape(x["name"])}</a></li>' for x in same)
    group_name = {g[0]: g[2] for g in GROUPS}.get(s["group"], "HVAC Engineering")
    aside = f"""<aside class="aside">
<div class="box dark"><h4>Talk to an engineer</h4><p>Get expert advice or book a site survey.</p><a class="tel" href="tel:{PHONE_1_LINK}">{PHONE_1}</a>
{btn("{r}contact.html", "Request a Survey")}<a class="btn btn-ghost" style="width:100%;margin-top:10px" href="{wa_link(f'Hello Q Ventus, I am interested in {s["name"]}.')}" target="_blank" rel="noopener">WhatsApp</a></div>
<div class="box"><h4>{escape(group_name)}</h4><ul>{side_links}</ul></div>
<div class="box"><h4>Certified</h4><p style="margin:0;font-size:.9rem">ISO 9001:2015 · ISO 45001:2018 · ISO 14001:2015</p></div>
</aside>"""
    rel = "".join(f'<a href="{{r}}services/{x}.html"><span><small>Related service</small>{escape(SVC[x]["name"])}</span><span>→</span></a>' for x in s["related"])
    body = hero + f"""<section class="section"><div class="container svc-layout"><div class="prose">{main}</div>{aside}</div></section>
<section class="section-sm bg-paper"><div class="container"><div class="eyebrow">Related services</div><div class="related">{rel}</div></div></section>
{cta_band()}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["desc"],
               "areaServed": "Qatar", "provider": {"@type": "HVACBusiness", "name": COMPANY, "url": SITE_URL + "/"}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
                  {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE_URL + "/services.html"},
                  {"@type": "ListItem", "position": 3, "name": s["name"], "item": f"{SITE_URL}/services/{s['slug']}.html"}]}]
    page(f"services/{s['slug']}.html", s["title"], s["desc"], body, "services", schema)


def build_projects():
    jump = "".join(f'<a href="#{p["id"]}">{p["n"]} · {escape(p["industry"].split("·")[0].strip())}</a>' for p in PROJECTS)
    body = page_hero([("Home", "index.html"), ("Featured Projects", None)], "Featured Engineering Projects",
                     "Each project below follows the same discipline: understand the challenge, engineer the solution, and prove the outcome.", "rooftop-condensers",
                     f'<div class="jump">{jump}</div>')
    body += "<div>"
    for p in PROJECTS:
        def lst(xs):
            return "<ul>" + "".join(f"<li>{escape(x)}</li>" for x in xs) + "</ul>"
        ci, cl, cn = p["challenge"]
        si, sl, sn = p["solution"]
        ri, rl = p["results"]
        kp = "".join(f"<div><strong>{escape(a)}</strong><span>{escape(b)}</span></div>" for a, b in p["kpis"])
        venues = ""
        if p.get("venues"):
            venues = '<h4 style="margin-top:22px;font-size:.95rem">Venues &amp; facilities</h4><ul class="venues">' + "".join(f"<li>{escape(v)}</li>" for v in p["venues"]) + "</ul>"
        body += f"""<article class="case" id="{p['id']}"><div class="container">
<div class="case-head">
  <div>{eyebrow("Featured Engineering Project " + p['n'])}<h2>{escape(p['title'])}</h2>
    <table class="case-meta"><tr><th>Client</th><td>{escape(p['client'])}</td></tr><tr><th>Industry</th><td>{escape(p['industry'])}</td></tr></table>
    <p style="margin-top:20px">{escape(p['overview'])}</p>{venues}<div class="kpis">{kp}</div></div>
  <img src="{{r}}assets/img/{p['img']}.jpg" alt="" loading="lazy">
</div>
<div class="case-grid">
  <div class="case-col c1"><div class="lab">The Challenge</div><p>{escape(ci)}</p>{lst(cl)}{f"<p style='margin-top:12px'>{escape(cn)}</p>" if cn else ""}</div>
  <div class="case-col c2"><div class="lab">Engineering Solution</div><p>{escape(si)}</p>{lst(sl)}{f"<p style='margin-top:12px'>{escape(sn)}</p>" if sn else ""}</div>
  <div class="case-col c3"><div class="lab">Results</div><p>{escape(ri)}</p>{lst(rl)}</div>
</div>
<div class="case-value"><strong>Engineering value delivered</strong><p>{escape(p['value'])}</p></div>
</div></article>"""
    body += "</div>" + cta_band("Have a project with no room for downtime?", "Tell us about your facility. We'll plan the work around your operation.")
    page("projects.html", "Featured Engineering Projects — HVAC Case Studies in Qatar",
         "Q Ventus featured engineering projects: cold storage modernization, hotel chiller plant replacement, offshore pressurized HVAC upgrade, superyacht HVAC retrofit and FIFA World Cup Qatar 2022 temporary HVAC.",
         body, "projects")


def build_contact():
    opts = "".join(f"<option>{escape(s['name'])}</option>" for s in SERVICES) + "<option>Other / not sure</option>"
    hours = "".join(f"<tr><td>{d}</td><td>{h}</td></tr>" for d, h in HOURS)
    body = page_hero([("Home", "index.html"), ("Contact", None)], "Talk to an HVAC Engineer",
                     "Request a site survey, a maintenance proposal or urgent breakdown support. We respond quickly — and for emergencies, immediately.", "rooftop-hvac-aerial")
    body += f"""<section class="section"><div class="container contact-grid">
<div class="cinfo">
  <div class="row em">{icon('alert')}<div><h4>24/7 Emergency breakdown</h4><p><a href="tel:{PHONE_1_LINK}">{PHONE_1}</a></p></div></div>
  <div class="row">{icon('phone')}<div><h4>Phone</h4><p><a href="tel:{PHONE_1_LINK}">{PHONE_1}</a><br><a href="tel:{PHONE_2_LINK}">{PHONE_2}</a></p></div></div>
  <div class="row">{wa_icon().replace('<svg', '<svg style="color:#25d366"')}<div><h4>WhatsApp</h4><p><a href="{wa_link()}" target="_blank" rel="noopener">Chat with an engineer →</a></p></div></div>
  <div class="row">{icon('mail')}<div><h4>Email</h4><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
  <div class="row">{icon('pin')}<div><h4>Office</h4><p>{escape(ADDRESS)}</p></div></div>
  <div class="row">{icon('clock')}<div style="flex:1"><h4>Office hours</h4><table class="hours">{hours}</table></div></div>
</div>
<form class="quote" data-to="{EMAIL}" novalidate>
  {eyebrow("Request a site survey")}
  <h2 style="font-size:1.8rem">Tell us about your facility</h2>
  <div class="fgrid">
    <div><label for="f-name">Full name *</label><input id="f-name" name="name" required autocomplete="name"></div>
    <div><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization"></div>
    <div><label for="f-email">Email *</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
    <div><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
    <div><label for="f-service">Service</label><select id="f-service" name="service">{opts}</select></div>
    <div><label for="f-loc">Facility / location</label><input id="f-loc" name="location" placeholder="e.g. Hotel, West Bay"></div>
    <div class="full"><label for="f-msg">How can we help? *</label><textarea id="f-msg" name="message" required placeholder="Equipment, capacity, symptoms, timeline…"></textarea></div>
  </div>
  <div style="margin-top:22px"><button class="btn btn-primary" type="submit">Send Enquiry {icon('arrow')}</button></div>
  <p class="form-note">Submitting opens your email app with the details filled in. For urgent breakdowns please call {PHONE_1}.</p>
</form>
</div></section>
<section><iframe class="map" title="Q Ventus office location — Al Mirqab Mall, Doha" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
 src="https://www.google.com/maps?q={quote(MAP_QUERY)}&amp;output=embed"></iframe></section>"""
    page("contact.html", "Contact Q Ventus — HVAC Engineers in Doha, Qatar",
         f"Contact Q Ventus in Doha: {PHONE_1}, {EMAIL}. Office 81, Zone E, Al Mirqab Mall. 24/7 emergency HVAC breakdown support and WhatsApp.",
         body, "contact", [org_schema()])


def build_meta():
    urls = "".join(f"<url><loc>{SITE_URL}/{'' if p == 'index.html' else p}</loc></url>\n" for p in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_build/\nSitemap: {SITE_URL}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    build_about()
    build_services_hub()
    for s in SERVICES:
        build_service(s)
    build_projects()
    build_contact()
    build_meta()
    print(f"Built {len(PAGES)} pages into {OUT}")
