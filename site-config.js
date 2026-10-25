// Retain the dependency-free feature-switch pattern used by arpitsidana.com.
window.SITE_FEATURES = Object.freeze({});
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-feature]').forEach((element) => {
    element.hidden = !window.SITE_FEATURES[element.dataset.feature];
  });
});
