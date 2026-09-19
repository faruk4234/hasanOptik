import re

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

brands_gunes = [
    "Ray-Ban", "Vogue", "Emporio Armani", "Armani Exchange", 
    "Miu Miu", "Prada", "Oakley", "Tom Ford", "Lee Cooper", "Rachael"
]

brands_cam = [
    "Zeiss", "Seiko", "Hoya", "Essilor"
]

brands_optik = [
    "Ray-Ban", "Vogue", "Michael Kors", "Emporio Armani", 
    "Morlin Bron", "Marius Morel", "Lee Cooper", "Armani Exchange"
]

top_brands = ["Ray-Ban", "Prada", "Tom Ford", "Zeiss", "Oakley", "Michael Kors", "Miu Miu", "Seiko", "Emporio Armani", "Vogue", "Essilor", "Lee Cooper"]

def generate_grid(brand_list):
    html = '<div class="brands-grid">\n'
    for brand in brand_list:
        domain = domain_map.get(brand, "unknown.com")
        img_tag = f'<img src="https://logo.clearbit.com/{domain}" alt="{brand}" onerror="this.style.display=\\\'none\\\'; this.nextElementSibling.style.display=\\\'block\\\';">'
        html += f'          <div class="brand-cell">{img_tag}<span class="brand-name" style="display: none;">{brand}</span></div>\n'
    html += '        </div>'
    return html

# 1. Update markalar.html
with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'r') as f:
    markalar_html = f.read()

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

markalar_html = re.sub(r'<div class="brands-category">.*</div>\n      </div>\n      </div>', new_content.strip(), markalar_html, flags=re.DOTALL)

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'w') as f:
    f.write(markalar_html)


# 2. Update index.html
with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'r') as f:
    index_html = f.read()

index_grid = f'''<div class="brands-grid-container">
        {generate_grid(top_brands)}
      </div>'''

index_html = re.sub(r'<div class="brands-grid-container">.*?</div>\n      </div>', index_grid, index_html, flags=re.DOTALL)

with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'w') as f:
    f.write(index_html)

print("Added Clearbit logos with text fallbacks.")
