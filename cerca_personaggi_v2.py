#!/usr/bin/env python3
"""
Script per cercare personaggi e immagini per i cartoni animati del Gruppo 1.
Usa titoli inglesi/originali corretti per MyAnimeList.
"""

import json
import re
import urllib.request
import urllib.parse
from html import unescape

# Mappatura dei titoli italiani a titoli MAL corretti
cartoni_mapping = [
    {"id": "antologia-di-supergulp", "title": "Antologia di Supergulp!", "mal_title": "Super GALS! Kotobuki Ran"},
    {"id": "fantasupermega", "title": "Fantasupermega", "mal_title": None},  # Live action italiano
    {"id": "una-porta-socchiusa-ai-confini-del-sole", "title": "Una porta socchiusa ai confini del sole", "mal_title": None},  # Film italiano
    {"id": "la-canzone-di-charlotte", "title": "la canzone di charlotte", "mal_title": None},  # Film italiano
    {"id": "fantazoo", "title": "Fantazoo", "mal_title": None},  # Cartone italiano
    {"id": "marsupilami", "title": "Marsupilami", "mal_title": "Marsupilami (1993)"},
    {"id": "80-sogni-per-viaggiare", "title": "80 sogni per viaggiare", "mal_title": "Around the World with Willy Fog"},
    {"id": "all-arrembaggio-sandokan", "title": "All'arrembaggio Sandokan", "mal_title": "Sandokan, la tigre di Mompracem"},
    {"id": "belle-e-sebastien", "title": "Belle e Sebastien", "mal_title": "Meiken Lassie"},
    {"id": "caccia-al-tesoro-con-montana", "title": "Caccia al tesoro con Montana", "mal_title": "Montana Jones"},
    {"id": "coccinella", "title": "Coccinella", "mal_title": "Ladybug"},
    {"id": "col-vento-in-poppa-verso-l-avventura", "title": "Col vento in poppa verso l'avventura", "mal_title": "Tatoeba Last Dungeon Mae no Musume ga Shijou Ichi no Newcomer Datta"},
    {"id": "com-e-grande-l-america", "title": "Com'e' grande l'America", "mal_title": "Ahiru no Quack"},
    {"id": "d-artacan-e-i-tre-moschettieri", "title": "D'Artacan e i tre moschettieri", "mal_title": "Wan Wan Sanjuushi: D'Artacan to Musketeers"},
    {"id": "d-artagnan-e-i-moschettieri-del-re", "title": "D'Artagnan e i Moschettieri del Re", "mal_title": "Anime Sanjuushi: D'Artagnan to Rapide Kishi"},
]

def fetch_url(url, headers=None):
    """Fetch URL content with error handling."""
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def verify_image_url(url):
    """Verify that URL returns an image (HTTP 200 and content-type is image)."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }
        req = urllib.request.Request(url, headers=headers, method='HEAD')
        with urllib.request.urlopen(req, timeout=10) as response:
            content_type = response.headers.get('Content-Type', '')
            return response.status == 200 and 'image' in content_type
    except:
        return False

def search_mal_anime(title):
    """Search for anime on MyAnimeList and return the anime URL."""
    query = urllib.parse.quote(title)
    url = f"https://myanimelist.net/anime.php?q={query}"
    html = fetch_url(url)
    if html:
        # Look for first result link - more specific pattern
        match = re.search(r'href="([^"]+/anime/\d+/[^"]+)"[^>]*>\s*<img[^>]*alt="[^"]*"', html)
        if match:
            return match.group(1)
        # Alternative pattern
        match = re.search(r'<a href="([^"]+/anime/\d+/[^"]+)"[^>]*>', html)
        if match:
            return match.group(1)
    return None

def get_mal_characters(anime_url):
    """Get characters from MAL anime page."""
    if not anime_url:
        return []
    
    # Build characters URL
    if '/characters' not in anime_url:
        chars_url = anime_url.rstrip('/') + '/characters'
    else:
        chars_url = anime_url
    
    html = fetch_url(chars_url)
    if not html:
        return []
    
    characters = []
    # Parse character entries - look for character table rows
    # Pattern: character link followed by image
    char_pattern = r'<a href="https://myanimelist\.net/character/(\d+)/([^"]+)"[^>]*>\s*<img[^>]*data-src="([^"]+)"'
    
    for match in re.finditer(char_pattern, html, re.DOTALL | re.IGNORECASE):
        char_id = match.group(1)
        char_name = unescape(match.group(2)).replace('_', ' ')
        img_url = match.group(3)
        
        characters.append({
            'nome': char_name,
            'url_img': img_url
        })
    
    return characters

def get_anilist_character_image(char_name):
    """Try to get character image from AniList API."""
    try:
        query = f'''
        query {{
          Character(page: 1, perPage: 3, search: "{char_name.replace('"', '\\"')}") {{
            id
            name {{
              full
            }}
            image {{
              large
            }}
          }}
        }}
        '''
        req = urllib.request.Request(
            'https://graphql.anilist.co',
            data=json.dumps({'query': query}).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0'
            },
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get('data', {}).get('Character'):
                for char in data['data']['Character']:
                    if char.get('image', {}).get('large'):
                        return char['image']['large']
    except Exception as e:
        pass
    
    return None

# Main execution
print("Starting character search for Gruppo 01...")
print("=" * 60)

results = {}

for cartone in cartoni_mapping:
    cid = cartone['id']
    title = cartone['title']
    mal_title = cartone.get('mal_title')
    
    print(f"\nProcessing: {title} ({cid})")
    
    if not mal_title:
        print(f"  Skipping - no MAL mapping available (likely Italian production)")
        continue
    
    # Search on MAL with correct title
    mal_url = search_mal_anime(mal_title)
    if mal_url:
        print(f"  Found MAL URL: {mal_url}")
        characters = get_mal_characters(mal_url)
        print(f"  Found {len(characters)} characters")
        
        if characters:
            personaggi = []
            for char in characters[:20]:  # Limit to 20 characters per show
                # Try to get better image from AniList
                img_url = get_anilist_character_image(char['nome'])
                
                if not img_url or not verify_image_url(img_url):
                    # Use MAL image - convert to larger size
                    img_url = char['url_img'].replace('/r/42x62/', '/r/225x350/')
                
                # Verify image URL
                if verify_image_url(img_url):
                    personaggi.append({
                        'nome': char['nome'],
                        'url': img_url
                    })
                elif verify_image_url(char['url_img']):
                    personaggi.append({
                        'nome': char['nome'],
                        'url': char['url_img']
                    })
            
            if personaggi:
                results[cid] = {
                    'title': title,
                    'personaggi': personaggi
                }
                print(f"  Successfully added {len(personaggi)} characters with verified images")
    else:
        print(f"  No MAL URL found for: {mal_title}")

print("\n" + "=" * 60)
print("Final JSON result:")
print(json.dumps(results, indent=2, ensure_ascii=False))
