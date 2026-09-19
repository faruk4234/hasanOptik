import re
import os

with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'r') as f:
    html = f.read()

# Generate the 18 brands grid for homepage
homepage_grid = '<div class="brands-grid-container">\n        <div class="brands-grid">\n'
for i in range(1, 19):
    homepage_grid += f'          <div class="brand-cell"><img src="https://galaxyoptik.com/assets/img/markalar/{i}.png" alt="Brand {i}" loading="lazy"></div>\n'
homepage_grid += '        </div>\n      </div>'

# Replace the marquee in index.html
new_html = re.sub(r'<div class="logo-section">.*?</div>\n      </div>\n    </div>', homepage_grid + '\n    </div>', html, flags=re.DOTALL)
new_html = new_html.replace('href="https://galaxyoptik.com/markalar"', 'href="markalar.html"')

with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'w') as f:
    f.write(new_html)

# Generate markalar.html with 98 brands
markalar_html = html.replace('href="https://galaxyoptik.com/markalar"', 'href="markalar.html"')
full_grid = '<div class="brands-grid-container">\n        <div class="brands-grid">\n'
for i in range(1, 99):
    full_grid += f'          <div class="brand-cell"><img src="https://galaxyoptik.com/assets/img/markalar/{i}.png" alt="Brand {i}" loading="lazy"></div>\n'
full_grid += '        </div>\n      </div>'

# We also need to strip everything between <section id="home"... and <section id="brands"...
# Wait, it's easier to just strip sections from a copy of new_html.
# Let's remove hero, hizmetlerimiz, why-choose-us, reviews, contact, map from markalar.html
sections_to_remove = [
    r'<section id="home".*?</section>',
    r'<section id="hizmetlerimiz".*?</section>',
    r'<section class="why-choose-us.*?</section>',
    r'<section id="reviews".*?</section>',
    r'<section id="contact".*?</section>',
    r'<div class="map-container".*?</div>'
]

markalar_html = re.sub(r'<div class="logo-section">.*?</div>\n      </div>\n    </div>', full_grid + '\n    </div>', html, flags=re.DOTALL)
for section_regex in sections_to_remove:
    markalar_html = re.sub(section_regex, '', markalar_html, flags=re.DOTALL)

# Let's also change the title and nav in markalar.html
markalar_html = markalar_html.replace('href="#brands"', 'href="markalar.html"')
markalar_html = markalar_html.replace('<title>Merkezefendi Optik - Tarzınıza Uygun Gözlükler</title>', '<title>Markalar | Merkezefendi Optik</title>')
markalar_html = markalar_html.replace('href="https://galaxyoptik.com/markalar"', 'href="markalar.html"')
markalar_html = markalar_html.replace('class="link-btn">Tüm Markaları Gör <i class="fa-solid fa-arrow-right"></i></a>', '') # remove button on the full page

# Add some padding to the main section since it's the only one
markalar_html = markalar_html.replace('<section id="brands" class="brands section bg-light">', '<section id="brands" class="brands section bg-light" style="padding-top: 150px; min-height: 80vh;">')

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'w') as f:
    f.write(markalar_html)

print("Done generating markalar.html and updating index.html")
