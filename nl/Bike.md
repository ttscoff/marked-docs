# <%= @title %>

Sleep een [Bike][bike]-overzicht (`.bike`) naar Marked om het als geneste Markdown-lijst te bekijken, met kopregels vet en taken als selectievakjes.

## Een Bike-overzicht openen [opening-a-bike-outline]

Marked zet het overzicht om wanneer u het bestand opent:

- Regels die als kop zijn gemarkeerd worden **vette** lijstonderdelen.
- Taken worden selectievakjes in GitHub-stijl. Een taak is aangevinkt wanneer Bike een voltooiingstijd bewaart of de taak als gedaan markeert.
- Koppelingen en opmaak in de regeltekst blijven Markdown.

Een geopend `.bike`-bestand gebruikt altijd deze lijst. Het overzicht wordt geen Mermaid-diagram.

## Een Bike-overzicht invoegen [including-a-bike-outline]

Een `.bike`-bestand kan ook in een ander Markdown-document worden ingevoegd. Zie [Mindmaps en overzichten insluiten](Embedding_Mind_Maps_and_Outlines.html).

In {% prefspane Apps %}, onder *Mind Maps and Outlines*, geldt **Bike outlines** voor ingevoegde bestanden:

- **Aan** (standaard) — een Mermaid-diagram. De bestandsnaam zonder `.bike` is de hoofdknoop.
- **Uit** — dezelfde geneste Markdown-lijst als bij het openen van het bestand, zonder documenttitel.

Mermaid-diagrammen hebben MultiMarkdown, CommonMark (GFM) of Kramdown nodig. Ze worden niet getekend met de Discount-processor.

[bike]: https://www.hogbaysoftware.com/bike/
