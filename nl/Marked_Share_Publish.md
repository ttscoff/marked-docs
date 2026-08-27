<!-- MT draft for nl — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** is de online publicatieservice van Marked op [share.markedapp.com](https://share.markedapp.com). Sluit uw Mac één keer aan en publiceer vervolgens het voorste document als een **TextPack** met afbeeldingen en optionele leesmodusmarkeringen. Iedereen met de link kan het document op internet bekijken.

Deze functie staat los van de macOS **Share-extensie** (systeem Share-menu). Zie [Using the Share Extension](Share_Extension.html) voor het verzenden van bestanden of selecties naar Marked vanuit andere apps.

## Verbind uw account [connect-your-account]

Voordat u voor het eerst publiceert, koppelt u Marked aan uw Share-account:

1. Kies {% appmenu Archief, Publiceren, Account verbinden… %}.
2. Marked opent uw standaardbrowser om u aan te melden bij share.markedapp.com.
3. Nadat u de verbinding heeft goedgekeurd, keert de browser terug naar Marked met een beveiligde inloglink. Bevestig het accountlabel dat in het dialoogvenster wordt weergegeven.

Marked slaat het API-token en de apparaatsleutel op in de macOS-sleutelhanger op deze Mac. Inloggegevens worden niet naar logboeken of crashrapporten geschreven.

Om de verbinding te verbreken, kiest u {% appmenu Archief, Publiceren, Account loskoppelen… %}. Gepubliceerde documenten blijven online; indien nodig kunt u de toegang op elk gewenst moment intrekken op share.markedapp.com.

## Een document publiceren [publiceer-een-document]

Terwijl een document geopend is in het voorbeeld, kiest u {% appmenu Archief, Publiceren, Publiceren… %}.

De eerste keer dat u een document publiceert, toont Marked een klein optieblad:

- **Titel** — weergegeven op Share (standaard de documentnaam zonder de extensie).
- **Zichtbaarheid** — Privé, verborgen of openbaar. Nieuwe publicaties zijn standaard **Niet vermeld** (bereikbaar via een link, niet openbaar vermeld).
- **Voeg hoogtepunten en opmerkingen toe** — sluit hoogtepunten van de Leesmodus in de TextPack in. Staat standaard aan wanneer het document hoogtepunten bevat.
- **Anderen toestaan ​​om te remixen**: indien ingeschakeld kunnen kijkers het document op Share splitsen.

Marked bouwt een TextPack op de achtergrond (Markdown, assets en optioneel `highlights.json`), uploadt deze en registreert de gedeelde URL op deze Mac.

### Een bestaande publicatie bijwerken [update-an-existing-publish]

Nadat een document is gekoppeld aan Delen, luidt het menu-item **Gepubliceerd document bijwerken** in plaats van **Publiceren…**. Kies deze optie om een ​​nieuwe TextPack versie te uploaden. Marked verzendt de inhoudshash van de server, zodat gelijktijdige bewerkingen vanaf een andere Mac of internet worden gedetecteerd.

Als iemand anders het document eerst op Share heeft bijgewerkt, vraagt ​​Marked of u wilt **Overschrijven** met de versie van deze Mac, **Openen op internet** of **Annuleren**.

## Na publicatie [na publicatie]

Wanneer een publicatie is voltooid, bevestigt Marked succes en biedt het:

- **Kopieer de deellink** — {% appmenu Archief, Publiceren, Share-link kopiëren %}
- **Openen op internet** — {% appmenu Archief, Publiceren, Openen op het web %}

Deze opdrachten zijn van toepassing op het voordocument als het een gekoppeld publicatierecord heeft.

## Venster gepubliceerde documenten [venster gepubliceerde documenten]

Kies {% appmenu Archief, Publiceren, Gepubliceerde documenten… %} om een ​​lijst met documenten te openen die vanaf deze Mac zijn gepubliceerd en zijn gesynchroniseerd vanuit uw Share-account.

Voor elke inzending kunt u:

- **Open** het lokale bestand wanneer Marked nog steeds een link ernaar op schijf heeft.
- **Importeer** een TextPack als er geen lokaal bestand is (sla het ergens op en open het in Marked).
- **Openen op internet** of **Kopieer link** voor de deel-URL.
- **Onthulling in Finder** wanneer een lokaal pad bekend is.
- **Vergeten** verwijdert de record van deze Mac zonder het online document te verwijderen.

De lijst wordt vernieuwd vanuit Share wanneer u verbonden bent. Als u offline bent of de verbinding niet is verbroken, toont Marked gegevens in de cache en wordt u mogelijk gevraagd opnieuw verbinding te maken.

## Wat je kunt publiceren [wat-je-kan-publiceren]

Je kunt elk document publiceren dat Marked kan weergeven, waaronder:

- Opgeslagen Markdown en tekstbestanden
- Tijdelijke voorbeelden (klembord, streaming of niet-opgeslagen documenten)
- TextBundles en andere ondersteunde formaten

Per documentvenster wordt slechts één publicatiebewerking tegelijk uitgevoerd; het menu-item is uitgeschakeld terwijl er wordt geüpload.

## Tips [tips]

- Publiceren omvat afbeeldingen waarnaar in het voorbeeld wordt verwezen. Zeer grote bundels kunnen vóór het uploaden worden afgewezen; verminder ingebedde assets als u een limiet voor de grootte bereikt.
- Hoogtepunten die in TextPack worden geëxporteerd, gebruiken het JSON-formaat voor hoogtepunten van Marked. Zie [Reading Mode](Reading_Mode.html) voor het maken en exporteren van hoogtepunten.
- Marked Share is beschikbaar in de Direct-, Mac App Store-, Setapp- en Marked Pro-builds. Voor publiceren is geen apart abonnement vereist.
