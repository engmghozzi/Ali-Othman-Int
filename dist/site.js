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
  document.querySelectorAll('.contact-form form').forEach(form => {
    form.addEventListener('submit', async event => {
      event.preventDefault();
      const ar = document.documentElement.lang === 'ar';
      const modal = document.createElement('div');
      modal.className = 'form-modal';
      modal.innerHTML = `<div class="form-modal-card" role="dialog" aria-modal="true"><button class="form-modal-close" type="button" aria-label="${ar ? 'إغلاق' : 'Close'}">×</button><p class="form-modal-message">${ar ? 'جارٍ إرسال طلبك…' : 'Sending your enquiry…'}</p></div>`;
      document.body.append(modal);
      const close = () => modal.remove();
      modal.querySelector('.form-modal-close').addEventListener('click', close);
      try {
        const response = await fetch(form.action, {method:'POST', body:new FormData(form), headers:{Accept:'text/plain'}});
        if (!response.ok) throw new Error('send failed');
        modal.querySelector('.form-modal-message').textContent = ar ? 'تم إرسال طلبك بنجاح. سنتواصل معك قريبًا.' : 'Your enquiry was sent successfully. We will contact you soon.';
        modal.querySelector('.form-modal-card').classList.add('is-success');
        form.reset();
      } catch (error) {
        modal.querySelector('.form-modal-message').textContent = ar ? 'تعذر إرسال الطلب حاليًا. حاول مرة أخرى أو تواصل معنا عبر واتساب.' : 'The enquiry could not be sent. Please try again or contact us on WhatsApp.';
        modal.querySelector('.form-modal-card').classList.add('is-error');
      }
    });
  });
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

(() => {
'use strict'; const reduced=matchMedia('(prefers-reduced-motion: reduce)');let scrollY=window.scrollY;addEventListener('scroll',()=>{scrollY=window.scrollY;},{passive:true});const stopReveals=()=>{};
 const canvases=[...document.querySelectorAll('.flow-canvas')];const scenes=[];let pointer={x:.6,y:.45},anim=0,visible=true;
 addEventListener('pointermove',e=>{pointer.x=e.clientX/innerWidth;pointer.y=e.clientY/innerHeight;},{passive:true});
 for(const canvas of canvases){const ctx=canvas.getContext('2d');if(!ctx)continue;const scene={canvas,ctx,w:0,h:0,active:true};scenes.push(scene);const resize=()=>{const r=canvas.getBoundingClientRect();scene.w=r.width;scene.h=r.height;const d=Math.min(devicePixelRatio||1,1.5);canvas.width=Math.round(r.width*d);canvas.height=Math.round(r.height*d);ctx.setTransform(d,0,0,d,0,0);};resize();if('ResizeObserver'in window)new ResizeObserver(()=>{resize();if(reduced.matches)draw(scene,0);}).observe(canvas.parentElement);if('IntersectionObserver'in window)new IntersectionObserver(es=>{scene.active=es[0].isIntersecting;}).observe(canvas);}
 function draw(s,time){const {ctx:c,w,h}=s;if(!w||!h)return;c.clearRect(0,0,w,h);const t=time*.00017,px=reduced.matches?.6:pointer.x,py=reduced.matches?.45:pointer.y;const cx=w*(.62+(px-.5)*.08),cy=h*(.43+(py-.5)*.07);const g=c.createRadialGradient(cx,cy,0,cx,cy,w*.58);g.addColorStop(0,'rgba(45,95,245,.27)');g.addColorStop(.45,'rgba(22,55,140,.16)');g.addColorStop(1,'rgba(5,8,18,0)');c.fillStyle=g;c.fillRect(0,0,w,h);c.save();c.translate(cx,cy-scrollY*.035);c.globalCompositeOperation='screen';
 // Layered abstract airflow: depth, perspective and a gentle pointer response.
 for(let j=0;j<64;j++){const depth=j/63,rotation=.45+Math.sin(t+depth*2)*.17;c.beginPath();for(let i=0;i<=130;i++){const angle=i/130*Math.PI*2;const wave=1+Math.sin(angle*3+t*2+depth*5)*.12;const rx=(w*.12+depth*w*.35)*wave,ry=(h*.075+depth*h*.22)*wave;const x=Math.cos(angle)*rx,y=Math.sin(angle)*ry;const xx=x*Math.cos(rotation)-y*Math.sin(rotation),yy=x*Math.sin(rotation)+y*Math.cos(rotation)+Math.sin(depth*5+t)*h*.055;if(i===0)c.moveTo(xx,yy);else c.lineTo(xx,yy);}c.closePath();c.strokeStyle=`rgba(${90+Math.round(depth*45)},${135+Math.round(depth*50)},255,${.13+Math.sin(depth*Math.PI)*.3})`;c.lineWidth=depth>.75?1.1:.65;c.stroke();}c.restore();}
 let last=0;function loop(time){if(visible&&time-last>32){scenes.forEach(s=>{if(s.active)draw(s,time);});last=time;}if(!reduced.matches)anim=requestAnimationFrame(loop);}
 const start=()=>{cancelAnimationFrame(anim);if(reduced.matches)scenes.forEach(s=>draw(s,0));else anim=requestAnimationFrame(loop);};start();
 reduced.addEventListener('change',()=>{stopReveals();start();});document.addEventListener('visibilitychange',()=>{visible=!document.hidden;if(visible)start();else cancelAnimationFrame(anim);});addEventListener('pagehide',()=>{cancelAnimationFrame(anim);stopReveals();});addEventListener('pageshow',e=>{if(e.persisted){stopReveals();start();scrollY=window.scrollY;}});addEventListener('beforeprint',stopReveals);
})();
(() => {
 const open=()=>{const card=document.getElementById(location.hash.slice(1));const details=card?.querySelector('.service-details');if(details)details.open=true;};
 addEventListener('hashchange',open);open();
 document.addEventListener('click',event=>{const link=event.target.closest('.lusion-card a[href]');if(!link)return;const url=new URL(link.href,location.href);if(url.pathname===location.pathname&&url.hash){const details=document.getElementById(url.hash.slice(1))?.querySelector('.service-details');if(details)details.open=true;}});
})();
