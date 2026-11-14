/* =============================================
   OLIVE'S SPACE — home.js
   ============================================= */

/* ---- Carousel ---- */
const track = document.getElementById('carouselTrack');
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.dot');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let current = 0;
let autoTimer = null;

function goTo(index) {
  slides[current].classList.remove('active');
  dots[current].classList.remove('active');
  current = (index + slides.length) % slides.length;
  slides[current].classList.add('active');
  dots[current].classList.add('active');
  track.style.transform = `translateX(-${current * 100}%)`;
}

function startAuto() {
  autoTimer = setInterval(() => goTo(current + 1), 5500);
}
function stopAuto() {
  clearInterval(autoTimer);
}

// Init
slides[0].classList.add('active');
startAuto();

prevBtn.addEventListener('click', () => { stopAuto(); goTo(current - 1); startAuto(); });
nextBtn.addEventListener('click', () => { stopAuto(); goTo(current + 1); startAuto(); });
dots.forEach(dot => {
  dot.addEventListener('click', () => {
    stopAuto();
    goTo(parseInt(dot.dataset.index));
    startAuto();
  });
});

// Touch/swipe support
let touchStartX = 0;
const carousel = document.getElementById('carousel');
carousel.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
carousel.addEventListener('touchend', e => {
  const diff = touchStartX - e.changedTouches[0].clientX;
  if (Math.abs(diff) > 50) {
    stopAuto();
    goTo(diff > 0 ? current + 1 : current - 1);
    startAuto();
  }
});
