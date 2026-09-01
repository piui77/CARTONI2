# COMPITO PER QWEN CODER — Cerca E Scarica personaggi da AnimeClick.it (25 cartoni)

Scrivi ed esegui uno script Python che cerca i personaggi di questi 25 cartoni animati **usando SOLO il sito animeclick.it** e **scarica fisicamente le immagini su disco**, nella cartella dove ti trovi (`immagini_personaggi/<Titolo Cartone>/<Nome Personaggio>.jpg`).

Non usare altre fonti (niente Fandom, Wikipedia, AniList, Wikidata) — solo animeclick.it. Sono tutti anime giapponesi, quindi il sito dovrebbe coprirli quasi tutti.

## Come funziona animeclick.it (metodo verificato)

### 1. Trova la scheda dell'anime
Ogni anime ha una pagina con questo formato: `https://www.animeclick.it/anime/<ID>/<slug>`. Per trovarla:
- Prova prima a cercare direttamente sul sito: `https://www.animeclick.it/cerca/anime?keyword=<titolo>` (se questo endpoint non funziona, prova a cercare su Google/Bing con `site:animeclick.it <titolo originale o italiano dell'anime>` e prendi il link che finisce in `/anime/<ID>/<slug>` — NON quelli che finiscono in `/manga/`, `/episodio/`, `/news/`).
- Se il titolo italiano non dà risultati, prova con il titolo originale giapponese/inglese dell'opera (spesso più efficace).
- **Attenzione alla pertinenza**: se trovi più risultati per titoli simili ma di anni/adattamenti diversi (es. una serie del 1980 e un remake del 2020), scegli quello dell'anno giusto per il nostro cartone. Se non sei sicuro di quale sia quello giusto, ometti il cartone.

### 2. Vai alla pagina dei personaggi
La pagina personaggi è sempre: `https://www.animeclick.it/anime/<ID>/<slug>/personaggi`

### 3. Estrai nome e immagine di ogni personaggio
Ogni personaggio nella lista ha:
- Un nome (es. "Parn", "Deedlit")
- Un'immagine thumbnail con URL in questo formato prevedibile:
  `https://www.animeclick.it/immagini/personaggio/<Nome_Con_Underscore>/cover/<ID_NUMERICO>-<Nome_Con_Underscore>-thumb.jpg`

Se un personaggio non ha immagine (a volte c'è scritto "foto non disponibile"), saltalo — non inventare un URL.

### 4. Scarica l'immagine
```python
import requests, os, time

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def scarica(url, cartella, nome_file):
    r = requests.get(url, headers=HEADERS, timeout=15, stream=True)
    ctype = r.headers.get('content-type', '')
    if r.status_code != 200 or 'image' not in ctype:
        return False
    os.makedirs(cartella, exist_ok=True)
    path = os.path.join(cartella, nome_file)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    if os.path.getsize(path) < 1000:  # troppo piccola, probabilmente rotta
        os.remove(path)
        return False
    return True
```
Aggiungi `time.sleep(0.3)` tra una richiesta e l'altra.

## REGOLA ANTI-INVENZIONE (fondamentale)
Ogni URL che scrivi nel codice deve venire da una pagina che hai DAVVERO recuperato e letto in questo momento (con una vera richiesta HTTP, non a memoria). Se non riesci a trovare la pagina personaggi di un anime, o non trovi immagini, ometti quel cartone — non inventare nomi di file o ID numerici a caso.

## Lista dei 25 cartoni da cercare su animeclick.it

```json
[
  {"id": "david-gnomo-amico-mio", "title": "David Gnomo amico mio", "year": 1985},
  {"id": "dolceluna", "title": "Dolceluna", "year": 1990},
  {"id": "doredo-doremi", "title": "Doredo Doremi", "year": 2001},
  {"id": "dr-slump-e-arale-the-movie-avventura-nello-spazio", "title": "Dr. Slump e Arale the Movie Avventura nello spazio", "year": 1982},
  {"id": "i-5-samurai", "title": "I 5 samurai", "year": 1988},
  {"id": "i-bon-bon-magici-di-lilly", "title": "I bon bon magici di Lilly", "year": 1971},
  {"id": "il-magico-mondo-di-gigi", "title": "Il magico mondo di Gigì", "year": 1982},
  {"id": "il-mago-pancione-etci", "title": "Il mago pancione Etcì", "year": 1969},
  {"id": "john-e-solfami", "title": "John e Solfami", "year": 1981},
  {"id": "koseidon", "title": "Koseidon", "year": 1978},
  {"id": "kum-kum", "title": "Kum Kum", "year": 1975},
  {"id": "l-isola-del-corallo", "title": "L'isola del corallo", "year": 1990},
  {"id": "la-balena-giuseppina-addio-giuseppina", "title": "La balena Giuseppina (Addio Giuseppina)", "year": 1979},
  {"id": "la-maga-chappy", "title": "La Maga Chappy", "year": 1972},
  {"id": "la-principessa-dai-capelli-blu", "title": "La principessa dai capelli blu", "year": 1986},
  {"id": "la-principessa-zaffiro", "title": "La principessa Zaffiro", "year": 1967},
  {"id": "la-spada-di-king-arthur", "title": "La spada di King Arthur", "year": 1979},
  {"id": "lady-lovely", "title": "Lady Lovely", "year": 1987},
  {"id": "le-magiche-ballerine-volanti", "title": "Le magiche Ballerine Volanti", "year": 1996},
  {"id": "lo-strano-mondo-di-minu", "title": "Lo strano mondo di Minù", "year": 1983},
  {"id": "lucy-may", "title": "Lucy May", "year": 1982},
  {"id": "lulu-l-angelo-tra-i-fiori", "title": "Lulù l'Angelo tra i Fiori", "year": 1979},
  {"id": "magica-sabrina", "title": "Magica Sabrina", "year": 1999},
  {"id": "martina-e-il-campanello-misterioso", "title": "Martina e il campanello misterioso", "year": 1987},
  {"id": "memole-dolce-memole", "title": "Memole dolce Memole", "year": 1984}
]
```

## Alla fine
Genera un file `immagini_personaggi/risultati.json` con questa struttura, solo per i cartoni dove hai trovato e scaricato almeno un personaggio:
```json
{
  "id-del-cartone": {
    "title": "Titolo esatto",
    "personaggi": [
      {"nome": "Nome Personaggio", "file": "Nome Personaggio.jpg"}
    ]
  }
}
```
Poi mandami QUI IN CHAT il contenuto di `risultati.json` e dimmi in quale cartella hai salvato le immagini (le prendo da lì, non serve che me le mandi tu).
