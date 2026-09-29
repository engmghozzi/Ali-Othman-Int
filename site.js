(() => {
  const query = new URLSearchParams(location.search);
  if (query.get('sent') === '1') {
    const ar = document.documentElement.lang === 'ar';
    const form = document.querySelector('.contact-form');
    if (form) {
      const status = document.createElement('div');
      status.className = 'form-status form-status-success';
      status.setAttribute('role', 'status');
      status.textContent = ar ? 'تم إرسال طلبك بنجاح. سنتواصل معك قريبًا.' : 'Your enquiry was sent successfully. We will contact you soon.';
      form.prepend(status);
    }
    history.replaceState({}, '', location.pathname);
  }
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-navigation');
  if (menu && nav) {
    document.documentElement.classList.add('menu-ready');
    const close = () => { nav.classList.remove('is-open'); menu.setAttribute('aria-expanded', 'false'); };
    menu.addEventListener('click', () => {
      const open = menu.getAttribute('aria-expanded') !== 'true';
      menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open);
    });
    nav.addEventListener('click', event => { if (event.target.closest('a')) close(); });
    document.addEventListener('keydown', event => { if (event.key === 'Escape' && nav.classList.contains('is-open')) { close(); menu.focus(); } });
  }
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  if (reduce.matches || !('IntersectionObserver' in window)) return;
  const animations = new Set();
  const observer = new IntersectionObserver(entries => {
    let stagger = 0;
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      observer.unobserve(entry.target);
      if (!entry.target.animate) continue;
      const animation = entry.target.animate([{opacity:0,transform:'translateY(18px)'},{opacity:1,transform:'translateY(0)'}], {duration:650,delay:Math.min(stagger++ * 65,195),fill:'backwards',easing:'cubic-bezier(.2,.7,.2,1)'});
      animations.add(animation);
      animation.finished.then(()=>animations.delete(animation),()=>animations.delete(animation));
    }
  }, {threshold:.06});
  document.querySelectorAll('.reveal,.hero-copy > *, .page-heading > *, .section-top > *, .form-field').forEach(el=>observer.observe(el));
  const cancel=()=>{observer.disconnect();animations.forEach(a=>a.cancel());animations.clear();};
  reduce.addEventListener('change', e=>{if(e.matches)cancel();});
  addEventListener('beforeprint',cancel);
  addEventListener('pagehide',cancel);
  addEventListener('pageshow',e=>{if(e.persisted)cancel();});
})();
