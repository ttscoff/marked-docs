<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

Geef een LLM-agent een skillbestand, zodat die bestanden en mappen in Marked kan openen, naar een onderdeel van Instellingen kan gaan en voorkeuren kan wijzigen. De agent gebruikt de [URL Handler](URL_Handler.md) van Marked. Een extra plug-in of server is niet nodig.

## De skill downloaden [download-the-skill]

{% download "SKILL.md" "Agentskill om bestanden in Marked te openen en voorkeuren te wijzigen. Bewaar het bestand als SKILL.md." %}

Het bestand is gewone Markdown met een korte kop die de agent leest voordat hij iets doet. U kunt hetzelfde bestand geven aan elke agent die een skill of een vaste instructie accepteert.

## Installeren [install-it]

Zet het bestand in een map die naar de skill is genoemd, en houd de bestandsnaam `SKILL.md`.

Voor Cursor werken beide locaties:

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

De eerste is in elk project beschikbaar. De tweede geldt alleen voor dat project. Andere agents kunnen dezelfde tekst als projectinstructie gebruiken als zij geen skillmap hebben.

Vraag de agent daarna om een bestand of map in Marked te openen. Die hoort een opdracht als deze uit te voeren:

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

Een map gebruikt dezelfde opdracht. Het pad moet bestaan, en spaties en andere gereserveerde tekens moeten procentgecodeerd zijn. Zie [URL Handler](URL_Handler.md) voor het volledige schema, inclusief refresh, Streaming Preview en callbacks.

## Voorkeuren [preferences]

De skill beschrijft ook twee opdrachten voor voorkeuren:

`pref`
: Opent Instellingen op een benoemd onderdeel. De naam in de URL blijft Engels, bijvoorbeeld `Preview` of `Style`. Er wordt geen waarde gewijzigd.

`defaults`
: Zet een voorkeur die Marked al bewaart, en laadt open voorbeelden opnieuw. Geef `refresh=0` mee om de voorbeelden ongemoeid te laten. De agent moet de huidige voorkeuren lezen voordat hij er een schrijft, want een onbekende sleutel wordt genegeerd.

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## Verwant [related]

[Using Marked with Agentic Coding](Using_Marked_with_Agentic_Coding.md) beschrijft hoe u een map met plannen en notities volgt terwijl een agent die schrijft. De [Command Line Utility](Command_Line_Utility.md) biedt dezelfde soort toegang vanuit de shell, zonder agent.
