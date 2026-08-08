# <%= @title %>

De Custom Stijlgenerator is een webgebaseerde tool waarmee u aangepaste stijlen voor Marked kunt maken zonder handmatig CSS te schrijven. Het biedt een visuele interface met bedieningselementen voor typografie, kleuren, spatiëring en meer, met een live voorbeeld dat wordt bijgewerkt naarmate u wijzigingen aanbrengt.

## Toegang tot de generator [accessing-the-generator]

De Stijlgenerator is verkrijgbaar op [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/). U kunt het rechtstreeks in uw webbrowser gebruiken; er is geen installatie vereist.

![Style Generator][img-style-generator]

  [img-style-generator]: images/style-generator-800.jpg @2x width=800 class=center

## Aan de slag [getting-started]

Wanneer u de generator voor het eerst opent, ziet u het volgende:

- **Voorbeeldvenster** (links): een live voorbeeld van uw stijl toegepast op voorbeelden van markdown-inhoud
- **Besturingspaneel** (rechts): alle stijlregelaars georganiseerd in secties
- **Werkbalk** (boven): Stijltitel, basisthemakiezer en CSS-importoptie

### Een basisthema kiezen [choosing-a-base-theme]

Begin door een **Basisthema** te selecteren in de vervolgkeuzelijst. Dit vormt de basis voor uw stijl; u kunt vervolgens elk aspect ervan aanpassen. Populaire opties zijn onder meer Blank (om helemaal opnieuw te beginnen), Default en verschillende ingebouwde thema's.

### Bestaande CSS importeren [importing-existing-css]

Als u een bestaand CSS-bestand heeft dat u als uitgangspunt wilt gebruiken, klikt u op **CSS importeren** en selecteert u uw bestand. De generator laadt deze stijlen en u kunt ze vervolgens wijzigen met de bedieningselementen.

## Stijlbediening [style-controls]

De generator organiseert de bedieningselementen in logische secties:

### Basistypografie [base-typography]

Beheer de fundamentele typografie-instellingen:

- **Gebruik ritme**: indien ingeschakeld, wordt een wiskundige typografische schaal gebruikt voor consistente kopgroottes en spatiëring
- **Basislettergrootte**: de hoofdlettergrootte (meestal 16px)
- **Lijnhoogte**: de afstand tussen tekstregels
- **Schaalverhouding**: de verhouding die wordt gebruikt voor de typografische schaal (is van invloed op de kopgroottes)

### Indeling [layout]

Pas de afstand en inspringing aan:

- **Wrapper Padding**: ruimte rond het inhoudsgebied
- **Alinea-inspringing**: eerste regelinspringing voor alinea's
- **Lijstinspringing**: Inspringing voor lijsten
- **Blockquote Inspringen**: linkermarge voor blokquotes

### Lettertypen [fonts]

Configureer lettertypefamilies en gewichten:

- **Koptekstlettertypen**: door komma's gescheiden lijst met lettertypen voor koppen (bijvoorbeeld 'Georgia, serif')
- **Body-lettertypen**: door komma's gescheiden lijst met lettertypen voor hoofdtekst
- **Koptekstgewicht**: lettertypegewicht voor koppen (100–900)
- **Lichaamsgewicht**: lettertypegewicht voor hoofdtekst
- **Vetgewicht**: lettertypegewicht voor vetgedrukte tekst
- **Letterafstand**: tekenafstand voor kopteksten en hoofdtekst

### Google-lettertypen [google-fonts]

Voeg Google Fonts toe aan uw stijl:

1. Typ een lettertypenaam in het zoekveld (suggesties voor automatisch aanvullen verschijnen)
2. Geef eventueel stijlen op (bijvoorbeeld "400,400i,700" voor normaal, cursief, vet)
3. Klik op **Toevoegen** om deze op te nemen
4. Gebruik **Browse Google Fonts** om de volledige catalogus met voorbeelden te verkennen

Toegevoegde lettertypen verschijnen in een lijst onder de besturingselementen. Klik op de × om ze te verwijderen.

### Kleuren [colors]

Kleuren instellen voor verschillende elementen:

- **Achtergrond**: achtergrondkleur van de pagina
- **Basistekst**: standaard tekstkleur
- **Kopkleur**: kleur voor alle kopjes (kan per kopniveau worden overschreven)
- **Bodykleur**: tekstkleur van de body
- **Linkkleur**: kleur voor links
- **Nadrukkleur**: kleur voor benadrukte tekst (`<em>`)
- **Sterke kleur**: kleur voor krachtige tekst (`<strong>`)
- **Achtergrond markeren**: achtergrondkleur voor gemarkeerde tekst (`<mark>`)

Individuele kopkleuren (H1–H6) kunnen afzonderlijk worden ingesteld. Gebruik **Reset** om een ​​overschrijving op te heffen en terug te keren naar de kopkleur.

### Donkere modus [dark-mode]

Schakel **Donkere modus** in om kleuren in de donkere modus te bekijken en te configureren. Indien ingeschakeld, zie je afzonderlijke kleurbedieningen voor varianten in de donkere modus. Stijlen voor de donkere modus zijn van toepassing wanneer `.inverted` is ingesteld op het body-element in Marked.

Gebruik **Kleuren genereren** om automatisch een palet voor de donkere modus te maken op basis van uw kleuren in de lichte modus.

### Afbeeldingen [images]

Controle van het uiterlijk van de afbeelding:

- **Max. breedte**: maximale breedte voor afbeeldingen (bijvoorbeeld "100%", "800px")
- **Randradius**: afgeronde hoeken (bijvoorbeeld "8px", "0")
- **Uitlijning**: Documentstandaard, Links, Midden of Rechts

### Blokcitaten [blockquotes]

Stijl blokcitaten:

- **Linkerrandbreedte**: dikte van de linkerrand
- **Linkerrandkleur**: Kleur van de linkerrand
- **Achtergrondkleur**: achtergrondkleur voor blokcitaten
- **Lettertype**: Normaal of Cursief
- **Linkermarge**: afstand vanaf de linkerrand
- **Geneste linkermarge**: afstand voor geneste blokaanhalingstekens (kan "overnemen")

Er zijn aparte bedieningselementen beschikbaar voor blockquotes in de donkere modus.

### Lijsten [lists]

Configureer de weergave van de lijst:

- **Lijststijlpositie**: binnen of buiten (waar opsommingstekens/cijfers verschijnen)
- **Linkermarge**: afstand vanaf de linkerrand
- **Geneste linkermarge**: afstand voor geneste lijsten (kan "overnemen")

### Definitielijsten [definition-lists]

Stijldefinitielijsten (`<dl>`, `<dt>`, `<dd>`):

- **DL-inspringing**: algehele inspringing
- **DT** (term) instellingen: lettergrootte, gewicht en stijl
- **DD** (definitie) instellingen: lettergrootte, gewicht, stijl en inspringing

### Tabellen [tables]

Uitgebreide tafelstijl:

- **Achtergrondkleur**: Tabelachtergrond
- **Randkleur**: Randkleur voor cellen
- **Tabeltekstkleur**: standaard tekstkleur in tabellen
- **Afwisselende rijen/kolommen**: schakel zebrastrepen in met aangepaste kleuren
- **Rand**: tabeloverzicht tonen/verbergen
- **Raster**: interne rasterlijnen tonen/verbergen
- **Uitlijning**: links of midden
- **Randradius**: afgeronde hoeken
- **Max. breedte**: Maximale tafelbreedte
- **Celvulling**: interne afstand
- **Koptekst**-instellingen: lettertypegewicht, -grootte en -stijl
- **Bijschrift**-instellingen: lettergrootte, -grootte, -stijl en tekstkleur

Er zijn aparte bedieningselementen beschikbaar voor tabellen in de donkere modus.

### Codeblokken [code-blocks]

Stijlcodeblokken en inlinecode:

- **Codelettertypefamilie**: Monospace-lettertypestapel
- **Achtergrond**: achtergrondkleur
- **Randkleur**: Randkleur
- **Randradius**: afgeronde hoeken
- **Wrapmodus**: Geen wrap (pre), Conserveren + wrap (pre-wrap) of Normaal (wrap)
- **Codevulling**: interne afstand

Er zijn aparte bedieningselementen beschikbaar voor codeblokken in de donkere modus.

### Voetnoten [footnotes]

Stijl voetnoten:

- **Markeringskleur**: kleur van voetnootmarkeringen
- **Tekstkleur**: Kleur van voetnoottekst
- **Tekststijl**: Normaal of Cursief

Er zijn aparte bedieningselementen beschikbaar voor voetnoten in de donkere modus.

### Slagschaduw [drop-shadow]

Slagschaduwen toevoegen aan elementen:

1. Kies schaduw **Kracht**: Zacht, Medium of Sterk
2. Selecteer op welke elementen schaduwen moeten worden toegepast:
   - Afbeeldingen
   - Codeblokken
   - Blokcitaten
   - Tafels

## Custom CSS [custom-css]

Voor geavanceerde aanpassingen die verder gaan dan de beschikbare besturingselementen, gebruikt u de knop **Custom CSS** om een ​​code-editor te openen. Alle CSS die u hier toevoegt, wordt toegevoegd aan de gegenereerde stijl en automatisch aangepast aan de documentstructuur van Marked.

De editor bevat syntaxisaccentuering en validatie: ongeldige CSS wordt gemarkeerd met foutmeldingen.

## Live voorbeeld [live-preview]

In het voorbeeldvenster wordt uw stijl weergegeven die is toegepast op voorbeelden van prijsverlagingsinhoud, waaronder:

- Koppen (H1–H6)
- Alinea's met verschillende inline-opmaak
- Tafels
- Codeblokken
- Afbeeldingen
- Lijsten (geordend en ongeordend)
- Blokcitaten
- Definitielijsten
- Voetnoten
- Takenlijsten

Wijzigingen worden in realtime bijgewerkt terwijl u de bedieningselementen aanpast.

## Opslaan en delen [saving-and-sharing]

Als je eenmaal tevreden bent met je stijl, heb je verschillende opties:

### CSS bekijken [view-css]

Klik op **CSS bekijken** om de volledige gegenereerde CSS in een popover te zien. U kunt het naar uw klembord kopiëren of bekijken voordat u het opslaat.

### CSS opslaan [save-css]

Klik op **CSS opslaan** om uw stijl als CSS-bestand te downloaden. Voordat u gaat downloaden, wordt u gevraagd om metagegevens (titel, auteur, beschrijving) in te voeren.

### Toevoegen aan Marked [add-to-marked]

Klik op **Toevoegen aan Marked** om de stijl direct toe te voegen aan uw Marked installatie. Hiervoor moet Marked actief zijn en er wordt een dialoogvenster geopend om de stijlnaam en auteursinformatie te bevestigen.

### Deel stijl [share-style]

Klik op **Stijl delen** om uw stijl te publiceren op de [Marked Style Gallery](https://markedapp.com/styles) zodat anderen deze kunnen gebruiken. U moet het volgende opgeven:

- Stijltitel
- Jouw naam
- Auteur-URL (optioneel)
- Beschrijving
- Opmerking (optioneel)

Er verschijnt een voorbeeld van uw stijl in het dialoogvenster voor delen voordat u deze publiceert.

## Metagegevens [metadata]

Gebruik het metadatagedeelte (uitbreidbaar via de pijlknop naast de stijltitel) om het volgende in te stellen:

- **Auteur**: uw naam (blijft bestaan tijdens sessies)
- **Auteur-URL**: uw website of profiel-URL
- **Beschrijving**: een beschrijving van de stijl
- **Opmerking**: aanvullende opmerkingen (niet opgenomen in gedeelde stijlen)

Deze metagegevens zijn opgenomen in de CSS-bestandskop en worden gebruikt bij het delen van stijlen.

## Tips [tips]

- Begin met een basisthema dat dicht bij uw wensen ligt en pas het vervolgens aan
- Gebruik het **Leeg**-thema als u volledige controle vanaf het begin wilt
- Schakel **Ritme** in voor wiskundig consistente typografie
- Test je stijl met de schakelaar **Donkere modus** als je van plan bent deze te ondersteunen
- Gebruik **Custom CSS** spaarzaam; aan de meeste behoeften kan worden voldaan met de ingebouwde besturingselementen
- Bekijk een voorbeeld van uw stijl met verschillende inhoudstypen voordat u deze deelt

## Browsercompatibiliteit [browser-compatibility]

De Stijlgenerator werkt het beste in moderne browsers (Chrome, Firefox, Safari, Edge). Het vereist dat JavaScript is ingeschakeld.