# <%= @title %>

Marked werkt op twee manieren met [Obsidian][obsidian-app] notities: open een **kluismap** voor automatisch volgen, of gebruik de **community-plug-in** voor nauwere synchronisatie.

De ingebouwde preview van Obsidian is ideaal als je de app nooit verlaat. Kies Marked als u export van publicatiekwaliteit, geavanceerd proeflezen, aangepaste CSS-thema's of dezelfde live preview-workflow voor meerdere editors wilt. Zie [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) voor een volledige vergelijking.

## Open een hele kluis [open-an-entire-vault]

Sleep de **kluismap** (de map die de verborgen configuratiemap van Obsidian in de kluismap bevat) naar Marked in het Dock. Marked houdt de boom in de gaten, bewaart de **meest recent bewerkte** notitie in het voorbeeld en wordt bijgewerkt terwijl je hem opslaat in Obsidian.

Voor kluisspecifieke standaardwaarden (stijl, processor, basis-URL voor afbeeldingen, enzovoort) voegt u een [Custom Rule](http://support.markedapp.com) toe die overeenkomt met de paden onder die kluis.

## Obsidiaan callout-syntaxis [obsidian-callout-syntax]

Wanneer de MultiMarkdown processor draait, converteert Marked algemene **Obsidian-stijl callouts** (het `> [!note]` patroon) naar opgemaakte blokmarkeringen, zodat ze overeenkomen met de rest van uw voorbeeld.

## Marked 3 Obsidian-plug-in [marked-3-obsidian-plugin]

De [Marked 3 Obsidian plugin][plugin] kan de huidige notitie of de hele kluis openen met opdrachten of sneltoetsen, zodat het venster Marked bijhoudt wat u aan het bewerken bent. Gebruik het opdrachtenpalet (**⌘P**) en zoek naar **Marked**, of wijs sneltoetsen toe in de **Hotkeys**-instellingen van Obsidian.

### Installeren vanuit community-plug-ins [installing-from-community-plugins]

Open in Obsidian **Instellingen → Community-plug-ins**, blader of zoek naar **marked** en installeer **Open in Marked**.

### De plug-in handmatig installeren [manually-installing-the-plugin]

Als u liever vanaf GitHub installeert:

1. Download `main.js` en `manifest.json` van de [latest release][plugin-releases] op GitHub (of bouw ze vanuit de [Marked3-obsidian][plugin] repository).
2. Maak in uw kluis de plug-inmap aan onder `plugins/` in de configuratiemap van Obsidian in de hoofdmap van de kluis. De mapnaam moet overeenkomen met de plug-in `id` in `manifest.json` (zie [plugin README][plugin] voor het volledige pad).
3. Kopieer `main.js` en `manifest.json` naar die map.
4. Open in Obsidian **Instellingen → Community-plug-ins**, schakel indien nodig de **Beperkte modus** uit en schakel **Openen in Marked** in.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest