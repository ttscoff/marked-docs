# <%= @title %>

Marked biedt u opties.

## Live voorbeeldworkflow [live-preview-workflow]

1. Sleep een Markdown bestand naar Marked (of gebruik {% appmenu File, Open... ({{cmd}}O) %}).
2. Bewerk het bestand in de editor van uw voorkeur.
3. Opslaan --- Marked werkt het voorbeeld automatisch bij.

Zie [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) voor kluisweergave, streamingvoorbeeld en editorspecifieke handleidingen.

## Sleep naar Dock-pictogram [drag-to-dock-icon]

De eenvoudigste manier om Marked te gebruiken voor een bestand dat je al aan het bewerken bent, is door het documentpictogram van de werkbalk van je editor of vanuit de Finder naar het Marked-pictogram in je Dock te slepen. Marked zal onmiddellijk beginnen met het bijhouden van elk Markdown bestand (of tekstbestand) dat erop wordt geplaatst. U kunt bestanden ook rechtstreeks vanuit de Finder slepen.

## Het menu gebruiken [using-the-menu]

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

U kunt Markdown bestanden uiteraard rechtstreeks openen met de menuoptie {% appmenu File, Open... ({{cmd}}O) %}. Marked werkt ook prima _zonder_ een teksteditor. U kunt uw Markdown met slechts één klik bekijken en converteren.

Marked kan ook **`.rtf` en `.rtfd`** bestanden rechtstreeks openen (bijvoorbeeld exports vanuit Pages of TextEdit). Ze worden geconverteerd naar Markdown voor een voorbeeld en update wanneer u ze opslaat in de oorspronkelijke app. Zie [RTF and RTFD Support](RTF_Support.html) voor details, inclusief afbeeldingen en beperkingen.

Marked kan **`.pdf`** bestanden op dezelfde manier openen: de conversie wordt op de achtergrond uitgevoerd en het voorbeeld wordt bijgewerkt als het klaar is. Dit werkt het beste voor kortere, op tekst gebaseerde PDFs; grote handleidingen en gescande documenten zijn langzamer en minder nauwkeurig. Zie [PDF Support](PDF_Support.html) voor details en beperkingen.

## Vanaf het klembord [from-the-clipboard]

Als er compatibele tekst (bijvoorbeeld Markdown) op uw klembord staat, kunt u direct een voorbeeld openen door {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} te selecteren. Als u een selectie hebt gekopieerd uit een webbrowser of een andere app die HTML of RTF op het klembord heeft geplaatst, converteert Marked deze naar Markdown voor een voorbeeld. Wanneer u RTF vanuit een app als Teksteditor of Pages plakt, worden grotere lettergroottes grofweg omgezet naar kopniveaus (zeer grote tekst wordt bijvoorbeeld een kop van niveau 1, kleinere grote tekst wordt niveau 2, enzovoort). U kunt meerdere klembordvoorbeelden tegelijk openen en u kunt deze in een nieuw bestand opslaan door {% appmenu File, Save Clipboard Preview %} te kiezen.

## Een nieuw document maken [creating-a-new-document]

Met Marked kunt u een nieuw, leeg tekstbestand maken met de opdracht {% appmenu File, New ({{cmd}}N) %}. Het zal u onmiddellijk vragen om een ​​locatie om het bestand op te slaan, en u kunt de optie "Nieuwe bestanden automatisch bewerken" inschakelen in de {% prefspane Apps %}, naast de knop Teksteditor om het nieuw gemaakte bestand automatisch in uw standaardeditor te openen.

## Recent geopend [open-recent]

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked houdt ook recente documenten bij. De menuoptie {% appmenu File, Open Recent %} toont de bestanden die je hebt geopend en laat je ernaar terugspringen. Je kunt het laatste bestand dat je aan het bekijken was snel opnieuw openen met {% kbd shift cmd R %}. Gebruik {% kbd shift cmd P %} of [Quick Actions](Quick_Actions.html) om menu- en voorbeeldopdrachten vanaf het toetsenbord uit te voeren. Er zijn nog veel meer sneltoetsen. Als je ze wilt leren, kun je een overzicht vinden onder [Keyboard Shortcuts](Keyboard_Shortcuts.html).

## Snel openen ## [multiview]

U kunt snel schakelen tussen geopende documenten, recente documenten openen of het dialoogvenster Bestand->Openen openen met de [Quick Open panel](Quick_Open.html) ({% kbd cmd shift o %}).