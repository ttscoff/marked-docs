# <%= @title %>

Marked bevat een AppleScript-woordenboek voor het automatiseren van voorbeeld-, export- en workflow-integratie. U kunt documenten openen, het voorbeeld beheren (herladen, scrollen, markeren, automatisch scrollen, snel lezen), statistieken lezen, processors en stijlen wijzigen, HTML of RTF naar het klembord kopiëren en exporteren naar de meeste van dezelfde formaten die beschikbaar zijn in het {% appmenu File, Export %} menu. **Voorbeeld van koppen/inhoudsopgave via AppleScript wordt aan gewerkt** (zie hieronder).

Voor op URL gebaseerde automatisering (shellscripts, `open` opdrachten en callbacks), zie [URL Handler](URL_Handler.html). AppleScript en de URL-handler vullen elkaar aan: gebruik AppleScript als u zich op een specifiek document of venster moet richten, en URL's als een simpele `open 'x-marked://...'`-aanroep voldoende is.

## Het woordenboek bekijken [viewing-the-dictionary]

In **Scripteditor** kiest u {% appmenu File, Open Dictionary... %} en selecteert u Marked. Het woordenboek bevat opdrachten voor de objecten **application**, **document** en **window**, plus exportopdrachten in de Marked suite.

Op macOS kunt u door scriptdefinities bladeren met **Script Editor**.

## Targeting Marked [targeting-marked]

Voor de standaardinstallatie:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Documenten en vensters [documents-and-windows]

**Sollicitatie**

- `documents` -- open voorbeelddocumenten (geordende lijst).
- `windows` -- voorbeeldvensters.

**Document**

- `name` -- weergavenaam.
- `path` -- bestandspad wanneer het document op schijf wordt opgeslagen.
- `modified` -- of het document niet-opgeslagen editorwijzigingen bevat.
- `processor` -- Markdown processor voor deze preview (lezen/schrijven). Geldige namen: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. Door `processor` in te stellen wordt een overschrijving per document toegepast en wordt het voorbeeld opnieuw geladen; het verandert niets aan de globale standaard in {% prefspane Processor %}.
- `preprocessor` -- preprocessor voor deze preview (lezen/schrijven). Gebruik `true` of `false` om de aangepaste preprocessor of, indien van toepassing, een preprocessornaam in of uit te schakelen.
- `source text` -- onbewerkte Markdown bron (alleen-lezen).
- `critic markup mode` -- of CriticMarkup-verwerking is ingeschakeld (lezen/schrijven). Als u dit wijzigt, wordt het voorbeeld opnieuw geladen.
- `is autoscrolling` -- of autoscroll actief is (alleen-lezen).
- `is speed reading` -- of de snelheidsleesmodus actief is (alleen-lezen).
- Preview-, reader-, statistieken- en exportopdrachten (zie hieronder).

**Raam**

- `document` -- de `MarkdownDocument` die in dat venster wordt weergegeven.
- `style` -- huidige naam van de voorbeeldstijl (lezen/schrijven). Door `style` in te stellen, wordt de preview opnieuw geladen met het gekozen thema (hetzelfde als het kiezen van een stijl uit het preview-stijlmenu).
- `close`, `save`, `print` -- standaard vensteropdrachten.
- Dezelfde preview-, reader-, statistieken- en exportopdrachten als op documenten (doorgestuurd naar het vensterdocument).

Geef de voorkeur aan `tell document 1` of `tell window 1's document` wanneer u een specifiek voorbeeld exporteert. Exportopdrachten in de toepassing gebruiken het sleutelvenster of het huidige document als er geen ontvanger is opgegeven.

### Voorbeeld: pad openen en lezen [example-open-and-read-path]

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Voorbeeld: voorbeeldstijl wijzigen [example-change-preview-style]

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

Stijlnamen komen overeen met het voorbeeldstijlmenu (weergavenaam, CSS-bronnaam zoals `swiss`, of interne identificatie). Custom stijlen die u in Stijlbeheer hebt toegevoegd, worden ondersteund.

Gebruik **`get preview style names`** op het toepassingsobject om de weergavenamen van ingeschakelde stijlen weer te geven.

### Voorbeeld: processor en brontekst [example-processor-and-source-text]

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Applicatieopdrachten [application-commands]

Deze opdrachten zijn van toepassing op het **applicatie**-object (niet op een specifiek document).

| Commando | Beschrijving |
| --- | --- |
| `open streaming preview` | Open een [streaming clipboard preview](Streaming_Preview.html) venster. |
| `preview clipboard` | Open een [clipboard preview](Opening_Files.html) van de huidige inhoud van het klembord (hetzelfde als {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}). |
| `close all` | Sluit alle geopende voorbeelddocumenten (geen opslagprompt; Marked bewerkt de bronbestanden niet). |
| `get available processors` | Lijst met processornamen: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Lijst met ingeschakelde weergavenamen van voorbeeldstijlen. |
| `get_available_formats` | Lijst met ondersteunde `convert_to` formaatnamen. |
| `get_available_profiles` | Lijst met exportprofielnamen (hetzelfde als de eigenschap `profiles`). |

Breng Marked naar voren met het standaard AppleScript **`activate`** commando:

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Voorbeeldcontrole [preview-control]

Beschikbaar op **document** en **venster**. De meeste hiervan vereisen een geladen preview-WebView.

| Commando | Parameters | Beschrijving |
| --- | --- | --- |
| `refresh preview` | — | Laad het voorbeeld opnieuw vanuit het bronbestand (hetzelfde als {% appmenu Preview, Refresh %}). |
| `reveal in finder` | — | Onthul het documentbestand in Finder. |
| `show highlights` | — | Schakel trefwoordmarkering in (vermijd woorden, alternatieven, passieve stem, aangepaste lijsten). |
| `full screen` | optioneel `enabled` boolean | Open de voorbeeldmodus op volledig scherm, verlaat deze of schakel deze in of uit. |
| `scroll to heading` | `title` of `id` | Scroll naar een kop op zichtbare titeltekst of DOM `id`. |
| `scroll to position` | `percent` of `line` | Blader op percentage van de documenthoogte of op een geschat regelnummer. |
| `copy html` | — | Kopieer voorbeeld HTML naar het klembord (tandwielmenu of {% kbd shift cmd C %}; zie [Copy HTML](Exporting.html#copyhtml)). |
| `copy rtf` | — | Kopieer rijke tekst naar het klembord. |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## Autoscroll en leessnelheid [autoscroll-and-speed-read]

| Commando | Beschrijving |
| --- | --- |
| `autoscroll` | Start automatisch scrollen. Optioneel `wpm` geheel getal stelt woorden per minuut in voordat wordt gestart. |
| `stop autoscroll` | Stop automatisch scrollen. |
| `pause autoscroll` | Pauzeer of hervat automatisch scrollen. |
| `speed read` | Start of schakel [speed read](Speed_Reading.html). |
| `stop speed read` | Stopsnelheid lezen. |
| `pause speed read` | Pauzeer of hervat de leessnelheid. |

Controleer de status met de documenteigenschappen `is autoscrolling` en `is speed reading`.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Statistieken [statistics]

**`get statistics`** retourneert een `statistics_record` met numerieke waarden berekend op basis van de huidige Markdown bron (niet de opgemaakte tekenreeksen die worden weergegeven in de statistiekenlade).

| Eigendom | Beschrijving |
| --- | --- |
| `word_count` | Aantal woorden |
| `sentence_count` | Aantal zinnen |
| `character_count` | Aantal tekens |
| `paragraph_count` | Aantal alinea's |
| `average_words_per_sentence` | Gemiddelde woorden per zin |
| `average_syllables_per_word` | Gemiddelde lettergrepen per woord |
| `complex_word_percentage` | Complex woordpercentage |
| `reading_ease` | Leesgemak van vlees |
| `fog_index` | Gunning mist-index |
| `grade_level` | Flesch-Kincaid-niveau |
| `gulpease` | Gulpease-index (Italiaanse leesbaarheid; `0` indien niet van toepassing) |
| `gulpease_band` | Gulpease-band `1`–`4` (indien van toepassing) |
| `reading_time_minutes` | Leestijd bij **250 WPM** |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Inhoudsopgave (werk in uitvoering) [table-of-contents-work-in-progress]

{% note %}
**WIP — nog niet betrouwbaar.** Het woordenboek bevat een eigenschap **`headings`** en een **`headings`** opdracht voor het lezen van geneste voorbeeldkoppen (`heading_item` records). Deze automatisering werkt **niet correct** in de huidige builds (lege resultaten, dwangfouten of "er is geen resultaat geretourneerd"). Het zal in een latere release worden opgelost. Geef tot die tijd de voorkeur aan **`scroll to heading`** met een bekende titel of ID.
{% endnote %}

**Gepland gedrag** (indien voltooid): geneste `heading_item` records uit kopteksten in de **preview** (`h1`–`h6`), niet uit onbewerkte Markdown.

| Eigendom | Beschrijving |
| --- | --- |
| `title` | Koptekst |
| `id` | DOM `id` attribuut (lege string indien afwezig) |
| `level` | Kopniveau `1`–`6` |
| `children` | Geneste lijst met `heading_item` records |

**`headings`** (documenteigenschap) — alle niveaus. **`headings levels {2, 3}`** (opdracht) — optioneel filter: alleen die koersdieptes (geen bereik).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Gebruik `id` waarden met **`scroll to heading id "..."`** zodra de automatisering van de kopteksten stabiel is.

## Afdrukken met profiel [print-with-profile]

**`print with profile`** past tijdelijk de afdrukinstellingen van een exportprofiel toe en drukt vervolgens het document af (dezelfde voorkeursbundel als exportprofielen van {% prefspane Export %}).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

Profielnamen zijn hoofdlettergevoelig. Na het afdrukken herstelt Marked het eerder actieve exportprofiel.

## Profielen exporteren [export-profiles]

Exportprofielen slaan bundels export-/afdrukvoorkeuren op (marges, kopteksten, TOC-opties en soortgelijke instellingen van {% prefspane Export %}).

**Profielnamen lezen**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Exporteren met een profiel**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

Profielnamen zijn hoofdlettergevoelig en moeten exact overeenkomen met een opgeslagen profiel.

## Exportopdrachten [export-commands]

Exportopdrachten zijn beschikbaar voor de objecten **application**, **document** en **window**. Elke opdracht vereist een parameter **`to`** met het uitvoerpad (POSIX-padtekenreeks of `file` object).

| Commando | Uitvoer |
| --- | --- |
| `export markdown` | Markdown (.md) |
| `export html` | HTML |
| `export paginated pdf` | Gepagineerd PDF (afdrukindeling) |
| `export continuous pdf` | Continu scrollen PDF |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | OpenDocument-tekst |
| `export textbundle` | TextBundle |
| `export rtf` | RTF |
| `export opml` | OPML |

**Opmerkingen**

- Gepagineerde PDF gebruikt dezelfde HTML-naar-PDF pijplijn als {% appmenu File, Export, Paginated PDF %}. Het is niet beschikbaar voor onbewerkte HTML voorbeelddocumenten.
- HTML export gebruikt het **gerenderde voorbeeld** (wat u ziet in de WebView), niet het onbewerkte Markdown bronbestand.
- Continu PDF legt de huidige preview-WebView-indeling vast.

### Basisexport [basic-export]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Paden exporteren en sandboxen [export-paths-and-sandboxing]

- Gebruik een volledig POSIX-pad voor het doelbestand.
- Marked kan tussenmappen maken als het exportpad **binnen de map van het geopende document** ligt (bijvoorbeeld exporteren naar `.../MyProject/build/output.pdf` terwijl u een voorbeeld van `.../MyProject/chapter.md` bekijkt).
- Voor exporten buiten de map van het document is een beschrijfbaar pad nodig waartoe Marked toegang heeft (opgeslagen documentlocatie, bladwijzers met veiligheidsreikwijdte of mappen die u hebt toegekend via Open-dialoogvensters). Als het pad niet beschrijfbaar is, retourneert de opdracht een fout voordat het exporteren begint.

## `with` opties (eigenschappenrecord) [with-options-properties-record]

In plaats van `with profile` kunt u een record met opties doorgeven met behulp van **`with`** of **`with properties`**:

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

AppleScript herkent deze sleutels rechtstreeks (ze worden vóór het exporteren in kaart gebracht):

| Sleutel | Beschrijving | Voorbeeld |
| --- | --- | --- |
| `style` | Voorbeeldstijl die moet worden toegepast vóór het exporteren (volledige voorbeeldherladen) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Naam van paginaformaat afdrukken | `"A4"`, `"Letter"` |
| `margins` | Printmarges (zie hieronder) | `"1in"`, `"1in 2in"` |
| `fontSize` | Basislettergrootte voor exporteren/afdrukken in punten overschrijven (gepagineerd en doorlopend PDF) | `"14"`, `"12pt"` |

`fontSize` schakelt dezelfde **Custom lettergrootte in voor exporteren/afdrukken** van {% prefspane Export %}. Het heeft geen invloed op Fountain-documenten, die een vaste schermgrootte gebruiken.

Wanneer `style` is opgenomen, past Marked dat thema toe, wacht tot het voorbeeld opnieuw is geladen en exporteert vervolgens. U heeft geen aparte `set style` stap nodig.

Andere sleutels in de record kunnen overeenkomen met namen van **exportvoorkeur** uit profielen (dezelfde sleutels opgeslagen in {% prefspane Export %}, zoals `printBackgrounds`, `printTOC`, `topPrintMargin`). Deze waarden worden tijdelijk toegepast voor de export.

Je kunt conflicterende bronnen niet achteloos combineren: als je `with profile` gebruikt, laad dan eerst dat profiel; als u een `with` record gebruikt, overschrijven profielsleutels in de record de huidige instellingen voor die export.

### Marge afkorting [margin-shorthand]

De `margins` waarde is een string met één tot vier metingen. Eenheden: `in`, `cm`, `mm`, `pt`, of `"` voor inches. Een getal zonder eenheid wordt behandeld als punten.

| Waarden | Betekenis |
| --- | --- |
| `1in` | Alle kanten |
| `1in 2in` | Boven en onder `1in`, links en rechts `2in` |
| `1in 2in 1in` | Boven `1in`, links en rechts `2in`, onder `1in` |
| `1in 2in 1in 2in` | Boven, rechts, onder, links |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Gecombineerd voorbeeld [combined-example]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to` [convert_to]

Het toepassingsobject geeft ook verouderde scriptopdrachten weer:

- **`convert_to`** -- converteer Markdown tekst of een bestandspad naar een indeling (`html`, `pdf`, `epub`, `docx`, `rtf` en andere), optioneel met `profile` en `output_path`.
- **`get_available_formats`** -- lijst met namen van ondersteunde conversieformaten.
- **`get_available_profiles`** -- lijst met exportprofielnamen (hetzelfde als de `profiles` eigenschap).

`convert_to` blijft beschikbaar voor oudere workflows en automatisering met alleen AppleScript.

## Foutopsporing [debugging]

Schakel de **Debug-modus** in {% prefspane Advanced %} in (of de foutopsporingsvoorkeur in Instellingen). Marked registreert vervolgens de AppleScript-exportstappen op Info-niveau met het voorvoegsel `[AppleScript]` in Console.app en de logviewer van Marked.

Handige logregels bij het traceren van een gepagineerde PDF export:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

Bij lange exports (vooral gepagineerd PDF) wordt de AppleScript-gebeurtenis opgeschort tot voltooiing, zodat clients tijdens het exporteren geen time-out krijgen.

## Fouten [errors]

Bij mislukte exports wordt de scriptfoutreeks voor de opdracht ingesteld (zichtbaar in Script Editor en `on error` handlers). Veel voorkomende berichten:

- Exportpad is vereist.
- Exportmap bestaat niet (buiten de documentmap).
- Kan geen exportmap maken of er is een toestemmingsfout opgetreden bij het schrijven van het bestand.
- Onbekende naam van de voorbeeldstijl.
- Er is een time-out opgetreden tijdens het wachten tot het voorbeeld opnieuw werd geladen na een stijlwijziging.
- Gepagineerde PDF-export is verlopen of mislukt tijdens het genereren van pagina's.

## Integratie met andere tools [integration-with-other-tools]

Programma's kunnen het AppleScript-oppervlak van Marked gebruiken om metagegevens van documenten te lezen. Voor shell-gestuurde workflows, mapwatchers en callbacks van editors is de [URL Handler](URL_Handler.html) vaak eenvoudiger. De [Marked Bonus Pack](Workflow_Integration.html#marked-bonus-pack) bevat aanvullende scripts en services.