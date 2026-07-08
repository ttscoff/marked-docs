<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Gemarkeerd geeft je opties.

## Live voorbeeldworkflow

1. Sleep een Markdown-bestand naar Marked (of gebruik {% appmenu File, Open... ({{cmd}}O) %}).
2. Bewerk het bestand in de editor van uw voorkeur.
3. Opslaan --- Gemarkeerd werkt het voorbeeld automatisch bij.

Zie [Live Markdown Preview op Mac](Live_Markdown_Preview_on_Mac.html) voor kluisweergave, streamingvoorbeeld en editorspecifieke handleidingen.

## Sleep naar Dock-pictogram

De eenvoudigste manier om Marked te gebruiken voor een bestand dat je al aan het bewerken bent, is door het documentpictogram van de werkbalk van je editor of vanuit de Finder naar het Marked-pictogram in je Dock te slepen. Marked zal onmiddellijk beginnen met het volgen van elk Markdown-bestand (of tekstbestand) dat erop wordt geplaatst. U kunt bestanden ook rechtstreeks vanuit de Finder slepen.

## Het menu gebruiken

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

U kunt Markdown-bestanden uiteraard rechtstreeks openen via de menuoptie {% appmenu File, Open... ({{cmd}}O) %}. Gemarkeerd werkt ook prima _zonder_ een teksteditor. U kunt uw Markdown met slechts één klik bekijken en converteren.

Gemarkeerd kan ook **`.rtf` en `.rtfd`** bestanden rechtstreeks openen (bijvoorbeeld exports vanuit Pages of Teksteditor). Ze worden geconverteerd naar Markdown voor een voorbeeld en update wanneer u ze opslaat in de oorspronkelijke app. Zie [RTF- en RTFD-ondersteuning](RTF_Support.html) voor details, inclusief afbeeldingen en beperkingen.

Gemarkeerd kan **`.pdf`** bestanden op dezelfde manier openen: de conversie wordt op de achtergrond uitgevoerd en het voorbeeld wordt bijgewerkt als het klaar is. Dit werkt het beste voor kortere, op tekst gebaseerde PDF's; grote handleidingen en gescande documenten zijn langzamer en minder nauwkeurig. Zie [PDF-ondersteuning](PDF_Support.html) voor details en beperkingen.

## Vanaf het klembord

Als er compatibele tekst (bijvoorbeeld Markdown) op uw klembord staat, kunt u direct een voorbeeld openen door {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} te selecteren. Als u een selectie hebt gekopieerd uit een webbrowser of een andere app die HTML of RTF op het klembord heeft geplaatst, converteert Marked deze naar Markdown voor een voorbeeld. Wanneer u RTF vanuit een app als TextEdit of Pages plakt, worden grotere lettergroottes grofweg omgezet naar kopniveaus (zeer grote tekst wordt bijvoorbeeld een kop van niveau 1, kleinere grote tekst wordt niveau 2, enzovoort). U kunt meerdere klembordvoorbeelden tegelijk openen en u kunt deze in een nieuw bestand opslaan door {% appmenu File, Save Transient Preview %} te kiezen.

## Een nieuw document maken

Met Gemarkeerd kunt u een nieuw, leeg tekstbestand maken met de opdracht {% appmenu File, New ({{cmd}}N) %}. Het zal u onmiddellijk vragen om een ​​locatie om het bestand op te slaan, en u kunt de optie "Nieuwe bestanden automatisch bewerken" inschakelen in {% prefspane Apps %}, naast de knop Teksteditor om het nieuw gemaakte bestand automatisch in uw standaardeditor te openen.

## Recent geopend

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked houdt ook recente documenten bij. Met de menuoptie {% appmenu File, Open Recent %} worden de bestanden weergegeven die je hebt geopend en kun je ernaar terugkeren. Je kunt het laatste bestand dat je aan het bekijken was snel opnieuw openen met {% kbd shift cmd R %}. Gebruik {% kbd shift cmd P %} of [Snelle acties](Quick_Actions.html) om menu- en voorbeeldopdrachten vanaf het toetsenbord uit te voeren. Er zijn nog een heleboel andere sneltoetsen. Als je ze wilt leren, kun je een diagram vinden onder [Toetsenbord Snelkoppelingen](Keyboard_Shortcuts.html).

## Nieuwe weergave in huidig bestand [multiview]

Gebruik {% appmenu File, New View into Current File %} ({% kbd
shift cmd N %}, ook in het voorbeeldcontextmenu) om een
tweede voorbeeldvenster op hetzelfde opgeslagen bestand. Beide ramen
bekijk het bestand op schijf en update het wanneer u het opslaat in uw
editor, maar elke weergave behoudt zijn eigen scrollpositie,
bladwijzers, voorbeeldstijl en [Aangepaste regel
overschrijvingen](Custom_Processor.html#manuallyenabled).

**Voorbeeld van gebruik:** U bewerkt een lang manuscript in
MultiMarkdown met uw gebruikelijke stijl en processor. Open een
tweede weergave, schakel over naar een proefdrukstijl, zet een proces vast
regel die een andere ingebouwde processor uitvoert, en schakel a
handmatige regel die revisiemarkeringen markeert. Jij vergelijkt
ontwerp- en proeflay-outs naast elkaar zonder er twee te behouden
kopieën van het bestand.

Wanneer er meer dan één weergave van een bestand geopend is, wordt de venstertitel
omvat **Weergave 2**, **Weergave 3**, enzovoort, zodat u het kunt zien
vensters uit elkaar in het menu Venster en Mission Control.

Alternatieve weergaven zijn niet beschikbaar voor niet-opgeslagen documenten,
klembordvoorbeelden, streamingvoorbeelden of mapgebaseerd
projecten die niet aan één enkel bestand op schijf zijn gekoppeld.

## Snel openen ##

U kunt snel schakelen tussen geopende documenten, recente documenten openen of het dialoogvenster Bestand->Openen openen met het [Snel openen-paneel](Quick_Open.html) ({% kbd cmd shift o %}).