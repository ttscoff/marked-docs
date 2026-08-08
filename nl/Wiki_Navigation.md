# <%= @title %>

Marked bevat een wiki-navigatiesysteem waarmee u snel tussen gerelateerde tekstbestanden kunt springen met behulp van eenvoudige `[[wiki]]` links. Dit systeem is ontworpen voor naadloze navigatie en werkt het beste wanneer het is geconfigureerd om links in het huidige venster te openen.

## Optimale instellingen [optimal-settings]

Om wiki-koppelingen te gebruiken, schakelt u **Convert `[[wiki links]]`** in {% prefspane Preview %} in en stelt u de standaardextensie in die Marked zal gebruiken bij het zoeken naar overeenkomende bestanden.

Voor de beste ervaring stelt u **"Koppelingen naar tekstbestanden moeten openen in:"** in op *"het huidige venster"* in {% prefspane Apps %}. Dit zorgt ervoor dat de navigatie natuurlijk aanvoelt en de geschiedenis behouden blijft.

Als **Syntaxisfouten Markdown markeren** is ingeschakeld in {% prefspane Proofing %}, wordt de syntaxis `[[wiki link]]` die niet overeenkomt met een bestandsnaam in de huidige map rood gemarkeerd om aan te geven dat het bestand waarnaar wordt verwezen niet bestaat. Deze hoogtepunten worden bijgewerkt naarmate er bestanden worden toegevoegd, maar pas nadat het huidige bestand is opgeslagen of opnieuw is geladen. Als u op een gemarkeerde ontbrekende bestandslink klikt, wordt u aangeboden een nieuw bestand voor u te maken, waarbij indien nodig de standaardextensie wordt toegevoegd. Het nieuwe lege bestand wordt geopend in Marked en als Nieuwe documenten bewerken is ingeschakeld, wordt uw editor geopend met het nieuwe bestand.

## Hoe Wiki-links werken [how-wiki-links-work]

- **Wiki-links** gebruiken het formaat: `[[wiki link]]`.
- Wanneer u op een wikilink klikt, zoekt Marked naar een overeenkomend bestand in **dezelfde map** als het huidige document.
- Het bestand moet de extensie hebben die is opgegeven in de instellingen van Marked (bijvoorbeeld `.md`), tenzij u een volledige bestandsnaam met extensie opgeeft in de link (bijvoorbeeld `[[notes.txt]]`).
- Als u voor de link tekst wilt gebruiken die afwijkt van de bestandsnaam, voeg deze dan toe na een pipe (`|`) in de link, b.v. `[[wiki linking|A note about linking]]`, dat wordt weergegeven als `[A note about linking](wiki-link.md)`.
- Als een wikilink begint met een `#`, wordt deze gezien als een ankerlink op dezelfde pagina. Ankernamen worden genormaliseerd door kleine letters te gebruiken en alle spaties te vervangen door streepjes. Voor processors die header-ID's zonder streepjes maken (zoals MultiMarkdown), b.v. `## wiki links` krijgt de id `wikilinks`, deze navigatie kan kapot gaan. Geef in die gevallen de juiste link-ID op, indien nodig met een pipe en titel, b.v. `[[#wikilinks|#wiki links]]`.

### Overeenkomende bestandsnamen [matching-file-names]

Wanneer u een link als `[[wiki link]]` gebruikt, zoekt Marked naar een bestand met een van de volgende namen (ervan uitgaande dat uw standaardextensie `.md` is):

- `wiki link.md`
- `WikiLink.md`
- `wiki-link.md`
- `Wiki-Link.md`
- `wiki_link.md`
- `Wiki_Link.md`
- `wikilink.md`
- `WikiLink.md`
- (en andere combinaties van spaties, streepjes, onderstrepingstekens en intercaps)

**Alle overeenkomsten zijn hoofdlettergevoelig en flexibel met scheidingstekens.**
Als u een extensie opgeeft in de link (bijvoorbeeld `[[notes.txt]]`), zoekt Marked naar dat exacte bestand.

## Backlinks [backlinks]

Wanneer een tekstbestand wordt geopend en wiki-navigatie is ingeschakeld, wordt de rest van de bestanden in de map gescand op `[[links]]` naar het huidige bestand. Dit gebeurt op de achtergrond en het geopende document wordt bijgewerkt met een lijst met backlinks als deze worden gevonden. Om de backlinks te bekijken, moet de zijbalk met opmerkingen geopend zijn. Als het gesloten is, gebruik dan het tandwielmenu (**Proofing->Toon opmerkingen**) of druk op {% kbd ^@c %} om het te openen.


## Navigatiegeschiedenis [navigation-history]

Marked houdt uw navigatie bij via wiki-links, zodat u **vooruit en achteruit** door uw bestandsgeschiedenis kunt bladeren, net als bij een webbrowser.

- **Terug:** {% kbd @[ %}
- **Vooruit:** {% kbd @] %}

U kunt ook het menu **Geschiedenis** gebruiken om naar een eerder bezocht bestand te gaan.