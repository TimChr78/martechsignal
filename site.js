// MartechSignal site.js (2026-09-27): the single first-party script.
// L4: the inline IIFEs moved here so the CSP can drop 'unsafe-inline'.
(function () {
  document.documentElement.classList.remove('no-js');
  document.documentElement.classList.add('js');
})();
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || reduced) {
    els.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
})();

// M10: directory filter (category / price model / licence). The bar is rendered
// hidden in the HTML: with JS off the full list simply stays visible and browsable.
(function () {
  var bar = document.getElementById('tool-filter');
  if (!bar) return;
  bar.hidden = false;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.tool-card[data-cat]'));
  var cat = document.getElementById('flt-cat'),
      price = document.getElementById('flt-price'),
      lic = document.getElementById('flt-licence'),
      count = document.getElementById('flt-count');
  function apply() {
    var n = 0;
    cards.forEach(function (c) {
      var ok = (!cat.value || c.getAttribute('data-cat') === cat.value) &&
               (!price.value || c.getAttribute('data-price') === price.value) &&
               (!lic.value || c.getAttribute('data-licence') === lic.value);
      c.classList.toggle('is-hidden', !ok);
      if (ok) n++;
    });
    document.querySelectorAll('.hub-group').forEach(function (g) {
      var any = g.querySelectorAll('.tool-card[data-cat]:not(.is-hidden)').length;
      g.classList.toggle('is-hidden', any === 0);
    });
    count.textContent = n + ' of ' + cards.length + ' tools shown';
  }
  [cat, price, lic].forEach(function (s) { s.addEventListener('change', apply); });
  apply();
})();

// r7 C7 (2026-09-27): checklist state is URL-serialisable (#q=<bitmask>).
(function () {
  var f = document.getElementById('checklist-form');
  if (!f) return;
  var boxes = [];
  for (var i = 1; i <= 12; i++) {
    var b = document.getElementById('q' + i);
    if (b) boxes.push(b);
  }
  function mask() {
    var m = 0;
    boxes.forEach(function (b, i) { if (b.checked) m |= (1 << i); });
    return m;
  }
  var m = /^#q=(\d+)/.exec(location.hash);
  if (m) {
    var bits = parseInt(m[1], 10);
    boxes.forEach(function (b, i) { b.checked = !!(bits & (1 << i)); });
  }
  boxes.forEach(function (b) {
    b.addEventListener('change', function () {
      history.replaceState(null, '', '#q=' + mask());
    });
  });
})();
