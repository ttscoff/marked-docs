# <%= @title %>

[Drafts][drafts] sur Mac peut refléter le brouillon actif dans Marked à l'aide de l'**aperçu en continu de Marked**, le même canal basé sur le presse-papiers décrit dans [Aperçu en continu](Streaming_Preview.html). Vous pouvez également envoyer le brouillon actuel une fois avec une **action** communautaire (pas de mises à jour en direct jusqu'à ce que vous l'exécutiez à nouveau).

## Aperçu en continu (Drafts pour Mac) [streaming-preview-drafts-for-mac]

1. Dans Marked, choisissez {% appmenu File, New, Streaming Preview %} pour qu'une fenêtre d'aperçu en continu soit prête.
2. Dans **Drafts pour Mac**, ouvrez **Paramètres** (onglet Général, icône en roue dentée) et activez **Enable Marked App Streaming Preview support**.
3. Cliquez sur **Open Marked** pour faire avancer Marked, puis modifiez votre brouillon dans Drafts ; l'aperçu est mis à jour à mesure que votre brouillon change.

![][draftsprefs]

Lorsque cette option est activée, Drafts pousse Markdown vers Marked via l'intégration que Marked expose pour les aperçus en continu (plutôt que de compter sur la visualisation d'un fichier sur le disque).

### Obtenir Marked [get-marked]

Si le lien *Get Marked App →*, situé juste à côté du bouton *Open Marked* dans l'onglet Général des réglages de Drafts (icône en roue dentée), apparaît actif, cliquez-le pour installer Marked s'il n'est pas déjà présent sur votre Mac.

## Action Aperçu dans Marked (actualisation manuelle) [preview-in-marked-action-manual-refresh]

Installez l'action communautaire [**Aperçu dans Marked**](https://actions.getdrafts.com/a/11f) à partir du répertoire Drafts. Il envoie le **brouillon de texte actuel** à Marked à l'aide d'une URL `x-marked://preview?text=…` (Drafts encode le contenu de votre brouillon pour l'URL). **Le contenu n'est pas mis à jour en direct** : réexécutez l'action chaque fois que vous souhaitez que Marked corresponde au brouillon.

Cette approche est pratique pour les vérifications occasionnelles, tandis que l'**aperçu en continu** convient aux sessions d'écriture continues.

Drafts fonctionne également sur iPhone et iPad ; l'intégration de l'aperçu en continu documentée ici s'applique à **Drafts pour Mac** avec Marked sur le même Mac.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/
