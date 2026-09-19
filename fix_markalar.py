import re

# 1. Update markalar.html to include floating back button and fix padding
with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'r') as f:
    html = f.read()

# Add floating back button right after <body>
back_btn = '  <a href="index.html" class="floating-back-btn"><i class="fa-solid fa-arrow-left"></i> Ana Sayfaya Dön</a>\n'
html = html.replace('<body>\n', '<body>\n' + back_btn)

# Remove the inline style padding-top: 150px and replace with a class
html = html.replace('style="padding-top: 150px; min-height: 80vh;"', 'class="brands-page-section"')

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'w') as f:
    f.write(html)

# 2. Update style.css
with open('/Users/farukcetiner/Desktop/code/hasanOptik/style.css', 'r') as f:
    css = f.read()

# Add CSS for floating-back-btn and brands-page-section
new_css = '''
/* Markalar Page Specific */
.brands-page-section {
  padding-top: 120px;
  min-height: 100vh;
}

.floating-back-btn {
  display: none;
  position: fixed;
  top: 20px;
  left: 20px;
  background: var(--accent);
  color: var(--white);
  padding: 12px 24px;
  border-radius: 30px;
  z-index: 9999;
  text-decoration: none;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  align-items: center;
  gap: 10px;
}

@media (max-width: 768px) {
  .brands-page-section {
    padding-top: 80px !important;
  }
  .floating-back-btn {
    display: flex;
  }
}
'''
css += new_css

with open('/Users/farukcetiner/Desktop/code/hasanOptik/style.css', 'w') as f:
    f.write(css)

print("Fixed markalar.html and style.css")
