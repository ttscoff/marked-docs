# <%= @title %>

## AppleScript [applescript]

Marked bevat een volledige [AppleScript dictionary](AppleScript_Support.html) voor het openen van bestanden, het beheren van de voorbeeldweergave (herladen, scrollen, markeren, automatisch scrollen, snel lezen), het lezen van statistieken, het instellen van processors, het kopiëren van HTML of RTF, het wijzigen van voorbeeldstijlen en het exporteren naar Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF en OPML. **Voorbeeldkoppen / inhoudsopgave** via AppleScript is [documented as work in progress](AppleScript_Support.html#table-of-contents-work-in-progress) en is nog niet betrouwbaar.

U kunt de toepassing, een specifiek venster of een document targeten. Toepassingsopdrachten omvatten **open streaming preview**, **preview klembord** en **alles sluiten**. Documentopdrachten omvatten **statistieken ophalen** en **afdrukken met profiel**. Exportopdrachten accepteren een optioneel export **profiel** of een **`with`** record voor opties zoals voorbeeld **stijl**, **pageSize** en **marges**. Bijvoorbeeld:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Zie [AppleScript Support](AppleScript_Support.html) voor de opdrachtenlijst, korte marges, sandbox-opmerkingen en tips voor foutopsporing.

Dankzij de AppleScript-integratie kunnen applicaties zoals Tags.app ook rechtstreeks binnen Marked functioneren.

## URL-handler [url-handler]

De [Marked URL handler][urlhandler] maakt uitgebreide integratie mogelijk door simpelweg URL's aan te roepen, hetzij vanuit AppleScript, hetzij met een standaard `open` commando in een shellscript.

## Marked Bonuspakket [marked-bonus-pack]

Het Marked Bonuspakket is een verzameling scripts, opdrachten en services. Sommige werken met meerdere editors, andere zijn specifiek voor bepaalde editors. De Services werken doorgaans met elke editor die over de benodigde mogelijkheden beschikt. De rest is georganiseerd in mappen op basis van de applicatie waarmee ze werken.

U kunt het Bonuspakket downloaden en instructies vinden voor de installatie en het gebruik ervan in deze [knowledge base article](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html

