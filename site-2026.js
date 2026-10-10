/* Shared core-page navigation. Form delivery remains in contact.html. */
(() => {
  const toggle = document.getElementById('mobileToggle');
  const links = document.getElementById('navLinks');
  if (!toggle || !links) return;
  function closeMenu(returnFocus = false) {
    links.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    if (returnFocus) toggle.focus();
  }
  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  links.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && links.classList.contains('open')) closeMenu(true);
  });
  window.matchMedia('(min-width: 1121px)').addEventListener('change', event => {
    if (event.matches) closeMenu();
  });
})();
