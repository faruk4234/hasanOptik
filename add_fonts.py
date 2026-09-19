import re

files = ['/Users/farukcetiner/Desktop/code/hasanOptik/index.html', '/Users/farukcetiner/Desktop/code/hasanOptik/markalar.html']

fonts = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">\n'

for path in files:
    with open(path, 'r') as f:
        html = f.read()
    
    html = html.replace('</head>', fonts + '</head>')
    
    with open(path, 'w') as f:
        f.write(html)

print("Fonts added.")
