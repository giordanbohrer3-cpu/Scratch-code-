/* Drysul — efeitos: fundo técnico em canvas, entradas ao rolar, parallax, camadas do hero,
   luz no ponteiro, inclinação de cartões, botões magnéticos e controle de pausa.
   Rolagem nativa (sem scroll hijacking). Tudo respeita prefers-reduced-motion e o botão de pausa. */
(function () {
  'use strict';

  var root = document.documentElement;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var KEY = 'drysul-motion';
  var mqReduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var mqFine = window.matchMedia('(hover: hover) and (pointer: fine)');
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var on = root.classList.contains('motion-on');
  var hasIO = 'IntersectionObserver' in window;

  function pref() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }

  /* ---------- controle de pausa ---------- */
  var toggle = $('#motion-toggle');
  function updateToggle() {
    if (!toggle) return;
    $('span', toggle).textContent = on ? 'Pausar efeitos' : 'Ativar efeitos';
    $('use', toggle).setAttribute('href', on ? '#i-pause' : '#i-play');
    toggle.title = mqReduce.matches && !pref() ? 'Seu dispositivo pede menos movimento — efeitos reduzidos' : '';
  }
  function apply(v) {
    on = v;
    root.classList.toggle('motion-on', v);
    root.classList.toggle('motion-paused', !v);
    updateToggle();
    if (v) { revealVisibleNow(); requestUpdate(); startCanvas(); }
    else { resetTransforms(); stopCanvas(); drawStatic(); }
  }
  if (toggle) toggle.addEventListener('click', function () {
    var next = !on;
    try { localStorage.setItem(KEY, next ? 'on' : 'off'); } catch (e) {}
    apply(next);
  });
  var onMq = function () { if (!pref()) apply(!mqReduce.matches); else updateToggle(); };
  if (mqReduce.addEventListener) mqReduce.addEventListener('change', onMq); else if (mqReduce.addListener) mqReduce.addListener(onMq);

  /* ---------- entradas ao rolar ---------- */
  $$('[data-stagger]').forEach(function (g) {
    $$('[data-reveal]', g).forEach(function (el, i) { el.style.setProperty('--d', Math.min(i, 6) * 80 + 'ms'); });
  });
  var revealIO = hasIO ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); revealIO.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 }) : null;
  function observeReveals() {
    $$('[data-reveal]:not(.is-in)').forEach(function (el) {
      if (revealIO) revealIO.observe(el); else el.classList.add('is-in');
    });
  }
  // Ao reativar efeitos, o que já está na tela não deve sumir para reanimar
  function revealVisibleNow() {
    var vh = window.innerHeight;
    $$('[data-reveal]').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < vh && r.bottom > 0) el.classList.add('is-in');
      if (r.bottom <= 0) el.classList.add('is-in'); // acima da tela: já foi lido
    });
  }
  observeReveals();

  /* ---------- parallax e camadas ---------- */
  var parallax = $$('[data-parallax]'), photos = $$('[data-parallax-img]'), drift = $('[data-drift]');
  var hero = $('.hero'), layers = $$('[data-layer]');
  var visible = new Set();
  var visIO = hasIO ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) visible.add(e.target); else visible.delete(e.target); });
    requestUpdate();
  }, { rootMargin: '120px 0px' }) : null;
  var targets = parallax.map(function (el) { return el.parentElement; })
    .concat(photos.map(function (el) { return el.parentElement; }))
    .concat(drift ? [drift.parentElement] : [], hero ? [hero] : []);
  targets.forEach(function (t) { if (visIO) visIO.observe(t); });

  var ticking = false;
  function requestUpdate() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  function update() {
    ticking = false;
    if (!on) return;
    var vh = window.innerHeight, small = window.innerWidth < 720, k = small ? 0.5 : 1;

    parallax.forEach(function (el) {
      var p = el.parentElement; if (!visible.has(p)) return;
      var r = p.getBoundingClientRect();
      var s = parseFloat(el.getAttribute('data-parallax')) || 0.1;
      var y = clamp((r.top + r.height / 2 - vh / 2) * -s, -48, 48) * k;
      el.style.transform = 'translate3d(0,' + y.toFixed(1) + 'px,0)';
    });
    photos.forEach(function (img) {
      var f = img.parentElement; if (!visible.has(f)) return;
      var r = f.getBoundingClientRect();
      var prog = clamp((r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2), -1, 1);
      img.style.transform = 'translate3d(0,' + (-prog * r.height * 0.06 * k).toFixed(1) + 'px,0)';
    });
    if (drift && visible.has(drift.parentElement)) {
      var dr = drift.parentElement.getBoundingClientRect();
      var dp = clamp((vh - dr.top) / (vh + dr.height), 0, 1);
      drift.style.transform = 'translate3d(' + (-dp * 22).toFixed(2) + 'vw,0,0)';
    }
    if (hero && visible.has(hero) && layers.length) {
      var hr = hero.getBoundingClientRect();
      var hp = clamp(-hr.top / hr.height, 0, 1);
      layers.forEach(function (g) {
        var front = g.getAttribute('data-layer') === 'front';
        var x = hp * (front ? 46 : 18) * k, y = -hp * (front ? 30 : 12) * k;
        g.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)';
      });
    }
  }
  function resetTransforms() {
    parallax.concat(photos, layers, drift ? [drift] : []).forEach(function (el) { el.style.transform = ''; });
    $$('.is-tilting').forEach(function (el) { el.classList.remove('is-tilting'); el.style.transform = ''; });
    $$('[data-magnetic]').forEach(function (el) { el.style.transform = ''; });
  }
  window.addEventListener('scroll', requestUpdate, { passive: true });
  window.addEventListener('resize', requestUpdate);

  /* ---------- ponteiro: luz, inclinação e magnetismo (só mouse/trackpad) ---------- */
  var tiltEl = null, magEl = null, pointerFrame = 0, lastEv = null;
  function onPointer(ev) {
    if (!on || !mqFine.matches || ev.pointerType === 'touch') return;
    lastEv = ev;
    if (!pointerFrame) pointerFrame = requestAnimationFrame(applyPointer);
  }
  function applyPointer() {
    pointerFrame = 0;
    var ev = lastEv; if (!ev) return;
    var t = ev.target instanceof Element ? ev.target : null;

    if (hero && t && hero.contains(t)) {
      var hr = hero.getBoundingClientRect();
      hero.style.setProperty('--px', ((ev.clientX - hr.left) / hr.width * 100).toFixed(1) + '%');
      hero.style.setProperty('--py', ((ev.clientY - hr.top) / hr.height * 100).toFixed(1) + '%');
    }

    var tilt = t && t.closest('[data-tilt]');
    if (tiltEl && tiltEl !== tilt) releaseTilt(tiltEl);
    tiltEl = tilt;
    if (tilt) {
      var r = tilt.getBoundingClientRect();
      var px = (ev.clientX - r.left) / r.width, py = (ev.clientY - r.top) / r.height;
      tilt.classList.add('is-tilting');
      tilt.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
      tilt.style.setProperty('--my', (py * 100).toFixed(1) + '%');
      tilt.style.transform = 'perspective(900px) rotateX(' + ((0.5 - py) * 5).toFixed(2) + 'deg) rotateY(' + ((px - 0.5) * 6).toFixed(2) + 'deg) translateY(-4px)';
    }

    var mag = t && t.closest('[data-magnetic]');
    if (magEl && magEl !== mag) magEl.style.transform = '';
    magEl = mag;
    if (mag) {
      var m = mag.getBoundingClientRect();
      var dx = clamp((ev.clientX - (m.left + m.width / 2)) * 0.12, -4, 4);
      var dy = clamp((ev.clientY - (m.top + m.height / 2)) * 0.2, -3, 3);
      mag.style.transform = 'translate(' + dx.toFixed(1) + 'px,' + dy.toFixed(1) + 'px)';
    }
  }
  function releaseTilt(el) { el.classList.remove('is-tilting'); el.style.transform = ''; }
  document.addEventListener('pointermove', onPointer, { passive: true });
  document.addEventListener('pointerleave', function () {
    if (tiltEl) releaseTilt(tiltEl); if (magEl) magEl.style.transform = ''; tiltEl = magEl = null;
  });

  /* ---------- fundo técnico em canvas ---------- */
  function TechCanvas(cv) {
    this.cv = cv; this.ctx = cv.getContext('2d'); this.dark = cv.getAttribute('data-canvas') === 'dark';
    this.visible = false; this.w = 0; this.h = 0; this.crosses = [];
    this.resize();
  }
  TechCanvas.prototype.resize = function () {
    var r = this.cv.getBoundingClientRect();
    var dpr = Math.min(window.devicePixelRatio || 1, window.innerWidth < 720 ? 1.25 : 1.5);
    this.w = r.width; this.h = r.height;
    this.cv.width = Math.max(1, Math.round(r.width * dpr)); this.cv.height = Math.max(1, Math.round(r.height * dpr));
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var n = Math.round(clamp(this.w * this.h / 26000, 10, 70));
    this.crosses = [];
    for (var i = 0; i < n; i++) {
      this.crosses.push({ gx: Math.floor(Math.random() * 40), gy: Math.floor(Math.random() * 40), ph: Math.random() * 6.28, sp: 0.4 + Math.random() * 0.9, hot: Math.random() < 0.35 });
    }
  };
  TechCanvas.prototype.draw = function (t) {
    var c = this.ctx, w = this.w, h = this.h, dark = this.dark;
    if (!w || !h) return;
    c.clearRect(0, 0, w, h);
    var minor = 24, major = 120, off = (t * 0.008) % major;
    var ink = dark ? '216,217,210' : '16,22,43';

    c.lineWidth = 1;
    c.strokeStyle = 'rgba(' + ink + ',' + (dark ? 0.04 : 0.035) + ')';
    c.beginPath();
    for (var x = (off % minor) - minor; x < w; x += minor) { c.moveTo(x + 0.5, 0); c.lineTo(x + 0.5, h); }
    for (var y = (off % minor) - minor; y < h; y += minor) { c.moveTo(0, y + 0.5); c.lineTo(w, y + 0.5); }
    c.stroke();
    c.strokeStyle = 'rgba(' + ink + ',' + (dark ? 0.08 : 0.06) + ')';
    c.beginPath();
    for (x = off - major; x < w; x += major) { c.moveTo(x + 0.5, 0); c.lineTo(x + 0.5, h); }
    for (y = off - major; y < h; y += major) { c.moveTo(0, y + 0.5); c.lineTo(w, y + 0.5); }
    c.stroke();

    // guias de construção
    var rot = t * 0.00004;
    c.save();
    c.setLineDash([4, 7]);
    c.strokeStyle = dark ? 'rgba(239,80,35,.22)' : 'rgba(239,80,35,.16)';
    c.beginPath(); c.arc(w * 0.8, h * 0.28, Math.min(w, h) * 0.34, rot, rot + Math.PI * 1.35); c.stroke();
    c.beginPath(); c.moveTo(0, h * 0.86); c.lineTo(w, h * 0.52); c.stroke();
    c.setLineDash([]);
    c.strokeStyle = 'rgba(' + ink + ',' + (dark ? 0.12 : 0.08) + ')';
    c.beginPath(); c.moveTo(w * 0.62, 0); c.lineTo(w * 0.62, h); c.stroke();
    c.restore();

    // cruzes de marcação intermitentes
    for (var i = 0; i < this.crosses.length; i++) {
      var k = this.crosses[i];
      var a = Math.pow(Math.max(0, Math.sin(t * 0.001 * k.sp + k.ph)), 3);
      if (a < 0.02) continue;
      var cx = ((k.gx * major / 2 + off) % (w + major)) - major / 4, cy = ((k.gy * major / 2 + off) % (h + major)) - major / 4;
      if (dark && cx < w * 0.52 && w > 900) continue; // não cruzar o texto
      c.strokeStyle = k.hot ? 'rgba(239,80,35,' + (a * 0.75).toFixed(3) + ')' : 'rgba(' + ink + ',' + (a * (dark ? 0.5 : 0.35)).toFixed(3) + ')';
      c.beginPath(); c.moveTo(cx - 5, cy); c.lineTo(cx + 5, cy); c.moveTo(cx, cy - 5); c.lineTo(cx, cy + 5); c.stroke();
    }

    // passagem sutil de luz
    var band = 280, pos = ((t * 0.00006) % 1.6 - 0.3) * (w + band);
    var g = c.createLinearGradient(pos - band, 0, pos + band, 0);
    var lum = dark ? '255,255,255' : '239,80,35';
    g.addColorStop(0, 'rgba(' + lum + ',0)'); g.addColorStop(0.5, 'rgba(' + lum + ',' + (dark ? 0.035 : 0.025) + ')'); g.addColorStop(1, 'rgba(' + lum + ',0)');
    c.fillStyle = g; c.fillRect(pos - band, 0, band * 2, h);
  };

  var canvases = $$('canvas[data-canvas]').map(function (cv) { return new TechCanvas(cv); });

  var raf = 0, last = 0;
  function loop(t) {
    raf = requestAnimationFrame(loop);
    if (t - last < 33) return; // ~30 fps
    last = t;
    canvases.forEach(function (cv) { if (cv.visible) cv.draw(t); });
  }
  function startCanvas() { if (!raf && on && !document.hidden && canvases.length) raf = requestAnimationFrame(loop); }
  function stopCanvas() { if (raf) cancelAnimationFrame(raf); raf = 0; }
  function drawStatic() { canvases.forEach(function (cv) { cv.draw(4000); }); }

  if (hasIO) {
    var cvIO = new IntersectionObserver(function (es) {
      es.forEach(function (e) { canvases.forEach(function (cv) { if (cv.cv === e.target) cv.visible = e.isIntersecting; }); });
    });
    canvases.forEach(function (cv) { cvIO.observe(cv.cv); });
  } else canvases.forEach(function (cv) { cv.visible = true; });
  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function (es) {
      es.forEach(function (e) { canvases.forEach(function (cv) { if (cv.cv === e.target) { cv.resize(); if (!on) cv.draw(4000); } }); });
      requestUpdate();
    });
    canvases.forEach(function (cv) { ro.observe(cv.cv); });
  }
  document.addEventListener('visibilitychange', function () { if (document.hidden) stopCanvas(); else startCanvas(); });

  /* ---------- início ---------- */
  updateToggle();
  if (on) { startCanvas(); requestUpdate(); } else drawStatic();
  window.DrysulMotion = { refresh: observeReveals, isOn: function () { return on; } };
})();
