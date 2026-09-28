"""Editorial content based on the supplied company and HVAC brochures.

Sources: ao-all-services.pdf pp. 2-12; HVAC brochure pp. 7-12.
No project counts, client endorsements, certifications or availability guarantees
have been added. Contact details supplied directly by the owner take precedence.
"""
SERVICES = [
 {'id':'air-conditioning','image':'service-ac.jpg','ar':('التكييف والتبريد','صيانة تُحافظ على راحة المكان.','صيانة وحدات التكييف والأنظمة المركزية، مع أعمال الصيانة الدورية والعقود السنوية للمنازل والمنشآت.',['صيانة الوحدات الداخلية والخارجية','فحص أدوات السلامة وضوابط الحماية الميكانيكية','فحص الصمامات والضوابط وضبطها','فحص الأحزمة والتآكل وضبط الشد']), 'en':('Air conditioning & cooling','Keep your space comfortable.','Maintenance of individual AC units and central systems, with periodic maintenance and annual contracts for homes and facilities.',['Indoor and outdoor unit maintenance','Safety devices and mechanical protection checks','Control and valve inspection and adjustment','Belt wear and tension checks'])},
 {'id':'duct-installation','image':'service-duct.jpg','ar':('تركيب وصيانة الدكت','شبكة هواء متكاملة للمبنى.','أعمال تركيب وصيانة الدكت المركزي ضمن الخدمات الميكانيكية للمباني والمنشآت.',['تركيب مجاري الهواء المركزية','صيانة أنظمة الدكت','أعمال ميكانيكية مرتبطة بالتهوية']), 'en':('Duct installation & maintenance','Air distribution for your building.','Central duct installation and maintenance as part of our mechanical services for buildings and facilities.',['Central air duct installation','Duct system maintenance','Mechanical ventilation works'])},
 {'id':'duct-cleaning','image':'cleaning-examples.jpg','ar':('تنظيف الدكت المركزي','عناية بمسار الهواء، من الداخل.','تنظيف مجاري الهواء باستخدام أدوات وكاميرات فحص ومواد تنظيف مناسبة، لإزالة الأتربة والتراكمات داخل الدكت.',['فحص مجاري الهواء بالكاميرات','تنظيف الأجزاء الداخلية من الدكت','استخدام أدوات ومواد تنظيف مناسبة']), 'en':('Central duct cleaning','Care for the air pathways inside.','Cleaning air ducts with inspection cameras, suitable tools and cleaning materials to remove dust and buildup from inside the system.',['Camera inspection of air ducts','Cleaning internal duct surfaces','Suitable cleaning tools and materials'])},
 {'id':'electrical','image':'service-electrical.jpg','ar':('الأعمال الكهربائية','تجهيزات كهربائية تخدم منشأتك.','أعمال الكهرباء والإنارة وشبكات الخدمات والبنية التحتية، إلى جانب أعمال الاتصالات والتحكم.',['أعمال الإنارة والكهرباء','المحولات ومحطات التوليد','شبكات الخدمات والبنية التحتية','أعمال الاتصالات والتحكم']), 'en':('Electrical works','Electrical systems for your facility.','Electrical and lighting works, utility networks and infrastructure, alongside communications and control works.',['Electrical and lighting works','Transformers and generation stations','Utility networks and infrastructure','Communications and control works'])},
 {'id':'plumbing','image':'service-plumbing.jpg','ar':('الأعمال الصحية والسباكة','حلول للشبكات والصيانة اليومية.','أعمال صحية للمجمعات السكنية والمباني، تشمل شبكات الصرف والسيول والخدمات والصيانة المنزلية.',['خطوط الصرف الصحي','شبكات تصريف مياه الأمطار','شبكات الخدمات للمجمعات السكنية','أعمال السباكة والصيانة المنزلية']), 'en':('Plumbing & sanitary works','From networks to everyday maintenance.','Sanitary works for residential complexes and buildings, covering drainage, stormwater, utility networks and home maintenance.',['Sewer and sanitary drainage lines','Stormwater drainage networks','Residential utility networks','Plumbing and home maintenance'])},
 {'id':'cctv','image':'service-cctv.jpg','ar':('كاميرات المراقبة','تركيب وصيانة أنظمة المراقبة.','خدمات تركيب وصيانة الكاميرات للمجمعات والمستشفيات والمباني السكنية، من خلال مهندسين وفنيين.',['تركيب كاميرات المراقبة','صيانة أنظمة الكاميرات','خدمة المجمعات والمستشفيات والمباني السكنية']), 'en':('CCTV systems','Installation and ongoing care.','Camera installation and maintenance for complexes, hospitals and residential buildings, delivered by engineers and technicians.',['Surveillance camera installation','Camera system maintenance','Support for complexes, hospitals and residential buildings'])},
 {'id':'interiors','image':'service-interiors.jpg','ar':('الديكورات والتشطيبات','تفاصيل تُكمل مساحة العمل والمعيشة.','أعمال ديكورات داخلية وخارجية للأسواق والقسائم والمباني ضمن خدمات المقاولات العامة.',['أعمال الديكور الداخلي','أعمال الديكور الخارجي','تشطيبات الأسواق والقسائم']), 'en':('Interiors & finishing','Finishing touches for work and living.','Interior and exterior decoration for markets, plots and buildings as part of our general contracting services.',['Interior decoration','Exterior decoration','Finishing for markets and properties'])},
]

COPY = {
 'ar': {
  'name':'علي وعثمان العالمية','sub':'للتجارة العامة والمقاولات','nav':['الرئيسية','عن الشركة','خدماتنا','تواصل معنا','البروشورات'],
  'quote':'اطلب عرض سعر','explore':'اكتشف خدماتنا','more':'تفاصيل الخدمة','since':'خبرة في الكويت منذ 2007',
  'hero':'نهتم بتفاصيل المبنى.<br><em>لتطمئن إلى كل يوم.</em>',
  'intro':'خدمات التكييف والصيانة والمقاولات للمنازل والمنشآت. خبرة تجمع بين الأعمال الفنية والعناية بالتفاصيل، من أنظمة الهواء إلى التشطيبات.',
  'service_label':'خبراتنا','service_title':'خدمات متكاملة.<br>فريق تتواصل معه بثقة.',
  'service_intro':'التكييف، الأنظمة الميكانيكية، الكهرباء، السباكة والتشطيبات — خدمات تجمع احتياجات مبناك في مكان واحد.',
  'about_label':'علي وعثمان العالمية','about_title':'منذ 2007،<br>نبني علاقات تدوم.',
  'about_text':'تأسست شركة علي وعثمان العالمية في الكويت عام 2007، وتخصصت في الصيانة العامة والمقاولات والأعمال الميكانيكية والكهربائية والصحية. وتشمل خبرتها التعامل مع القطاعين الحكومي والخاص والجمعيات التعاونية.',
  'about_more':'تعرّف على الشركة','quality_label':'كيف نعمل','quality_title':'الجودة والسلامة<br>في كل تفصيل.',
  'quality_text':'يعتمد نهجنا على الفحص المستمر والمراقبة الدورية للأعمال، ومتابعة الأداء ورضا العملاء، مع مراعاة احتياطات الأمن والسلامة.',
  'quality_items':[('فحص ومتابعة','مراقبة دورية لمختلف الأعمال ومتابعة مؤشرات الأداء.'),('عناية بالسلامة','الالتزام باحتياطات الأمن والسلامة أثناء تنفيذ الأعمال.'),('فهم احتياجاتك','تحديد متطلبات الموقع ونطاق العمل قبل التنفيذ.')],
  'sectors':'نخدم احتياجات قطاعات متعددة','sector_list':['المنازل والمباني السكنية','المنشآت والقطاع الخاص','الجهات الحكومية','الجمعيات التعاونية'],
  'hvac_label':'تخصصنا في التكييف','hvac_title':'راحة المكان تبدأ<br>من كفاءة أنظمته.',
  'hvac_text':'صيانة دورية وعقود سنوية لوحدات التكييف والأنظمة المركزية، إلى جانب تركيب الدكت وصيانته وتنظيفه. اكتشف نطاق الأعمال والصور التوضيحية في بروشور التكييف.',
  'hvac_brochure':'بروشور خدمات التكييف','all_brochure':'بروشور جميع الخدمات',
  'cta_title':'ما الذي يحتاجه مبناك؟','cta_text':'حدّثنا عن متطلباتك لننسّق المعاينة ونناقش نطاق العمل المناسب.',
  'phone':'اتصل بنا','whatsapp':'تواصل عبر واتساب','address':'موقعنا','address_text':'المرقاب، برج التجار، الدور السادس، مكتب 17، الكويت',
  'email':'البريد الإلكتروني','footer_text':'خبرة في الصيانة العامة والمقاولات، لخدمة المنازل والمنشآت في الكويت.',
  'rights':'جميع الحقوق محفوظة','brochure_title':'تعرّف على خدماتنا،<br>بالتفصيل.',
  'brochure_intro':'ملفات الشركة الأصلية، للعرض أو التحميل: نطاق الخدمات ونبذة الشركة وصور توضيحية للأعمال.',
  'download':'تحميل PDF','view':'عرض البروشور','sample':'صور توضيحية من بروشور الشركة',
  'contact_title':'لنتحدث عن<br>احتياجاتك.', 'contact_intro':'أرسل تفاصيل طلبك والوقت الأنسب للاتصال، أو تواصل معنا مباشرة عبر الهاتف أو واتساب.',
  'services_title':'لكل جزء من مبناك،<br>خبرة تهتم به.', 'scope':'نطاق الخدمة',
  'vision':'رؤيتنا','vision_text':'خدمات متكاملة في المقاولات العامة والصيانة، تقوم على التخطيط الجيد والتنفيذ المتقن والمصداقية.',
  'mission':'هدفنا','mission_text':'توظيف خبراتنا ومواردنا الفنية لتقديم أعمال دقيقة وفعالة، وحلول تستجيب لاحتياجات العملاء.',
  'back':'الرئيسية','menu':'القائمة','print':'طباعة هذه الصفحة','annual':'صيانة دورية وعقود سنوية','year':'سنة التأسيس','disciplines':'مجالات خدمات','kuwait':'الكويت','location_label':'مقر أعمالنا',
 },
 'en': {
  'name':'Ali & Othman International','sub':'General Trading & Contracting','nav':['Home','About us','Our services','Contact','Brochures'],
  'quote':'Request a quote','explore':'Explore our services','more':'Service details','since':'Serving Kuwait since 2007',
  'hero':'We care for your building.<br><em>You get on with your day.</em>',
  'intro':'Air conditioning, maintenance and contracting for homes and facilities. Technical experience and attention to detail, from air systems to finishing works.',
  'service_label':'Our expertise','service_title':'Connected services.<br>A team you can talk to.',
  'service_intro':'Air conditioning, mechanical systems, electrical works, plumbing and finishing — expertise for your building, all in one place.',
  'about_label':'Ali & Othman International','about_title':'Building relationships.<br>Since 2007.',
  'about_text':'Established in Kuwait in 2007, Ali & Othman International specialises in general maintenance, contracting, mechanical, electrical and sanitary works. Its experience includes working with government and private sectors and cooperative societies.',
  'about_more':'More about the company','quality_label':'Our approach','quality_title':'Quality and safety.<br>In every detail.',
  'quality_text':'Our approach combines continuous inspection, periodic monitoring, performance follow-up and attention to customer satisfaction, with appropriate safety precautions.',
  'quality_items':[('Inspection & follow-up','Periodic checks across the work and ongoing performance monitoring.'),('Attention to safety','Safety precautions throughout the delivery of our work.'),('Understanding your needs','Defining site requirements and the scope before work begins.')],
  'sectors':'Supporting a range of sectors','sector_list':['Homes & residential buildings','Businesses & private facilities','Government entities','Cooperative societies'],
  'hvac_label':'Air conditioning expertise','hvac_title':'Comfort starts<br>with the systems behind it.',
  'hvac_text':'Periodic maintenance and annual contracts for AC units and central systems, alongside duct installation, maintenance and cleaning. Explore the scope and sample pictures in our HVAC brochure.',
  'hvac_brochure':'HVAC services brochure','all_brochure':'All services brochure',
  'cta_title':'What does your building need?','cta_text':'Tell us about your requirements so we can discuss the scope and arrange a site visit.',
  'phone':'Call us','whatsapp':'Chat on WhatsApp','address':'Visit us','address_text':'Merqab, Al Tujjar Tower, 6th floor, Office 17, Kuwait',
  'email':'Email','footer_text':'General maintenance and contracting expertise for homes and facilities in Kuwait.',
  'rights':'All rights reserved','brochure_title':'A closer look<br>at our expertise.',
  'brochure_intro':'Our original company brochures, ready to view or download: service scope, company background and illustrative work pictures.',
  'download':'Download PDF','view':'View brochure','sample':'Illustrative pictures from our company brochure',
  'contact_title':'Let’s talk about<br>your requirements.','contact_intro':'Share your enquiry and preferred callback time, or reach us directly by phone or WhatsApp.',
  'services_title':'Expertise for every<br>part of your building.','scope':'Scope of service',
  'vision':'Our vision','vision_text':'Integrated contracting and maintenance services built on sound planning, careful execution and credibility.',
  'mission':'Our purpose','mission_text':'Apply our technical experience and resources to deliver precise, effective work and solutions that respond to customer needs.',
  'back':'Home','menu':'Menu','print':'Print this page','annual':'Periodic maintenance & annual contracts','year':'Established','disciplines':'Service areas','kuwait':'Kuwait','location_label':'Our home base',
 }
}
