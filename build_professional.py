"""Build bilingual static pages for Hostinger: python -X utf8 build_professional.py."""
from pathlib import Path
from html import escape
from content_data import COPY, SERVICES
from contact_form import contact_form
from site_assets import social_links
from service_catalog import groups, CATALOG

OUT=Path('dist')
ROUTES=['','about/','services/','contact/','brochure/']
def url(lang,page): return f'/{lang}/{ROUTES[page]}'
def arrow(): return ''
def button(href,label,secondary=False): return f'<a class="button {"secondary" if secondary else ""}" href="{href}">{label}{arrow()}</a>'
def picture(name,alt='',eager=False): return f'<img src="/assets/{name}" alt="{escape(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async" width="800" height="600">'

def header(lang,page):
 t=COPY[lang]; alt='en' if lang=='ar' else 'ar'
 nav=''.join(f'<a href="{url(lang,i)}"'+(' aria-current="page"' if i==page else '')+f'>{label}</a>' for i,label in enumerate(t['nav']))
 return f'''<a class="skip-link" href="#main">{'انتقل إلى المحتوى' if lang=='ar' else 'Skip to content'}</a><div class="utility"><div class="container"><span>{t['since']}</span><div><a href="mailto:info@aliandothman.com.kw">info@aliandothman.com.kw</a><a dir="ltr" href="tel:+96522092040">+965 2209 2040</a></div></div></div>
 <header class="site-header"><div class="container navigation"><a class="brand" href="{url(lang,0)}"><img src="/assets/ao-logo.png" width="64" height="64" alt=""><span>{t['name']}<small>{t['sub']}</small></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="main-navigation">{t['menu']} <span aria-hidden="true">☰</span></button><nav id="main-navigation" aria-label="{t['menu']}">{nav}</nav><a class="language" lang="{alt}" href="{url(alt,page)}">{'EN' if lang=='ar' else 'العربية'}</a></div></header>'''

def footer(lang):
 t=COPY[lang]; links=''.join(f'<a href="{url(lang,i)}">{label}</a>' for i,label in enumerate(t['nav']))
 return f'''<footer><div class="container footer-grid"><div><a class="footer-brand" href="{url(lang,0)}"><img src="/assets/ao-logo.png" width="60" height="60" alt="">{t['name']}</a><p>{t['footer_text']}</p>{social_links(lang)}</div><div class="footer-nav"><h2>{t['nav'][2]}</h2>{links}</div><div><h2>{t['nav'][3]}</h2><a class="footer-phone" href="tel:+96522092040" dir="ltr">+965 2209 2040</a><a href="mailto:info@aliandothman.com.kw">info@aliandothman.com.kw</a><p>{t['address_text']}</p></div></div><div class="container footer-bottom"><span>© 2026 {t['name']}. {t['rights']}.</span><span>KUWAIT · <span lang="ar">الكويت</span></span></div></footer>'''

def cta(lang):
 t=COPY[lang]
 return f'<section class="cta"><div class="container cta-inner"><div><span class="eyebrow">{t["nav"][3]}</span><h2>{t["cta_title"]}</h2><p>{t["cta_text"]}</p></div>{button(url(lang,3),t["quote"])}</div></section>'

def heading(lang,title,intro,label):
 t=COPY[lang]
 return f'<section class="page-hero"><canvas class="flow-canvas" aria-hidden="true"></canvas><div class="container"><div class="breadcrumb"><a href="{url(lang,0)}">{t["back"]}</a><span>/</span>{label}</div><div class="page-heading"><h1>{title}</h1><p>{intro}</p></div></div></section>'

def cards(lang):
 return groups(lang)

def quality(lang):
 t=COPY[lang]; rows=''.join(f'<div class="quality-row reveal"><span>0{i+1}</span><div><h3>{a}</h3><p>{b}</p></div></div>' for i,(a,b) in enumerate(t['quality_items']))
 return f'<section class="section quality"><div class="container split"><div><span class="eyebrow">{t["quality_label"]}</span><h2>{t["quality_title"]}</h2><p class="muted">{t["quality_text"]}</p>{rows}</div><figure class="quality-photo reveal">{picture("company-engineers.jpg")}<figcaption>{t["since"]}</figcaption></figure></div></section>'

def home(lang):
 t=COPY[lang]; sectors=''.join(f'<span>{s}</span>' for s in t['sector_list'])
 return f'''<section class="home-hero"><canvas class="flow-canvas" aria-hidden="true"></canvas><div class="container hero-layout"><div class="hero-copy"><span class="eyebrow light">{t['since']}</span><h1>{t['hero']}</h1><p>{t['intro']}</p><div class="actions">{button(url(lang,3),t['quote'])}{button(url(lang,2),t['explore'],True)}</div></div><div class="hero-note"><span class="hero-monogram">A<span>&</span>O</span><span>{t['sub']}</span></div></div><div class="hero-bottom container"><span>ALI & OTHMAN</span><span>{t['annual']}</span><a href="#expertise" aria-label="{t['explore']}">↓</a></div></section>
 <div class="sector-strip"><div class="container"><strong>{t['sectors']}</strong>{sectors}</div></div>
 <section class="section" id="expertise"><div class="container"><div class="section-top"><div><span class="eyebrow">{t['service_label']}</span><h2>{t['service_title']}</h2></div><p class="muted">{t['service_intro']}</p></div>{cards(lang)}</div></section>
 <section class="about-band section"><div class="container split"><div class="about-visual reveal">{picture('company-engineers.jpg')}<div class="year-stamp"><strong>2007</strong><span>{t['year']}</span></div></div><div><span class="eyebrow">{t['about_label']}</span><h2>{t['about_title']}</h2><p>{t['about_text']}</p><a class="text-link" href="{url(lang,1)}">{t['about_more']}{arrow()}</a><div class="facts"><div><strong>07</strong><span>{t['disciplines']}</span></div><div><strong>{t['kuwait']}</strong><span>{t['location_label']}</span></div></div></div></div></section>
 <section class="section hvac"><div class="container split"><div><span class="eyebrow">{t['hvac_label']}</span><h2>{t['hvac_title']}</h2><p>{t['hvac_text']}</p>{button('/assets/ao-hvac-services.pdf',t['hvac_brochure'])}</div><div class="hvac-visual reveal">{picture('service-ac.jpg',t['hvac_label'])}<div class="image-label">{t['annual']}</div></div></div></section>{quality(lang)}{cta(lang)}'''

def about(lang):
 t=COPY[lang]
 return heading(lang,t['about_title'],t['about_text'],t['nav'][1])+f'<section class="section"><div class="container split"><figure class="about-visual reveal">{picture("company-engineers.jpg")}<div class="year-stamp"><strong>2007</strong><span>{t["year"]}</span></div></figure><div class="values"><article><span class="eyebrow">01</span><h2>{t["mission"]}</h2><p>{t["mission_text"]}</p></article><article><span class="eyebrow">02</span><h2>{t["vision"]}</h2><p>{t["vision_text"]}</p></article></div></div></section>'+quality(lang)+cta(lang)

def services(lang):
 t=COPY[lang]
 return heading(lang,t['services_title'],t['service_intro'],t['nav'][2])+f'<section class="section"><div class="container">'+groups(lang,True)+'</div></section>'+cta(lang)

def contact(lang):
 t=COPY[lang]
 return heading(lang,t['contact_title'],t['contact_intro'],t['nav'][3])+f'''<section class="section"><div class="container contact-layout"><aside class="contact-info"><span class="eyebrow">{t['name']}</span><h2>{t['nav'][3]}</h2><div class="contact-item"><span>{t['phone']}</span><a class="big-phone" dir="ltr" href="tel:+96522092040">+965 2209 2040</a><a href="https://wa.me/96522092040" class="text-link">{t['whatsapp']}{arrow()}</a></div><div class="contact-item"><span>{t['email']}</span><a href="mailto:info@aliandothman.com.kw">info@aliandothman.com.kw</a></div><div class="contact-item"><span>{t['address']}</span><p>{t['address_text']}</p></div>{social_links(lang,True)}</aside>{contact_form(lang)}</div></section>'''

def brochures(lang):
 t=COPY[lang]; result=[]
 for i,(file,title,size) in enumerate([('ao-hvac-services.pdf',t['hvac_brochure'],'1.9 MB'),('ao-all-services.pdf',t['all_brochure'],'1.5 MB')]):
  result.append(f'<article class="brochure-card reveal"><div class="brochure-art">{picture("brochure-cover.jpg",title)}<span>0{i+1}</span></div><div class="brochure-info"><span class="eyebrow" dir="ltr">PDF / {size}</span><h2>{title}</h2><div class="actions">{button("/assets/"+file,t["view"])}<a class="text-link" href="/assets/{file}" download>{t["download"]} ↓</a></div></div></article>')
 return heading(lang,t['brochure_title'],t['brochure_intro'],t['nav'][4])+'<section class="section"><div class="container brochure-list">'+''.join(result)+f'<button class="print-link" onclick="window.print()">{t["print"]}</button></div></section>'+cta(lang)

def build():
 OUT.mkdir(exist_ok=True)
 (OUT/'ao-website.css').write_text(Path('professional.css').read_text(encoding='utf-8') + Path('immersive.css').read_text(encoding='utf-8'),encoding='utf-8')
 (OUT/'site.js').write_text(Path('site.js').read_text(encoding='utf-8') + Path('immersive.js').read_text(encoding='utf-8'),encoding='utf-8')
 (OUT/'submit.php').write_text(Path('submit.php').read_text(encoding='utf-8'),encoding='utf-8')
 for lang,t in COPY.items():
  for page,render in enumerate([home,about,services,contact,brochures]):
   title=t['name']+' | '+t['nav'][page]; desc=[t['intro'],t['about_text'],t['service_intro'],t['contact_intro'],t['brochure_intro']][page]
   markup=f'''<!doctype html><html lang="{lang}" dir="{'rtl' if lang=='ar' else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(desc)}"><meta name="theme-color" content="#0c2541"><link rel="icon" href="/assets/ao-logo.png"><link rel="canonical" href="https://aliandothman.com.kw{url(lang,page)}"><link rel="alternate" hreflang="ar" href="https://aliandothman.com.kw{url('ar',page)}"><link rel="alternate" hreflang="en" href="https://aliandothman.com.kw{url('en',page)}"><link rel="stylesheet" href="/ao-website.css?v=3"><script src="/site.js?v=3" defer></script></head><body>{header(lang,page)}<main id="main">{render(lang)}</main>{footer(lang)}</body></html>'''
   dest=OUT/lang/ROUTES[page]/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(markup,encoding='utf-8')
 (OUT/'index.html').write_text('<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/ar/"><meta name="viewport" content="width=device-width,initial-scale=1"><title>علي وعثمان العالمية</title></head><body><a href="/ar/">العربية</a> · <a href="/en/">English</a></body></html>',encoding='utf-8')
 print('Built 10 bilingual pages and root entry point.')

if __name__=='__main__': build()
