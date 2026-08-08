<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked bevat een macOS **Deel-extensie** die in het systeemmenu Deel verschijnt. Gebruik deze om een bestand of geselecteerde tekst naar Marked te sturen zonder van app te wisselen of URL's handmatig te kopiëren.

De Deel-extensie **zit in Marked 3**. U downloadt en installeert deze niet apart. Hij zit in de Direct-, Mac App Store-, Marked Pro- en Setapp-builds.

## Werking [how-it-works]

Wanneer u **Marked** kiest in een Deel-menu, opent Marked meteen. Er is geen tussenscherm om te bewerken.

### Een bestand delen [share-a-file]

Kies in **Finder** (of een andere app die bestanden deelt) **Deel → Marked**.

Marked ontvangt het bestandspad en opent het met dezelfde `x-marked-3://open`-URL-handler als elders. Het bestand opent in Marked zoals wanneer u het naar het Dock-symbool sleept of kiest met {% appmenu File, Open... ({{cmd}}O) %}.

Ondersteunde invoer: bestands-URL's, lokale bestanden en web-URL's wanneer de bron-app die levert.

### Geselecteerde tekst delen [share-selected-text]

Selecteer tekst in een app zoals **TextEdit**, **Safari** of **Mail** en kies **Deel → Marked**.

Marked plaatst de tekst op het klembord en opent een **tijdelijke preview** via de handler `x-marked-3://paste`. Dat is hetzelfde type niet-opgeslagen preview als {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. U kunt later opslaan met {% appmenu File, Save Transient Preview %}.

Platte tekst, HTML, RTF en Markdown worden ondersteund wanneer de bron-app die levert.

Zie [URL Handler](URL_Handler.html) voor details over de onderliggende commando's.

## Het Deel-menu gebruiken [using-the-share-menu]

### Vanuit Finder [from-finder]

1. Klik met rechts op een Markdown- of tekstbestand (of selecteer het en klik op **Deel** in de Finder-werkbalk).
2. Kies **Marked** in het Deel-menu.

Als **Marked** niet zichtbaar is, zie [De Deel-extensie inschakelen](#enable-the-share-extension) hieronder.

### Vanuit tekstselectie [from-a-text-selection]

1. Selecteer de tekst die u wilt bekijken.
2. Open het **Deel**-menu van de app (menubalk, werkbalkknop of contextmenu).
3. Kies **Marked**.

Marked start (of komt naar voren) met een preview van de gedeelde inhoud.

## De Deel-extensie inschakelen [enable-the-share-extension]

Marked moet in `/Applications` (of uw gebruikelijke map Programma's) staan en minstens één keer zijn gestart voordat macOS de Deel-extensie toont.

### Marked inschakelen in Systeeminstellingen [turn-on-marked-in-system-settings]

1. Open **Systeeminstellingen**.
2. Ga naar **Algemeen → Inlogitems en extensies** (op sommige macOS-versies: **Privacy en beveiliging → Extensies**).
3. Klik op **Extensies** (of de knop **ⓘ** naast Extensies).
4. Selecteer **Delen** (of **Sharing**).
5. Schakel **Marked** in.

### Marked toevoegen aan het Deel-menu van een app [add-marked-to-an-apps-share-menu]

Ook als de extensie systeembreed aan staat, kiest elke app welke Deel-bestemmingen zichtbaar zijn:

1. Open een app met Deel (Finder en TextEdit zijn makkelijk te testen).
2. Open het **Deel**-menu.
3. Kies **Extensies bewerken…** (op oudere macOS: **Meer…** of **Extensievoorkeuren…**).
4. Vink onder **Deel** **Marked** aan.
5. Sleep **Marked** optioneel hoger in de lijst voor snellere toegang.

Wijzigingen gelden in de meeste apps meteen.

## Als Marked niet in Deel verschijnt [if-marked-does-not-appear-in-share]

W> De Deel-extensie is beschikbaar vanaf Marked 3.1.9. Zorg dat u minstens die versie gebruikt.

Probeer deze stappen in volgorde:

1. **Start Marked één keer** na installatie of update. Sluit en open Marked opnieuw na een upgrade.
2. **Controleer of de extensie is ingeschakeld** in Systeeminstellingen zoals hierboven.
3. **Pas het Deel-menu aan** in de app waaruit u deelt. macOS verbergt weinig gebruikte bestemmingen tot u ze inschakelt.
4. **Meerdere Marked-kopieën:** bij Direct- en Mac App Store-builds registreert alleen de draaiende kopie zijn extensie. Verwijder of hernoem de andere kopie en start de gewenste.
5. **Start de Mac opnieuw** als de extensie na een update nog ontbreekt. macOS cachet registratie van Deel-extensies.
6. **Installeer Marked opnieuw** in `/Applications` als u een handmatig gekopieerde build uit Xcode of een schijfafbeelding test. De Deel-extensie moet in `Marked.app/Contents/PlugIns/` zitten.

## Tips [tips]

- De Deel-extensie is ideaal voor snelle previews van webfragmenten, e-mailalinea's of notities zonder eerst een bestand te maken.
- Voor hele pagina's of complexe browserselecties bieden de [browserextensies](Using_the_Browser_Extensions.html) vaak meer controle (sectieselectie, Markdownify URL, enz.).
- Gedeelde bestanden openen als normale Marked-documenten met bestandsbewaking. Gedeelde tekst opent als tijdelijke preview tot u opslaat.
