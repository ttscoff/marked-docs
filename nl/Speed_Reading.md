# <%= @title %>

Speed ​​Read is een leesmodus in RSVP-stijl waarbij één woord tegelijk wordt weergegeven in een gerichte overlay.

## Hoe Snel lezen werkt [how-speed-read-works]

Speed ​​Read maakt gebruik van een methode genaamd **Rapid Serial Visual Presentation** (RSVP). In plaats van uw ogen over tekstregels te bewegen, verschijnen de woorden op één vaste positie. Dit vermindert de oogbewegingen, lijnwisselingen en terugspoelen die normaal gesproken tijdens het lezen plaatsvinden, wat het handig kan maken om te skimmen, vertrouwd materiaal te bekijken of snel door de tekst te bladeren zonder uw plaats te verliezen.

De methode is geen magie en garandeert geen beter begrip bij zeer hoge snelheden. Begrijpend lezen hangt nog steeds af van de complexiteit van het schrijven, uw bekendheid met het onderwerp en de WPM-instelling. Voor dicht of onbekend materiaal is een gematigde snelheid meestal effectiever dan de snelheid zo hoog mogelijk te duwen.

De rode letter markeert het visuele ankerpunt van het woord, ook wel het **optimale herkenningspunt** genoemd. In veel woorden identificeren lezers het woord het meest efficiënt wanneer hun blik iets links van het midden terechtkomt in plaats van op de eerste letter. Door dat ankerpunt op dezelfde plaats te houden en te markeren, geeft Speed ​​Read uw oog een consistent doelwit. Het resultaat is minder heroriëntatie tussen woorden en een stabieler ritme terwijl de tekst vordert.

## Openingssnelheid lezen [opening-speed-read]

Gebruik **Voorbeeld > Snel lezen**, het item **Snel lezen** in het tandwielmenu van het voorbeeldvenster, of druk op {% kbd ctrl opt S %}. Het menu-item is beschikbaar wanneer een Markdown voorbeelddocumentvenster actief is (het is uitgeschakeld voor onbewerkte HTML voorbeelden en wanneer er geen document geopend is).

Wanneer Speed ​​Read wordt geopend, wordt het in een gepauzeerde toestand gestart, zodat u zich kunt oriënteren voordat het afspelen begint.

<videocontroles preload="metadata" poster="images/speedread-poster.png">
  <source src="images/speedread.webm" type="video/webm">
  <source src="images/speedread.mp4" type="video/mp4">
  Uw browser ondersteunt de Speed Read-demovideo niet.
</video>
<p><em>Overlay voor snel lezen met afspeelknoppen, synchronisatieopties en toegang tot Help.</em></p>

## Overlay-bedieningselementen [overlay-controls]

Zodra de overlay zichtbaar is, zijn deze toetsen beschikbaar:

| Sneltoets | Functie |
| :-- | :-- |
| {% kbd space %} | Afspelen/pauzeren |
| {% kbd [ %} | Ga naar het begin van de alinea (druk nogmaals voor de vorige alinea) |
| {% kbd ] %} | Spring naar het begin van de volgende paragraaf |
| {% kbd left %} | Leessnelheid (WPM) verlagen |
| {% kbd right %} | Leessnelheid verhogen (WPM) |
| {% kbd esc %} | Uitgangssnelheid Lezen |

Er worden haakjes vastgelegd voor alineanavigatie en pijlen naar links/rechts voor snelheidswijzigingen. Deze toetsen activeren dus geen voorbeeldnavigatie terwijl Snel lezen geopend is. U kunt ook op de ronde knop **X** in de linkerbovenhoek van de overlay klikken om deze te sluiten.

Andere normale sneltoetsen voor voorbeeldnavigatie werken nog steeds terwijl Snel lezen actief is, waaronder `t`/`gg` (boven), `G`/`b` (onder) en `,`/`.` (koptekstnavigatie). Zie [Preview Navigation](Keyboard_Shortcuts#preview-navigation) voor de volledige lijst.

De inhoudsopgave kan ook worden gebruikt tijdens snellezen. Druk op {% kbd cmd t %} om het te openen en te navigeren, of druk op {% kbd f %} om de snelle zoekactie onmiddellijk te richten op het navigeren door documentkoppen.

## Vertrekkend vanuit een selectie [starting-from-a-selection]

Als er tekst is geselecteerd in het voorbeeld wanneer u Snel lezen start, wordt bij het afspelen de geselecteerde tekst gebruikt. Als er geen selectie actief is, gebruikt Snel lezen de volledige documenttekst.

## Synchroniseren met scrollpositie [syncing-with-scroll-position]

Schakel **Synchroniseer snel lezen met scrollpositie** in {% prefspane Preview %} in, of gebruik het selectievakje in de snellezen-overlay om het voorbeeld en de snellezen-positie bij elkaar te houden.

Wanneer deze optie is ingeschakeld, begint Snel lezen bij de inhoud die momenteel zichtbaar is bovenaan het voorbeeld, in plaats van bij het begin van het document. Naarmate het afspelen vordert, scrollt het voorbeeld mee met de weergegeven woorden.

Als u Snel lezen sluit, door het voorbeeld bladert en de overlay opnieuw opent, begint het afspelen vanaf de nieuwe zichtbare positie. Als u het overlay-selectievakje inschakelt nadat Speed ​​Read al is geopend, wordt het afspelen teruggezet naar de huidige schuifpositie en gaat het vanaf daar verder.

## Herinnerde snelheid [remembered-speed]

De WPM-waarde wordt automatisch opgeslagen als u deze wijzigt met {% kbd ← %} en {% kbd → %}. De door u gekozen snelheid wordt hersteld de volgende keer dat u Speed ​​Read gebruikt.