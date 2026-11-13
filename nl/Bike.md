# <%= @title %>

Sleep een [Bike][bike]-overzicht naar Marked om het als geneste Markdown-lijst te bekijken, met kopregels vet en taken als selectievakjes. Een los overzicht is een `.bike`-bestand. Bike 2 bewaart een `.biked`-pakket wanneer het overzicht ingesloten afbeeldingen bevat.

## Een Bike-overzicht openen [opening-a-bike-outline]

Marked zet het overzicht om wanneer u het bestand opent:

- Regels die als kop zijn gemarkeerd worden **vette** lijstonderdelen.
- Taken worden selectievakjes in GitHub-stijl. Een taak is aangevinkt wanneer Bike een voltooiingstijd bewaart of de taak als gedaan markeert.
- Koppelingen en opmaak in de regeltekst blijven Markdown.

Een geopend `.bike`-bestand gebruikt altijd deze lijst. Het overzicht wordt geen Mermaid-diagram. Een `.biked`-pakket volgt de instelling **Bike outlines** die hieronder staat.

## Een Bike-overzicht invoegen [including-a-bike-outline]

Een `.bike`-bestand kan ook in een ander Markdown-document worden ingevoegd. Zie [Mindmaps en overzichten insluiten](Embedding_Mind_Maps_and_Outlines.html).

In {% prefspane Apps %}, onder *Mind Maps and Outlines*, geldt **Bike outlines** voor ingevoegde bestanden:

- **Aan** (standaard) — een Mermaid-diagram. De bestandsnaam zonder `.bike` is de hoofdknoop.
- **Uit** — dezelfde geneste Markdown-lijst als bij het openen van het bestand, zonder documenttitel.

## Overzichten met afbeeldingen [outlines-with-images]

Bike 2 bewaart een `.biked`-pakket wanneer het overzicht ingesloten afbeeldingen bevat. Het pakket is een TextBundle: `text.bike` plus een map `assets`. Open het `.biked`-bestand zelf. Marked leest het overzicht daarin en gebruikt de pakketnaam als venstertitel.

Zet **Bike outlines** uit om dat pakket als geneste lijst te bekijken, met de ingesloten afbeeldingen. **Aan** maakt van het overzicht een Mermaid-diagram.

[bike]: https://www.hogbaysoftware.com/bike/
