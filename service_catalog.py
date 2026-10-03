from pathlib import Path
from html import escape
import json
CATALOG=json.loads(Path(__file__).with_name('services-data.json').read_text(encoding='utf-8'))
def card(item,lang,detailed=False):
 t=item[lang];key=item['id'];ar=lang=='ar';number=next(i for i,s in enumerate(CATALOG,1) if s['id']==key)
 extension='jpg' if key=='interiors' else 'webp'
 image=f'<img src="/assets/service-{key}.{extension}" alt="{escape(t["alt"])}" loading="lazy" decoding="async" width="1600" height="1040">'
 href=f'/{lang}/services/#{key}'
 result=f'<article class="service-card lusion-card reveal" id="{key}"><a class="service-image" href="{href}" aria-label="{escape(t["title"])}">{image}<span class="service-number">0{number}</span></a><div class="service-meta">{escape(t["tags"])}</div><a href="{href}" class="service-title"><h3>{escape(t["title"])}</h3></a><p class="service-intro">{escape(t["intro"])}</p>'
 if detailed:
  result+='<details class="service-details"><summary>'+('نطاق الخدمة بالتفصيل' if ar else 'Explore the full service')+'</summary><div class="service-detail-body">'
  result+=''.join('<p>'+escape(p)+'</p>' for p in t['paragraphs'])
  result+='<dl>'+''.join('<div><dt>'+escape(a)+'</dt><dd>'+escape(b)+'</dd></div>' for a,b in t['items'])+'</dl>'
  if t.get('legacy'):
   result+='<h4>'+('أعمال تخصصية ضمن نطاق المشروع' if ar else 'Specialist work within the project scope')+'</h4><ul>'+''.join('<li>'+escape(p)+'</li>' for p in t['legacy'])+'</ul>'
  result+=f'<a class="text-link" href="/{lang}/contact/">'+('اطلب معاينة أو عرض سعر' if ar else 'Arrange an inspection or quotation')+'</a></div></details>'
 else:result+=f'<a class="text-link" href="{href}">'+('تفاصيل الخدمة' if ar else 'Service details')+'</a>'
 return result+'</article>'
def groups(lang,detailed=False):
 ar=lang=='ar';result=''
 for start,end,title in [(0,3,'الخدمات الأساسية للشركة' if ar else 'Our core services'),(3,6,'خدمات المقاولات العامة' if ar else 'General contracting'),(6,7,'خدمات إضافية' if ar else 'Additional services')]:
  result+=f'<div class="service-group"><h2>{title}</h2><div class="service-grid services-gallery">'+''.join(card(x,lang,detailed) for x in CATALOG[start:end])+'</div></div>'
 return result
