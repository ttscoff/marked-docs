# <%= @title %>

Marked exporteert HTML vanuit uw **live preview** --- dezelfde weergegeven uitvoer die u op het scherm ziet. Gebruik HTML export als je een fragment nodig hebt om in een blog of CMS te plakken, of een op zichzelf staand `.html` bestand met ingesloten stijlen en afbeeldingen die je in elke browser of host waar dan ook kunt openen.

De typische workflow is **eerst een voorbeeld bekijken, HTML seconde** exporteren: open of compileer uw document in Marked, kies een thema, proeflezen in de live preview en exporteer vervolgens wanneer de opmaak er goed uitziet.

## Twee manieren om HTML te krijgen [two-ways-to-get-html]

### Kopieer HTML (fragment) [copy-html-snippet]

**Kopieer HTML** plaatst de HTML bron van het voorbeeld op het klembord --- klaar om te plakken in WordPress, Ghost, Squarespace, een forum, een e-mailsjabloon of elke app die HTML fragmenten accepteert.

* Tandwielmenu → **Kopieer HTML**, of {% kbd shift cmd C %} met de focus op het voorbeeld
* Kopieert de **gerenderde hoofdtekst HTML** (geen volledig document met `<html>` wrapper)
* Optioneel: schakel **Afbeeldingen insluiten bij het kopiëren van HTML** in {% prefspane Export %} naar Base64-codering van lokale afbeeldingen als `data:` URL's in de geplakte broncode

Kopieer HTML is ideaal wanneer uw bestemming al een eigen stylesheet heeft en u alleen de inhoudsopmaak nodig heeft.

### Opslaan HTML (bestand) [save-html-file]

**Opslaan HTML** schrijft een compleet `.html` bestand naar schijf.

* Exporteren → **Opslaan HTML**, {% kbd cmd S %} of **HTML** uit de [Export Panel](Exporting.html#drawer) ({% kbd shift cmd e %})
* Kies de bestandsnaam en locatie in het dialoogvenster Opslaan
* Configureer exportopties in het dialoogvensteraccessoire (zie hieronder)

Opslaan HTML is ideaal voor archivering, het delen van een zelfstandig bestand of het rechtstreeks openen van het resultaat in een browser.

## Bewaar HTML opties [save-html-options]

Het dialoogvenster Save HTML bevat een exportprofielkiezer en deze opties:

![Save HTML options][savehtml]

**Stijl opnemen in uitvoer**

Indien aangevinkt, sluit Marked de CSS van het geselecteerde voorbeeldthema in een `<style>` blok in het geëxporteerde bestand in. Kies een ingebouwd thema of [Custom Style](Custom_Styles.html) uit het stijlmenu naast het selectievakje. De uitvoer is een compleet HTML document met `<!DOCTYPE html>`, `<head>` en een `#wrapper` div rond uw inhoud --- passend bij wat u hebt bekeken.

Indien uitgeschakeld, slaat Marked een minimaal HTML document op met alleen uw weergegeven inhoud (geen Marked thema-CSS). Gebruik dit als u ruwe HTML wilt plakken of importeren in een ander systeem dat zijn eigen stijl levert.

**Lokale afbeeldingen insluiten voor standalone HTML**

Wanneer **Stijl opnemen in uitvoer** is ingeschakeld, kunt u ook lokale afbeeldingen insluiten als Base64 `data:` URL's in het HTML bestand. Het resultaat is één enkel bestand dat u kunt e-mailen, uploaden of hosten zonder een aparte `images/` map.

* Werkt met afbeeldingen waarnaar wordt verwezen door **relatieve of absolute paden** op uw lokale schijf
* Vermijd `file:///` URL's --- deze kunnen niet betrouwbaar worden ingesloten
* Externe afbeeldingen (http/https) blijven als externe URL's, tenzij u ze eerst downloadt
* Base64-inbedding kan grote bestanden produceren; gebruik het wanneer draagbaarheid belangrijker is dan de bestandsgrootte

**Inclusief syntaxisaccentuering van JavaScript**

Wanneer syntaxisaccentuering is ingeschakeld in {% prefspane Preview %}, voegt deze optie highlight.js CSS en JavaScript uit een CDN toe, zodat codeblokken hun kleuren in het geëxporteerde bestand behouden. De geëxporteerde HTML heeft een internetverbinding nodig om de CDN-bronnen te kunnen laden.

**Inclusief MathJax of KaTeX CDN-link**

Wanneer [MathJax](MathJax.html) of KaTeX is ingeschakeld voor voorbeeldweergave, kunt u de overeenkomende CDN-scripts opnemen in de opgeslagen HTML, zodat vergelijkingen in een browser worden weergegeven. Net als syntaxisaccentuering vereist dit netwerktoegang bij het bekijken van het bestand, tenzij u de scripts zelf host.

**CriticMarkup exporttype**

Documenten met [CriticMarkup](CriticMarkup.html) kunnen kiezen of de export bewerkte tekst, originele tekst of volledige markup toont.

**Profiel exporteren**

Selecteer een opgeslagen [Export Profile](Exporting.html#export-profiles) om uw favoriete HTML exportinstellingen (ingesloten stijlen, afbeeldingen, syntaxisaccentuering, wiskunde) in één stap te herstellen.

## Styling met ingebouwde en aangepaste thema's [styling-with-built-in-and-custom-themes]

De **voorbeeldstijl** bepaalt de weergave van HTML wanneer **Stijl opnemen in uitvoer** is aangevinkt:

1. Kies een stijl uit het stijlmenu van het voorbeeldvenster (of stel een standaard in {% prefspane Style %}).
2. Bekijk typografie, koppen, codeblokken en afbeeldingen in de live preview.
3. Sla HTML op met dezelfde stijl als geselecteerd in het exportdialoogvenster.

Elk ingebouwd Marked thema --- Zwitsers, GitHub, Manuscript en de rest --- kan worden ingesloten. [Custom Styles](Custom_Styles.html) en stijlen uit [Style Manager](Custom_Styles.html) werken op dezelfde manier.

I> Sommige CSS-voorbeelden (vaste positionering, viewport-trucs, donkere modus `@media screen` inversie) worden mogelijk niet één-op-één vertaald buiten Marked. Open het opgeslagen bestand in een browser om het te verifiëren voordat u het publiceert.

Voor richtlijnen bij het schrijven, zie [Creating Custom CSS](Writing_Custom_CSS.html).

## Metagegevens en MultiMarkdown headers [metadata-and-multimarkdown-headers]

MeerdereMarkdown metadata bovenaan uw bronbestand kunnen de export van HTML beïnvloeden:

* **`Title:`** --- gebruikt voor het `<title>` element bij het opslaan van een volledig HTML document
* **`XHTML Header:`** / **`HTML Header:`** --- injecteert extra tags in de geëxporteerde `<head>` (scripts, linktags, metatags)
* Andere metadatasleutels worden verwerkt volgens uw [Markdown processor](Choosing_a_Processor.html)

Als u metagegevens gebruikt voor exportinstellingen, maar niet wilt dat sleutels zichtbaar zijn in andere uitvoer, verpak ze dan in HTML opmerkingen --- Marked vindt en verwerkt metagegevens met commentaar waar dan ook in het document. Zie [Per-Document Settings](Per-Document_Settings.html).

## Documenten met meerdere bestanden [multi-file-documents]

Voor boeken- en hoofdstukcompilaties gebruikt u [Multi-File Documents](Multi-File_Documents.html). Marked geeft een voorbeeld van het samengevoegde document weer en exporteert één HTML bestand uit het gecompileerde resultaat. Inbegrepen bestanden zijn gemarkeerd met HTML opmerkingen die hun bronpaden tonen --- handig bij het controleren van welk hoofdstuk aan welke sectie heeft bijgedragen.

## Plakken in andere applicaties [pasting-into-other-applications]

| Bestemming | Voorgestelde aanpak |
| :-- | :-- |
| Blog / CMS met een eigen thema | **Kopieer HTML** (fragment, geen ingesloten Marked CSS) |
| Statische site of archief | **Opslaan HTML** met **Stijl opnemen in uitvoer** |
| E-mail of bestandsdeling (één bijlage) | **Opslaan HTML** met **Lokale afbeeldingen insluiten** |
| WordPress, Ghost, Notion, enz. | **Kopieer HTML**; enable **Afbeeldingen insluiten bij het kopiëren van HTML** als de editor de lokale paden niet omzet |
| Verder bewerken in een code-editor | **Opslaan HTML** zonder ingesloten stijl, of fragment kopiëren en handmatig inpakken |

[Copy Rich Text](Exporting.html#rtfexportoptions) (tandwielmenu) is een alternatief wanneer de doelapp opgemaakte tekst accepteert in plaats van de HTML bron.

## Gerelateerde onderwerpen [related-topics]

* [Exporting](Exporting.html) --- exportpaneel, profielen en andere formaten
* [EPUB Export](EPUB_Export.html) --- e-boekuitvoer met ingebouwde CSS
* [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) --- bekijk een voorbeeld van de workflow vóór het exporteren
* [Custom Styles](Custom_Styles.html) en [Settings: Export](Settings_Export.html)
* [HTML Specific Settings](HTML_Specific_Settings.html) --- processoropties voor HTML uitvoer
* [AppleScript export](AppleScript_Support.html) --- automatiseer HTML kopiëren en opslaan

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
r