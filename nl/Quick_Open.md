# <%= @title %>

Quick Open biedt snelle toegang tot uw geopende documenten en recente bestanden.

## Snel openen [opening-quick-open]

Open het paneel Quick Open met {% kbd shift cmd O %} of via het menu {% appmenu File, Quick Open %}. Het paneel verschijnt als een zwevend venster boven uw huidige document, zodat u snel kunt schakelen tussen geopende documenten of recente bestanden kunt openen.

![Quick Open Panel][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Documentsecties [document-sections]

Het Quick Open-paneel organiseert documenten in duidelijke secties:

### Documenten openen [open-documents]

Bovenaan de lijst ziet u alle momenteel geopende documenten. Documenten worden visueel gegroepeerd op basis van hun venster:

- **Vensters met tabbladen**: Documenten in vensters met tabbladen tonen "Venster met X-tabbladen" als ondertitel, waarmee wordt aangegeven hoeveel tabbladen zich in die venstergroep bevinden
- **Zelfstandige Windows**: Documenten in individuele vensters tonen "Venster" als ondertitel

Bij elk geopend document wordt het volgende weergegeven:
- De bestandsnaam van het document als hoofdtitel
- De venstergroeperingsinformatie als ondertitel
- Een documentpictogram

### Recente documenten [recent-documents]

Onder de geopende documenten verdeelt een scheidingsteken "Recente documenten" de lijst. In het gedeelte Recente documenten worden maximaal 10 van uw meest recent geopende bestanden weergegeven die momenteel niet zijn geopend. Bij elk recent document wordt het volgende weergegeven:

- De bestandsnaam van het document als hoofdtitel
- "Recent" als ondertitel
- Een documentpictogram

### Open Overige [open-other]

Onderaan de lijst kunt u met de optie "Anders openen..." de standaard macOS-bestandskiezer openen om elk bestand te selecteren. Deze optie wordt weergegeven:

- "Open Andere…" als hoofdtitel
- "Open een bestand of map" als ondertitel
- Een mappictogram

## Zoeken en filteren [search-and-filter]

Typ het zoekveld bovenaan het paneel om de lijst in realtime te filteren. De zoekopdracht komt overeen met:

- Documentbestandsnamen
- Volledige bestandspaden

Terwijl u typt, wordt de lijst onmiddellijk bijgewerkt en worden alleen overeenkomende documenten weergegeven. De optie "Anders openen..." blijft altijd zichtbaar onderaan de gefilterde resultaten.

## Toetsenbordnavigatie [keyboard-navigation]

Navigeer volledig met uw toetsenbord door het Quick Open-paneel:

- **↑/↓ Pijltjestoetsen**: Beweeg omhoog en omlaag door de lijst
- **Retour**: Open het geselecteerde document of de geselecteerde optie
- **Escape**: Sluit het Quick Open-paneel
- **Commando (⌘)**: Houd ingedrukt om bestandspaden weer te geven (zie hieronder)

## Bestandspaden bekijken [viewing-file-paths]

Houd de **Command (⌘)**-toets ingedrukt terwijl het paneel Snel openen geopend is om het volledige bestandspad voor elk document in het ondertitelgebied te zien. Paden in uw thuismap worden weergegeven met de afkorting `~` (bijvoorbeeld `~/Documents/file.md`). Laat de Command-toets los om terug te keren naar de normale weergave met venstergroepering of "Recente" informatie.

Dit is vooral handig als u meerdere bestanden met dezelfde naam geopend heeft, of als u de exacte locatie van een document moet verifiëren.

## Documenten openen [opening-documents]

- **Geopende documenten**: als u een geopend document selecteert, wordt het bijbehorende venster op de voorgrond geplaatst en wordt overgeschakeld naar het tabblad van dat document als het zich in een venster met tabbladen bevindt
- **Recente documenten**: als u een recent document selecteert, wordt het in een nieuw venster geopend of wordt het als tabblad toegevoegd (afhankelijk van uw voorkeur voor "Open documenten in tabbladen" in {% prefspane General %})
- **Anders openen...**: als u deze optie selecteert, wordt het standaard macOS-dialoogvenster voor het kiezen van bestanden geopend

