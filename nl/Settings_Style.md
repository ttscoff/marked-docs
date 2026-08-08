# <%= @title %>

Opties in de {% prefspane Style %}:

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Lay-out en typografie [layout-and-typography]

Beperk de tekstbreedte in Voorvertoning
: stel een maximale breedte in voor de hoofdtekst van het voorbeeld met behulp van de schuifregelaar (in pixels).

Automatisch afbreken in alinea's
: toestaan dat woorden automatisch worden afgebroken met woordafbreking.

Voorkom weduwen in koppen en paragrafen
: Forceert een niet-afbrekende spatie tussen de laatste twee woorden van koppen en alinea's om te voorkomen dat afzonderlijke woorden op een nieuwe regel terechtkomen.

Genereer typografisch correcte aanhalingstekens en interpunctie
: Gebruik SmartyPants voor slimme aanhalingstekens, conversie van ellipsen en andere typografische functies (MultiMarkdown).

Omring voetnotenmarkeringen met vierkante haakjes
: Indien aangevinkt, gebruik dan de standaard MultiMarkdown opmaak voor voetnootmarkeringen ([1]). Haal het vinkje weg om vierkante haakjes te verwijderen.

Schakel Overzicht in voor extensies
: automatisch de overzichtsmodus inschakelen voor bestanden met de vermelde extensies.

Gebruik APA-stijl
: Gebruik APA-stijlcontouren in plaats van het standaard decimale formaat.

Stijl letterlijke (code)blokken als poëzie
: Indien aangevinkt, wordt met tabs ingesprongen, omheinde of opgenomen code weergegeven als poëzie in plaats van een codeblok (geen syntaxisaccentuering en speciale stijl afhankelijk van het thema).

Sta toe dat thema's tekst binnen codeblokken laten lopen
: Indien aangevinkt, mogen thema's een terugloop veroorzaken binnen `pre>code` blokken. Als dit niet is aangevinkt, zal de horizontale overloop altijd scrollen.

Wrap-code altijd
: Forceer codeblokken om terug te lopen, ongeacht de thema-instellingen (overschrijft het gedrag van thema-inloop).

RTL-tekst detecteren en stylen
: Detecteer de taal per element in het document en de stijl van rechts naar links dienovereenkomstig.

### Thema [theme]

Beheer stijlen
: Opent het [Style Manager](Style_Manager.html) venster. Voeg CSS-bestanden van uw schijf toe om ze te laten verschijnen in de stijlkiezermenu's. Gebruik de knop `Add New Style` of sleep CSS-bestanden naar dit venster. Sleep om de volgorde te wijzigen en gebruik de selectievakjes om stijlen in of uit te schakelen.

Meer thema's
: Open de online themagalerij om door aanvullende stijlen te bladeren en deze te installeren.

Standaardstijl
: De hier geselecteerde stijl wordt voor alle nieuwe vensters geladen, tenzij een [document-specific style is indicated in metadata](Per-Document_Settings.html) (bijvoorbeeld "Marked Stijl: Grump").

Houd CSS-wijzigingen bij
: Wanneer dit is ingeschakeld, zal Marked de huidige stijl controleren op schijfwijzigingen, wat helpt bij het bewerken van aangepaste stijl en webontwikkeling.

Extra CSS
: CSS die hier wordt toegevoegd, wordt opgenomen na het normale stylesheet met alle thema's. U kunt het onder andere gebruiken om instellingen over de hele linie te overschrijven zonder interne stijlen te bewerken.
: Dit geldt voor alle documenten en alle stijlen. Als u aangepaste CSS wilt toepassen op documenten op basis van voorwaarden, gebruikt u Custom Regels onder {% prefspane Processor %}.

### Scripts opnemen [include-scripts]

Syntaxisaccentuering
: Schakel highlight.js [syntax highlighting](Syntax_Highlighting.html) in voor codeblokken. Selecteer een thema in de vervolgkeuzelijst.
: Als **Alleen als taal is opgegeven** is aangevinkt, wordt syntaxisaccentuering alleen toegepast op afgeschermde codeblokken met een opgegeven taal.

Schakel MathJax in
: Laadt [MathJax](MathJax.html) voor het weergeven van MathML-vergelijkingen. Kies **Lokaal** (gebundeld) of **CDN** in de vervolgkeuzelijst.
: **Aanvullende pakketten** opent een blad met extra MathJax pakketten (bijvoorbeeld natuurkunde en scheikunde).
: **Geavanceerde configuratie** opent een blad voor aangepaste MathJax configuratie.

Schakel KaTeX in
: Laadt [KaTeX](MathJax.html#katex) als alternatief voor MathJax. Er kan slechts het een of het ander worden geselecteerd.

Getalvergelijkingen
: Indien van toepassing zal Marked cijfernummers toevoegen aan weergegeven vergelijkingen. Kies **Linkerzijde** of **Rechterzijde** voor nummering. Als u MathJax gebruikt, kunt u **Alleen AMS** kiezen om alleen AMS-vergelijkingen te nummeren.

Zeemeermin
: Laadt [mermaid.js](https://mermaid.js) van een CDN om diagrammen in Markdown-stijl mogelijk te maken. De hook die nodig is om zeemeermindiagrammen weer te geven bij elke documentupdate wordt automatisch meegeleverd.

Pan- en zoomdiagrammen
: Als zeemeermindiagrammen aanwezig zijn, schakelt u zoom in met {% kbd cmd %}-scroll en pan door te klikken en te slepen.