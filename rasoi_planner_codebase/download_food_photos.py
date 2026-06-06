import os
import urllib.request

# Unsplash image references for realistic food plates
FOOD_PHOTO_URLS = {
    "poha": "https://images.unsplash.com/photo-1601050690597-df056fb49785?w=450&q=80",
    "dosa": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=450&q=80",
    "paratha": "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=450&q=80",
    "chilla": "https://images.unsplash.com/photo-1626132647523-66f5bf380027?w=450&q=80",
    "dal_rice": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=450&q=80",
    "paneer": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=450&q=80",
    "chole": "https://images.unsplash.com/photo-1626509653299-0e12322daebe?w=450&q=80",
    "rajma": "https://images.unsplash.com/photo-1585857188823-7762857c093a?w=450&q=80",
    "chicken": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=450&q=80",
    "bhindi": "https://images.unsplash.com/photo-1601303589827-8f55e4e70ac9?w=450&q=80",
    "palak_paneer": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=450&q=80",
    "egg_curry": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=450&q=80",
    "khichdi": "https://images.unsplash.com/photo-1605888969139-42cca532b26b?w=450&q=80",
    "veg_diet": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400&q=80",
    "vegan_diet": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&q=80"
}

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "frontend", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    for name, url in FOOD_PHOTO_URLS.items():
        filepath = os.path.join(assets_dir, f"{name}.png")
        print(f"Downloading real food image for {name}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                with open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
            print(f"Saved to {filepath}")
        except Exception as e:
            print(f"Error downloading {name}: {e}")

if __name__ == "__main__":
    main()
