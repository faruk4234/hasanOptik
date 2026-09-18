const fs = require('fs');

// INDEX.HTML
let html = fs.readFileSync('index.html', 'utf8');

if (!html.includes('mobile-swiper">\n        <div class="swiper-wrapper hizmet-grid">')) {
  html = html.replace('<div class="hizmet-grid">', '<div class="swiper mobile-swiper">\n        <div class="swiper-wrapper hizmet-grid">');
  html = html.replace(/class="hizmet-item"/g, 'class="swiper-slide hizmet-item"');
  html = html.replace(/<\/div>\n    <\/div>\n  <\/section>\n\n  <!-- Why Choose Us Section -->/, '</div>\n        <div class="swiper-pagination"></div>\n      </div>\n    </div>\n  </section>\n\n  <!-- Why Choose Us Section -->');
}

if (!html.includes('mobile-swiper">\n        <div class="swiper-wrapper features-grid">')) {
  html = html.replace('<div class="features-grid">', '<div class="swiper mobile-swiper">\n        <div class="swiper-wrapper features-grid">');
  html = html.replace(/class="feature-card"/g, 'class="swiper-slide feature-card"');
  html = html.replace(/<\/div>\n    <\/div>\n  <\/section>\n\n  <!-- Reviews Section -->/, '</div>\n        <div class="swiper-pagination"></div>\n      </div>\n    </div>\n  </section>\n\n  <!-- Reviews Section -->');
}

if (!html.includes('mobile-swiper">\n        <div class="swiper-wrapper review-grid">')) {
  html = html.replace('<div class="review-grid">', '<div class="swiper mobile-swiper">\n        <div class="swiper-wrapper review-grid">');
  html = html.replace(/class="review-card"/g, 'class="swiper-slide review-card"');
  html = html.replace(/<\/div>\n      <div style="text-align: center; margin-top: 40px;">/, '</div>\n        <div class="swiper-pagination"></div>\n      </div>\n      <div style="text-align: center; margin-top: 40px;">');
}

if (!html.includes('swiper-bundle.min.css')) {
  html = html.replace('</head>', '  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n</head>');
}
if (!html.includes('swiper-bundle.min.js')) {
  html = html.replace('<script type="module" src="/main.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n  <script type="module" src="/main.js"></script>');
}
fs.writeFileSync('index.html', html);

// MAIN.JS
let js = fs.readFileSync('main.js', 'utf8');
const swiperJs = `
// Mobile Swiper Initialization
let swiperInstances = [];

function initMobileSwipers() {
  const isMobile = window.innerWidth <= 768;
  const swiperContainers = document.querySelectorAll('.mobile-swiper');
  
  if (isMobile && swiperInstances.length === 0) {
    swiperContainers.forEach(container => {
      const swiper = new Swiper(container, {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
          rotate: 0,
          stretch: 0,
          depth: 150,
          modifier: 1.5,
          slideShadows: false,
        },
        autoplay: {
          delay: 3000,
          disableOnInteraction: false,
        },
        pagination: {
          el: container.querySelector('.swiper-pagination'),
          clickable: true,
        },
        loop: true,
        initialSlide: 1
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
`;
if (!js.includes('initMobileSwipers')) {
  fs.appendFileSync('main.js', swiperJs);
}

// STYLE.CSS
let css = fs.readFileSync('style.css', 'utf8');
const swiperCss = `
@media (min-width: 769px) {
  .mobile-swiper { overflow: visible !important; }
  .mobile-swiper .swiper-wrapper { display: grid !important; transform: none !important; }
  .mobile-swiper .swiper-slide { width: auto !important; margin-right: 0 !important; }
  .swiper-pagination { display: none !important; }
}

@media (max-width: 768px) {
  .navbar { display: none !important; }
  .hero { padding-top: 0 !important; }
  
  .mobile-swiper {
    padding-bottom: 50px !important; /* Space for dots */
    width: 100%;
    overflow: hidden;
  }
  .mobile-swiper .swiper-slide {
    width: 75% !important; /* Forces 1 center slide and pieces of adjacent slides */
    height: auto !important;
    opacity: 0.5; /* Dim non-active slides slightly */
    transition: opacity 0.3s ease;
  }
  .mobile-swiper .swiper-slide-active {
    opacity: 1; /* Highlight active center slide */
  }
  
  .swiper-pagination {
    bottom: 10px !important;
  }
  .swiper-pagination-bullet {
    background: #000000 !important;
    opacity: 0.3 !important;
    width: 10px !important;
    height: 10px !important;
    margin: 0 5px !important;
  }
  .swiper-pagination-bullet-active {
    background: #000000 !important;
    opacity: 1 !important;
  }

  /* Optimize card paddings for mobile */
  .hizmet-item, .feature-card, .review-card {
    padding: 20px !important;
    text-align: center;
    border: 1px solid rgba(0,0,0,0.05);
    background: var(--white);
    border-radius: var(--border-radius);
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
  }
  .review-header { flex-direction: column; align-items: center; gap: 10px; }
}
`;
if (!css.includes('/* Space for dots */')) {
  fs.appendFileSync('style.css', swiperCss);
}

console.log("All updates applied perfectly.");
