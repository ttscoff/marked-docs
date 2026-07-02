# <%= @title %>

Marked heeft een ingebouwde stijleditor en kan aangepaste CSS-bestanden toepassen.

Je kunt de editor gebruiken om prachtige stijlen te maken, of als je net genoeg CSS kent om gevaarlijk te zijn, kun je Marked er zo uit laten zien als je wilt.

## Aan de slag

Er is een galerij met Custom stijlen gemaakt door de ontwikkelaar en door gebruikers op [markedapp.com/styles](https://markedapp.com/styles/). In de galerij kunt u stijlen direct in Marked bekijken en installeren. Elke geïnstalleerde stijl kan in Finder worden weergegeven voor onderzoek en aanpassing. De galerij kan worden geopend met behulp van een interne viewer met {% appmenu Style, Generate a Custom Style %}, of klik op het potloodpictogram (bewerken) naast een bewerkbare stijl in de Stijlmanager. Als u wilt bewerken een ingebouwde stijl heeft, moet u deze eerst dupliceren in de manager.

Er is ook een [repository for Custom Styles](https://github.com/ttscoff/MarkedCustomStyles) op GitHub met voorbeelden. Voel je vrij om daar te bladeren, te gebruiken en bij te dragen. Als u uw thema distribueert op basis van een van de basisthema's, kunt u uzelf als bijdrager aan de aftiteling toevoegen.

Met de mogelijkheid van Marked om aangepaste CSS-bestanden te gebruiken, zijn de mogelijkheden eindeloos bij het aanpassen van uw voorbeeld. Alle CSS3-opties die in Safari werken, werken ook in Marked. Met standaard Markdown bestanden in Marked zijn er slechts een paar HTML elementen die u moet verwerken; alle inhoud bevindt zich in een div met de id "wrapper", al het andere wordt bepaald door uw documentopmaak.

Als u ontwerpt voor persoonlijk gebruik, zijn er geen regels. Schakel CSS-tracking in met het selectievakje onder de aangepaste CSS-kiezer. Wanneer u uw aangepaste CSS bewerkt en opslaat, wordt het voorbeeld bijgewerkt.

**Een [skeleton theme is available](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) om aan de slag te gaan.**

Als u van plan bent uw CSS-creatie te delen, zijn er een paar punten die u moet bespreken. Ten eerste zijn er enkele lichaamsklassen waarop stijlen moeten worden toegepast:

## Lichaamslessen

De volgende stijlen moeten worden opgenomen in elke Marked CSS die kan worden gedeeld. Met de lichaamsklassen kunt u elke selector onder verschillende voorkeursopties targeten en wijzigen.

### Omgekeerd

Wanneer de gebruiker {% appmenu Preview, Dark Mode %} selecteert, wordt een klasse "geïnverteerd" toegevoegd aan de body-tag. U kunt dit gebruiken om de contrastrijke, licht op donkere stijlen te targeten.

U wilt alleen omgekeerde stijlen toepassen op het voorbeeld en niet op afdrukken. Gebruik daarom een ​​mediaquery (@media screen) om deze te beperken. De onderstaande code is redelijk universeel en in de meeste gevallen kunt u deze gewoon in uw stylesheet plaatsen voor compatibiliteit, maar u kunt deze gerust aanpassen.

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

### Poëzie

De gebruiker kan kiezen of de met tabs ingesprongen tekst poëzie of code is. Het enige verschil is dat pre/code-blokken poëtischer worden vormgegeven als de poëziemodus wordt gekozen. De klasse 'poëzie' wordt toegepast op de body-tag.

Wees zo creatief als je wilt met de opmaak, maar hier is een basisfragment:

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

## Speciale gevallen

Tabellen, figuur/figuurbijschrift en het speciale geval van `a.footnote` en `div.footnotes>a` moeten ook in overweging worden genomen. Er zijn geen vaste regels voor hoe je ermee omgaat, maar kijk eens naar de standaardstijlen om een ​​idee te krijgen welke CSS-regels Marked nodig hebben.

De standaardtabelstijl voor alle standaardstijlen maakt gebruik van transparantie op de afwisselende rijen, zodat deze zacht overvloeit in elke achtergrond. Je kunt die stijlen kopiëren, of je eigen route volgen, zorg er wel voor dat je ze hebt gestyled! Hetzelfde voor figuur en bijschrift; voeg een afbeelding toe aan een document met alternatieve tekst om te zien hoe de opmaak eruit zal zien en op de juiste manier zal worden vormgegeven.

Voetnoten in een document geven een link binnen de inhoud weer (a.footnote) en een div aan het einde met de tekst waarnaar wordt verwezen (div.footnotes). Zie nogmaals de standaardstijlen ter referentie. Om te voorkomen dat de regelhoogte wordt gewijzigd op regels die een voetnootreferentienummer bevatten, moet u iets opnemen als:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Om de retourpijl op dezelfde lijn te houden, voegt u het volgende toe:

```css
.footnotes p {display:inline}
```

Het is ook een goed idee om voor alle afbeeldingen een algemene regel op te nemen, zodat ze binnen de breedte van de pagina blijven. Zoiets als:

```css
#wrapper img { max-width: 100% }
```

Als uw thema extra opvulling of een vaste breedte heeft, past u de maximale breedte aan zodat deze past.

## Afdrukstijlen

Zorg ervoor dat u afdrukstijlen opneemt die eventuele achtergrondkleuren, vast scrollen, enz. verwijderen. Gebruik "@media print" om deze binnen uw thema te definiëren.

Het verbergen van links in gedrukte vorm gebeurt buiten het hoofdthema, waardoor gebruikers ervoor kunnen kiezen om linkaccenten en onderstrepingen verborgen te houden op de afdruk. Zolang u een basisstijl voor de tekst heeft ingesteld, hoeft u zich hier geen zorgen over te maken.

Dus, ga ervoor. Converteer uw blogthema, creëer een geweldige printstijl voor PDF documenten, of maak de perfecte preview voor de schrijfstijl die u gebruikt. Als je iets geweldigs maakt, laat het me weten, dan post ik het voor de hele Marked community.

## Aanvullende CSS-instellingen

In de {% prefspane Style %} kunt u aanvullende CSS bewerken. Deze stijlen worden aan elk geladen thema toegevoegd en kunnen worden gebruikt om universele wijzigingen in alle thema's aan te brengen.

Met [high specificity](#overridingspecificity) en @media-query's voor afdrukken en scherm kunt u met een beetje CSS-kennis vrijwel elk stijlaspect beheersen.

## WebKit-inspecteur

Safari's Web Inspector is de gemakkelijkste manier om precies te zien wat HTML en CSS Marked genereert, en om live met Custom Stijlen te experimenteren.

### Het ontwikkelmenu inschakelen in Safari

1. Open Safari en kies {% appmenu Safari, Settings… %}.
2. Selecteer het tabblad **Geavanceerd**.
3. Schakel **Functies tonen voor webontwikkelaars** in (of **Toon ontwikkelmenu in menubalk** op oudere macOS-versies).

Eenmaal ingeschakeld, verschijnt er een **Ontwikkel**-menu in de menubalk van Safari.

![Safari Develop menu showing Marked documents][develop-menu]

### Een Marked document inspecteren

1. Schakel over naar Safari terwijl er een voorbeeldvenster geopend is in Marked.
2. Kies in de menubalk **Ontwikkelen → _\<uw Mac-naam\>_ → Marked → _\<documenttitel\>_**.
3. Safari opent een Web Inspector-venster dat is gekoppeld aan het geselecteerde Marked voorbeeld.

Vanaf hier kunt u:

- Gebruik het tabblad **Elementen** om de DOM binnen de `#wrapper` div te inspecteren en te zien welke CSS-regels worden toegepast.
- Beweeg de muis over elementen in de DOM-structuur om ze in het venster Marked te markeren.
- Gebruik de zijbalk **Stijlen** om de regels live aan te passen en kopieer vervolgens de werkfragmenten terug naar een Custom stijl of **Aanvullende CSS**.
    - Nadat u CSS op het tabblad Elementen hebt bewerkt, kunt u een samenvatting van uw bewerkingen krijgen door het tabblad Wijzigingen te selecteren

![Changes][css-changes]
- Gebruik het tabblad **Console** om JavaScript uit te voeren op de live preview. De volledige [Marked JavaScript API](https://markedapp.com/help/jsapi/) is beschikbaar in deze console.
- Verken andere tabbladen zoals **Netwerk** bij het opsporen van fouten in bronnen die door uw document zijn geladen.

![Inspecting a Marked preview with Safari Web Inspector][inspecting]

## Custom CSS delen

Gebruik {% appmenu Style, Share a Custom Style %} om de deelapp in uw webbrowser te openen. Sleep uw CSS naar de neerzetzone (of klik om te selecteren vanaf schijf) en upload de CSS voor uw Custom stijl.

Gedeelde stijlen moeten door de ontwikkelaar worden goedgekeurd voordat ze in de galerij verschijnen, dus je ziet geen onmiddellijke resultaten.

## Andere tips

### Overschrijvende specificiteit

Binnen de Marked preview wordt een body-klasse toegevoegd, gebaseerd op de bestandsnaam van de huidige stijl. Als het voorbeeld is ingesteld op "Swiss", dan zal er een klasse op de `<body>` tag staan ​​met de naam `mkstyle--swiss`. Als uw aangepaste CSS MyCustom.css heet, is de body-klasse `mkstyle--mycustom`. U kunt dit gebruiken vóór de regels die in de basisstijlen zijn gedefinieerd, om deze te overschrijven. Om absolute specificiteit in een regel te krijgen, gebruikt u ook de #wrapper ID uit de container-div:

.mkstyle--mycustom #wrapper p+p { ... }

### Inhoudsopgave styling

Als u het token `<!--toc-->` gebruikt voor [insert a table of contents](Special_Syntax.html#tableofcontents), kunt u de instellingen voor niveau-indicatoren voor de inhoudsopgave in een Custom stijl overschrijven met behulp van de "#wrapper" om de specificiteit te vergroten:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Dit zou ervoor zorgen dat alle lijstitems in de inhoudsopgave een vierkante opsommingsteken gebruiken in plaats van wat is gedefinieerd in Instellingen wanneer uw Custom stijl actief is.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
