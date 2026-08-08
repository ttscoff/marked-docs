# <%= @title %>

Bekijk uw documenten *op uw* manier.

## Aangepaste stijlen gebruiken [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

De eenvoudigste manier om Custom Stijlen te verkennen is via de
[Custom Style Gallery][2]. Van daaruit kunt u bladeren door de
beschikbare stijlen in actie, installeer ze met een klik op a
knop, en zelfs [submit your own creations][6] voor
inclusie.

Om aangepaste stylesheets van uw lokale schijf toe te voegen aan Marked,
gebruik de {% prefspane Style %}. Er zullen nieuwe stijlen worden toegevoegd
de vervolgkeuzemenu's in Vensterinstellingen en in elk venster,
en krijgt een naam op basis van de basisbestandsnaam van het CSS-bestand
toegevoegd. Bewaar uw aangepaste CSS-bestanden op een veilige plaats op uw computer
rijden. Als ze zich op uw schijf verplaatsen, worden ze verwijderd
Marked totdat je ze opnieuw toevoegt vanaf de nieuwe locatie. Het is
een goed idee om geopende documenten te sluiten en de stijl te verwijderen
uit Instellingen voordat u een CSS-bestand verwijdert of hernoemt dat wordt gebruikt door
Marked. Als je het niet doet, gaat er niets kapot, maar het bespaart wel
enige verwarring.

Voeg Custom Stijlen toe met behulp van de Stijlmanager met de knop Toevoegen, of door een of meer CSS-bestanden naar de Instellingen te slepen
venster.

## Stijlen beheren met de Stijlmanager [managing-styles-with-the-style-manager]

Door de Style Manager te starten, beschikt u over één plek waar u alle ingebouwde apparaten kunt beheren
en aangepast thema. Klik op de knop **Stijlen beheren…** in de {% prefspane Style %}
ruit,
of zet gewoon CSS-bestanden neer in het voorkeurenvenster --- Marked zal ze importeren,
open de Stijlmanager en selecteer de nieuw toegevoegde rij voor u. CSS slepen
bestanden rechtstreeks naar het Style Manager-venster werken ook; wanneer meerdere bestanden
worden gesleept, ziet u de overlay-update naar "N Custom stijlen toevoegen", dus het is duidelijk
u importeert een batch.

![][img-style-manager]

In de Style Manager vindt u een sorteerbare tabel met een mix van ingebouwde en
aangepaste stijlen. Elke rij biedt:

- Een **Ingeschakeld** selectievakje dat de stijl onmiddellijk aan de stijl toevoegt/verwijdert
  menu, pop-up Standaardstijl en sneltoetsen. Het uitschakelen van de huidige
  actieve stijl schakelt automatisch over naar het volgende beschikbare item.
- Een kolom **Naam** die u inline kunt bewerken; veranderingen blijven bestaan en verspreiden zich naar iedereen
  menukaart. Klik op de naam van de stijl om deze op zijn plaats te bewerken.
- Een kolom **Bron** die Ingebouwd, Custom of Gedupliceerd aanroept.
- Een **Acties**-stapel met knoppen voor **Bewerken** (opent het CSS-bestand in uw
  editor), **Dupliceren** (maakt een kopie en een nieuw CSS-bestand op schijf), **Onthullen**
  (toont het bestand in Finder) en **Verwijderen** (met opties om de verwijzing te verwijderen of
  verplaats het CSS-bestand naar de prullenmand).

De volgorde van rijen wordt gewijzigd via slepen en neerzetten, en de volgorde bepaalt ook het menu Stijl
de `⌘/#` snelkoppelingen, zodat je stijlen letterlijk naar de slots kunt slepen
jij wilt. Je kunt ook externe CSS-bestanden naar specifieke posities slepen; de druppel
indicator bepaalt waar de nieuwe stijl wordt ingevoegd.

### Livevoorbeeld [live-preview]

Het rechterdeelvenster bevat een voorbeeld dat de geselecteerde stijl weergeeft
in een volledig HTML document met een uitgebreide reeks koppen, lijsten, tabellen, codeblokken, enz. De
preview gebruikt de daadwerkelijke CSS op schijf, dus bewerkingen die u in uw externe editor aanbrengt, worden onmiddellijk bijgewerkt. Een selectievakje schakelt het voorbeeld van de donkere modus in of uit.

U kunt aanvullende stijlen vinden voor gebruik (of als voorbeelden voor
uw eigen maken) [on GitHub][1] (zie de [examples][2] voor
een snelle blik op wat er is). Zie [Creating Custom CSS][3]
voor details en tips.

## Extra CSS [additional-css]

Onder de {% prefspane Style %} vindt u een optie
getiteld Extra CSS met een knop met het label 'CSS bewerken'.
Als u op deze knop klikt, wordt een venster geopend waarin u kunt toevoegen
universele CSS-regels die op alle stijlen worden toegepast. Let op
die specificiteit van de regels kan daarbij belangrijk zijn
waarbij een deel van de standaardstijlen van Marked wordt overschreven. Het hoofdlichaam
van het document is verpakt in een div met de id "#wrapper".
Het kan eenvoudiger zijn om een selector hiermee vooraf te laten gaan
overschrijvingen, bijvoorbeeld:

#wrapper img { breedte: 100%; hoogte: automatisch; }

CSS in dit veld wordt op elk document toegepast, nee
het maakt niet uit welke stijl het gebruikt. Als u aangepast wilt toepassen
CSS gebaseerd op voorwaardelijke overeenkomsten, gebruik Set Style, Insert
CSS-bestand, of CSS-acties invoegen in {% prefspane Processor %}
Custom Regels.

## Afdrukken en PDF exporteren [print-and-pdf-export]

Marked injecteert een ingebouwd `@media print` blok (`mkprintstyles`) op elke
voorbeeld. Het stelt standaardinstellingen in, zoals een **10pt**-basis op `html`, `body`, en
`#wrapper` (of de grootte van **Custom lettergrootte voor exporteren/afdrukken** in
{% prefspane Export %} wanneer die optie is ingeschakeld), en normaliseert de alinea
tekst met `p { font-size: 1em; }` en `li p { font-size: 1em; }` dus
Regels voor alleen scherm, zoals `p { font-size: 1.1429em; }` blazen de hoofdtekst niet op
in PDFs en afgedrukte uitvoer.

PDF export maakt gebruik van gedrukte media op de verborgen WebView die wordt gebruikt voor het genereren, dus
`@media print { ... }` regels in uw stylesheet zijn op dezelfde manier van toepassing als voor
afdrukken.

Voeg expliciete regels toe om formaten in te stellen die afwijken van de afdrukstandaarden van Marked
binnen `@media print` in uw aangepaste CSS (of in aanvullende CSS). Gebruik
`!important` wanneer u de geïnjecteerde afdrukstijlen van Marked moet overschrijven --- voor
voorbeeld:

```css
@media afdrukken {
  #wikkel p,
  lichaam p,
  p {
    lettergrootte: 9pt !belangrijk;
    lijnhoogte: 1,4 !belangrijk;
  }

h1 {
    lettergrootte: 16pt !belangrijk;
  }
}
```

Regels zonder `!important` kunnen verliezen van latere regels in `mkprintstyles` of van
andere niet-gekwalificeerde selectors in uw blad die nog steeds van toepassing zijn in gedrukte vorm. Zetten
Alleen print-aanpassingen in `@media print` (in plaats van alleen in schermregels) blijven behouden
het voorbeeld- en exportgedrag is gemakkelijker om over te redeneren.

## CSS-wijzigingen bekijken [watching-css-changes]

U kunt een vakje aanvinken in de sectie Custom Stijlen van de {% prefspane Style %}
om Marked het actieve CSS-bestand te laten bekijken
naast het Markdown bestand dat je aan het bewerken bent. Wanneer
Als er wijzigingen in beide bestanden worden gedetecteerd, wordt het voorbeeld weergegeven
bijwerken. Dit is handig voor het bewerken van aangepaste stijlen zonder
voortdurend verfrissend en kan ook worden gebruikt voor eenvoudig internet
ontwikkelingstaken.

Dit is ook handig voor wat basiswerk voor webontwerp en CSS
experimenteren (zoals het maken van aangepaste stijlen). Laad een
Markdown bestand met alle markeringen die u wilt opmaken
Maak bijvoorbeeld een aangepaste stijl en bekijk de preview live
verandert terwijl u het bewerkt.

## Aangepaste CSS schrijven [writing-custom-css]

Als u bekend bent met CSS, kunt u uw eigen stijl creëren
bladen voor gebruik in Marked. Zie [Writing Custom CSS][3] voor
details. Overweeg elke keer dat u iets nieuws creëert
[submitting it][6] naar de [gallery][2] om te delen met anderen
gebruikers. Zorg ervoor dat u de basisbeginselen behandelt die in de gids worden vermeld, en
voeg de metadata-opmerking bovenaan toe.

### Automatische Custom Stijlen met StyleStealer [automatic-custom-styles-with-stylestealer]

U kunt zelfs automatisch een stijl genereren op basis van een
bestaande website met behulp van de [Style Stealer][4]. Hierdoor kunt u een webpagina laden en de berekende stijlen ophalen voor alle belangrijke elementen gevonden in Markdown, en deze vervolgens opslaan in een aangepaste stijl.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Beheer Custom Stijlen (hernoemen, opnieuw ordenen, dupliceren en verwijderen) vanuit de [Style Manager](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

