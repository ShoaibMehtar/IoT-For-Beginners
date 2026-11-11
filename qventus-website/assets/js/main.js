(function () {
  document.documentElement.classList.remove('no-js');

  // Mobile navigation
  var body = document.body;
  var burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = body.classList.toggle('nav-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Services dropdown: click toggles (needed on touch and mobile)
  document.querySelectorAll('.nav .dd > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var dd = btn.parentElement;
      var open = dd.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.nav .dd.open').forEach(function (dd) {
      if (!dd.contains(e.target) && window.innerWidth > 1080) dd.classList.remove('open');
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      body.classList.remove('nav-open');
      document.querySelectorAll('.nav .dd.open').forEach(function (dd) { dd.classList.remove('open'); });
    }
  });

  // Header shadow on scroll
  var header = document.querySelector('.site-header');
  var onScroll = function () { if (header) header.classList.toggle('scrolled', window.scrollY > 10); };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Reveal-on-scroll and counters
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var countUp = function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    if (reduce || isNaN(target)) { el.textContent = el.getAttribute('data-count'); return; }
    var start = null, dur = 1400;
    var step = function (t) {
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        en.target.querySelectorAll('[data-count]').forEach(countUp);
        if (en.target.hasAttribute('data-count')) countUp(en.target);
        io.unobserve(en.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal, .stats').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  // Enquiry form: sends online (FormSubmit), with an "email instead" option and email fallback
  var form = document.querySelector('form.quote');
  if (form) {
    var status = form.querySelector('.form-status');
    var submitBtn = form.querySelector('button[type="submit"]');
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('service');
    if (pre) {
      var sel = form.querySelector('select[name="service"]');
      Array.prototype.forEach.call(sel.options, function (o) { if (o.text === pre) sel.value = o.text; });
    }
    if (params.get('type') === 'amc') {
      var msg = form.querySelector('textarea[name="message"]');
      if (!msg.value) msg.value = 'We would like to request an Annual Maintenance Contract (AMC) proposal.\n\nEquipment / site details: ';
    }
    var show = function (cls, text) { status.className = 'form-status ' + cls; status.textContent = text; };
    var mailto = function () {
      var d = new FormData(form);
      var subject = 'Enquiry: ' + (d.get('service') || 'General') + ' — ' + (d.get('company') || d.get('name') || 'Website');
      var lines = ['Name: ' + (d.get('name') || ''), 'Company: ' + (d.get('company') || '-'), 'Email: ' + (d.get('email') || ''),
        'Phone: ' + (d.get('phone') || '-'), 'Service: ' + (d.get('service') || '-'), 'Facility / location: ' + (d.get('location') || '-'), '', d.get('message') || ''];
      window.location.href = 'mailto:' + form.getAttribute('data-to') + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    };
    form.querySelector('[data-action="email"]').addEventListener('click', mailto);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      if (d.get('_honey')) return;
      var payload = {};
      d.forEach(function (v, k) { if (k !== '_honey') payload[k] = v; });
      payload._subject = 'Website enquiry: ' + (payload.service || 'General') + ' — ' + (payload.company || payload.name);
      payload._template = 'table';
      payload._replyto = payload.email;
      submitBtn.disabled = true;
      show('', 'Sending…');
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && String(res.j.success) === 'true') {
            show('ok', 'Thank you — your enquiry has been sent. Our team will contact you shortly.');
            form.reset();
          } else { throw new Error('send failed'); }
        })
        .catch(function () {
          show('err', 'We could not send the form online. Opening your email app instead…');
          setTimeout(mailto, 900);
        })
        .then(function () { submitBtn.disabled = false; });
    });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
