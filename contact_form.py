from html import escape

def contact_form(lang):
    ar = lang == 'ar'
    def field(key, label, kind='text', required=True, autocomplete=None, placeholder=None, maxlength=120):
        attrs = f' id="contact-{key}" name="{key}" type="{kind}" maxlength="{maxlength}"'
        if required: attrs += ' required'
        if autocomplete: attrs += f' autocomplete="{autocomplete}"'
        if placeholder: attrs += f' placeholder="{placeholder}"'
        if kind == 'tel': attrs += ' dir="ltr" inputmode="tel" pattern="[+0-9٠-٩۰-۹() .\\-]{8,25}"'
        optional = '' if required else (' (اختياري)' if ar else ' (optional)')
        return f'<div class="form-field"><label for="contact-{key}">{label}{optional}</label><input{attrs}></div>'

    heading = 'أرسل طلبك' if ar else 'Send an enquiry'
    intro = 'اترك بياناتك وتفاصيل الطلب لنتواصل معك. جميع الحقول مطلوبة عدا الرقم البديل.' if ar else 'Leave your details and enquiry so we can call you. All fields are required except the alternative phone number.'
    fields = field('name', 'الاسم' if ar else 'Name', autocomplete='name')
    address = [('area','المنطقة','Area'), ('block','القطعة','Block'), ('street','الشارع','Street'), ('house','المنزل','House')]
    fields += '<fieldset class="address-fields"><legend>' + ('العنوان' if ar else 'Address') + '</legend><div class="form-grid">'
    for key, arabic, english in address:
        fields += field(key, arabic if ar else english)
    fields += '</div></fieldset><div class="form-grid">'
    fields += field('phone', 'رقم الهاتف' if ar else 'Phone number', 'tel', autocomplete='tel', maxlength=25)
    fields += field('alternative', 'رقم الهاتف البديل' if ar else 'Alternative phone number', 'tel', required=False, maxlength=25)
    fields += '</div>'
    fields += field('time', 'الوقت المفضل للاتصال' if ar else 'Preferred callback time', placeholder='مثال: من ٤ إلى ٦ مساءً بتوقيت الكويت' if ar else 'e.g. 4–6 PM, Kuwait time')
    description = 'الوصف' if ar else 'Description'
    fields += f'<div class="form-field"><label for="contact-description">{description}</label><textarea id="contact-description" name="description" rows="5" maxlength="5000" required></textarea></div>'
    note = 'بالإرسال، تُرسل بياناتك عبر FormSubmit إلى فريقنا للتواصل بشأن طلبك. ستفتح صفحة إتمام الإرسال والتحقق في نافذة جديدة.' if ar else 'Your details are sent through FormSubmit to our team to follow up on your enquiry. Submission and verification will continue in a new tab.'
    button = 'إرسال الطلب' if ar else 'Send enquiry'
    return f'''<div class="contact-form panel">
      <h2>{heading}</h2><p class="lead">{intro}</p>
      <form action="/submit.php" method="POST" accept-charset="UTF-8">
        <input type="hidden" name="_lang" value="{lang}">
        <input type="hidden" name="_subject" value="طلب اتصال جديد | Ali &amp; Othman Website Enquiry">
        <input type="hidden" name="_template" value="table">
        <input type="text" name="_honey" class="form-trap" tabindex="-1" autocomplete="off" aria-hidden="true">
        {fields}
        <p class="form-note" id="contact-privacy">{note}</p>
        <button class="btn" type="submit" aria-describedby="contact-privacy">{button}</button>
      </form>
    </div>'''
