<?php
declare(strict_types=1);
$recipient = 'aliothmanintl@gmail.com';
$redirect = '/ar/contact/?sent=1';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('Method Not Allowed'); }
if (!empty($_POST['_honey'] ?? '')) { header('Location: '.$redirect, true, 303); exit; }
$fields = [
    ['الاسم','Name'], ['المنطقة','Area'], ['القطعة','Block'], ['الشارع','Street'],
    ['المنزل','House'], ['رقم الهاتف','Phone number'], ['رقم الهاتف البديل','Alternative phone number'],
    ['الوقت المفضل للاتصال','Preferred callback time'], ['الوصف','Description'],
];
$lines = [];
foreach ($fields as [$arabic, $english]) {
    $value = trim((string)($_POST[$arabic] ?? $_POST[$english] ?? ''));
    if ($value === '' && $arabic !== 'رقم الهاتف البديل') { http_response_code(422); exit('Please complete all required fields.'); }
    $lines[] = $arabic.': '.preg_replace('/[\r\n]+/', ' ', $value);
}
$headers = "From: website@aliandothman.com.kw\r\nReply-To: website@aliandothman.com.kw\r\nContent-Type: text/plain; charset=UTF-8";
if (!mail($recipient, 'طلب اتصال جديد | Ali & Othman Website Enquiry', implode("\n", $lines), $headers)) { http_response_code(500); exit('Unable to send the enquiry at this time.'); }
header('Location: '.$redirect, true, 303); exit;
