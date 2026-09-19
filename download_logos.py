import os
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

brands = {
    "Ray-Ban": "https://upload.wikimedia.org/wikipedia/commons/1/14/Ray-Ban_logo.svg",
    "Vogue": "https://upload.wikimedia.org/wikipedia/commons/8/87/Vogue_logo.svg",
    "Emporio Armani": "https://upload.wikimedia.org/wikipedia/commons/2/23/Emporio_Armani_logo.svg",
    "Armani Exchange": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Armani_Exchange_logo.svg",
    "Miu Miu": "https://upload.wikimedia.org/wikipedia/commons/8/82/Miu_Miu_logo.svg",
    "Prada": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Prada-Logo.svg",
    "Oakley": "https://upload.wikimedia.org/wikipedia/commons/5/52/Oakley_logo.svg",
    "Tom Ford": "https://upload.wikimedia.org/wikipedia/commons/7/76/Tom_Ford_logo.svg",
    "Lee Cooper": "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Lee_Cooper_Logo.svg/500px-Lee_Cooper_Logo.svg.png",
    "Zeiss": "https://upload.wikimedia.org/wikipedia/commons/1/16/Carl_Zeiss_AG_logo.svg",
    "Seiko": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Seiko_logo.svg",
    "Hoya": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Hoya_Corporation_logo.svg",
    "Essilor": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Essilor_logo.svg/500px-Essilor_logo.svg.png",
    "Michael Kors": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Michael_Kors_Logo.svg/500px-Michael_Kors_Logo.svg.png",
    "Marius Morel": "https://morel-france.com/cdn/shop/files/LOGO_MOREL.svg",
    "Rachael": "",
    "Morlin Bron": ""
}

os.makedirs('/Users/farukcetiner/Desktop/code/hasanOptik/src/assets/brands', exist_ok=True)
# wait, actually we can just create a mapping dictionary and put it directly into the HTML to load from external URLs.
# But downloading them makes it robust.

success = {}
for name, url in brands.items():
    if not url:
        success[name] = False
        continue
        
    filename = name.lower().replace(' ', '_').replace('-', '_')
    ext = ".png" if ".png" in url else ".svg"
    filepath = f'/Users/farukcetiner/Desktop/code/hasanOptik/public/brands/{filename}{ext}'
    os.makedirs('/Users/farukcetiner/Desktop/code/hasanOptik/public/brands', exist_ok=True)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        success[name] = f'/brands/{filename}{ext}'
        print(f"Downloaded: {name}")
    except Exception as e:
        print(f"Failed to download {name} from {url}: {e}")
        success[name] = False

print(success)
