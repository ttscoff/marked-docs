# <%= @title %>

Marked heeft een ingebouwde stijleditor en kan aangepaste CSS-bestanden toepassen.

Je kunt de editor gebruiken om prachtige stijlen te maken, of als je net genoeg CSS kent om gevaarlijk te zijn, kun je Marked eruit laten zien zoals jij dat wilt.

## Aan de slag [getting-started]

Er is een galerij met Custom Styles, gemaakt door de ontwikkelaar en door gebruikers, op [markedapp.com/styles](https://markedapp.com/styles/). In de galerij kun je stijlen rechtstreeks in Marked bekijken en installeren. Elke geïnstalleerde stijl kan in de Finder worden getoond voor onderzoek en aanpassing. De galerij kan worden geopend met een interne viewer via {% appmenu Style, Generate a Custom Style %}, of klik op het potlood- (bewerk-)icoon naast een bewerkbare stijl in de Style Manager. Als je een ingebouwde stijl wilt bewerken, moet je deze eerst dupliceren in de manager.

Er is ook een [repository voor Custom Styles](https://github.com/ttscoff/MarkedCustomStyles) op GitHub met voorbeelden. Kijk gerust rond, gebruik ze, en draag er iets aan bij. Als je jouw thema verspreidt op basis van een van de basisthema's, voeg jezelf dan gerust toe aan de credits als bijdrager.

Met de mogelijkheid van Marked om aangepaste CSS-bestanden te gebruiken, zijn de mogelijkheden om je Preview aan te passen vrijwel onbeperkt. Alle CSS3-opties die in Safari werken, werken ook in Marked. Bij standaard Markdown-bestanden in Marked hoef je maar met een paar HTML-elementen rekening te houden; alle inhoud staat in een div met de id "wrapper", de rest wordt bepaald door je documentopmaak.

Als je voor persoonlijk gebruik ontwerpt, gelden er geen regels. Schakel CSS-tracking in met het selectievakje onder de aangepaste CSS-selector, en wanneer je je aangepaste CSS bewerkt en opslaat, wordt de preview bijgewerkt.

**Er is een [skeletonthema beschikbaar](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) om mee te beginnen.**

Als je van plan bent je CSS-creatie te delen, zijn er een paar punten waar je rekening mee moet houden. Ten eerste zijn er enkele body-classes waar stijlen op toegepast moeten worden:

## Body-classes [body-classes]

De volgende stijlen moeten worden opgenomen in elke CSS die je met Marked wilt delen. Met de body-classes kun je elke selector onder verschillende voorkeursopties targeten en aanpassen.

### Geïnverteerd [inverted]

Wanneer de gebruiker {% appmenu Preview, Dark Mode %} selecteert, wordt de class "inverted" toegevoegd aan de body-tag. Hiermee kun je de hoogcontrast-stijlen (licht op donker) targeten.

Je wilt geïnverteerde stijlen alleen op de preview toepassen, niet op afdrukken, dus gebruik een media query (@media screen) om dit te beperken. Onderstaande code is redelijk algemeen bruikbaar en in de meeste gevallen kun je hem gewoon in je stylesheet plakken voor compatibiliteit, maar pas hem gerust aan naar wens.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poëzie [poetry]

De gebruiker kan kiezen of tekst met tab-inspringing als poëzie of als code wordt behandeld. Het enige verschil is dat pre/code-blokken wat, laten we zeggen, poëtischer worden vormgegeven wanneer de poëziemodus is gekozen. De class "poetry" wordt toegepast op de body-tag.

Wees zo creatief als je wilt met de opmaak, maar hier is een basissnippet:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Speciale gevallen [special-cases]

Ook tabellen, Figure/Figcaption, en het speciale geval van `a.footnote` en `div.footnotes>a` verdienen aandacht. Er zijn geen vaste regels voor hoe je hiermee omgaat, maar bekijk de standaardstijlen voor een idee van welke CSS-regels Marked nodig heeft.

De standaard tabelopmaak in alle standaardstijlen gebruikt transparantie op de afwisselende rijen, zodat de tabel zacht overloopt in elke achtergrond. Je kunt die stijlen overnemen, of je eigen weg gaan — zorg er in elk geval voor dat je ze hebt gestileerd! Hetzelfde geldt voor figure en figcaption; voeg een afbeelding met alt-tekst toe aan een document om te zien hoe de opmaak eruitziet, en stem de stijl daarop af.

Voetnoten in een document renderen een link binnen de inhoud (a.footnote), en een div aan het einde met de bijbehorende tekst (div.footnotes). Kijk ook hier weer naar de standaardstijlen ter referentie. Om te voorkomen dat de regelhoogte verandert op regels met een voetnootverwijzingsnummer, zorg dat je iets als het volgende opneemt:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Om de terugkeerpijl op dezelfde regel te houden, neem het volgende op:

```css
.footnotes p {display:inline}
```

Het is ook verstandig om een algemene regel voor alle afbeeldingen op te nemen, zodat ze binnen de breedte van de pagina blijven. Iets als:

```css
#wrapper img { max-width: 100% }
```

Als je thema extra padding of een vaste breedte heeft, pas de max-width daarop aan.

## Afdrukstijlen [printstyles]

Zorg dat je afdrukstijlen opneemt die achtergrondkleuren, vaste scrolling en preview-only UI-elementen verwijderen. Marked biedt twee manieren om afdrukken en PDF-uitvoer te targeten.

### `@media print` [media-print]

Standaard CSS-afdrukregels gelden wanneer je vanuit Marked afdrukt, of wanneer PDF-export print-media gebruikt:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### De class `.mkprinting` [the-mkprinting-class]

Wanneer Marked een document voorbereidt voor **PDF-export** of **Afdrukken/PDF-preview** ({% kbd cmd P %}), voegt het de class `mkprinting` toe aan de `<body>`-tag (naast exportclasses zoals `bandw`, `breakAfterTOC`, en de `mkstyle--*`-class van je stijl). De ingebouwde thema's van Marked gebruiken deze class voor de meeste afdrukspecifieke regels, in plaats van uitsluitend op `@media print` te vertrouwen.

Bij PDF-export wordt de verborgen render-WebView vaak geladen met **screen**-media (met name bij aangepaste stijlen en [Fountain](Fountain_for_Screenwriters.html)-documenten), waardoor `@media print`-blokken in je stylesheet mogelijk **niet** van toepassing zijn op PDF-uitvoer. Regels met het voorvoegsel `.mkprinting` gelden altijd tijdens export, omdat het gewone class-selectors zijn en geen media queries.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Voor stijlen die zowel bij afdrukken vanuit de browser **als** bij PDF-export vanuit Marked moeten werken, dupliceer je de belangrijkste regels of combineer je selectors:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Custom Style versus Additional CSS.** Schrijf in een Custom Style-stylesheet `.mkprinting #wrapper …` zoals hierboven getoond. In het veld **Additional CSS** herschrijft Marked selectors vóór injectie — gebruik daar in plaats daarvan de op body gebaseerde vorm:

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Zie [Instellingen voor Additional CSS](#additional-css-settings) voor hoe dat herschrijven werkt en waarom `.mkprinting #wrapper …` alleen daar niet matcht.

Gebruik bij het debuggen van aangepaste afdruk-CSS Afdrukken/PDF-preview of exporteer naar PDF, en gebruik dan [Safari's Web Inspector](#webkitinspector) om het document te inspecteren — de `<body>` heeft dan de class `mkprinting` zolang de afdruklay-out actief is.

Het verbergen van links bij het afdrukken wordt buiten het hoofdthema om afgehandeld, zodat gebruikers kunnen kiezen om linkmarkeringen en onderstrepingen in de afdruk te verbergen. Zolang je een basisstijl voor de tekst hebt ingesteld, hoef je je hier geen zorgen over te maken.

Dus, aan de slag. Zet je bloglay-out om, maak een geweldige afdrukstijl voor PDF-documenten, of ontwerp de perfecte preview voor het type schrijfwerk dat jij doet. Als je iets moois maakt, [deel het dan met de community](https://markedapp.com/styleshare/).

## Instellingen voor Additional CSS [additional-css-settings]

In het {% prefspane Style %} kun je **Additional CSS** bewerken. Deze regels worden **toegevoegd aan het thema dat al geladen is**. Het is bewust een gedeeltelijke overlay, geen volledig thema. Als je een complete stylesheet in dit veld plakt — of dezelfde partiële sheet via [Style Manager](Custom_Styles.html) importeert alsof het een thema was — blijft alles wat de sheet niet dekt ongestyled.

### Herschrijven van selectors [additional-css-selector-rewriting]

Marked herschrijft Additional CSS-selectors vóór injectie (als `body.mk-has-additional-css …`), zodat regels binnen de scope van de preview blijven:

- Een selectoronderdeel dat al begint met `body` of `#wrapper` krijgt het voorvoegsel `body.mk-has-additional-css`, waarbij body-classes worden samengevoegd in plaats van genest.
- Elk ander selectoronderdeel krijgt de scope onder `body.mk-has-additional-css #wrapper …`.
- Voorafgaande body-classes die Marked instelt op `<body>` — waaronder `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` en `.mkstyle--*` — worden behandeld als `body` en samengevoegd met de body-selector, in plaats van genest onder `#wrapper`.

| Ingevoerd in Additional CSS | Resultaat |
| :-- | :-- |
| `#wrapper h2` | Matcht (correct binnen scope) |
| `body.mkprinting #wrapper p` | Matcht tijdens afdrukken/PDF |
| `.mkprinting #wrapper p` | Matcht **niet** (zou een geneste `#wrapper` vereisen) |
| `:root { --x: 1; }` | Matcht **niet** (gebruik liever `body` of `#wrapper` voor custom properties) |

Geef voor afdrukregels in dit veld de voorkeur aan `body.mkprinting #wrapper …`. Dezelfde visuele bedoeling kan in een Custom Style-bestand de kortere vorm `.mkprinting #wrapper …` blijven gebruiken.

Er is **geen maximumgrootte en geen controle op geldige CSS** voor Additional CSS. Marked slaat op en injecteert precies wat je invoert; ongeldige CSS heeft simpelweg geen effect in de preview.

### HTML en andere exports [additional-css-exports]

Additional CSS geldt in de live preview, Afdrukken/PDF-preview, PDF-export en **HTML-export** wanneer stijlen worden meegenomen — de geëxporteerde `<body>` krijgt de class `mk-has-additional-css`, zodat herschreven selectors matchen. DOCX, ODT en EPUB gebruiken hun eigen stylingtrajecten en passen Additional CSS niet op dezelfde manier toe.

Met [hoge specificiteit](#overridingspecificity), `@media`-queries voor afdrukken en scherm, en `body.mkprinting`-selectors (in dit veld) of `.mkprinting`-selectors (in Custom Styles), kun je met een beetje CSS-kennis vrijwel elk aspect van de styling bepalen.

## WebKit Inspector [webkitinspector]

Safari's Web Inspector is de gemakkelijkste manier om precies te zien welke HTML en CSS Marked genereert, en om live met Custom Styles te experimenteren.

### Het Develop-menu inschakelen in Safari [enabling-the-develop-menu-in-safari]

1. Open Safari en kies {% appmenu Safari, Settings… %}.
2. Selecteer het tabblad **Advanced**.
3. Schakel **Show features for web developers** in (of **Show Develop menu in menu bar** op oudere versies van macOS).

Zodra dit is ingeschakeld, verschijnt er een **Develop**-menu in de menubalk van Safari.

![Safari Develop-menu met Marked-documenten][develop-menu]

### Een Marked-document inspecteren [inspecting-a-marked-document]

1. Zorg dat er een previewvenster open staat in Marked en schakel over naar Safari.
2. Kies in de menubalk **Develop → _\<naam van je Mac\>_ → Marked → _\<documenttitel\>_**.
3. Safari opent een Web Inspector-venster gekoppeld aan de geselecteerde Marked-preview.

Van hieruit kun je:

- Het tabblad **Elements** gebruiken om de DOM binnen de `#wrapper`-div te inspecteren en te zien welke CSS-regels worden toegepast.
- Elementen in de DOM-boomstructuur aanwijzen om ze in het Marked-venster te markeren.
- De **Styles**-zijbalk gebruiken om regels live aan te passen, en werkende snippets vervolgens terug te kopiëren naar een Custom Style of **Additional CSS**.
    - Na het bewerken van CSS in het tabblad Elements kun je een overzicht van je wijzigingen krijgen via het tabblad Changes

	![Wijzigingen][css-changes]
- Het tabblad **Console** gebruiken om JavaScript uit te voeren tegen de live preview. De volledige [Marked JavaScript API](https://markedapp.com/help/jsapi/) is beschikbaar in deze console.
- Andere tabbladen zoals **Network** verkennen bij het debuggen van bronnen die door je document worden geladen.

![Een Marked-preview inspecteren met Safari Web Inspector][inspecting]

## Aangepaste CSS delen [sharing-custom-css]

Gebruik {% appmenu Style, Share a Custom Style %} om de deel-app in je webbrowser te openen. Sleep je CSS naar de dropzone (of klik om een bestand van schijf te selecteren) en upload de CSS voor je Custom Style.

Gedeelde stijlen moeten eerst door de ontwikkelaar worden goedgekeurd voordat ze in de galerij verschijnen, dus je ziet niet meteen resultaat.

## Overige tips [other-tips]

### Specificiteit overschrijven [overridingspecificity]

Binnen de Marked-preview wordt een body-class toegevoegd op basis van de bestandsnaam van de huidige stijl. Als de preview is ingesteld op "Swiss", dan komt er op de `<body>`-tag een class te staan genaamd `mkstyle--swiss`. Als je aangepaste CSS MyCustom.css heet, dan is de body-class `mkstyle--mycustom`. Je kunt dit vóór de regels uit de basisstijlen gebruiken om ze te overschrijven. Voor absolute specificiteit in een regel gebruik je ook de #wrapper-ID van de container-div:

	.mkstyle--mycustom #wrapper p+p { ... }

### Opmaak van de inhoudsopgave [table-of-contents-styling]

Als je het token `<!--toc-->` gebruikt om [een inhoudsopgave in te voegen](Special_Syntax.html#tableofcontents), kun je de instellingen voor de niveau-indicatoren van de inhoudsopgave in een Custom Style overschrijven door "#wrapper" te gebruiken voor extra specificiteit:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Hierdoor gebruiken alle lijstitems in de inhoudsopgave een vierkant opsommingsteken in plaats van wat in Settings is ingesteld, zolang je Custom Style actief is.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
