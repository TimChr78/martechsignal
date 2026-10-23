// Apply a stored theme choice before first paint so there is no flash.
// The OS preference needs no script: style.css handles it via prefers-color-scheme.
(function () {
  try {
    var t = localStorage.getItem('ms-theme');
    if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
  } catch (e) {}
})();
