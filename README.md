# Ali & Othman International

Arabic/English static company website for https://aliandothman.com.kw.

## Build and preview

Python 3 only; no external packages are required to build.

```sh
python -X utf8 build_pages.py
python -m http.server 8765 --directory dist
```

Open http://localhost:8765/ar/ or http://localhost:8765/en/.

Current sources: `content_data.py`, `build_professional.py`, `professional.css`,
`site.js`, `contact_form.py`, `service_catalog.py`, `services-data.json`,
`immersive.css` and `immersive.js`. `site_assets.py` supplies the social links. Original
brochures, logo, photos and self-hosted Cairo fonts are in `dist/assets/`.
Legacy `modern.css`, `polish.css`, `dist/style.css` and `dist/motion.js` are not
loaded by the current pages and are excluded from the Hostinger package.

## Content sources

The owner-supplied general brochure provides the establishment year (2007),
company background, quality/safety approach, service scope, CCTV and decoration
services. The HVAC brochure provides AC maintenance, central duct installation,
duct cleaning and illustrative pictures. Photographs are brochure illustrations,
not a verified portfolio of completed company projects. Directly supplied phone,
email and social links take precedence over older brochure contact details.
No fabricated client counts, certifications, testimonials or 24/7 availability
claims are included.

## Contact form

The local `submit.php` handler sends requests to `aliothmanintl@gmail.com`.
This address is not displayed in the footer. The page shows success or failure
without navigating away. No test enquiry is sent by the build or checks.
Mailbox delivery depends on the Hostinger PHP mail configuration.

Service photos are licensed stock illustrations, not a project portfolio;
source references are recorded in `photo-credits.json`. The six requested core
services have detailed bilingual descriptions. Original brochure specialty
scopes and the additional interiors service remain available.

## Hostinger release

```sh
python package_hostinger.py
```

The generated ZIP contains only `ar/`, `en/`, `assets/`, `index.html`,
`ao-website.css`, `site.js` and `submit.php`, at archive root (no enclosing dist directory).

Before updating production, back up the existing company-site paths above.
Extract into a staging folder and copy ONLY these paths into `public_html`,
merging the website directories rather than replacing the entire public_html.
Do not modify `cmapp/`, `cms/`, `cmsys/`, `test/`, database files, `.htaccess`,
domain settings, DNS or mail settings. Those belong to separate live systems.
The Hostinger workflow supports manual deployment and deliberate releases:
a push to main that changes `deploy/release.json` triggers the SSH upload. Keep the previous release
until the new Arabic/English pages, PDFs, contact form and subdomains are checked.

The stylesheet and script use a version query to avoid using the previous cached
design after deployment. The primary domain is the canonical URL; language
switching preserves the current page.
