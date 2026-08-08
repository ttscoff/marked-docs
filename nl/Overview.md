# <%= @title %>

{% apponly div %}
*Ga voor de nieuwste versie van deze documentatie naar [online version][help].*
{% endapponly %}

**Bekijk zeker de groeiende collectie van [Marked tutorial videos](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ).**

## Wat is Markdown? [whats-markdown]

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown is een eenvoudige opmaaktaal die gebruikmaakt van eenvoudige symbolen, waardoor u HTML kunt schrijven (en naar andere formaten kunt exporteren) met eenvoudige syntaxis zoals `*italics*` en `**bold**`. Markdown is gemaakt door John Gruber en wordt snel de defacto standaard voor webpublicaties, het maken van aantekeningen en zelfs het publiceren van boeken. Hiermee kun je schrijven zonder een heleboel werkbalken en gedoe met opmaak, je hoeft alleen maar woorden op de pagina te krijgen en je processors (zoals Marked) de styling en opmaak te laten afhandelen.

Marked werkt met GitHub Flavored Markdown, CommonMark (GFM), Kramdown en MultiMarkdown, en kan syntaxis van verschillende varianten converteren voor preview (het kan ook worden uitgebreid om met vrijwel elke processor te werken die je nodig hebt, inclusief Textile, reStructuredText, Wikitext en meer). Ik neem aan dat --- aangezien je hier bent --- je weet wat ten minste één van deze opmaaktalen is. Zo niet, dan moet je beginnen bij John Gruber's [Markdown Basics][daringfireball], kijk eens naar [MarkdownGuide.org][mdguide]. Marked bevat een volledige Markdown syntaxisgids onder het helpmenu.

Je kunt de [Markdown Dingus](x-marked-3://dingus) gebruiken om te experimenteren met de verschillende smaken van Markdown die Marked ondersteunt.

## Wat is Marked? [whats-marked]

Marked is een live Markdown preview-app voor macOS --- een editor-agnostische (Multi)Markdown Preview-applicatie die een bestand controleert op wijzigingen en de preview bijwerkt elke keer dat u het opslaat. Door de details van de opmaak te scheiden en te automatiseren, kunt u zich meer concentreren op het schrijven en minder op de presentatie, terwijl u toch uw eindproduct in de gaten kunt houden.

Voor installatieworkflows en editorspecifieke snelle starts, zie [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html). Voor een korter productoverzicht, ga naar [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marked werkt met elk bestand dat lokaal toegankelijk is, inclusief iCloud-documenten. Sleep gewoon een tekstdocument van de werkbalk van een willekeurige editor naar Marked en het zal het weergeven als een HTML voorbeeld en beginnen met het bijhouden van wijzigingen, waarbij het voorbeeld wordt bijgewerkt terwijl u schrijft. Het kan zelfs [multi-file documents](Multi-File_Documents.html) compileren met behulp van een standaard "include" syntaxis, of vanuit de indexformaten Scrivener, Leanpub en mmd_merge.

Marked heeft extra functies, waaronder het aantal woorden en andere documentstatistieken, de mogelijkheid om boven andere applicaties te zweven of op de achtergrond te dimmen, en het kan uw werk in verschillende goed ontworpen stijlen weergeven. Het kan met één druk op de knop worden uitgevoerd om PDF Word-documenten af ​​te drukken of te voltooien, HTML documenten te voltooien (inclusief stijlen en afbeeldingen) of HTML bron- of RTF gegevens naar uw klembord te kopiëren. Marked heeft ook een basis AppleScript-woordenboek en een [URL handler](URL_Handler.html) waardoor het gemakkelijk te integreren is in uw workflow.

Oh ja, en het werkt met heel veel van je favoriete apps: teksteditors variërend van Vim en Emacs tot Sublime Text en TextMate, Markdown editors zoals MultiMarkdown Composer, Byword en iA Writer, zelfs apps die je misschien niet verwacht, zoals Ulysses, Scrivener, VoodooPad, MarsEdit en meer.

## Voorbeeldgebruik [example-uses]

Marked verandert elke teksteditor in een editor die geschikt is voor Markdown. Uw voorbeeld is altijd beschikbaar en wordt bijgewerkt terwijl u werkt.

* Als uw favoriete editor geen live Markdown voorbeeld biedt, opent u het document waaraan u werkt in Marked en beweegt u het venster opzij voor een volledige Markdown schrijfervaring.
* Houd je van schrijven of bloggen in MacVim of een andere terminalgebaseerde editor? Nu hebt u een gesynchroniseerd Markdown voorbeeld terwijl u werkt.
* Marked biedt ook weergavemogelijkheden die verder gaan dan elk bestaand Markdown voorbeeld, en kan in plaats daarvan worden gebruikt om het volledige aantal woorden en documentstatistieken weer te geven, suggesties te schrijven en zelfs fouten in uw Markdown-opmaak te markeren.
* Je kunt Marked ook gebruiken zonder editor. Sleep gewoon Markdown bestanden naar het pictogram om ze te bekijken, druk ze af en exporteer ze naar PDF, DOC, RTF of HTML broncode. Marked kan ook **`.rtf` en `.rtfd` bestanden** openen als brondocumenten ([RTF and RTFD Support](RTF_Support.html)).
* In apps die automatisch worden opgeslagen, zult u merken dat het voorbeeld zonder enige hulp uw schrijven bijhoudt. Gebruik het met elke editor... of *al* uw editors.
*Een boek schrijven? Marked kan meerdere bestanden compileren voor een volledig voorbeeld van uw werk, en zelfs de meegeleverde bestanden bekijken op wijzigingen, waarbij het hoofddocument bij elke opslag wordt bijgewerkt. Het kan zelfs een hele map controleren op wijzigingen, waarbij het voorbeeld automatisch wordt overgeschakeld naar het bestand dat u momenteel bijwerkt. Wanneer u klaar bent, kunt u publiceren in de indelingen EPUB, DOCX of TextBundle.
* Werken met een AI-coderingsplatform? Open een plan- of documentatiemap in Marked en telkens wanneer een Markdown bestand in die map verandert, zal Marked dit weergeven, waarbij automatisch naar het punt van de meest recente bewerking wordt gescrolld. Marked geeft zeemeermindiagrammen weer en kan overweg met allerlei uitgebreide syntaxis. Houd plannen en documentatie bij terwijl u werkt, zonder te schakelen tussen bestanden.