# <%= @title %>

Op deze pagina wordt beschreven hoe u door lange voorbeelden kunt navigeren: de [Table of Contents](#table-of-contents), [fast search](#fast-search), [bookmarks](#bookmarks-and-mini-map) en de [Mini Map](#minimap). Voor scrollsnelkoppelingen die overal van toepassing zijn (zoals {% kbd j %}/{% kbd k %}), zie [Keyboard Navigation](Interface_Features.html#keyboardnavigation) onder [Interface Features](Interface_Features.html).

## Inhoudsopgave [table-of-contents]

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Als uw document kopteksten bevat, verschijnt er een lijstknop in de werkbalk. Klik erop om de inhoudsopgave uit te vouwen; klik op een kop om naar dat gedeelte van het voorbeeld te gaan. Gebruik {% kbd j %}/{% kbd k %} (omlaag/omhoog) om door de lijst te bladeren, en {% kbd Enter %} of {% kbd o %} om naar de gemarkeerde koptekst te springen.

**Filterbalk:** Terwijl de inhoudsopgave geopend is, drukt u op {% kbd Space %} (spatiebalk) om het veld voor typen te openen. Typ een deel van de kopnaam (Marked gebruikt overeenkomsten in TextMate-stijl, u kunt bijvoorbeeld de eerste letter van elk woord typen) en druk op Tab ({% kbd ⇥ %}) of de pijl-omlaag ({% kbd ↓ %}) om door de gefilterde lijst te bladeren.

Als u op {% kbd cmd T %} drukt, wordt ook de inhoudsopgave geopend (of gesloten).

Als ["Headlines Collapse Sections"](Interface_Features.html#collapsibleheadlines) is ingeschakeld in de {% prefspane General %} en u de Command-toets ingedrukt houdt terwijl u op een item in de inhoudsopgave klikt, wordt die sectie samengevouwen of uitgevouwen, waarbij indien nodig de bovenliggende secties zichtbaar worden.

In de modus Volledig scherm verschijnt de inhoudsopgave als een vaste zijbalk in plaats van als een pop-upmenu. Om die lay-out in een normaal venstervoorbeeld te gebruiken, gebruikt u de schakelaar voor volledig scherm rechtsonder in het inhoudsopgavepaneel.

![Toggle Full Screen][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


Voor een verkorte lijst met sleutels, zie [Keyboard Shortcuts](Keyboard_Shortcuts.html#TableofContentsNavigation).

Zie ook de [Document Navigation video on YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Volledig schermmodus voor de inhoudsopgave [full-screen-mode-for-the-table-of-contents]

Wanneer een Marked voorbeeldvenster op volledig scherm wordt weergegeven, kan de inhoudsopgave aan de linkerkant vast blijven staan ​​voor constante navigatie. Het schakelt nog steeds met {% kbd cmd T %}; Als u buiten de inhoudsopgave klikt, wordt deze in deze lay-out vaak niet verwijderd.

In een normaal venster klikt u op het pictogram onder aan het inhoudsopgavepaneel om het als zijbalk vast te zetten; klik op het pictogram bovenaan de zijbalk om terug te keren naar de pop-upmodus.

### Customaanpassen waar de inhoudsopgave verschijnt [customizing-where-the-toc-appears]

De inhoudsopgave kan in het geëxporteerde document worden ingevoegd met behulp van de [special syntax](Special_Syntax.html#tableofcontents) `<!--TOC-->`.

Voeg `max#` toe (bijvoorbeeld `<!--TOC max2-->`) om te beperken hoeveel kopniveaus er verschijnen.

## Snel zoeken [fast-search]

**Snelle navigatie** combineert de inhoudsopgave met de focus op het filter, zodat u kunt springen met minimaal typen:

- Druk op {% kbd f %} in het voorbeeld om de inhoudsopgave te openen met het **filterveld gericht** (hetzelfde idee als het openen van de inhoudsopgave en vervolgens op {% kbd Space %} te drukken, zonder de extra stap).
- Typ een deel van een koptitel; de lijst filtert op overeenkomsten.
- Als er nog maar één kop overblijft, springt u door op Return ({% kbd ↩ %}) te drukken er rechtstreeks naartoe.
- Als er meerdere koppen overblijven, drukt u op Tab ({% kbd ⇥ %}) om het filterveld te verlaten, beweegt u met {% kbd j %}/{% kbd k %} of de pijltoetsen en drukt u vervolgens op {% kbd o %} of Return ({% kbd ↩ %}) om naar de kop te gaan en de inhoudsopgave te sluiten.
- Tab keert opnieuw de focus terug naar het zoekveld.

> **Snelkoppelingherinnering:** Als u de inhoudsopgave opent en op {% kbd Space %} drukt, wordt de filterbalk geopend – handig wanneer de inhoudsopgave al zichtbaar is.

(Eerdere documenten noemden dit "Fast Switcher"; het is dezelfde functie.)

## Bladwijzers en minikaart [bookmarks-and-mini-map]

Gebruik het {% appmenu Gear %} voorbeeldmenu en {% kbd Tab %} ({% kbd ⇥ %}) om het document naast [search](Interface_Features.html#search) te plaatsen en opnieuw te bekijken terwijl u bladert.

### Bladwijzers instellen [setting-bookmarks]

Zet bladwijzers op de schuifpositie met behulp van {% kbd shift 1 %}--{% kbd shift 9 %} en spring terug met alleen {% kbd 1 %}--{% kbd 9 %}. Gebruik {% kbd n %} en {% kbd p %} voor volgende/vorige in **documentvolgorde**; {% kbd shift n %} en {% kbd shift p %} voor volgende/vorige in **numerieke** volgorde.

Als u de stijl of het paginaformaat wijzigt, kunt u verplaatsen waar een bladwijzer verschijnt. Bladwijzers zijn bedoeld als tijdelijke beoordelingshulpmiddelen: ze blijven niet bestaan ​​tussen documentsessies, maar ze overleven wel vernieuwingen en bewerkingen van voorbeelden.

**Kopbladwijzers:** Houd Option ingedrukt en druk op {% kbd opt 1 %}--{% kbd opt 9 %} om een ​​bladwijzer te maken voor de kop die zich het dichtst bij de bovenkant van de viewport bevindt (of de laatste kop vóór de bovenkant).

**Volgend vrij slot:** {% kbd cmd D %} (of backtick {% kbd \`\` %}, voor vim-gebruikers) voegt een bladwijzer toe aan het volgende beschikbare genummerde slot.

Druk op {% kbd 0 %} om de bladwijzerstrook uit te vouwen (koptitels indien beschikbaar). Wanneer de [Mini Map](#minimap) is ingeschakeld, wordt deze tegelijkertijd weergegeven door {% kbd 0 %}. Druk nogmaals op Escape of {% kbd 0 %} om samen te vouwen.

Druk tweemaal op {% kbd x %} ({% kbd xx %}) om alle bladwijzers te wissen.

Er zijn [more preview shortcuts](Keyboard_Shortcuts.html); druk op {% kbd h %} in de preview voor een heads-up-lijst, of op {% kbd opt cmd K %} voor de volledige referentie.

### Minikaart [minimap]

Als de minikaart is ingeschakeld in de {% prefspane Preview %} instellingen, opent {% kbd 0 %} een geschaalde miniatuur van het hele document langs de bladwijzerstrook. Klik ergens op de kaart om daar door het volledige voorbeeld te scrollen. Opgeslagen bladwijzers verschijnen als horizontale lijnen met cijfers (en koppen indien relevant).

Houd **Command** ingedrukt en beweeg over de minikaart voor een vergrote loep; houd **Option** ingedrukt en sleep om te scrollen alsof je de schuifbalk sleept.

De kaart wordt opnieuw gegenereerd wanneer de venstergrootte of lay-out verandert. Bij zeer lange documenten kan het even duren als u eenmaal op {% kbd 0 %} drukt; Marked vermijdt dat de minikaart automatisch wordt opgebouwd bij de eerste keer laden totdat u erom vraagt.

Druk op {% kbd 0 %} of Escape om de minikaart te sluiten.

**Prestatieopmerking:** Door het genereren van de kaart kan het voorbeeld van grote documenten kort worden gepauzeerd; dit werkt alleen als de kaart zichtbaar is of na een formaatwijziging.

### Zoomoverzicht (gerelateerd) [zoom-overview-related]

Voor een overzicht op tekstschaal zonder de minikaart, zie [Zoom Overview](Zoom_Overview.html) ({% kbd z %}).