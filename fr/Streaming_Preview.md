# <%= @title %>

En ouvrant {% appmenu File, New, Streaming Preview %}, Marked reçoit des mises à jour en direct via un presse-papiers nommé, plutôt qu'en surveillant un fichier sur le disque. L'application source doit s'intégrer avec Marked.

[Curio](Curio.html), [Drafts](Drafts.html) et [The Archive](The_Archive.html) et [Traverse](Traverse.html) documentent leurs propres options et commandes de menu. nvUltra, nvALT, Bear et d'autres utilisent le même canal : ouvrez l'aperçu en continu dans Marked, activez l'intégration dans votre éditeur, et commencez à taper ; les mises à jour arrivent quasiment en temps réel.

## Développeurs [developers]

Pour intégrer l'aperçu en continu à votre application, il vous suffit de placer le texte Markdown à prévisualiser sur un presse-papiers nommé. Utilisez le code suivant (Objective-C) pour effectuer la mise à jour, de préférence dans une méthode didEndEditing ou à intervalles limités :

```obj-c
NSString *rawString = @"the text to process";
// le presse-papiers *doit* être nommé 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Déclarer l'app d'origine et le format [declaring-the-origin-app-and-format]

Placez un mot-clé `source` ou `format` dans un commentaire HTML au début du texte envoyé. Marked lit le commentaire et le retire de l'aperçu, donc la note reste compatible avec les processeurs GFM et MultiMarkdown. L'espace après les deux-points est facultatif (`source:Bear.app` et `source: Bear.app` sont identiques), et le mot-clé ignore la casse.

Les deux valeurs sont libres. Marked a un comportement intégré pour certaines d'entre elles, et chaque valeur est disponible dans le [Custom Processor](Custom_Processor.html) (Conductor) sous **Source de l'aperçu en continu** et **Format de l'aperçu en continu**. Ces critères acceptent **est**, **n'est pas**, **contient** et **ne contient pas**.

**`source: APP_NAME`** nomme l'app d'origine, par son nom ou son bundle id. Marked s'en sert pour ajouter un traitement particulier à cette app. `source: Bear.app` et `source: Drafts.app` activent le comportement d'aperçu de ces apps. Tout autre nom peut encore être comparé par une règle Conductor, pour lancer vos propres actions pour cette app :

```html
<!--source:Bear.app-->
```

**`format: fountain`** active le traitement [Fountain](Fountain_for_Screenwriters.html), donc le flux est affiché comme un scénario plutôt que comme du Markdown. Toute autre valeur de format ne change pas le processeur. Elle sert à une règle Conductor, par exemple **Format de l'aperçu en continu** `est` `fountain`.

```html
<!--format:fountain-->
```

Un commentaire peut porter les deux mots-clés :

```html
<!--
source: Bear.app
format: fountain
-->
```

### Ouvrir l'aperçu en continu par programmation [opening-the-streaming-preview-programatically]

Votre application peut ouvrir l'aperçu en continu par programmation à l'aide de la méthode du gestionnaire d'URL `x-marked-3://stream/`. Cette méthode accepte également un paramètre `x-success`, dans lequel vous pouvez transmettre l'identifiant de bundle d'une application à activer une fois l'opération terminée.
