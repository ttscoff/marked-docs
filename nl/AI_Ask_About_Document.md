# <%= @title %>

Vragen over Document gebruikt **Apple Intelligence** en het taalmodel op het apparaat dat is ingebouwd in recente versies van macOS om uw Markdown voorbeeld samen te vatten en vragen over de inhoud ervan te beantwoorden. Alle verwerking vindt plaats op uw Mac; documenttekst wordt voor deze functie niet naar de servers van Marked of AI-services van derden verzonden.

## Wat Apple Intelligence biedt [what-apple-intelligence-provides]

Apple Intelligence is het systeem van Apple voor generatieve functies op apparaten. Marked maakt gebruik van het **Foundation Models**-framework van Apple om toegang te krijgen tot hetzelfde model op het apparaat dat systeemschrijftools aanstuurt, dat direct in Marked wordt weergegeven voor documentgerichte taken.

Marked verzendt de platte tekst van uw document (de syntaxis van Markdown is voor de duidelijkheid verwijderd) naar dit lokale model. Het model genereert samenvattingen, overzichten en antwoorden in een zwevend paneel naast uw voorbeeldvenster. Omdat het model lokaal draait, werkt het offline zodra Apple Intelligence is ingesteld en het systeemmodel is gedownload.

Apple Intelligence is het beste in taaltaken zoals samenvatten, schetsen, kernpunten extraheren en vragen over de aangeboden tekst beantwoorden. Het is geen algemene codeerassistent of rekenmachine, en zeer lange documenten worden in secties behandeld, zodat de resultaten binnen de contextgrenzen van het model blijven.

## Systeemcompatibiliteit [system-compatibility]

Vragen over document wordt alleen weergegeven als uw Mac de functie kan uitvoeren.

**Vereist:**

- **macOS 26 (Tahoe)** of hoger
- Een **Mac met Apple Intelligence ondersteuning** (Silicium-Macs van Apple die voldoen aan de apparaatvereisten van Apple)
- **Apple Intelligence ingeschakeld** in Systeeminstellingen

**Niet ondersteund:**

- Intel Macs en andere Macs die zijn gemarkeerd als niet geschikt voor Apple Intelligence
- macOS-versies eerder dan Tahoe 26
- Ruwe **HTML previews** (de functie is voor Markdown en op tekst gebaseerde documentworkflows)

Als uw Mac in aanmerking komt maar het menu-item ontbreekt, controleer dan of Apple Intelligence is ingeschakeld en dat u een huidige versie van Marked gebruikt die deze functie bevat. Het menu is volledig verborgen op niet-ondersteunde systemen en wordt niet weergegeven in een uitgeschakelde status.

## Apple Intelligence inschakelen [enabling-apple-intelligence]

1. Open **Systeeminstellingen**.
2. Ga naar **Apple Intelligence & Siri** (of **Apple Intelligence**, afhankelijk van je macOS-versie).
3. Schakel **Apple Intelligence** in en voltooi alle installatiestappen die Apple vraagt.
4. Wacht tot het model op het apparaat klaar is met downloaden als daarom wordt gevraagd. Totdat het model klaar is, kan Marked het menu-item weergeven, maar een bericht weergeven dat Apple Intelligence nog bezig is met voorbereiden.

Marked bevat geen afzonderlijke voorkeur voor deze functie. Beschikbaarheid volgt de systeemmodelstatus gerapporteerd door macOS.

## Vraag over document openen [opening-ask-about-document]

Open het paneel op een van deze manieren:

- **Voorbeeld > Vragen over document...**
- Sneltoets {% kbd shift ctrl cmd I %} (terwijl een Markdown voorbeelddocument het actieve venster is)

Het paneel wordt aan de linkerkant van het documentvenster gekoppeld. Je hebt een open document nodig met leesbare tekst; een leeg document of een voorbeeld met alleen HTML biedt de opdracht niet.

## Het paneel Vragen over document [the-ask-about-document-panel]

Het paneel is georganiseerd als een eenvoudige chatweergave:

- **Vooraf ingestelde acties** bovenaan voor algemene taken
- Een **reactiegebied** in het midden waar samenvattingen en antwoorden verschijnen (streaming terwijl ze worden gegenereerd)
- Een **vraagveld** onderaan waar u aangepaste vragen typt, met de knoppen **Vragen** en **Annuleren**

Nadat een antwoord is voltooid, keert de focus terug naar het vraagveld, zodat u een vervolgvraag kunt stellen zonder te klikken.

### Vooraf ingestelde acties [preset-actions]

| Actie | Wat het doet |
| :-- | :-- |
| **Document samenvatten** | Produceert een korte, samenhangende samenvatting van het volledige document. Lange documenten worden in secties samengevat en gecombineerd. |
| **Selectie samenvatten** | Geeft alleen een samenvatting van de tekst die momenteel in het voorbeeld is geselecteerd. Selecteer eerst tekst; anders wordt u door Marked gevraagd een selectie te maken of Document samenvatten te gebruiken. |
| **Overzicht** | Creëert een hiërarchische schets van de documentstructuur met behulp van koppen en opsommingstekens. |
| **Belangrijkste punten** | Geeft de belangrijkste punten uit het document weer als een lijst met opsommingstekens. |

Vooraf ingestelde acties vereisen geen tekst in het vraagveld. Klik op een knop en wacht op het antwoord in het bovenstaande paneel.

### Je eigen vragen stellen [asking-your-own-questions]

1. Typ een vraag in het veld onder aan het paneel, bijvoorbeeld 'Welk probleem lost dit document op?' of "Wie is het beoogde publiek?"
2. Druk op **Return** of klik op **Vragen**.
3. Lees het antwoord terwijl het naar het antwoordgebied stroomt.

Voor vragen over een specifieke passage **selecteert u die tekst in het voorbeeld** voordat u deze stelt. Marked verzendt de selectie als context in plaats van het hele document wanneer een selectie actief is.

Klik op **Annuleren** om een ​​lopende aanvraag te stoppen.

## Voorbeelden [examples]

### Snel overzicht van een lang artikel [quick-overview-of-a-long-article]

Open een lange blogpost of rapport in Marked, kies **Voorbeeld > Vragen over document…** en klik op **Document samenvatten**. Gebruik de samenvatting om te beslissen of u het volledige stuk wilt lezen of uw geheugen wilt opfrissen als u even niet aan het concept hebt gewerkt.

### Opmerkingen over een geselecteerde paragraaf [notes-on-a-selected-paragraph]

Markeer een compacte alinea in het voorbeeld, open Vragen over document en klik op **Selectie samenvatten**. Handig als je slechts een kortere versie van één sectie nodig hebt.

### Structurele herziening [structural-review]

Klik op **Overzicht** op een concept met veel koppen om te zien of de redenering logisch verloopt, of gebruik **Kernpunten** voordat u een document naar iemand anders verzendt om te controleren of de hoofdideeën duidelijk zijn.

### Gerichte vragen [targeted-questions]

Terwijl er geen selectie actief is, typt u vragen zoals:

- "Wat zijn de drie belangrijkste aanbevelingen?"
- "Vermeldt dit document licenties?"
- "Vermeld alle genoemde data of deadlines."

Terwijl een selectie actief is, kunt u specifiekere vragen stellen, zoals 'Wat veronderstelt deze paragraaf over de lezer?' of "Herschrijf dit idee in één zin" (het model antwoordt over de selectie; het bewerkt uw bronbestand niet).

## Tips en beperkingen [tips-and-limitations]

- **Privacy:** Bij de verwerking wordt gebruik gemaakt van het on-device-model van Apple. Marked leest uw documenttekst nog steeds lokaal om inhoud aan dat model te leveren; behandel gevoelig materiaal dienovereenkomstig.
- **Nauwkeurigheid:** Controleer belangrijke feiten aan de hand van uw bron. AI-samenvattingen kunnen details weglaten of dubbelzinnige passages verkeerd lezen.
- **Lengte:** Extreem lange documenten worden in stukjes verwerkt. Samenvattingen en antwoorden geven indirect de volledige tekst weer; voor precisie op één sectie selecteert u eerst die sectie.
- **Taal:** De resultaten volgen de taalmogelijkheden van het systeem Apple Intelligence model op uw Mac.
- **Weigeringen:** Het systeem kan sommige verzoeken afwijzen op basis van het veiligheidsbeleid van Apple.

Als Vragen over document niet beschikbaar is, controleer dan de Systeeminstellingen voor de status Apple Intelligence en zorg ervoor dat u een voorbeeld van een Markdown document bekijkt op een ondersteunde Mac met macOS 26 of hoger.