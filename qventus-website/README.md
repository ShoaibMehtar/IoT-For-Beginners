# Q Ventus website (www.qventus.qa)

Static, multi-page website. No server code needed: upload everything in this folder (except `_build/`) to your web host's root folder.

## Pages
- `index.html` (Home), `about.html`, `services.html`, `projects.html`, `contact.html`
- `services/*.html`: 15 service landing pages, one per main service, each with its own SEO title and description
- `sitemap.xml`, `robots.txt`

## Editing text
All copy (services, projects, phone numbers, office hours, ISO certificates, stats, clients) lives in `_build/content.py`.
After editing, rebuild the pages:

    python3 _build/build.py

## Preview locally

    python3 -m http.server 8000

then open http://localhost:8000

## Notes
- The contact form opens the visitor's email app addressed to inquiry@qventus.qa. To receive submissions directly, connect a form service (e.g. Formspree) or your host's form handler.
- Images and client logos were taken from the company profile PDF (`assets/img`).
