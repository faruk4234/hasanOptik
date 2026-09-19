domain_map = {
    "Ray-Ban": "ray-ban.com",
    "Vogue": "vogue-eyewear.com",
    "Emporio Armani": "armani.com",
    "Armani Exchange": "armaniexchange.com",
    "Miu Miu": "miumiu.com",
    "Prada": "prada.com",
    "Oakley": "oakley.com",
    "Tom Ford": "tomford.com",
    "Lee Cooper": "leecooper.com",
    "Zeiss": "zeiss.com",
    "Seiko": "seikowatches.com",
    "Hoya": "hoya.com",
    "Essilor": "essilor.com",
    "Michael Kors": "michaelkors.com",
    "Marius Morel": "morel-france.com",
    "Rachael": "rachaellondon.com",
    "Morlin Bron": "morlinbron.com"
}

def generate_grid(brand_list):
    html = '<div class="brands-grid">\n'
    for brand in brand_list:
        domain = domain_map.get(brand, "unknown.com")
        html += f'          <div class="brand-cell"><img src="https://logo.clearbit.com/{domain}" alt="{brand}" onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'block\';"><span class="brand-name" style="display: none;">{brand}</span></div>\n'
    html += '        </div>'
    return html

brands_gunes = ["Ray-Ban", "Vogue", "Emporio Armani", "Armani Exchange", "Miu Miu", "Prada", "Oakley", "Tom Ford", "Lee Cooper", "Rachael"]
brands_cam = ["Zeiss", "Seiko", "Hoya", "Essilor"]
brands_optik = ["Ray-Ban", "Vogue", "Michael Kors", "Emporio Armani", "Morlin Bron", "Marius Morel", "Lee Cooper", "Armani Exchange"]
top_brands = ["Ray-Ban", "Prada", "Tom Ford", "Zeiss", "Oakley", "Michael Kors", "Miu Miu", "Seiko", "Emporio Armani", "Vogue", "Essilor", "Lee Cooper"]

import re

# 1. Update index.html
with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'r') as f:
    html = f.read()

index_grid = f'<div class="brands-grid-container">\n        {generate_grid(top_brands)}\n      </div>'
html = re.sub(r'<div class="brands-grid-container">.*?</div>\n      </div>', index_grid, html, flags=re.DOTALL)

with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'w') as f:
    f.write(html)

# 2. Update markalar.html
with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'r') as f:
    html = f.read()

new_content = f'''
      <div class="brands-category">
        <h3 class="category-title">Güneş & Moda Markaları</h3>
        <div class="brands-grid-container">
          {generate_grid(brands_gunes)}
        </div>
      </div>
      
      <div class="brands-category" style="margin-top: 50px;">
        <h3 class="category-title">Cam Markaları</h3>
        <div class="brands-grid-container">
          {generate_grid(brands_cam)}
        </div>
      </div>

      <div class="brands-category" style="margin-top: 50px;">
        <h3 class="category-title">Optik Markaları</h3>
        <div class="brands-grid-container">
          {generate_grid(brands_optik)}
        </div>
      </div>
'''

# Replace everything between <div class="container"> and </div>\n    </div>\n  </section> in markalar.html
header = html.split('<section id="brands" class="brands section bg-light"')[0]
brands_section_start = '<section id="brands" class="brands section bg-light" class="brands-page-section">'
if 'class="brands-page-section"' not in html:
    brands_section_start = '<section id="brands" class="brands section bg-light brands-page-section">'
    
footer = html.split('<!-- Pre-footer Banner -->')[1]

final_html = header + f'''
  <section id="brands" class="brands section bg-light brands-page-section">
    <div class="container">
      <div class="section-header">
        <h2>Seçkin Markalar</h2>
      </div>
      {new_content}
    </div>
  </section>

  <!-- Pre-footer Banner -->
''' + footer

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'w') as f:
    f.write(final_html)

print("Done")
