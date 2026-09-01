# COMPITO PER QWEN CODER — 20 cartoni animati (gruppo di prova)

## Regola più importante di tutte: PERTINENZA
Negli ultimi test, la maggior parte degli errori non erano URL falsi ma **personaggi presi dallo show sbagliato**: ad esempio per "Il giro del mondo di Willy Fog" è stata trovata un'immagine dei Puffi, per "Coccinella" un'immagine di "A Flintstone Christmas", per "Le avventure di Gamba" un personaggio del film Pixar "Luca". Questo succede quando si cerca il titolo come testo libero su wiki Fandom generici e si prende il primo risultato senza controllare che appartenga davvero al cartone giusto.

**Prima di accettare un personaggio, verifica sempre:**
1. La pagina/wiki da cui viene l'immagine parla DAVVERO di questo cartone specifico (stesso titolo originale, stessa trama, stesso studio/anno)? Se il wiki è di un altro franchise (es. Looney Tunes, Disney generico, Hanna-Barbera generico) e il nome del personaggio coincide solo per assonanza, NON usarlo.
2. Se non sei sicuro al 100% che il personaggio appartenga a questo cartone, ometti il personaggio invece di indovinare.

## Regola sugli URL: MAI INVENTARE
Ogni URL deve venire da una risposta reale di una chiamata API che hai effettivamente eseguito in questa conversazione. Se non hai davvero fatto la chiamata e non hai davvero visto il risultato, non scrivere l'URL — lascialo vuoto o ometti il personaggio.

## Fonti da usare, in ordine di affidabilità (più affidabile = più in alto)
1. **AniList** (solo per anime/cartoni giapponesi) — query GraphQL su `https://graphql.anilist.co`, cerca per titolo originale giapponese/inglese se lo conosci, altrimenti per titolo italiano.
2. **Wikidata** — cerca l'entità con `action=wbsearchentities`, poi usa la proprietà P674 (characters) per trovare i personaggi reali collegati a QUELLA entità, e P18 per l'immagine. Questo è affidabile perché il collegamento personaggio→opera è esplicito nel database, non una ricerca testuale.
3. **Wikipedia** (IT poi EN) — cerca la pagina del cartone, leggi la sezione "Personaggi"/"Characters" per i nomi, poi cerca l'immagine di ciascun personaggio SOLO se la sua pagina Wikipedia menziona esplicitamente questo cartone.
4. **Fandom/Wikia** — usa questa fonte SOLO se riesci a identificare il wiki specifico dedicato a questo cartone (es. dal nome del wiki, tipo "willyfog.fandom.com"). Non prendere mai il primo risultato di ricerca da un wiki generico/di un altro franchise (hanna-barbera.fandom.com, disney.fandom.com, looneytunes.fandom.com) a meno che tu non abbia verificato che quella specifica pagina parli di questo cartone.

Ogni chiamata HTTP deve avere questo header, altrimenti Fandom/Wikipedia rispondono errore 403:
```python
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
```

## Formato di output richiesto (ESATTO)
Non salvare nulla su disco. Scrivi il risultato **direttamente in questa risposta**, come JSON, con questa struttura:

```json
{
  "id-del-cartone": {
    "title": "Titolo esatto",
    "personaggi": [
      {"nome": "Nome Personaggio", "url": "https://url-reale-verificato.jpg"}
    ]
  }
}
```

Se per un cartone non trovi nulla di affidabile, scrivi comunque la entry con `"personaggi": []` e passa oltre — va benissimo, meglio zero personaggi che personaggi sbagliati.

## Lista dei 20 cartoni

```json
[
  {"id": "aladdin-il-mondo-e-mio", "title": "Aladdin - Il mondo è mio", "genre": "Fantasy/Magia", "year": 1994},
  {"id": "alice-nel-paese-delle-meraviglie", "title": "Alice nel Paese delle Meraviglie", "genre": "Fantasy/Magia", "year": 1983},
  {"id": "all-arrembaggio-sandokan", "title": "All'arrembaggio Sandokan", "genre": "Avventura", "year": 1992},
  {"id": "antologia-di-supergulp", "title": "Antologia di Supergulp!", "genre": "Altro", "year": 1972},
  {"id": "astrorobot-contatto-y", "title": "Astrorobot Contatto Y", "genre": "Robot/Mecha", "year": 1976},
  {"id": "banana-split-cover", "title": "banana split cover", "genre": "Musicale", "year": 1968},
  {"id": "belfagor", "title": "Belfagor", "genre": "Poliziesco/Giallo", "year": 2000},
  {"id": "belle-e-sebastien", "title": "Belle e Sebastien", "genre": "Avventura", "year": 1980},
  {"id": "biancaneve", "title": "Biancaneve", "genre": "Fantasy/Magia", "year": 1995},
  {"id": "bonjour-marianne", "title": "Bonjour Marianne", "genre": "Storico", "year": 1990},
  {"id": "bravo-moliere", "title": "Bravo Molière", "genre": "Commedia", "year": 1988},
  {"id": "carnaby-street", "title": "Carnaby Street", "genre": "Azione", "year": 1999},
  {"id": "che-baby-sitter-questa-mummia", "title": "Che baby sitter questa mummia!", "genre": "Commedia", "year": 1999},
  {"id": "che-papa-braccio-di-ferro", "title": "Che papà Braccio di Ferro", "genre": "Commedia", "year": 1987},
  {"id": "chiudi-gli-occhi-e-sogna-little-rosey", "title": "Chiudi gli occhi e sogna - Little Rosey", "genre": "Per bambini piccoli", "year": 1990},
  {"id": "chobin-il-ragazzo-dello-spazio", "title": "Chobin, il ragazzo dello spazio", "genre": "Fantascienza/Spazio", "year": 1974},
  {"id": "coccinella", "title": "Coccinella", "genre": "Avventura", "year": 1974},
  {"id": "col-vento-in-poppa-verso-l-avventura", "title": "Col vento in poppa verso l'avventura", "genre": "Avventura", "year": 1986},
  {"id": "com-e-grande-l-america", "title": "Com'e' grande l'America", "genre": "Avventura", "year": 1989},
  {"id": "conte-dacula", "title": "Conte Dacula", "genre": "Commedia", "year": 1987}
]
```

## Prima di rispondere
Rileggi ogni personaggio che hai trovato e chiediti: "sono sicuro che questo personaggio appartiene proprio a QUESTO cartone e non a un altro show con un nome simile?" Se la risposta non è un sì sicuro, togli quel personaggio.
