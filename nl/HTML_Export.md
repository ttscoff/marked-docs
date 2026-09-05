# <%= @title %>

Marked exporteert HTML vanuit je **live voorvertoning** --- dezelfde weergave die je op het scherm ziet. Gebruik HTML-export wanneer je een fragment nodig hebt om in een blog of CMS te plakken, of een op zichzelf staand `.html`-bestand met ingesloten stijlen en afbeeldingen dat je in elke browser kunt openen of overal kunt hosten.

De gebruikelijke werkwijze is **eerst voorvertonen, dan HTML exporteren**: open of compileer je document in Marked, kies een stijl, controleer het resultaat in de live voorvertoning en exporteer pas wanneer de opmaak klopt.

## Twee manieren om HTML te krijgen [two-ways-to-get-html]

### HTML kopiëren (fragment) [copy-html-snippet]

**HTML kopiëren** zet de HTML-broncode van de voorvertoning op het klembord --- klaar om te plakken in WordPress, Ghost, Squarespace, een forum, een e-mailsjabloon of elke andere app die HTML-fragmenten accepteert.

* Gear-menu → **HTML kopiëren**, of {% kbd shift cmd C %} terwijl de voorvertoning actief is
* Kopieert de **gerenderde HTML van de inhoud** (geen volledig document met `<html>`-wrapper)
* Optioneel: schakel **Afbeeldingen insluiten bij HTML kopiëren** in bij {% prefspane Export %} om lokale afbeeldingen als Base64-`data:`-URL's in de geplakte broncode te coderen

HTML kopiëren is ideaal wanneer je bestemming al een eigen stylesheet heeft en je alleen de inhoudsmarkup nodig hebt.

### HTML opslaan (bestand) [save-html-file]

**HTML opslaan** schrijft een volledig `.html`-bestand naar schijf.

* Exporteren → **HTML opslaan**, {% kbd cmd S %}, of **HTML** vanuit het [exportpaneel](Exporting.html#drawer) ({% kbd shift cmd e %})
* Kies bestandsnaam en locatie in het opslagvenster
* Configureer exportopties in het accessoirevenster (zie hieronder)

HTML opslaan is ideaal voor archivering, het delen van een op zichzelf staand bestand, of het rechtstreeks openen van het resultaat in een browser.

## Opties voor HTML opslaan [save-html-options]

Het dialoogvenster HTML opslaan bevat een keuzemenu voor exportprofielen en de volgende opties:

![Opties voor HTML opslaan][savehtml]

**Stijl opnemen in uitvoer**

Indien aangevinkt, sluit Marked de CSS van de geselecteerde voorvertoningsstijl in als `<style>`-blok in het geëxporteerde bestand. Kies een ingebouwde stijl of een [aangepaste stijl](Custom_Styles.html) uit het stijlmenu naast het selectievakje. De uitvoer is een compleet HTML-document met `<!DOCTYPE html>`, `<head>` en een `#wrapper`-div rond je inhoud --- overeenkomend met wat je in de voorvertoning zag.

Indien niet aangevinkt, slaat Marked een minimaal HTML-document op met alleen je gerenderde inhoud (zonder de themastijl van Marked). Gebruik dit wanneer je onbewerkte HTML wilt plakken of importeren in een ander systeem dat zijn eigen opmaak levert.

**Lokale afbeeldingen insluiten voor op zichzelf staande HTML**

Wanneer **Stijl opnemen in uitvoer** is ingeschakeld, kun je ook lokale afbeeldingen insluiten als Base64-`data:`-URL's binnen het HTML-bestand. Het resultaat is één bestand dat je kunt e-mailen, uploaden of hosten zonder aparte `images/`-map.

* Werkt met afbeeldingen die via **relatieve of absolute paden** op je lokale schijf worden aangeroepen
* Vermijd `file:///`-URL's --- deze kunnen niet betrouwbaar worden ingesloten
* Externe afbeeldingen (http/https) blijven externe URL's, tenzij je ze eerst downloadt
* Base64-insluiting kan grote bestanden opleveren; gebruik dit wanneer overdraagbaarheid belangrijker is dan bestandsgrootte

**Syntax highlighting-JavaScript opnemen**

Wanneer syntax highlighting is ingeschakeld in {% prefspane Preview %}, voegt deze optie CSS en JavaScript van highlight.js toe vanaf een CDN, zodat codeblokken hun kleuren behouden in het geëxporteerde bestand. De geëxporteerde HTML heeft internetverbinding nodig om de CDN-bronnen te laden.

**CDN-link voor MathJax of KaTeX opnemen**

Wanneer [MathJax](MathJax.html) of KaTeX is ingeschakeld voor de voorvertoning, kun je de bijbehorende CDN-scripts opnemen in de opgeslagen HTML, zodat vergelijkingen in een browser worden weergegeven. Net als bij syntax highlighting is hiervoor netwerktoegang nodig bij het bekijken van het bestand, tenzij je de scripts zelf host.

**Exporttype voor CriticMarkup**

Bij documenten met [CriticMarkup](CriticMarkup.html) kun je kiezen of de export de bewerkte tekst, de oorspronkelijke tekst of de volledige markup toont.

**Exportprofiel**

Selecteer een opgeslagen [exportprofiel](Exporting.html#export-profiles) om in één stap je gewenste HTML-exportinstellingen (ingesloten stijlen, afbeeldingen, syntax highlighting, wiskunde) te herstellen.

## Opmaken met ingebouwde en aangepaste stijlen [styling-with-built-in-and-custom-themes]

De **voorvertoningsstijl** bepaalt het uiterlijk van de HTML wanneer **Stijl opnemen in uitvoer** is aangevinkt:

1. Kies een stijl uit het stijlmenu van het voorvertoningsvenster (of stel een standaard in bij {% prefspane Style %}).
2. Controleer typografie, koppen, codeblokken en afbeeldingen in de live voorvertoning.
3. Sla de HTML op met dezelfde stijl geselecteerd in het exportvenster.

Elke ingebouwde Marked-stijl --- Swiss, GitHub, Manuscript en de rest --- kan worden ingesloten. [Aangepaste stijlen](Custom_Styles.html) en stijlen uit de [stijlbeheerder](Custom_Styles.html) werken op dezelfde manier.

**Extra CSS** uit {% prefspane Style %} wordt meegenomen bij HTML-export wanneer stijlen worden ingesloten. Het geëxporteerde `<body>` krijgt de `mk-has-additional-css`-klasse, zodat de door Marked herschreven selectors voor Extra CSS overeenkomen. Zie [Aangepaste CSS maken](Writing_Custom_CSS.html#additional-css-settings).

I> Sommige CSS die alleen voor de voorvertoning bedoeld is (fixed positioning, viewport-trucs, omkering van de `@media screen` voor Dark Mode) vertaalt zich mogelijk niet één-op-één buiten Marked. Open het opgeslagen bestand in een browser om dit te controleren voordat je het publiceert.

Zie [Aangepaste CSS maken](Writing_Custom_CSS.html) voor schrijfrichtlijnen.

## Metadata en MultiMarkdown-headers [metadata-and-multimarkdown-headers]

MultiMarkdown-metadata bovenaan je bronbestand kan de HTML-export beïnvloeden:

* **`Title:`** --- wordt gebruikt voor het `<title>`-element bij het opslaan van een volledig HTML-document
* **`XHTML Header:`** / **`HTML Header:`** --- voegt extra tags toe aan de geëxporteerde `<head>` (scripts, link-tags, meta-tags)
* Andere metadatasleutels worden verwerkt volgens je [Markdown-processor](Choosing_a_Processor.html)

Als je metadata gebruikt voor exportinstellingen maar de sleutels niet zichtbaar wilt hebben in andere uitvoer, plaats ze dan tussen HTML-commentaartags --- Marked vindt en verwerkt becommentarieerde metadata overal in het document. Zie [Instellingen per document](Per-Document_Settings.html).

## Documenten met meerdere bestanden [multi-file-documents]

Gebruik voor boeken en hoofdstukcompilaties [documenten met meerdere bestanden](Multi-File_Documents.html). Marked toont een voorvertoning van het samengevoegde document en exporteert één HTML-bestand vanuit het gecompileerde resultaat. Opgenomen bestanden worden gemarkeerd met HTML-commentaar dat hun bronpad toont --- handig wanneer je wilt controleren welk hoofdstuk welk onderdeel heeft aangeleverd.

## Plakken in andere toepassingen [pasting-into-other-applications]

| Bestemming | Aanbevolen aanpak |
| :-- | :-- |
| Blog/CMS met eigen thema | **HTML kopiëren** (fragment, zonder ingesloten Marked-CSS) |
| Statische site of archief | **HTML opslaan** met **Stijl opnemen in uitvoer** |
| E-mail of bestandsdeling (één bijlage) | **HTML opslaan** met **Lokale afbeeldingen insluiten** |
| WordPress, Ghost, Notion, enz. | **HTML kopiëren**; schakel **Afbeeldingen insluiten bij HTML kopiëren** in als de editor lokale paden niet kan omzetten |
| Verdere bewerking in een code-editor | **HTML opslaan** zonder ingesloten stijl, of kopieer het fragment en verpak het handmatig |

[Rich Text kopiëren](Exporting.html#rtfexportoptions) (gear-menu) is een alternatief wanneer de doeltoepassing opgemaakte tekst accepteert in plaats van HTML-broncode.

## Gerelateerde onderwerpen [related-topics]

* [Exporteren](Exporting.html) --- exportpaneel, profielen en andere formaten
* [EPUB-export](EPUB_Export.html) --- e-bookuitvoer met ingesloten CSS
* [Live Markdown-voorvertoning op de Mac](Live_Markdown_Preview_on_Mac.html) --- voorvertoningsworkflow vóór export
* [Aangepaste stijlen](Custom_Styles.html) en [Instellingen: Exporteren](Settings_Export.html)
* [HTML-specifieke instellingen](HTML_Specific_Settings.html) --- processoropties voor HTML-uitvoer
* [AppleScript-export](AppleScript_Support.html) --- HTML kopiëren en opslaan automatiseren

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
