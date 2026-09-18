import './style.css';

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth'
      });
      // Update active class
      document.querySelectorAll('.nav-links a').forEach(link => link.classList.remove('active'));
      this.classList.add('active');
    }
  });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.style.boxShadow = '0 2px 15px rgba(0,0,0,0.1)';
  } else {
    navbar.style.boxShadow = '0 2px 15px rgba(0,0,0,0.05)';
  }
});

// Mobile Swiper Initialization
let swiperInstances = [];

function initMobileSwipers() {
  const isMobile = window.innerWidth <= 768;
  const swiperContainers = document.querySelectorAll('.mobile-swiper');
  
  if (isMobile && swiperInstances.length === 0) {
    swiperContainers.forEach(container => {
      const swiper = new Swiper(container, {
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 1.5,
        spaceBetween: 20,
        autoplay: {
          delay: 3000,
          disableOnInteraction: false,
        },
        pagination: {
          el: container.querySelector('.swiper-pagination'),
          clickable: true,
        },
        loop: true
      });
      swiperInstances.push(swiper);
    });
  } else if (!isMobile && swiperInstances.length > 0) {
    swiperInstances.forEach(swiper => swiper.destroy(true, true));
    swiperInstances = [];
  }
}

window.addEventListener('load', initMobileSwipers);
window.addEventListener('resize', initMobileSwipers);
