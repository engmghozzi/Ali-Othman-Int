from html import escape

LOGO = '<img class="brand-logo" src="/assets/ao-logo.png" width="72" height="72" alt="">'

ICONS = {
    'Instagram': '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".7" fill="currentColor" stroke="none"/>',
    'Facebook': '<path d="M14 21v-8h3l.5-4H14V7c0-1 .4-2 2-2h2V1.5a23 23 0 0 0-3-.2c-3 0-5 1.9-5 5.3V9H7v4h3v8"/>',
    'WhatsApp': '<path d="M20.5 11.7a8.5 8.5 0 0 1-12.6 7.5L3 20.5l1.3-4.7A8.5 8.5 0 1 1 20.5 11.7Z"/><path d="m8 7 1.5 3-1 1c.8 1.5 2 2.7 3.5 3.5l1-1 3 1.5c-.2 1.4-1.2 2-2.5 1.8-3.9-.7-7.1-3.9-7.8-7.8C6.5 7.8 7 7.2 8 7Z"/>',
}
LINKS = {
    'Instagram': 'https://www.instagram.com/ali_othman_intl/',
    'Facebook': 'https://www.facebook.com/profile.php?id=100081159290485',
    'WhatsApp': 'https://wa.me/96522092040',
}

def social_links(lang, labels=False):
    names = {'Instagram': 'إنستغرام', 'Facebook': 'فيسبوك', 'WhatsApp': 'واتساب'} if lang == 'ar' else {k:k for k in LINKS}
    result = '<div class="social-links' + (' with-labels' if labels else '') + '">'
    for key, href in LINKS.items():
        label = names[key]
        icon = f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>'
        result += f'<a href="{escape(href)}" target="_blank" rel="noopener noreferrer" aria-label="{label}" title="{label}">{icon}' + (f'<span>{label}</span>' if labels else '') + '</a>'
    return result + '</div>'

def brochures(lang):
    ar = lang == 'ar'
    items = [
        ('ao-hvac-services.pdf', 'بروشور خدمات التكييف' if ar else 'HVAC services brochure', 'خدمات التكييف والتبريد مع صور توضيحية للأعمال.' if ar else 'Air conditioning and HVAC services with sample pictures.', '1.9 MB'),
        ('ao-all-services.pdf', 'بروشور جميع الخدمات' if ar else 'All services brochure', 'تعرّف على مجموعة خدمات علي وعثمان العالمية في بروشور واحد.' if ar else 'Explore Ali & Othman International services in one brochure.', '1.5 MB'),
    ]
    result = '<div class="grid brochure-downloads noprint">'
    for name, title, description, size in items:
        result += f'<article class="card"><span class="file-label" dir="ltr">PDF · {size}</span><h2>{title}</h2><p>{description}</p><div class="buttons"><a class="btn" href="/assets/{name}" target="_blank" rel="noopener">' + ('عرض البروشور' if ar else 'View brochure') + f'</a><a class="download-link" href="/assets/{name}" download>' + ('تحميل PDF' if ar else 'Download PDF') + '</a></div></article>'
    return result + '</div>'

def enhance(html, lang, page):
    import re
    html = html.replace('<span class="mark">ع</span>', LOGO)
    html = re.sub(r'<link rel="icon"[^>]+>', '<link rel="icon" type="image/png" href="/assets/ao-logo.png">', html)
    html = html.replace('<span>Kuwait · الكويت</span>', social_links(lang) + '<span>Kuwait · الكويت</span>')
    if page == 3:
        heading = 'تابعنا وتواصل معنا' if lang == 'ar' else 'Follow us and get in touch'
        html = html.replace('</section>', f'<div class="wrap social-contact"><h2>{heading}</h2>{social_links(lang, True)}</div></section>', 1)
    if page == 4:
        html = html.replace('<div class="noprint"><button', brochures(lang) + '<div class="noprint print-summary"><button', 1)
    return html.replace('Kuwait · الكويت', 'Kuwait · <span lang="ar">الكويت</span>')
