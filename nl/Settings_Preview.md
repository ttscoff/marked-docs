# <%= @title %>

Opties in de {% prefspane Preview %}:

![Settings: Preview][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Voorbeeldgedrag [preview-behavior]

Minikaartnavigatie inschakelen
: Genereer een visuele kaart van het document die verschijnt wanneer "0" wordt ingedrukt. Kan korte vertragingen veroorzaken bij het renderen van grote documenten.

Koppen samenvouwen secties
: Als u op een kopelement klikt, wordt het gedeelte tussen dit kopelement en de volgende kop samengevouwen.

Vereist {% kbd cmd %}‑klik
: Als dit is aangevinkt, worden de koppen alleen samengevouwen/uitgevouwen wanneer erop wordt geklikt terwijl de Command-toets ingedrukt wordt gehouden.

Synchronisatievoorbeeld en bronscrollen
: Wanneer uw editor dit ondersteunt, laat u het voorbeeld scrollen zodat het overeenkomt met de overeenkomstige locatie in het brondocument.

Synchroniseer snelheidsmeting met scrollpositie
: Houd de overlay [Speed Reading](Speed_Reading.html) uitgelijnd met de schuifpositie van het voorbeeld. U kunt dit ook wijzigen via de overlay Snel lezen.

### Scroll om te bewerken [scroll-to-edit]

Scroll om te bewerken
: Bij het bijwerken van het voorbeeld kan Marked het eerste punt bepalen waar het document is gewijzigd en er automatisch naartoe scrollen. Hierdoor blijft het voorbeeld gesynchroniseerd met uw huidige locatie in het document dat u aan het bewerken bent. De meest recente bewerkingsmarkering is het eerste verschil in het document sinds de laatste vernieuwing. Als u 'Omgekeerde diff-volgorde' inschakelt, wordt in plaats daarvan het laatste verschil in het document (van boven naar beneden) als de meest recente bewerking beschouwd.

Meest recente bewerkingsmarkering weergeven
: Er verschijnt een kleine rode markering op het punt van de eerste gedetecteerde bewerking. Schakel dit uit om het onzichtbaar te maken. (Vereist **Scroll om te bewerken**.)

Toon alle diff-markeringen
: Als dit is ingeschakeld, worden alle verschillen tussen de laatste vernieuwing en de huidige inhoud gemarkeerd in de rugmarge. U kunt door de bewerkingen navigeren en naar het midden van de weergave scrollen met behulp van <kbd>e</kbd> (vooruit) en {% kbd shift E %} (achteruit).

Omgekeerde diff-volgorde
: Als dit is ingeschakeld, worden verschillen in omgekeerde volgorde gemarkeerd (van onder naar boven). Dit heeft invloed op de navigatie, dus <kbd>e</kbd> zal omhoog navigeren, en {% kbd shift E %} zal naar beneden navigeren. De "meest recente bewerking" wordt het laatste verschil in het document.

### Extra functies [additional-features]

Inhoudsopgave scrollpositie van tracks
: Inhoudsopgave markeert het huidige gedeelte.

Pop-upstatistieken voor tekstselectie
: Toon een pop-up voor het tellen van woorden voor de geselecteerde tekst wanneer er een selectie wordt gemaakt.

Link-popovers inschakelen
: een pop-upmenu weergeven wanneer op externe links wordt geklikt en vastgehouden voordat ze worden vrijgegeven.

Valideer automatisch URL's bij update
: Valideer URL's bij het laden en vernieuwen van documenten. Geeft alleen resultaten weer als er fouten zijn.
: Dit voert [link validation](Link_Validation.html) uit elke keer dat het document wordt bijgewerkt (als u een aanzienlijk aantal links heeft, kan dit een langzaam proces zijn en moet dit worden vermeden).

### Wiki-koppeling [wiki-linking]

Converteer [[Wiki-links]]
: Schakel de [wiki navigation](Wiki_Navigation.html) van Marked in voor `[[wiki link]]` syntaxis.

Standaardextensie
: De bestandsnaamextensie Marked wordt gebruikt bij het omzetten van wiki-links die geen extensie bevatten (bijvoorbeeld `md`).

### Verschijning [appearance]

Donkere modus
: Geef alle vensters weer in de modus "Hoog contrast", met donker chroom en, indien beschikbaar, de omgekeerde versie van de huidige stijl (mogelijk niet van toepassing op Custom stijlen).

Match systeeminstelling
: automatisch overschakelen naar de donkere modus wanneer de donkere modus van macOS voor het hele systeem wordt in- of uitgeschakeld.

Toon het volledige pad in de venstertitel
: Indien ingeschakeld, zal Marked het volledige pad naar het huidige document in de venstertitel weergeven.