# <%= @title %>

Marked bevat browserextensies waarmee u pagina-URL's of geselecteerde inhoud rechtstreeks naar Marked kunt sturen 3.

## Installeren [install]

Downloaden en installeren vanaf [https://markedapp.com/extensions](https://markedapp.com/extensions):

-Firefox/Zen
- Chroom / Dapper / Rand
- Safari (gebundeld)

## Hoe de extensie werkt [how-the-extension-works]

Wanneer u op een extensieknop klikt, wordt er een aangepaste URL geopend die wordt afgehandeld door Marked 3 met behulp van het `x-marked-3://markdownify` schema.

### `Markdownify URL` [markdownify-url]

Klik in de extensiepop-up op **`Markdownify URL`** om de huidige pagina-URL naar Marked te verzenden.

### `Markdownify Selection` [markdownify-selection]

Klik in de extensiepop-up op **`Markdownify Selection`** wanneer u een selectie op de pagina hebt.

Marked ontvangt de HTML voor de huidige selectie en converteert deze naar Markdown.

### Sectie selecteren (blokselectiemodus) [select-section-block-selection-mode]

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Klik op **Selecteer sectie** om de “sectieselectiemodus” te openen:

- Beweeg over de pagina om blokelementen te markeren die u kunt selecteren.
- Klik op een blok om het onmiddellijk naar Marked te sturen (enkele verzending).
- Cmd-klik op blokken om meerdere blokken te selecteren (Cmd-klik nogmaals om een ​​blok te verwijderen).
- Druk op Return om de momenteel geselecteerde blokken te verzenden.
- Druk op Esc om de sectieselectiemodus te annuleren.

Tijdens het selecteren biedt de pop-up ook zoomknoppen waarmee u op kleine of dichte secties kunt klikken:

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` zoomt uit
- **Hoogte aanpassen** zoomt in zodat de pagina op de hoogte van de viewport past
- `+` zoomt in