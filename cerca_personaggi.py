#!/usr/bin/env python3
"""
Script per cercare personaggi e immagini per i cartoni animati del Gruppo 1.
"""

import json
import re
import urllib.request
import urllib.parse
from html import unescape

# Lista dei cartoni dal file QWEN_gruppo_01.md
cartoni = [
    {"id": "antologia-di-supergulp", "title": "Antologia di Supergulp!", "genre": "Altro", "year": 1972},
    {"id": "fantasupermega", "title": "Fantasupermega", "genre": "Altro", "year": 1980},
    {"id": "una-porta-socchiusa-ai-confini-del-sole", "title": "Una porta socchiusa ai confini del sole", "genre": "Altro", "year": 1994},
    {"id": "la-canzone-di-charlotte", "title": "la canzone di charlotte", "genre": "Altro", "year": 1985},
    {"id": "fantazoo", "title": "Fantazoo", "genre": "Animali", "year": 1987},
    {"id": "marsupilami", "title": "Marsupilami", "genre": "Animali", "year": 1993},
    {"id": "80-sogni-per-viaggiare", "title": "80 sogni per viaggiare", "genre": "Avventura", "year": 1992},
    {"id": "all-arrembaggio-sandokan", "title": "All'arrembaggio Sandokan", "genre": "Avventura", "year": 1992},
    {"id": "belle-e-sebastien", "title": "Belle e Sebastien", "genre": "Avventura", "year": 1980},
    {"id": "caccia-al-tesoro-con-montana", "title": "Caccia al tesoro con Montana", "genre": "Avventura", "year": 1994},
    {"id": "coccinella", "title": "Coccinella", "genre": "Avventura", "year": 1974},
    {"id": "col-vento-in-poppa-verso-l-avventura", "title": "Col vento in poppa verso l'avventura", "genre": "Avventura", "year": 1986},
    {"id": "com-e-grande-l-america", "title": "Com'e' grande l'America", "genre": "Avventura", "year": 1989},
    {"id": "d-artacan-e-i-tre-moschettieri", "title": "D'Artacan e i tre moschettieri", "genre": "Avventura", "year": 1982},
    {"id": "d-artagnan-e-i-moschettieri-del-re", "title": "D'Artagnan e i Moschettieri del Re", "genre": "Avventura", "year": 1989},
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
        # Look for first result link
        match = re.search(r'href="([^"]+/anime/\d+/[^"]+)"', html)
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
    # Parse character entries
    # Pattern for character links and images
    char_pattern = r'<a href="https://myanimelist\.net/character/(\d+)/([^"]+)" class="fw-n">.*?<img alt="[^"]*" data-src="([^"]+)"'
    
    for match in re.finditer(char_pattern, html, re.DOTALL):
        char_id = match.group(1)
        char_name = unescape(match.group(2)).replace('_', ' ')
        img_url = match.group(3)
        
        # Get full size image URL
        full_img = img_url.replace('/r/42x62/', '/r/225x350/').replace('?s=', '?s=')
        
        characters.append({
            'nome': char_name,
            'url_img_small': img_url,
            'url_img_large': full_img
        })
    
    return characters

def get_character_page_url(mal_url):
    """Get the character page URL from the name."""
    return mal_url

def get_best_image_url(char_name, anime_title):
    """Try to find best image URL for a character from various sources."""
    # Try AniList API
    try:
        query = f'''
        query {{
          Character(page: 1, perPage: 5, search: "{char_name.replace('"', '\\"')}") {{
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
        print(f"AniList error: {e}")
    
    return None

# Main execution
print("Starting character search for Gruppo 01...")
print("=" * 60)

results = {}

for cartone in cartoni:
    cid = cartone['id']
    title = cartone['title']
    print(f"\nProcessing: {title} ({cid})")
    
    # Search on MAL
    mal_url = search_mal_anime(title)
    if mal_url:
        print(f"  Found MAL URL: {mal_url}")
        characters = get_mal_characters(mal_url)
        print(f"  Found {len(characters)} characters")
        
        if characters:
            personaggi = []
            for char in characters[:20]:  # Limit to 20 characters per show
                # Try to get better image
                img_url = get_best_image_url(char['nome'], title)
                if not img_url:
                    # Use MAL image but get larger version
                    img_url = char['url_img_large'].replace('/r/42x62/', '/r/225x350/')
                
                # Verify image URL
                if verify_image_url(img_url):
                    personaggi.append({
                        'nome': char['nome'],
                        'url': img_url
                    })
                else:
                    # Try original small image
                    if verify_image_url(char['url_img_small']):
                        personaggi.append({
                            'nome': char['nome'],
                            'url': char['url_img_small']
                        })
            
            if personaggi:
                results[cid] = {
                    'title': title,
                    'personaggi': personaggi
                }
                print(f"  Successfully added {len(personaggi)} characters with verified images")
    else:
        print(f"  No MAL URL found for: {title}")

print("\n" + "=" * 60)
print("Final results:")
print(json.dumps(results, indent=2, ensure_ascii=False))
