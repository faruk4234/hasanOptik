import re

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'r') as f:
    content = f.read()

# Fix logo link
content = content.replace('href="#" class="logo"', 'href="index.html" class="logo"')

# Fix navbar and footer links
content = content.replace('href="#home"', 'href="index.html"')
content = content.replace('href="#hizmetlerimiz"', 'href="index.html#hizmetlerimiz"')
content = content.replace('href="#contact"', 'href="index.html#contact"')

with open('/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html', 'w') as f:
    f.write(content)

print("Links fixed.")
