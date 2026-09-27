(() => {
  'use strict';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const active = new Set();
  let observer;
  const reveal = (element, delay = 0) => {
    if (reduced.matches || typeof element.animate !== 'function') return;
    const animation = element.animate([
      { opacity: 0, transform: 'translateY(16px)' },
      { opacity: 1, transform: 'translateY(0)' }
    ], { duration: 560, delay, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards' });
    active.add(animation);
    animation.finished.then(() => active.delete(animation), () => active.delete(animation));
  };
  const showAll = () => {
    observer?.disconnect();
    active.forEach(animation => animation.cancel());
    active.clear();
  };
  // Content is visible by default; animation never gates access to the page.
  if (!reduced.matches && 'IntersectionObserver' in window) {
    const targets = [...document.querySelectorAll(
      '.hero .kicker,.hero h1,.hero p,.hero .buttons,.pagehead h1,.pagehead p,' +
      '.section .wrap > h2,.section .lead,.card,.detail > .panel,' +
      '.contact-form > h2,.form-field,.address-fields legend,.form-note,' +
      '.contact-form button,.band h2,.band p,.band .btn,.social-contact h2,.social-links'
    )];
    observer = new IntersectionObserver(entries => {
      let position = 0;
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        reveal(entry.target, Math.min(position++ * 55, 220));
      });
    }, { threshold: 0.08 });
    targets.forEach(target => observer.observe(target));
    document.querySelectorAll('header .brand,header .links a').forEach((item, index) => reveal(item, Math.min(index * 35, 180)));
  }
  reduced.addEventListener('change', event => { if (event.matches) showAll(); });
  window.addEventListener('beforeprint', showAll);
  window.addEventListener('pagehide', showAll);
  // A restored page remains fully visible, including when loaded from the back cache.
  window.addEventListener('pageshow', event => { if (event.persisted) showAll(); });
})();
