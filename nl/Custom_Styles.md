# <%= @title %>

Bekijk je documenten op *jouw* manier.

## Aangepaste stijlen gebruiken [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

De eenvoudigste manier om Aangepaste stijlen te verkennen is via de
[Custom Style Gallery][2]. Daar kun je de beschikbare stijlen in
actie bekijken, ze met één klik installeren en zelfs
[je eigen creaties insturen][6] voor opname in de galerij.

Om aangepaste stylesheets vanaf je lokale schijf aan Marked toe te
voegen, gebruik je {% prefspane Style %}. Nieuwe stijlen worden toegevoegd aan de
vervolgkeuzemenu's in de Vensterinstellingen en in elk venster, en
krijgen een naam op basis van de bestandsnaam van het toegevoegde
CSS-bestand. Bewaar je aangepaste CSS-bestanden op een veilige plek
op je schijf. Als ze op je schijf worden verplaatst, worden ze uit
Marked verwijderd totdat je ze opnieuw vanaf de nieuwe locatie
toevoegt. Het is verstandig om geopende documenten te sluiten en de
stijl in Instellingen te verwijderen voordat je een CSS-bestand dat
door Marked wordt gebruikt, verwijdert of hernoemt. Als je dat niet
doet, gaat er niets stuk, maar het voorkomt verwarring.

Voeg Aangepaste stijlen toe via de Stijlbeheerder met de knop
Toevoegen, of door een of meer CSS-bestanden naar het
instellingenvenster te slepen.

## Stijlen beheren met de Stijlbeheerder [managing-styles-with-the-style-manager]

Als je de Stijlbeheerder opent, heb je op één plek overzicht over
alle ingebouwde en aangepaste thema's. Klik op de knop **Stijlen
beheren…** in het paneel {% prefspane Style %},
of sleep gewoon CSS-bestanden naar het instellingenvenster --- Marked
importeert ze, opent de Stijlbeheerder en selecteert automatisch de
nieuw toegevoegde rij. Je kunt CSS-bestanden ook rechtstreeks naar
het venster van de Stijlbeheerder slepen; wanneer je meerdere
bestanden tegelijk sleept, verandert de overlay in "N aangepaste
stijlen toevoegen", zodat duidelijk is dat je een batch importeert.

![][img-style-manager]

In de Stijlbeheerder vind je een sorteerbare tabel met zowel
ingebouwde als aangepaste stijlen. Elke rij biedt:

- Een selectievakje **Ingeschakeld** dat de stijl direct toevoegt aan
  of verwijdert uit het Stijlmenu, het pop-upmenu Standaardstijl en
  de sneltoetsen. Als je de momenteel actieve stijl uitschakelt,
  schakelt Marked automatisch over naar de eerstvolgende beschikbare
  stijl.
- Een kolom **Naam** die je direct kunt bewerken; wijzigingen worden
  opgeslagen en doorgevoerd in alle menu's. Klik op de naam van de
  stijl om deze ter plekke te bewerken.
- Een kolom **Bron** die aangeeft of een stijl Ingebouwd, Aangepast
  of Gedupliceerd is.
- Een groep **Acties** met knoppen voor **Bewerken** (opent het
  CSS-bestand in je editor), **Dupliceren** (maakt een kopie en een
  nieuw CSS-bestand op schijf), **Onthullen** (toont het bestand in
  de Finder) en **Verwijderen** (met de mogelijkheid om alleen de
  verwijzing te verwijderen of het CSS-bestand naar de Prullenbak te
  verplaatsen).

Rijen kun je herschikken door ze te slepen, en die volgorde bepaalt
zowel het Stijlmenu als de sneltoetstoewijzingen voor `⌘/#`, zodat
je stijlen letterlijk naar de gewenste plek kunt slepen. Je kunt ook
externe CSS-bestanden naar specifieke posities slepen; de
sleepindicator bepaalt waar de nieuwe stijl wordt ingevoegd.

### Live voorbeeld [live-preview]

Het rechterpaneel toont een voorbeeld waarin de geselecteerde stijl
wordt weergegeven binnen een volledig HTML-document met een
uitgebreide set koppen, lijsten, tabellen, codeblokken, enzovoort.
Het voorbeeld gebruikt de daadwerkelijke CSS op schijf, dus
wijzigingen die je in je externe editor aanbrengt, worden direct
bijgewerkt. Een selectievakje schakelt het voorbeeld in Donkere
modus in of uit.

Extra stijlen om te gebruiken (of als voorbeeld voor het maken van
je eigen stijlen) vind je [op GitHub][1] (bekijk de
[voorbeelden][2] voor een snelle blik op wat daar te vinden is). Zie
[Aangepaste CSS maken][3] voor details en tips.

## Extra CSS [additional-css]

Onder {% prefspane Style %} vind je een optie met de naam Extra CSS, met een knop
met het label "CSS bewerken". Als je op deze knop klikt, opent een
venster waarin je universele CSS-regels kunt toevoegen die op alle
stijlen worden toegepast. Let op: de specificiteit van de regels kan
belangrijk zijn wanneer je een deel van Markeds standaardstijl wilt
overschrijven. De hoofdtekst van het document wordt omsloten door
een div met de id "#wrapper". Door een selector hiermee te laten
voorafgaan, kun je overschrijvingen eenvoudiger maken, bijvoorbeeld:

    #wrapper img { width: 100%; height: auto; }

CSS in dit veld wordt **toegevoegd aan het actieve thema**. Het is
geen vervanging voor een volledige Aangepaste stijl: een stylesheet
die alleen voor dit veld is geschreven, is bewust onvolledig, en als
je deze via de Stijlbeheerder als thema zou laden, zou alles wat
niet wordt behandeld zonder opmaak blijven.

Marked **herschrijft** selectors in Extra CSS voordat ze worden
toegepast. Voorloop-body-classes zoals `.mkprinting` worden samengevoegd
met `body` in plaats van genest onder `#wrapper`, dus printregels in
dit veld moeten `body.mkprinting #wrapper …` gebruiken (zie [Aangepaste CSS
maken](Writing_Custom_CSS.html#additional-css-settings) voor de
volledige herschrijfregels). Er is geen limiet aan de grootte en er
wordt niet gecontroleerd of de CSS geldig is --- ongeldige CSS heeft
simpelweg geen effect.

CSS in dit veld wordt toegepast op elk document, ongeacht welke
stijl er wordt gebruikt --- inclusief HTML-export wanneer stijlen
worden meegenomen. Als je aangepaste CSS wilt toepassen op basis van
voorwaardelijke overeenkomsten, gebruik dan de acties Stijl
instellen, CSS-bestand invoegen of CSS invoegen in {% prefspane Processor %}
Aangepaste regels.

## Afdrukken en pdf-export [print-and-pdf-export]

Marked voegt in elk voorbeeld een ingebouwd blok `@media print` toe
(`mkprintstyles`). Dit blok stelt standaardwaarden in, zoals een
basisgrootte van **10pt** op `html`, `body` en `#wrapper` (of de
grootte uit **Aangepaste lettergrootte voor export/afdrukken** in
{% prefspane Export %} wanneer die optie is ingeschakeld), en normaliseert
alineatekst met `p { font-size: 1em; }` en `li p { font-size: 1em; }`, zodat schermspecifieke regels
zoals `p { font-size: 1.1429em; }` de hoofdtekst in pdf's en afdrukken niet groter maken.

Pdf-export kan gebruikmaken van **print**- of **screen**-media op de
verborgen WebView die voor het genereren wordt gebruikt. Ingebouwde
thema's gebruiken doorgaans printmedia; **aangepaste stijlen** en
[Fountain](Fountain_for_Screenwriters.html)-documenten gebruiken
vaak screenmedia, zodat de opmaak overeenkomt met het voorbeeld. Dat
betekent dat `@media print { ... }`-regels niet altijd worden toegepast tijdens
pdf-export.

Voor betrouwbare opmaak bij pdf en Afdrukken/pdf-voorbeeld laat je
selectors vooraf gaan door de klasse `mkprinting` die Marked tijdens het
exporteren toevoegt aan `<body>` (zie [Aangepaste CSS
schrijven](Writing_Custom_CSS.html#printstyles) voor details en
voorbeelden). In een **Aangepaste stijl**-bestand kun je `.mkprinting`
los gebruiken. In **Extra CSS** gebruik je de aan body gekoppelde
vorm `body.mkprinting #wrapper …`, omdat dat veld selectors herschrijft. Je kunt beide
vormen ook combineren met `@media print` wanneer je beide paden wilt
afdekken.

Om groottes in te stellen die afwijken van Markeds standaardwaarden
voor afdrukken, voeg je expliciete regels toe aan je aangepaste CSS
(of aan Extra CSS). Gebruik `!important` wanneer je de door Marked
geïnjecteerde printstijlen wilt overschrijven --- bijvoorbeeld:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

Regels zonder `!important` kunnen het afleggen tegen latere regels in
`mkprintstyles` of tegen andere ongekwalificeerde selectors in je
stylesheet die nog steeds van toepassing zijn bij het afdrukken.
Door print-specifieke aanpassingen in `@media print` en/of `.mkprinting` /
`body.mkprinting`-regels te plaatsen (in plaats van alleen in screen-regels),
blijven het gedrag van het voorbeeld en de export makkelijker te
doorgronden.

## CSS-wijzigingen volgen [watching-css-changes]

Je kunt in het gedeelte Aangepaste stijlen van {% prefspane Style %} een
selectievakje inschakelen zodat Marked, naast het Markdown-bestand
dat je bewerkt, ook het actieve CSS-bestand in de gaten houdt. Zodra
er wijzigingen in een van beide bestanden worden gedetecteerd, wordt
het voorbeeld bijgewerkt. Dit is handig om aangepaste stijlen te
bewerken zonder steeds te hoeven verversen, en kan ook worden
gebruikt voor eenvoudige webontwikkeltaken.

Dit is ook handig voor eenvoudig webdesignwerk en CSS-experimenten
(zoals het maken van aangepaste stijlen). Laad een Markdown-bestand
met alle opmaak waarvoor je een stijl wilt maken, maak een
aangepaste stijl aan en bekijk het voorbeeld live terwijl je de
stijl bewerkt.

## Aangepaste CSS schrijven [writing-custom-css]

Als je bekend bent met CSS, kun je je eigen stylesheets maken voor
gebruik in Marked. Zie [Aangepaste CSS schrijven][3] voor details.
Overweeg om, wanneer je iets nieuws maakt, [dit in te sturen][6]
naar de [galerij][2] om het met andere gebruikers te delen. Zorg
ervoor dat je de basisprincipes uit de handleiding volgt en neem de
metadata-opmerking bovenaan op.

### Automatische aangepaste stijlen met StyleStealer [automatic-custom-styles-with-stylestealer]

Je kunt zelfs automatisch een stijl genereren op basis van een
bestaande website met behulp van de [Style Stealer][4]. Hiermee kun
je een webpagina laden en de berekende stijlen ophalen voor alle
belangrijke elementen die in Markdown voorkomen, en deze vervolgens
opslaan als aangepaste stijl.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Beheer Aangepaste stijlen (hernoemen, herschikken, dupliceren en
verwijderen) via de [Stijlbeheerder](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
