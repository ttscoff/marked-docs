# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) kan geselecteerde Markdown bestanden rechtstreeks in Marked openen met behulp van een AppleScript.

## Open geselecteerde Markdown over Marked [open-selected-markdown-in-marked]

Gebruik dit script in DEVONthink om de huidige selectie naar Marked te sturen. Het controleert of je iets hebt geselecteerd, bevestigt dat het Markdown is en opent het vervolgens met `x-marked-3://` met een URL-gecodeerd bestandspad.

```appelscript
-- Open het geselecteerde DEVONthink Markdown bestand in Marked 3

vertel applicatie-ID "DNtp"
	activeren
	
	zet sel op selectie
	als sel {} is dan
		waarschuwing weergeven "Geen selectie" bericht "Selecteer eerst een Markdown document in DEVONthink."
		terug
	eindigen als
	
	stel deRecord in op item 1 van sel
	
	-- Moet een bestand-backed item zijn
	stel p in op het pad van het record
	als p een waarde mist of p "" is, dan
		waarschuwing weergeven "Geen bestand" bericht "Het geselecteerde item heeft geen bestandspad."
		terug
	eindigen als
	
	-- Vink Markdown aan bij extensie
	stel ext in op mijn kleineletterExtension(p)
	stel mdExts in op {"md", "markdown", "mdown", "mkd", "mkdn", "mdtxt"}
	als mdExts geen ext bevat, dan
		waarschuwing weergeven "Niet Markdown" bericht "Geselecteerd item is geen Markdown document."
		terug
	eindigen als
einde vertellen

stel encodedPath in op mijn urlEncode(p)
stel gemarkeerdURL in op "x-marked-3://" en gecodeerdpad
open locatie gemarkeerdURL


op kleine letters Extensie (posixPath)
	stel oldTIDs in op de scheidingstekens voor tekstitems van AppleScript
	stel de scheidingstekens voor tekstitems van AppleScript in op "."
	stel onderdelen in op tekstitems van posixPath
	stel de scheidingstekens voor tekstitems van AppleScript in op oldTIDs
	
	als (aantal delen) < 2 retourneer dan ""
	stel ext in op item -1 van onderdelen
	return do shell-script "printf %s" & geciteerde vorm van ext & " | tr '[:upper:]' '[:lower:]'"
eind kleine letters Extensie

op urlEncode(s)
	-- URL-codeer pad veilig voor x-marked-3://
	stel py in op "import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe='/'))"
	return do shell script "/usr/bin/python3 -c " & de vorm van py tussen aanhalingstekens & " " en de vorm van s tussen aanhalingstekens
eind-URLEncode
```

## Installeer in het DEVONthink Scripts-menu [install-in-devonthink-scripts-menu]

1. Kopieer het bovenstaande script naar **Scripteditor**.
2. Sla het op als `Open in Marked.scpt`.
3. Open in DEVONthink het menu **Scripts** en kies **Open Scripts Folder**.
4. Verplaats `Open in Marked.scpt` naar de map `Contextual Menu`.
5. Klik in DEVONthink met de rechtermuisknop op een bestand en kies **Scripts -> Openen in Marked.scpt**.

I> Marked kan ook `hook://` assets oplossen wanneer ingeschakeld in {% prefspane Apps %}; zie [Hookmark](Hookmark.html).