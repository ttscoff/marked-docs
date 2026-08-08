# <%= @title %>

Marked heeft een speciale behandeling voor opmerkingen en annotaties.

## Annotatiebronnen [annotation-sources]

Marked herkent opmerkingen afkomstig van:

- Markdown Voetnoten
- CriticMarkup opmerkingen
- Microsoft Word-opmerkingen en wijzigingen

## De opmerkingenzijbalk [the-comments-sidebar]

Alle annotaties worden weergegeven in een zijbalk en verborgen in het documentvoorbeeld. Om de annotatiezijbalk weer te geven, gebruikt u **Gear Menu -> Proofing -> Show Comments**, of drukt u op {% kbd ctrl cmd C %}.

![A footnote in the Comments  Sidebar][sidebar]

  [sidebar]: images/comment-sidebar-800.jpg @2x width=800

Als u over een opmerking in de zijbalk beweegt, wordt een lijn naar de locatie in het document getrokken. In het geval van voetnoten verwijst dit naar de plaats in de tekst waar de voetnoot voorkomt. In het geval van opmerkingen verwijst het naar de oorspronkelijke locatie van de opmerking, wat een lege ruimte in het voorbeeld kan zijn.

Als u op een opmerking in de zijbalk klikt, wordt een gemarkeerde animatie getekend die naar de locatie ervan wijst.

Het lettertype en de stijl van de zijbalk zijn afhankelijk van de huidige stijl, dus deze kan er bij verschillende stijlen anders uitzien.