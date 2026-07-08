# <%= @title %>

En ouvrant {% appmenu File, New, Streaming Preview %}, Marked reçoit des mises à jour en direct via un presse-papiers nommé, plutôt qu'en surveillant un fichier sur le disque. L'application source doit s'intégrer avec Marked.

[Curio](Curio.html), [Drafts](Drafts.html) et [The Archive](The_Archive.html) documentent leurs propres options et commandes de menu. nvUltra, nvALT, Bear et d'autres utilisent le même canal : ouvrez l'aperçu en continu dans Marked, activez l'intégration dans votre éditeur, et commencez à taper ; les mises à jour arrivent quasiment en temps réel.

## Développeurs

Pour intégrer l'aperçu en continu à votre application, il vous suffit de placer le texte Markdown à prévisualiser sur un presse-papiers nommé. Utilisez le code suivant (Objective-C) pour effectuer la mise à jour, de préférence dans une méthode didEndEditing ou à intervalles limités :

```obj-c
NSString *rawString = @"the text to process";
// le presse-papiers *doit* être nommé 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Déclarer une URL de base pour les ressources relatives

Vous pouvez également fournir une URL de base pour l'aperçu en continu, afin que les URL relatives des images et autres ressources fonctionnent comme dans l'application source. Si l'URL de base inclut un nom de fichier, son nom et son extension seront mis à disposition des processeurs personnalisés, sans que cela soit obligatoire. Pour inclure l'URL de base, placez simplement un objet NSURL dans le presse-papiers :

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

Ou en Swift :

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Si la version Mac App Store de Marked est utilisée et que l'URL de base n'est pas accessible en raison du bac à sable, l'autorisation sera demandée la première fois que l'URL est chargée dans l'aperçu.

### Déclarer l'application source

Les applications peuvent également se déclarer comme source du contenu de l'aperçu en incluant une ligne de métadonnées `source`. Cela se fait généralement au sein d'un commentaire HTML, afin d'assurer la compatibilité avec les processeurs GFM et MultiMarkdown. Il suffit d'indiquer le nom de l'application ou son identifiant de bundle :

```html
<!--
source: Bear.app
-->
```

### Ouvrir l'aperçu en continu par programmation

Votre application peut ouvrir l'aperçu en continu par programmation à l'aide de la méthode du gestionnaire d'URL `x-marked-3://stream/`. Cette méthode accepte également un paramètre `x-success`, dans lequel vous pouvez transmettre l'identifiant de bundle d'une application à activer une fois l'opération terminée.
