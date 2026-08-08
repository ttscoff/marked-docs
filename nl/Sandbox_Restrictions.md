# <%= @title %>

De Mac App Store (MAS)-versie van Marked draait in een sandbox-omgeving die om veiligheidsredenen bepaalde bewerkingen beperkt. Dit kan van invloed zijn op sommige functies, vooral bij gebruik van Custom Processors met externe binaire bestanden of scripts.

## Algemene sandboxbeperkingen [common-sandbox-restrictions]

### Voer opdrachtbinaire bestanden uit [run-command-binaries]

Het meest voorkomende probleem dat gebruikers tegenkomen is dat externe binaire bestanden niet rechtstreeks in de MAS-versie kunnen worden uitgevoerd. Dit heeft invloed op:

- **Externe processors** zoals Pandoc, Kramdown of andere opdrachtregelprogramma's
- **Custom scripts** die afhankelijk zijn van externe binaire bestanden
- **Systeemhulpprogramma's** die niet toegankelijk zijn vanuit de sandbox

### Oplossingen [workarounds]

#### Binaire bestanden kopiëren naar de appbundel [copying-binaries-to-the-app-bundle]

Als u externe processors zoals Pandoc in de MAS-versie moet gebruiken, kunt u het binaire bestand naar de app-bundel kopiëren:

1. Klik met de rechtermuisknop op Marked.app → **Pakketinhoud weergeven**
2. Navigeer naar **Inhoud/Bronnen/**
3. Maak een map `bin` als deze niet bestaat
4. Kopieer uw binaire bestand (bijvoorbeeld `pandoc`) naar deze map `bin`
5. Maak het uitvoerbaar: `chmod +x` het binaire bestand
6. Verwijs er in de actie Opdracht uitvoeren naar als:
   - `YOUR_BINARY_NAME [arguments]`
   - Of gebruik het volledige pad: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Opmerking**: Scripts met externe shebangs (zoals Python-scripts die verwijzen naar `/opt/homebrew/bin/python`) worden automatisch uitgevoerd via systeeminterpreters wanneer ze naar de bundel worden gekopieerd. De MAS-versie kan nog steeds problemen ondervinden bij het uitvoeren van binaire bestanden die eigenlijk Python- of Ruby-scripts zijn in plaats van binaire bestanden.

**Belangrijk**: je moet de binaire bestanden na elke app-update opnieuw kopiëren, omdat updates de hele bundel vervangen.

#### Ingebedde scripts gebruiken [using-embedded-scripts]

In plaats van externe opdrachten uit te voeren, kunt u de actie **Ingesloten script uitvoeren** gebruiken in Custom Regels. Hierdoor kunt u scripts rechtstreeks in de code-editor van Marked schrijven, die toegang heeft tot systeemtolken die beschikbaar zijn in de sandbox.

## Overschakelen naar de niet-sandboxversie [crossgrade]

Als u vaak externe binaire bestanden moet gebruiken of als u andere sandbox-beperkingen tegenkomt, kunt u wellicht overschakelen naar de niet-sandbox-versie van Marked. De niet-sandboxversie kent dergelijke beperkingen niet en kan elk opdrachtregelprogramma of script uitvoeren dat u hebt geïnstalleerd.

### Voor abonnementsgebruikers [for-subscription-users]

Als je een actief Mac App Store-abonnement hebt:

1. **Annuleer uw MAS-abonnement** in Systeeminstellingen → Apple ID → Media en aankopen → Abonnementen
2. **Download de gratis proefversie** van [https://markedapp.com](https://markedapp.com)
3. **Start een Paddle-abonnement** rechtstreeks via de app of website

De Paddle-versie biedt dezelfde functies zonder beperkingen op het gebied van sandboxen.

### Voor permanente ontgrendelingshouders [for-permanent-unlock-holders]

Als je een permanente ontgrendeling of levenslange licentie hebt gekocht via de Mac App Store, [email the developer](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Please%20include%20your%20UUID%20%28Help-%3ECopy%20UUID%20in%20Marked%29%20in%20this%20email%20for%20receipt%20verification.) om een ​​gratis levenslange Paddle-licentie aan te vragen.

**Belangrijk**: Om uw aankoop te verifiëren, dient u een van de volgende zaken in uw e-mail op te nemen:

- Uw **gebruikers-ID** (UUID) - gebruik **Help->Kopieer UUID** om deze naar uw klembord te kopiëren en plak deze vervolgens in uw e-mail
- Uw **transactie-ID** uit uw App Store-bon (u kunt deze vinden in uw aankoopgeschiedenis in de App Store-app)

De Mac App Store verstrekt uw e-mailadres niet aan ontwikkelaars, dus verifiëren we aankopen met behulp van transactie-ID's of gebruikers-ID's die op onze server zijn opgeslagen. Door deze informatie op te nemen, kunnen we uw aankoop snel verifiëren en uw gratis Paddle-licentie genereren.

### Setapp-versie [setapp-version]

Als alternatief kunt u, als u een Setapp-abonnement heeft, de Setapp-versie van Marked gebruiken, die ook geen sandbox heeft en volledige toegang heeft tot systeembronnen.

## Aanvullende bronnen [additional-resources]

Voor meer informatie over Custom processors en hun mogelijkheden, zie [Custom Processor](Custom_Processor.html).

