<?php
declare(strict_types=1);
$recipient = 'aliothmanintl@gmail.com';
$lang = (($_POST['_lang'] ?? 'ar') === 'en') ? 'en' : 'ar';
$redirect = '/'.$lang.'/contact/?sent=1';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('Method Not Allowed'); }
if (!empty($_POST['_honey'] ?? '')) { header('Location: '.$redirect, true, 303); exit; }
$fields = [
    ['name','الاسم'], ['area','المنطقة'], ['block','القطعة'], ['street','الشارع'],
    ['house','المنزل'], ['phone','رقم الهاتف'], ['alternative','رقم الهاتف البديل'],
    ['time','الوقت المفضل للاتصال'], ['description','الوصف'],
];
$lines = [];
foreach ($fields as [$key, $label]) {
    $value = trim((string)($_POST[$key] ?? ''));
    if ($value === '' && $key !== 'alternative') { http_response_code(422); exit('Please complete all required fields.'); }
    $lines[] = $label.': '.preg_replace('/[\r\n]+/', ' ', $value);
}
$headers = "From: website@aliandothman.com.kw\r\nReply-To: website@aliandothman.com.kw\r\nContent-Type: text/plain; charset=UTF-8";
if (!mail($recipient, 'طلب اتصال جديد | Ali & Othman Website Enquiry', implode("\n", $lines), $headers)) { http_response_code(500); exit('Unable to send the enquiry at this time.'); }
header('Location: '.$redirect, true, 303); exit;
