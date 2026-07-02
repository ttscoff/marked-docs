# <%= @title %>

## Toelichtingen

## Beer/Obsidiaan ##

Marked ondersteunt callouts met de syntaxis die wordt gebruikt door Obsidian en Bear, wat een speciaal opgemaakte blokcitaat is:

> [!NOTE] Noteer de titel
	> Aanvullende tekst

De "NOTE" in `[!NOTE]` is niet hoofdlettergevoelig. Het kan een van de volgende zijn:

- OPMERKING
- SAMENVATTING, SAMENVATTING, TLDR
- INFO
- TODO
- TIP, HINT, BELANGRIJK
- SUCCES, CONTROLEER, KLAAR
- VRAAG, HULP, FAQ
- WAARSCHUWING, VOORZICHTIG, AANDACHT
- FALEN, FALEN, VERMIST
- GEVAAR, FOUT
- BUIG
- VOORBEELD
- CITEER, CITE

Hiermee worden speciaal opgemaakte blokken gemaakt.

U kunt een `+` of `-` gebruiken om de callout samenvouwbaar te maken. Een plusteken (`+`) betekent dat de callout samenvouwbaar is, maar standaard wordt geopend. Een minteken (`-`) betekent dat de callout samenvouwbaar is, maar standaard gesloten is.

![Callouts in Marked][callouts]

[callouts]: images/callouts-800.jpg @2x width=800

### Xcode-speeltuin ###

Bij het bekijken van Xcode Playground-bestanden ondersteunt Marked de native Xcode Playground callout-syntaxis:

- Let op: optionele titel
	Highlight-inhoud komt hier terecht.

Het callout-type (bijvoorbeeld 'Let op') is niet hoofdlettergevoelig en kan een van de volgende Xcode Playground-callout-typen zijn:

- **Let op** - Opgemaakt als info-bijschrift
- **Auteur** - Bijschrift metagegevens
- **Auteurs** - Bijschrift metagegevens
- **Bug** - Fout/gevaar-oproep
- **Complexiteit** - Toelichting in notitiestijl
- **Copyright** - Bijschrift metagegevens
- **Custom Toelichting** - Toelichting in voorbeeldstijl
- **Datum** - Bijschrift metagegevens
- **Voorbeeld** - Voorbeeldbijschrift
- **Experiment** - Toelichting in tipstijl
- **Belangrijk** - Toelichting in infostijl
- **Invariant** - Toelichting in notitiestijl
- **Opmerking** - Toelichting bij notitie
- **Voorwaarde** - Toelichting in notitiestijl
- **Postcondition** - Toelichting in notitiestijl
- **Opmerking** - Toelichting in notitiestijl
- **Vereist** - Toelichting in notitiestijl
- **Zie ook** - Toelichting in infostijl
- **Sinds** - Bijschrift metagegevens
- **Versie** - Bijschrift metagegevens
- **Waarschuwing** - Waarschuwingstekst

De optionele titel na de dubbele punt wordt gebruikt als bijschrifttitel. Als er geen titel is opgegeven, wordt de naam van het callouttype als titel gebruikt.

De inhoud van de callout volgt onmiddellijk op de volgende regel (geen lege regel vereist). De inhoud gaat door tot een lege regel, de volgende toelichting, een omheind codeblok of het einde van het document.

Voorbeeld:

````afwaardering
- Belangrijk: prestatienota
Dit algoritme heeft O(n log n) complexiteit.

- Voorbeeld: snel sorteren
Hier ziet u hoe u het kunt implementeren:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

Je kunt de titel ook geheel weglaten:

- Waarschuwing
	Dit is een waarschuwing zonder aangepaste titel.

Deze highlights worden automatisch geconverteerd naar de highlight-indeling van Marked en op de juiste manier vormgegeven. Het oorspronkelijke callout-type blijft behouden in het `data-callout` attribuut, waardoor indien gewenst een aangepaste CSS-stijl mogelijk is.

> Deze functie werkt alleen bij het bekijken van voorbeelden van Xcode Playground-bestanden (`.playground`). Normale markdown-bestanden verwerken deze syntaxis niet.


## Inhoudsopgave

Met `<!--TOC-->` kunt u opgeven waar in het document de inhoudsopgave moet verschijnen. Als dit is ingesteld, overschrijft dit de optie in Voorkeuren en wordt het altijd weergegeven in het voorbeeldvenster, evenals bij het opslaan en afdrukken. De inhoudsopgave wordt slechts één keer weergegeven, zelfs als de inhoud meerdere `<!--TOC-->`-specificaties bevat.

Als u `max#` aan de bovenstaande tag toevoegt (waarbij # een cijfer van 1-5 is), wordt de diepte van de weergegeven inhoudsopgave bepaald. `<!--TOC max2-->` zal bijvoorbeeld alleen headers van het eerste en tweede niveau in de lijst weergeven. U kunt ook een minimaal headerniveau opgeven met `<!--TOC min2-->`. Maximum- en minimumwaarden zijn gebaseerd op werkelijke kopniveaus, niet op geneste niveaus. Maximaal en minimaal kunnen samen worden gebruikt.

Marked herkent ook MultiMarkdown-stijl `<!--MKPH0-->` en Pandoc-stijl `<!--MKPH1-->`, waarbij `2-6` het bereik is van de minimale en maximale niveaus van headers die moeten worden opgenomen.

Standaard wordt de inhoudsopgave afgedrukt op de eerste pagina van het document als "Inhoudsopgave afdrukken" is ingeschakeld onder {% prefspane Export %}. Als er een markering in het document aanwezig is, wordt deze op dat punt geplaatst.

I> U kunt het type nummering of letters opgeven voor elk niveau van een geneste inhoudsopgavehiërarchie in {% prefspane Export %}.

## Pagina-einden

U kunt een pagina-einde forceren voor print/PDF-uitvoer met behulp van de syntaxis:

```html
<!--BREAK-->
```

Plaats het token op zichzelf op een regel en het genereert markeringen die op dat punt een nieuwe pagina forceren. Marked begrijpt ook het Leanpub-formaat:

{::paginaeinde /}

## Autoscroll pauzeert [pauzeert]

Marked kan functioneren als een teleprompter met behulp van de [Autoscroll](Autoscroll.html) functie (u moet de [Teleprompter style](https://markedapp.com/styles/preview?style=teleprompter) toevoegen). Daarbij kan het handig zijn om pauzes in het document op te nemen. Doe dit met behulp van:

```html
<!--PAUSE:X-->
```

Waarbij `X` het aantal seconden is waarvoor Marked moet pauzeren. Als u dus `<!--PAUSE:15-->` invoegt, krijgt u een pauze van 15 seconden wanneer dat punt in het document het midden van het scherm bereikt.

## Bestand bevat

De inhoud van extra bestanden kan worden ingevoegd met behulp van de syntaxis:

<<[map/bestandsnaam]

Het pad naar het bestand kan relatief zijn ten opzichte van het indexbestand of absoluut. Inclusief kan worden genest; u kunt dezelfde syntaxis gebruiken in een bijgevoegd bestand. Als u relatieve paden gebruikt, moeten de opnames in geneste bestanden relatief zijn ten opzichte van dat bestand. ***Echter*** MultiMarkdown verwerkt alles op basis van de locatie van het eerste geopende bestand, dus alle afbeeldingspaden of andere insluitingen moeten relatief zijn ten opzichte van het eerste bovenliggende bestand, zelfs als ze in onderliggende documenten voorkomen.

MultiMarkdown metadata en YAML headers worden automatisch verwijderd uit de opgenomen bestanden voordat ze worden weergegeven. Dit voorkomt dat de kopteksten in het document verschijnen, maar houd er rekening mee dat metagegevens zoals "basiskopniveau" in de opgenomen documenten worden genegeerd.

T> Houd er rekening mee dat u bij het bekijken van documenten met opgenomen bestanden "I" (shift-i) kunt typen om te zien welk opgenomen bestand zich in het zichtbare gebied bevindt.

Zie ["Multi-File Documents"][ext] voor meer informatie.

[ext]: Multi-File_Documents.html

## Inclusief code

Marked kan externe bestanden als code opnemen met een syntaxis die vergelijkbaar is met de bovenstaande bestandsindeling:

<<(map/bestandsnaam)

Let op de haakjes in plaats van vierkante haakjes. Voor compatibiliteit met de Leanpub-syntaxis herkent Marked ook een voorafgaande reeks vierkante haakjes die een titel bevatten, maar op dit moment wordt er in Marked niets mee gedaan:

<<[Code title](folder/filename)

De inhoud van het opgegeven bestand wordt ingevoegd in een precodeblok in uw document en is beschikbaar voor automatische syntaxisaccentuering als dit is ingeschakeld. Codeblokken kunnen niet worden genest en worden niet verwerkt met MultiMarkdown. Custom-processors worden nog steeds over het gemaakte pre>codeblok uitgevoerd.

## Inclusief onbewerkte tekst of html

E> **Opmerking:** Deze functie is voor gevorderde gebruikers.

Als u onbewerkte HTML of andere tekst wilt opnemen die niet door MultiMarkdown (of uw aangepaste processor) mag worden verwerkt, kunt u accolades (`{}`) gebruiken om een ​​bestand toe te voegen *na* het verwerken van de rest van het document:

<<{map/raw_bestand.html}

Er wordt geen include-syntaxis herkend in deze bestanden (geen nesting) en de **onbewerkte** inhoud van het bestand wordt ingevoegd in de uiteindelijke HTML uitvoer. Dit is geweldig voor het invoegen van HTML zonder dat de tekstverwerker vastloopt of dat dingen worden geconverteerd/geëscaped als u dat niet wilt, maar wees voorzichtig, want er zijn weinig waarborgen om ervoor te zorgen dat de opmaak van het document behouden blijft rond wat u invoegt.