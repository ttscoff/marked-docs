Opties in {% prefspane Style %}:

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Lay-out en typografie [layout-and-typography]

Tekstbreedte in Preview beperken
: Stel met de schuifregelaar een maximale breedte in (in pixels) voor de hoofdtekst van de preview.

Automatisch afbreken in alinea's
: Sta toe dat woorden automatisch worden afgebroken met koppeltekens.

Weduwen in kopregels en alinea's voorkomen
: Dwingt een niet-afbrekende spatie af tussen de laatste twee woorden van kopregels en alinea's, zodat losse woorden niet naar een nieuwe regel afbreken.

Typografisch correcte aanhalingstekens en interpunctie genereren
: Gebruik SmartyPants voor slimme aanhalingstekens, omzetting van beletseltekens en andere typografische functies (MultiMarkdown).

Voetnootmarkeringen omringen met vierkante haken
: Indien aangevinkt, wordt de standaard MultiMarkdown-opmaak voor voetnootmarkeringen gebruikt ([1]). Schakel uit om de vierkante haken te verwijderen.

Outline inschakelen voor extensies
: Schakelt de Outline-modus automatisch in voor bestanden met de vermelde extensies.

APA-stijl gebruiken
: Gebruik APA-stijl outlines in plaats van de standaard decimale indeling.

Verbatim (code)blokken opmaken als poëzie
: Indien aangevinkt, worden tab-ingesprongen, omheinde of ingesloten code weergegeven als poëzie in plaats van als codeblok (geen syntax highlighting, en speciale opmaak afhankelijk van het thema).

Thema's toestaan tekst binnen codeblokken te laten omslaan
: Indien aangevinkt, mogen thema's tekstomloop binnen `pre>code`-blokken veroorzaken. Indien uitgeschakeld, zal horizontale overloop altijd scrollen.

Code altijd laten omslaan
: Dwingt codeblokken af om te omslaan, ongeacht de themainstellingen (overschrijft het omloopgedrag van het thema).

RTL-tekst detecteren en opmaken
: Detecteert de taal per element in het document en past de opmaak dienovereenkomstig van rechts naar links (RTL) toe.

### Thema [theme]

Stijlen beheren
: Opent het venster [Stijlbeheer](Style_Manager.html). Voeg CSS-bestanden van uw schijf toe om ze te laten verschijnen in de Stijl-keuzemenu's. Gebruik de knop `Add New Style` of sleep CSS-bestanden naar dit venster. Sleep om de volgorde te wijzigen en gebruik de selectievakjes om Stijlen in of uit te schakelen.

Meer thema's
: Open de online themagalerij om extra stijlen te bekijken en te installeren.

Standaardstijl
: De hier geselecteerde stijl wordt geladen voor alle nieuwe vensters, tenzij [in de metadata een documentspecifieke stijl is opgegeven](Per-Document_Settings.html) (bijvoorbeeld "Marked Style: Grump").

CSS-wijzigingen volgen
: Wanneer dit is ingeschakeld, houdt Marked de huidige Stijl in de gaten voor wijzigingen op schijf, wat helpt bij het bewerken van aangepaste stijlen en webontwikkeling.

Extra CSS
: CSS die hier wordt toegevoegd, wordt na het normale stijlblad van elk thema toegevoegd. Het is een gedeeltelijke overlay, geen volledige vervanging van een thema.
: Marked herschrijft selectors in dit veld (afdrukregels moeten bijvoorbeeld `body.mkprinting #wrapper …` gebruiken). Er is geen grootte- of geldigheidscontrole --- zie [Aangepaste CSS maken](Writing_Custom_CSS.html#additional-css-settings).
: Dit geldt voor alle documenten en alle stijlen, inclusief HTML-export wanneer stijlen zijn inbegrepen. Als u aangepaste CSS wilt toepassen op documenten op basis van voorwaarden, gebruik dan Aangepaste Regels onder {% prefspane Processor %}.

### Scripts insluiten [include-scripts]

Syntax highlighting
: Schakel highlight.js [syntax highlighting](Syntax_Highlighting.html) voor codeblokken in. Kies een thema uit het uitklapmenu.
: Als **Alleen indien taal opgegeven** is aangevinkt, wordt syntax highlighting alleen toegepast op omheinde codeblokken waarvoor een taal is opgegeven.

MathJax inschakelen
: Laadt [MathJax](MathJax.html) voor het weergeven van MathML-vergelijkingen. Kies **Lokaal** (meegeleverd) of **CDN** uit het uitklapmenu.
: **Extra pakketten** opent een paneel om extra MathJax-pakketten toe te voegen (bijvoorbeeld Physics en Chemistry).
: **Geavanceerde configuratie** opent een paneel voor aangepaste MathJax-configuratie.

KaTeX inschakelen
: Laadt [KaTeX](MathJax.html#katex) als alternatief voor MathJax. Er kan slechts één van beide worden geselecteerd.

Vergelijkingen nummeren
: Indien van toepassing voegt Marked figuurnummers toe aan weergegeven vergelijkingen. Kies **Links** of **Rechts** voor de nummering. Bij gebruik van MathJax kunt u **Alleen AMS** kiezen om alleen AMS-vergelijkingen te nummeren.

Mermaid
: Laadt [mermaid.js](https://mermaid.js) van een CDN om Markdown-achtige diagrammen mogelijk te maken. De hook die nodig is om Mermaid-diagrammen bij elke documentupdate weer te geven, wordt automatisch meegeleverd.

Diagrammen pannen en zoomen
: Wanneer Mermaid-diagrammen aanwezig zijn, schakelt u zoomen in met {% kbd cmd %}-scroll en pannen door te klikken en te slepen.
