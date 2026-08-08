# <%= @title %>

Het Snelle Acties-palet is een doorzoekbare opdrachtstarter voor Marked. Het verzamelt acties uit de hoofdmenubalk en het voorbeeld **tandwielmenu**, plus alleen voorbeeldtoetsenbordopdrachten die niet in menu's verschijnen (zoals **Autoscroll**). Gebruik het als u weet wat u wilt doen, maar niet meer weet in welk menu het staat.

## Het palet Snelle acties openen [opening-the-quick-actions-palette]

Open het palet met {% kbd shift cmd P %} of met {% appmenu File, Quick Actions… %}. Het paneel verschijnt als een zwevend venster boven uw huidige document.

Druk nogmaals op dezelfde sneltoets of druk op **Escape** om het palet te sluiten. Als het palet al geopend is, wordt het ook gesloten door **Snelle acties…** in het menu te kiezen.

## Customde snelkoppeling aanpassen [customizing-the-shortcut]

De standaard sneltoets is {% kbd shift cmd P %}. Om dit te wijzigen, opent u {% prefspane General %} en neemt u een nieuwe combinatie op onder **Actiepalet openen** in de sectie **Snelkoppelingen**.

In tegenstelling tot **Activeer Marked** en **Eerste venster openen** werkt de sneltoets Snelle acties alleen wanneer Marked de actieve applicatie is. Het werkt de menusnelkoppeling {% appmenu File, Quick Actions… %} bij zodat deze overeenkomt met uw instelling.

## Zoeken en filteren [search-and-filter]

Typ het zoekveld bovenaan het paneel om opdrachten in realtime te filteren. Matchen is vaag en vergevingsgezind:

- Woordvolgorde doet er niet toe (`view source` komt overeen met **Toggle Source View**)
- Initialen werken goed (`sv` komt overeen met **Bronweergave**)
- Samengevouwen zoekt u naar opdrachten zonder spaties (`akdoc` komt overeen met **Vraag over document**)

Bij elk resultaat wordt de opdrachtnaam aan de linkerkant en de sneltoets (indien beschikbaar) aan de rechterkant in grijs weergegeven. Sommige opdrachten tonen ook een broodkruimelpad (bijvoorbeeld `Preview › Autoscroll`) wanneer de actie afkomstig is van een submenu of de preview-engine.

## Wat in de lijst verschijnt [what-appears-in-the-list]

Het palet bevat:

- **Menuopdrachten** vanuit de hoofdmenubalk, inclusief dynamische menu's zoals **Stijl**, **Geschiedenis** en geopende **Venster**-tabbladen
- **Gear menu**-opdrachten vanuit het voorbeeldvenster
- **Voorbeeldsnelkoppelingen** van de in-preview-toetsenbordkaart (dezelfde opdrachten die worden weergegeven in de preview-help-HUD), inclusief navigatie, automatisch scrollen, bladwijzers, zoeken en andere acties die alleen in het voorbeeld beschikbaar zijn

Wanneer dezelfde opdracht op meer dan één plaats verschijnt, toont Marked het kortste menupad en voegt snelkoppelingsinformatie uit duplicaten samen.

## Toetsenbordnavigatie [keyboard-navigation]

Navigeer volledig via het toetsenbord door het palet Snelle acties:

- **↑/↓ pijltjestoetsen**: door de gefilterde lijst bladeren
- **Return**: Voer de geselecteerde opdracht uit
- **Escape**: sluit het palet
- **⌘-sneltoetsen**: Sluit het palet en voer de bijbehorende menuopdracht uit (druk bijvoorbeeld op {% kbd cmd U %} om **Bronweergave wisselen** uit te voeren in plaats van deze in de lijst te selecteren)

Door gewoon te typen (zonder de Command-toets) wordt het zoekveld gefilterd. Sneltoetsen met slechts één toets, zoals `s` voor Autoscroll, filteren de lijst; druk op **Return** om de geselecteerde opdracht uit te voeren.

## Opdrachten uitvoeren [running-commands]

Als u een menuopdracht selecteert, wordt deze op dezelfde manier verzonden als wanneer u deze in het menu kiest, inclusief dynamische menu-items en tandwielmenu-items.

Als u een **voorbeeldsnelkoppeling** selecteert, wordt de bijbehorende actie uitgevoerd in het actieve voorbeeld (bijvoorbeeld het schakelen tussen automatisch scrollen of naar de volgende koptekst springen). Voor deze opdrachten is een geopend document met een voorbeeld vereist; als er geen voorbeeld beschikbaar is, wordt het palet nog steeds geopend, maar hebben alleen-voorbeeldacties geen effect.

Voor verwante bestandswisseling, zie [Quick Open](Quick_Open.html). Voor de volledige voorbeeldtoetsenbordreferentie, zie [Keyboard Shortcuts](Keyboard_Shortcuts.html) of druk op {% kbd h %} in het voorbeeld om de help-HUD weer te geven.