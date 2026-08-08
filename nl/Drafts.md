# <%= @title %>

[Drafts][drafts] op Mac kan het actieve concept spiegelen in Marked met behulp van **Marked streaming preview**: hetzelfde op het klembord gebaseerde kanaal dat wordt beschreven in [Streaming Preview](Streaming_Preview.html). Je kunt het huidige concept ook eenmalig verzenden met een **actie** van de community (geen live updates totdat je het opnieuw uitvoert).

## Streamingvoorbeeld (concepten voor Mac) [streaming-preview-drafts-for-mac]

1. Kies in Marked {% appmenu File, New, Streaming Preview %} zodat er een streamingvoorbeeldvenster gereed is.
2. Open in **Concepten voor Mac** **Instellingen** en schakel **Enable Marked Ondersteuning voor app-streamingpreview in**.
3. Gebruik **Open Marked** als Drafts dit aanbiedt om Marked naar voren te halen, en bewerk vervolgens in Drafts; het voorbeeld wordt bijgewerkt naarmate uw concept verandert.

![][draftsprefs]

Als deze optie is ingeschakeld, pusht Drafts Markdown naar Marked via de integratie die Marked beschikbaar stelt voor het streamen van voorbeelden (in plaats van te vertrouwen op het bekijken van een bestand op schijf).

### Ontvang Marked [get-marked]

Als **Get Marked App** verschijnt in het instellingenblad van Drafts, gebruik deze dan als Marked nog niet is geïnstalleerd.

## Voorbeeld in actie Marked (handmatig vernieuwen) [preview-in-marked-action-manual-refresh]

Installeer de communityactie [**Preview in Marked**](https://actions.getdrafts.com/a/11f) vanuit de conceptmap. Het verzendt de **huidige concepttekst** naar Marked met behulp van een `x-marked://preview?text=…` URL (Concepten vervangt uw conceptinhoud). **Inhoud wordt niet live bijgewerkt**: voer de actie opnieuw uit wanneer je wilt dat Marked overeenkomt met het concept.

Deze aanpak is handig voor incidentele controles, terwijl **streamingvoorbeeld** geschikt is voor continue schrijfsessies.

Drafts werkt ook op iPhone en iPad; De streaming preview-integratie die hier wordt gedocumenteerd, is van toepassing op **Concepten voor Mac** met Marked op dezelfde Mac.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/
