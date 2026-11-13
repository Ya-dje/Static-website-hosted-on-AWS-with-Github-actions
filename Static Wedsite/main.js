/* =============================================
   OLIVE'S SPACE — main.js (shared)
   ============================================= */

/* ---- Navbar scroll shadow ---- */
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 10) navbar.classList.add('scrolled');
  else navbar.classList.remove('scrolled');
});

/* ---- Hamburger Menu ---- */
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
const menuOverlay = document.getElementById('menuOverlay');

function openMenu() {
  hamburger.classList.add('open');
  mobileMenu.classList.add('open');
  menuOverlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeMenu() {
  hamburger.classList.remove('open');
  mobileMenu.classList.remove('open');
  menuOverlay.classList.remove('open');
  document.body.style.overflow = '';
}

hamburger.addEventListener('click', () => {
  mobileMenu.classList.contains('open') ? closeMenu() : openMenu();
});
menuOverlay.addEventListener('click', closeMenu);

// Close menu when a link is tapped
mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', closeMenu);
});

/* ---- Fade-in on scroll ---- */
const fadeEls = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, 80 * (entry.target.dataset.delay || 0));
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

fadeEls.forEach((el, i) => {
  el.dataset.delay = i % 4;
  observer.observe(el);
});
