# COMPITO PER QWEN CODER: ricerca immagini personaggi cartoni animati — LISTA AGGIORNATA (193 titoli rimanenti)

## Stato del progetto
Hai già trovato con successo personaggi per 68 titoli (anime giapponesi via AniList, alcuni titoli occidentali via Fandom/Wikidata). Questa è la lista AGGIORNATA dei 193 titoli ANCORA mancanti — non ricercare più i titoli già trovati, sono già stati rimossi da questa lista.

## Obiettivo
Per ciascuno dei 193 cartoni animati elencati sotto (id, title, genre, year), cerca i personaggi principali e secondari rilevanti e trova, per ognuno, un URL diretto e funzionante a un'immagine del personaggio.

## REGOLA TECNICA FONDAMENTALE
Ogni richiesta HTTP (a qualsiasi sito) deve includere questo header, altrimenti alcuni siti bloccano con errore 403:
```python
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
```
Se una richiesta fallisce o dà risultati vuoti, NON concludere subito "fonte non disponibile" — stampa la risposta grezza o l'errore esatto. Se un sito continua a dare errore 403 nonostante l'header (blocco Cloudflare persistente), è probabile un blocco temporaneo della tua rete per troppe richieste — passa alle fonti alternative sotto invece di insistere.

## FONTI DA PROVARE, IN ORDINE

**1. AniList** (solo anime giapponesi) — API GraphQL:
```
https://graphql.anilist.co
```
query `Media(search: $search, type: ANIME)` con i personaggi in `characters.edges.node`.

**2. Wikidata** (fonte principale per titoli occidentali/non-anime, molto affidabile):
```
https://www.wikidata.org/w/api.php?action=wbsearchentities&search=<Titolo Originale>&language=en&format=json
```
Prendi l'ID (es. Q12345), poi:
```
https://www.wikidata.org/wiki/Special:EntityData/Q12345.json
```
Cerca la proprietà **P674** ("characters") per la lista reale dei personaggi. Per ognuno, cerca **P18** ("image") nel suo elemento — link diretto a Wikimedia Commons.

**3. Fandom** (wiki dedicata o hub di studio) — usa SEMPRE l'API, mai lo scraping HTML:
```
https://<wiki>.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Characters&cmlimit=100&format=json
```
Se vuota, lista le categorie esistenti prima di arrenderti:
```
https://<wiki>.fandom.com/api.php?action=query&list=allcategories&acprefix=Char&format=json&aclimit=20
```
Poi per ogni personaggio:
```
https://<wiki>.fandom.com/api.php?action=query&titles=<NomePersonaggio>&prop=pageimages&format=json&pithumbsize=500
```
(se l'immagine dà 404, riprova aggiungendo `&path-prefix=en` in fondo all'URL)

Hub di studio utili se il cartone non ha una wiki propria: `hanna-barbera.fandom.com`, `looneytunes.fandom.com`, `disney.fandom.com`, `cartoonnetwork.fandom.com`, `nickelodeon.fandom.com`, `dic-entertainment.fandom.com`.

**4. TMDB** (opzionale, richiede API key gratuita da themoviedb.org/settings/api):
```
https://api.themoviedb.org/3/search/tv?api_key=<KEY>&query=<Titolo>
https://api.themoviedb.org/3/tv/<id>/aggregate_credits?api_key=<KEY>
```

**5. Pagina Wikipedia dello show** (non del singolo personaggio) — leggi il testo con `action=parse` e cerca nomi nella sezione "Characters"/"Personaggi".

## REGOLE ANTI-ERRORE (fondamentali)
- **Mai inventare un abbinamento tra titolo italiano e titolo originale.** Verifica sempre con una fonte reale (trama/anno/personaggi coerenti) prima di usare un abbinamento. In caso di dubbio, scarta il titolo.
- **Verifica ogni URL immagine**: HTTP 200 e Content-Type con "image".
- **Escludi le immagini placeholder** (URL con "default.jpg" o icone generiche).
- **Includi tutti i personaggi rilevanti trovati**, non fermarti a 3-5.
- Se un titolo risulta live-action o senza fonti disponibili dopo aver provato tutte le fonti sopra, ometti semplicemente quel titolo.

## FORMATO DI OUTPUT
Scrivi il risultato **direttamente in questa risposta** (non salvare su disco), dentro un blocco ```json```, con questa struttura esatta:
```json
{
  "id-del-cartone": {
    "title": "Titolo esatto come in lista",
    "personaggi": [
      {"nome": "Nome Personaggio", "url": "https://url-diretto-immagine.jpg"}
    ]
  }
}
```
Se la risposta è troppo lunga per un solo messaggio, dividila in più messaggi consecutivi ("parte 1 di N").

## Lista dei 193 cartoni ancora mancanti (id, titolo, genere, anno)

```json
[
  {
    "id": "antologia-di-supergulp",
    "title": "Antologia di Supergulp!",
    "genre": "Altro",
    "year": 1972
  },
  {
    "id": "fantasupermega",
    "title": "Fantasupermega",
    "genre": "Altro",
    "year": 1980
  },
  {
    "id": "una-porta-socchiusa-ai-confini-del-sole",
    "title": "Una porta socchiusa ai confini del sole",
    "genre": "Altro",
    "year": 1994
  },
  {
    "id": "la-canzone-di-charlotte",
    "title": "la canzone di charlotte",
    "genre": "Altro",
    "year": 1985
  },
  {
    "id": "fantazoo",
    "title": "Fantazoo",
    "genre": "Animali",
    "year": 1987
  },
  {
    "id": "marsupilami",
    "title": "Marsupilami",
    "genre": "Animali",
    "year": 1993
  },
  {
    "id": "all-arrembaggio-sandokan",
    "title": "All'arrembaggio Sandokan",
    "genre": "Avventura",
    "year": 1992
  },
  {
    "id": "belle-e-sebastien",
    "title": "Belle e Sebastien",
    "genre": "Avventura",
    "year": 1980
  },
  {
    "id": "coccinella",
    "title": "Coccinella",
    "genre": "Avventura",
    "year": 1974
  },
  {
    "id": "col-vento-in-poppa-verso-l-avventura",
    "title": "Col vento in poppa verso l'avventura",
    "genre": "Avventura",
    "year": 1986
  },
  {
    "id": "com-e-grande-l-america",
    "title": "Com'e' grande l'America",
    "genre": "Avventura",
    "year": 1989
  },
  {
    "id": "d-artagnan-e-i-moschettieri-del-re",
    "title": "D'Artagnan e i Moschettieri del Re",
    "genre": "Avventura",
    "year": 1989
  },
  {
    "id": "evviva-zorro",
    "title": "Evviva Zorro",
    "genre": "Avventura",
    "year": 1997
  },
  {
    "id": "flo-la-piccola-robinson",
    "title": "Flo, la piccola Robinson",
    "genre": "Avventura",
    "year": 1981
  },
  {
    "id": "gemelli-nel-segno-del-destino",
    "title": "Gemelli nel segno del destino",
    "genre": "Avventura",
    "year": 1991
  },
  {
    "id": "gladiator-s-academy",
    "title": "Gladiator's Academy",
    "genre": "Avventura",
    "year": 2001
  },
  {
    "id": "i-segreti-dell-isola-misteriosa",
    "title": "I segreti dell'isola misteriosa",
    "genre": "Avventura",
    "year": 1995
  },
  {
    "id": "il-giro-del-mondo-di-willy-fog",
    "title": "Il giro del mondo di Willy Fog",
    "genre": "Avventura",
    "year": 1983
  },
  {
    "id": "il-libro-della-giungla",
    "title": "Il libro della giungla",
    "genre": "Avventura",
    "year": 1989
  },
  {
    "id": "il-mio-amico-huck",
    "title": "Il mio amico Huck",
    "genre": "Avventura",
    "year": 1992
  },
  {
    "id": "il-piccolo-guerriero",
    "title": "Il piccolo guerriero",
    "genre": "Avventura",
    "year": 1979
  },
  {
    "id": "kum-kum",
    "title": "Kum Kum",
    "genre": "Avventura",
    "year": 1975
  },
  {
    "id": "le-avventure-di-gamba",
    "title": "Le avventure di Gamba",
    "genre": "Avventura",
    "year": 1975
  },
  {
    "id": "le-avventure-di-huckleberry-finn",
    "title": "Le avventure di Huckleberry Finn",
    "genre": "Avventura",
    "year": 1976
  },
  {
    "id": "le-avventure-di-super-mario-bros-3",
    "title": "Le avventure di Super Mario Bros. 3",
    "genre": "Avventura",
    "year": 1990
  },
  {
    "id": "le-voci-della-savana",
    "title": "Le voci della Savana",
    "genre": "Avventura",
    "year": 1992
  },
  {
    "id": "lucy-may",
    "title": "Lucy May",
    "genre": "Avventura",
    "year": 1982
  },
  {
    "id": "lulu-l-angelo-tra-i-fiori",
    "title": "Lulù l'Angelo tra i Fiori",
    "genre": "Avventura",
    "year": 1979
  },
  {
    "id": "mister-t",
    "title": "Mister T",
    "genre": "Avventura",
    "year": 1983
  },
  {
    "id": "moby-dick-e-il-grande-mightor",
    "title": "Moby Dick e il Grande Mightor",
    "genre": "Avventura",
    "year": 1967
  },
  {
    "id": "niente-paura-c-e-alfred",
    "title": "Niente paura, c'è Alfred",
    "genre": "Avventura",
    "year": 1989
  },
  {
    "id": "notizie-da-prima-pagina",
    "title": "Notizie da prima pagina",
    "genre": "Avventura",
    "year": 1993
  },
  {
    "id": "pandamonium",
    "title": "Pandamonium",
    "genre": "Avventura",
    "year": 1982
  },
  {
    "id": "pepin-un-piccolo-eroe-per-una-grande-leggenda",
    "title": "Pepin - Un piccolo eroe per una grande leggenda",
    "genre": "Avventura",
    "year": 1999
  },
  {
    "id": "principe-valiant",
    "title": "Principe Valiant",
    "genre": "Avventura",
    "year": 1991
  },
  {
    "id": "ryu-il-ragazzo-delle-caverne",
    "title": "Ryu, il ragazzo delle caverne",
    "genre": "Avventura",
    "year": 1971
  },
  {
    "id": "scodinzola-la-vita-e-abbaia-l-avventura-con-oliver-oliver-twist",
    "title": "Scodinzola la vita e abbaia l'avventura con Oliver - Oliver Twist",
    "genre": "Avventura",
    "year": 1996
  },
  {
    "id": "speed-buggy",
    "title": "Speed Buggy",
    "genre": "Avventura",
    "year": 1973
  },
  {
    "id": "temple-e-tam-tam",
    "title": "Temple e Tam-Tam",
    "genre": "Avventura",
    "year": 1977
  },
  {
    "id": "ti-voglio-bene-denver",
    "title": "Ti voglio bene Denver",
    "genre": "Avventura",
    "year": 1988
  },
  {
    "id": "un-complotto-tra-le-onde-del-mare",
    "title": "Un complotto tra le onde del mare",
    "genre": "Avventura",
    "year": 1993
  },
  {
    "id": "un-avventura-fantastica",
    "title": "Un'Avventura Fantastica",
    "genre": "Avventura",
    "year": 1997
  },
  {
    "id": "vicky-il-vichingo",
    "title": "Vicky il vichingo",
    "genre": "Avventura",
    "year": 1973
  },
  {
    "id": "carnaby-street",
    "title": "Carnaby Street",
    "genre": "Azione",
    "year": 1999
  },
  {
    "id": "g-i-joe-a-real-american-hero-eroi-senza-frontiere",
    "title": "G.I. Joe: A Real American Hero (Eroi senza frontiere)",
    "genre": "Azione",
    "year": 1983
  },
  {
    "id": "m-a-s-k",
    "title": "M.A.S.K.",
    "genre": "Azione",
    "year": 1985
  },
  {
    "id": "pole-position",
    "title": "Pole Position",
    "genre": "Azione",
    "year": 1984
  },
  {
    "id": "street-sharks-quattro-pinne-all-orizzonte",
    "title": "Street Sharks - Quattro pinne all'orizzonte",
    "genre": "Azione",
    "year": 1994
  },
  {
    "id": "braccio-di-ferro-1960",
    "title": "Braccio di Ferro (1960)",
    "genre": "Commedia",
    "year": 1960
  },
  {
    "id": "bravo-moliere",
    "title": "Bravo Molière",
    "genre": "Commedia",
    "year": 1988
  },
  {
    "id": "capitan-cavey-e-le-teen-angels",
    "title": "Capitan Cavey e le Teen Angels",
    "genre": "Commedia",
    "year": 1977
  },
  {
    "id": "che-baby-sitter-questa-mummia",
    "title": "Che baby sitter questa mummia!",
    "genre": "Commedia",
    "year": 1999
  },
  {
    "id": "che-papa-braccio-di-ferro",
    "title": "Che papà Braccio di Ferro",
    "genre": "Commedia",
    "year": 1987
  },
  {
    "id": "conte-dacula",
    "title": "Conte Dacula",
    "genre": "Commedia",
    "year": 1987
  },
  {
    "id": "dastardly-e-muttley-e-le-macchine-volanti",
    "title": "Dastardly e Muttley e le macchine volanti",
    "genre": "Commedia",
    "year": 1969
  },
  {
    "id": "denny",
    "title": "Denny",
    "genre": "Commedia",
    "year": 1986
  },
  {
    "id": "dr-slump-e-arale-the-movie-avventura-nello-spazio",
    "title": "Dr. Slump e Arale the Movie Avventura nello spazio",
    "genre": "Commedia",
    "year": 1982
  },
  {
    "id": "filmation-ghostbusters",
    "title": "Filmation Ghostbusters",
    "genre": "Commedia",
    "year": 1986
  },
  {
    "id": "galaxy-high-school",
    "title": "Galaxy High School",
    "genre": "Commedia",
    "year": 1986
  },
  {
    "id": "george-della-giungla-1967",
    "title": "George della giungla (1967)",
    "genre": "Commedia",
    "year": 1967
  },
  {
    "id": "gianni-e-pinotto",
    "title": "Gianni e Pinotto",
    "genre": "Commedia",
    "year": 1967
  },
  {
    "id": "gli-antenati",
    "title": "Gli Antenati",
    "genre": "Commedia",
    "year": 1960
  },
  {
    "id": "grande-piccolo-magoo",
    "title": "Grande, piccolo Magoo",
    "genre": "Commedia",
    "year": 1964
  },
  {
    "id": "grattachecca-fichetto",
    "title": "Grattachecca & Fichetto",
    "genre": "Commedia",
    "year": 1990
  },
  {
    "id": "i-3-marmittoni",
    "title": "I 3 Marmittoni",
    "genre": "Commedia",
    "year": 1965
  },
  {
    "id": "i-gatti-di-cattanooga",
    "title": "I Gatti di Cattanooga",
    "genre": "Commedia",
    "year": 1969
  },
  {
    "id": "i-simpson",
    "title": "I Simpson",
    "genre": "Commedia",
    "year": 1989
  },
  {
    "id": "il-mago-pancione-etci",
    "title": "Il mago pancione Etcì",
    "genre": "Commedia",
    "year": 1969
  },
  {
    "id": "la-pantera-rosa",
    "title": "La Pantera Rosa",
    "genre": "Commedia",
    "year": 1969
  },
  {
    "id": "la-famiglia-addams",
    "title": "La famiglia Addams",
    "genre": "Commedia",
    "year": 1992
  },
  {
    "id": "la-famiglia-mezil",
    "title": "La famiglia Mezil",
    "genre": "Commedia",
    "year": 1968
  },
  {
    "id": "la-furia-di-hong-kong",
    "title": "La furia di Hong Kong",
    "genre": "Commedia",
    "year": 1974
  },
  {
    "id": "lamu",
    "title": "Lamù",
    "genre": "Commedia",
    "year": 1981
  },
  {
    "id": "mechakko-dotakon",
    "title": "Mechakko Dotakon",
    "genre": "Commedia",
    "year": 1981
  },
  {
    "id": "mortadello-e-polpetta-la-coppia-che-scoppia",
    "title": "Mortadello e Polpetta - La coppia che scoppia",
    "genre": "Commedia",
    "year": 1994
  },
  {
    "id": "napo-orso-capo",
    "title": "Napo Orso Capo",
    "genre": "Commedia",
    "year": 1971
  },
  {
    "id": "norakuro-nero-cane-di-leva",
    "title": "Norakuro (Nero, cane di leva)",
    "genre": "Commedia",
    "year": 1970
  },
  {
    "id": "oggy-e-i-maledetti-scarafaggi",
    "title": "Oggy e i maledetti scarafaggi",
    "genre": "Commedia",
    "year": 1998
  },
  {
    "id": "pazze-risate-per-mostri-e-vampiri",
    "title": "Pazze risate per mostri e vampiri",
    "genre": "Commedia",
    "year": 1994
  },
  {
    "id": "picchiarello",
    "title": "Picchiarello",
    "genre": "Commedia",
    "year": 1957
  },
  {
    "id": "pippo-e-menelao",
    "title": "Pippo e Menelao",
    "genre": "Commedia",
    "year": 1991
  },
  {
    "id": "popeye",
    "title": "Popeye",
    "genre": "Commedia",
    "year": 1960
  },
  {
    "id": "scuola-di-polizia",
    "title": "Scuola di polizia",
    "genre": "Commedia",
    "year": 1988
  },
  {
    "id": "si-salvi-chi-puo-arriva-dennis",
    "title": "Si salvi chi può! Arriva Dennis",
    "genre": "Commedia",
    "year": 1996
  },
  {
    "id": "south-park",
    "title": "South Park",
    "genre": "Commedia",
    "year": 1997
  },
  {
    "id": "super-chicken-superpollo",
    "title": "Super Chicken (Superpollo)",
    "genre": "Commedia",
    "year": 1967
  },
  {
    "id": "tamagon-risolvetutto",
    "title": "Tamagon risolvetutto",
    "genre": "Commedia",
    "year": 1972
  },
  {
    "id": "tazmania",
    "title": "Tazmania",
    "genre": "Commedia",
    "year": 1991
  },
  {
    "id": "teodoro-e-l-invenzione-che-non-va",
    "title": "Teodoro e l'invenzione che non va",
    "genre": "Commedia",
    "year": 1988
  },
  {
    "id": "tom-slick",
    "title": "Tom Slick",
    "genre": "Commedia",
    "year": 1967
  },
  {
    "id": "tom-story-la-banda-di-tommy",
    "title": "Tom Story (La Banda di Tommy)",
    "genre": "Commedia",
    "year": 1970
  },
  {
    "id": "un-mostro-tutto-da-ridere",
    "title": "Un mostro tutto da ridere",
    "genre": "Commedia",
    "year": 1985
  },
  {
    "id": "wacky-races",
    "title": "Wacky Races",
    "genre": "Commedia",
    "year": 1968
  },
  {
    "id": "willy-il-coyote-e-beep-beep",
    "title": "Willy il Coyote e Beep Beep",
    "genre": "Commedia",
    "year": 1949
  },
  {
    "id": "yoghi-salsa-e-merende",
    "title": "Yoghi, salsa e merende",
    "genre": "Commedia",
    "year": 1988
  },
  {
    "id": "pronto-emergenza",
    "title": "Pronto Emergenza",
    "genre": "Drammatico",
    "year": 1970
  },
  {
    "id": "chobin-il-ragazzo-dello-spazio",
    "title": "Chobin, il ragazzo dello spazio",
    "genre": "Fantascienza/Spazio",
    "year": 1974
  },
  {
    "id": "microsuperman",
    "title": "Microsuperman",
    "genre": "Fantascienza/Spazio",
    "year": 1973
  },
  {
    "id": "robottino",
    "title": "Robottino",
    "genre": "Fantascienza/Spazio",
    "year": 1982
  },
  {
    "id": "rocket-robin-hood",
    "title": "Rocket Robin Hood",
    "genre": "Fantascienza/Spazio",
    "year": 1966
  },
  {
    "id": "aladdin-il-mondo-e-mio",
    "title": "Aladdin - Il mondo è mio",
    "genre": "Fantasy/Magia",
    "year": 1994
  },
  {
    "id": "alice-nel-paese-delle-meraviglie",
    "title": "Alice nel Paese delle Meraviglie",
    "genre": "Fantasy/Magia",
    "year": 1983
  },
  {
    "id": "biancaneve",
    "title": "Biancaneve",
    "genre": "Fantasy/Magia",
    "year": 1995
  },
  {
    "id": "blackstar",
    "title": "Blackstar",
    "genre": "Fantasy/Magia",
    "year": 1981
  },
  {
    "id": "david-gnomo-amico-mio",
    "title": "David Gnomo amico mio",
    "genre": "Fantasy/Magia",
    "year": 1985
  },
  {
    "id": "dolceluna",
    "title": "Dolceluna",
    "genre": "Fantasy/Magia",
    "year": 1990
  },
  {
    "id": "doredo-doremi",
    "title": "Doredo Doremi",
    "genre": "Fantasy/Magia",
    "year": 2001
  },
  {
    "id": "dragon-s-lair-una-spada-per-un-cavaliere",
    "title": "Dragon's Lair (Una spada per un cavaliere)",
    "genre": "Fantasy/Magia",
    "year": 1984
  },
  {
    "id": "fantaghiro",
    "title": "Fantaghirò",
    "genre": "Fantasy/Magia",
    "year": 1999
  },
  {
    "id": "gli-gnomi-delle-montagne",
    "title": "Gli gnomi delle montagne",
    "genre": "Fantasy/Magia",
    "year": 1973
  },
  {
    "id": "he-man-and-the-masters-of-the-universe",
    "title": "He-Man and the Masters of the Universe",
    "genre": "Fantasy/Magia",
    "year": 1983
  },
  {
    "id": "i-5-samurai",
    "title": "I 5 samurai",
    "genre": "Fantasy/Magia",
    "year": 1988
  },
  {
    "id": "i-puffi",
    "title": "I Puffi",
    "genre": "Fantasy/Magia",
    "year": 1981
  },
  {
    "id": "i-bon-bon-magici-di-lilly",
    "title": "I bon bon magici di Lilly",
    "genre": "Fantasy/Magia",
    "year": 1971
  },
  {
    "id": "il-magico-mondo-di-gigi",
    "title": "Il magico mondo di Gigì",
    "genre": "Fantasy/Magia",
    "year": 1982
  },
  {
    "id": "il-mago-di-oz",
    "title": "Il mago di Oz",
    "genre": "Fantasy/Magia",
    "year": 1986
  },
  {
    "id": "john-e-solfami",
    "title": "John e Solfami",
    "genre": "Fantasy/Magia",
    "year": 1981
  },
  {
    "id": "l-incantevole-creamy",
    "title": "L'incantevole Creamy",
    "genre": "Fantasy/Magia",
    "year": 1983
  },
  {
    "id": "l-isola-del-corallo",
    "title": "L'isola del corallo",
    "genre": "Fantasy/Magia",
    "year": 1990
  },
  {
    "id": "la-maga-chappy",
    "title": "La Maga Chappy",
    "genre": "Fantasy/Magia",
    "year": 1972
  },
  {
    "id": "la-balena-giuseppina-addio-giuseppina",
    "title": "La balena Giuseppina (Addio Giuseppina)",
    "genre": "Fantasy/Magia",
    "year": 1979
  },
  {
    "id": "la-principessa-zaffiro",
    "title": "La principessa Zaffiro",
    "genre": "Fantasy/Magia",
    "year": 1967
  },
  {
    "id": "la-principessa-dai-capelli-blu",
    "title": "La principessa dai capelli blu",
    "genre": "Fantasy/Magia",
    "year": 1986
  },
  {
    "id": "la-spada-di-king-arthur",
    "title": "La spada di King Arthur",
    "genre": "Fantasy/Magia",
    "year": 1979
  },
  {
    "id": "lady-lovely",
    "title": "Lady Lovely",
    "genre": "Fantasy/Magia",
    "year": 1987
  },
  {
    "id": "le-avventure-di-teddy-ruxpin",
    "title": "Le avventure di Teddy Ruxpin",
    "genre": "Fantasy/Magia",
    "year": 1986
  },
  {
    "id": "le-fiabe-piu-belle",
    "title": "Le fiabe più belle",
    "genre": "Fantasy/Magia",
    "year": 1994
  },
  {
    "id": "le-magiche-ballerine-volanti",
    "title": "Le magiche Ballerine Volanti",
    "genre": "Fantasy/Magia",
    "year": 1996
  },
  {
    "id": "pinocchio-no-bouken",
    "title": "Le nuove avventure di Pinocchio",
    "genre": "Fantasy/Magia",
    "year": 1972
  },
  {
    "id": "lo-strano-mondo-di-minu",
    "title": "Lo strano mondo di Minù",
    "genre": "Fantasy/Magia",
    "year": 1983
  },
  {
    "id": "ma-che-magie-doremi",
    "title": "Ma che magie Doremi",
    "genre": "Fantasy/Magia",
    "year": 2000
  },
  {
    "id": "magica-sabrina",
    "title": "Magica Sabrina",
    "genre": "Fantasy/Magia",
    "year": 1999
  },
  {
    "id": "martina-e-il-campanello-misterioso",
    "title": "Martina e il campanello misterioso",
    "genre": "Fantasy/Magia",
    "year": 1987
  },
  {
    "id": "memole-dolce-memole",
    "title": "Memole dolce Memole",
    "genre": "Fantasy/Magia",
    "year": 1984
  },
  {
    "id": "mew-mew-amiche-vincenti",
    "title": "Mew Mew - Amiche vincenti",
    "genre": "Fantasy/Magia",
    "year": 2002
  },
  {
    "id": "monkey",
    "title": "Monkey",
    "genre": "Fantasy/Magia",
    "year": 1967
  },
  {
    "id": "nel-meraviglioso-mondo-degli-gnomi",
    "title": "Nel meraviglioso mondo degli gnomi",
    "genre": "Fantasy/Magia",
    "year": 1987
  },
  {
    "id": "peterpan",
    "title": "Peterpan",
    "genre": "Fantasy/Magia",
    "year": 1989
  },
  {
    "id": "quella-strana-fattoria",
    "title": "Quella strana fattoria",
    "genre": "Fantasy/Magia",
    "year": 1998
  },
  {
    "id": "re-artu-king-arthur",
    "title": "Re Artù - King Arthur",
    "genre": "Fantasy/Magia",
    "year": 1992
  },
  {
    "id": "record-of-lodoss-war-la-saga-dei-cavalieri",
    "title": "Record of Lodoss War - Cronache della Guerra di Lodoss",
    "genre": "Fantasy/Magia",
    "year": 1990
  },
  {
    "id": "sabrina-vita-da-strega",
    "title": "Sabrina vita da strega",
    "genre": "Fantasy/Magia",
    "year": 2013
  },
  {
    "id": "sally-la-maga",
    "title": "Sally la maga",
    "genre": "Fantasy/Magia",
    "year": 1966
  },
  {
    "id": "shazzan",
    "title": "Shazzan",
    "genre": "Fantasy/Magia",
    "year": 1967
  },
  {
    "id": "thundercats",
    "title": "Thundercats",
    "genre": "Fantasy/Magia",
    "year": 1985
  },
  {
    "id": "toriton",
    "title": "Toriton",
    "genre": "Fantasy/Magia",
    "year": 1972
  },
  {
    "id": "tyltyl-mytyl-e-l-uccellino-azzurro",
    "title": "Tyltyl, Mytyl e l'uccellino azzurro",
    "genre": "Fantasy/Magia",
    "year": 1980
  },
  {
    "id": "una-sirenetta-fra-noi",
    "title": "Una Sirenetta fra Noi",
    "genre": "Fantasy/Magia",
    "year": 1970
  },
  {
    "id": "una-foresta-incantata-per-katia-e-carletto",
    "title": "Una foresta incantata per Katia e Carletto",
    "genre": "Fantasy/Magia",
    "year": 1998
  },
  {
    "id": "visionaries-knights-of-the-magical-light",
    "title": "Visionaries: Knights of the Magical Light",
    "genre": "Fantasy/Magia",
    "year": 1987
  },
  {
    "id": "vola-mio-mini-pony-1984",
    "title": "Vola mio mini pony (1984)",
    "genre": "Fantasy/Magia",
    "year": 1984
  },
  {
    "id": "widget-un-alieno-per-amico",
    "title": "Widget un alieno per amico",
    "genre": "Fantasy/Magia",
    "year": 1990
  },
  {
    "id": "e-un-po-magia-per-terry-e-maggie",
    "title": "È un po' Magia per Terry e Maggie",
    "genre": "Fantasy/Magia",
    "year": 1985
  },
  {
    "id": "goober-e-i-cacciatori-di-fantasmi",
    "title": "Goober e i cacciatori di fantasmi",
    "genre": "Horror/Mistero",
    "year": 1973
  },
  {
    "id": "jabberjaw",
    "title": "Jabberjaw",
    "genre": "Horror/Mistero",
    "year": 1976
  },
  {
    "id": "banana-split-cover",
    "title": "banana split cover",
    "genre": "Musicale",
    "year": 1968
  },
  {
    "id": "chiudi-gli-occhi-e-sogna-little-rosey",
    "title": "Chiudi gli occhi e sogna - Little Rosey",
    "genre": "Per bambini piccoli",
    "year": 1990
  },
  {
    "id": "cri-cri",
    "title": "Cri Cri",
    "genre": "Per bambini piccoli",
    "year": 1990
  },
  {
    "id": "cucciolandia",
    "title": "Cucciolandia",
    "genre": "Per bambini piccoli",
    "year": 1995
  },
  {
    "id": "la-pimpa",
    "title": "La Pimpa",
    "genre": "Per bambini piccoli",
    "year": 1982
  },
  {
    "id": "mille-luci-nel-bosco",
    "title": "Mille luci nel bosco",
    "genre": "Per bambini piccoli",
    "year": 1986
  },
  {
    "id": "minutino",
    "title": "Minutino",
    "genre": "Per bambini piccoli",
    "year": 1985
  },
  {
    "id": "belfagor",
    "title": "Belfagor",
    "genre": "Poliziesco/Giallo",
    "year": 2000
  },
  {
    "id": "astrorobot-contatto-y",
    "title": "Astrorobot Contatto Y",
    "genre": "Robot/Mecha",
    "year": 1976
  },
  {
    "id": "balatack",
    "title": "Balatack",
    "genre": "Robot/Mecha",
    "year": 1977
  },
  {
    "id": "capitan-gorilla",
    "title": "Capitan Gorilla",
    "genre": "Robot/Mecha",
    "year": 1983
  },
  {
    "id": "centurions",
    "title": "Centurions",
    "genre": "Robot/Mecha",
    "year": 1986
  },
  {
    "id": "goshogun-gotriniton",
    "title": "Goshogun (Gotriniton)",
    "genre": "Robot/Mecha",
    "year": 1981
  },
  {
    "id": "guyslugger-i-guerrieri-del-ghiaccio",
    "title": "Guyslugger (I guerrieri del ghiaccio)",
    "genre": "Robot/Mecha",
    "year": 1977
  },
  {
    "id": "i-gobots",
    "title": "I Gobots",
    "genre": "Robot/Mecha",
    "year": 1984
  },
  {
    "id": "mechander-robot",
    "title": "Mechander Robot",
    "genre": "Robot/Mecha",
    "year": 1977
  },
  {
    "id": "patlabor-la-polizia-mobile",
    "title": "Patlabor - La polizia mobile",
    "genre": "Robot/Mecha",
    "year": 1989
  },
  {
    "id": "tansor-5-avventura-nella-scienza",
    "title": "Tansor 5 (Avventura nella scienza)",
    "genre": "Robot/Mecha",
    "year": 1979
  },
  {
    "id": "trider-g7",
    "title": "Trider G7",
    "genre": "Robot/Mecha",
    "year": 1980
  },
  {
    "id": "piccole-donne",
    "title": "Piccole Donne",
    "genre": "Sentimentale/Romantico",
    "year": 1981
  },
  {
    "id": "automodelli-mini-4wd",
    "title": "Automodelli - Mini 4WD",
    "genre": "Sportivo",
    "year": 1989
  },
  {
    "id": "ken-falco",
    "title": "Ken Falco",
    "genre": "Sportivo",
    "year": 1976
  },
  {
    "id": "supercar-gattiger",
    "title": "Supercar Gattiger",
    "genre": "Sportivo",
    "year": 1977
  },
  {
    "id": "undici-campioni",
    "title": "Undici campioni",
    "genre": "Sportivo",
    "year": 1979
  },
  {
    "id": "bonjour-marianne",
    "title": "Bonjour Marianne",
    "genre": "Storico",
    "year": 1990
  },
  {
    "id": "l-invincibile-shogun",
    "title": "L'invincibile Shogun",
    "genre": "Storico",
    "year": 1981
  },
  {
    "id": "birdman-e-il-galaxy-trio",
    "title": "Birdman e il Galaxy Trio",
    "genre": "Supereroi",
    "year": 1967
  },
  {
    "id": "blue-falcon-e-cane-prodigio",
    "title": "Blue Falcon e Cane Prodigio",
    "genre": "Supereroi",
    "year": 1976
  },
  {
    "id": "capitan-planet-e-i-planeteers",
    "title": "Capitan Planet e i Planeteers",
    "genre": "Supereroi",
    "year": 1992
  },
  {
    "id": "frankenstein-jr-e-gli-impossibili",
    "title": "Frankenstein Jr. e gli Impossibili",
    "genre": "Supereroi",
    "year": 1966
  },
  {
    "id": "i-fantastici-quattro-1967",
    "title": "I Fantastici Quattro (1967)",
    "genre": "Supereroi",
    "year": 1967
  },
  {
    "id": "i-superamici",
    "title": "I Superamici",
    "genre": "Supereroi",
    "year": 1985
  },
  {
    "id": "space-ghost-il-fantasma-dello-spazio",
    "title": "Space Ghost (Il Fantasma dello Spazio)",
    "genre": "Supereroi",
    "year": 1966
  },
  {
    "id": "spider-man-e-i-suoi-fantastici-amici",
    "title": "Spider-Man e i suoi fantastici amici",
    "genre": "Supereroi",
    "year": 1981
  },
  {
    "id": "superboy-shadaw",
    "title": "Superboy Shadaw",
    "genre": "Supereroi",
    "year": 1967
  },
  {
    "id": "la-piccola-lul",
    "title": "La piccola Lulù",
    "genre": "Vita quotidiana/Scolastico",
    "year": 1976
  },
  {
    "id": "mostri-o-non-mostri-tutti-a-scuola",
    "title": "Mostri o non mostri... tutti a scuola",
    "genre": "Vita quotidiana/Scolastico",
    "year": 1990
  },
  {
    "id": "supermodels",
    "title": "Supermodels",
    "genre": "Vita quotidiana/Scolastico",
    "year": 1999
  }
]
```
