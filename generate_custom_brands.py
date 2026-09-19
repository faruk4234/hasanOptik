import re

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

def generate_grid(brand_list):
    html = '<div class="brands-grid">\n'
    for brand in brand_list:
        html += f'          <div class="brand-cell"><span class="brand-name">{brand}</span></div>\n'
    html += '        </div>'
    return html

# 1. Update markalar.html
with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'r') as f:
    markalar_html = f.read()

# We need to replace the entire brands-grid-container with the new categories
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

# Use regex to replace the old container
markalar_html = re.sub(r'<div class="brands-grid-container">.*?</div>\n      </div>', new_content.strip(), markalar_html, flags=re.DOTALL)

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'w') as f:
    f.write(markalar_html)


# 2. Update index.html
# For the homepage, let's just pick a mixed selection of top 12 brands
top_brands = ["Ray-Ban", "Prada", "Tom Ford", "Zeiss", "Oakley", "Michael Kors", "Miu Miu", "Seiko", "Emporio Armani", "Vogue", "Essilor", "Lee Cooper"]

with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'r') as f:
    index_html = f.read()

index_grid = f'''<div class="brands-grid-container">
        {generate_grid(top_brands)}
      </div>'''

index_html = re.sub(r'<div class="brands-grid-container">.*?</div>\n      </div>', index_grid, index_html, flags=re.DOTALL)

with open('/Users/farukcetiner/Desktop/code/hasanOptik/index.html', 'w') as f:
    f.write(index_html)


# 3. Update style.css to support typographic brand logos
with open('/Users/farukcetiner/Desktop/code/hasanOptik/style.css', 'r') as f:
    css = f.read()

new_css = '''
/* Typographic Brand Styles */
.brand-name {
  font-family: 'Cinzel', 'Montserrat', sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  color: #555;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-align: center;
  transition: all 0.3s ease;
}

.brand-cell:hover .brand-name {
  color: var(--primary);
  transform: scale(1.1);
}

.category-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 30px;
  color: var(--primary);
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.category-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 25%;
  width: 50%;
  height: 3px;
  background-color: var(--accent);
  border-radius: 2px;
}
'''
css += new_css

with open('/Users/farukcetiner/Desktop/code/hasanOptik/style.css', 'w') as f:
    f.write(css)

print("Updated brands successfully.")
