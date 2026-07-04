<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked inclut une **extension Partage** macOS qui apparaît dans le menu Partager du système. Utilisez-la pour envoyer un fichier ou du texte sélectionné à Marked sans changer d’application ni copier des URL à la main.

L’extension Partage est **fournie avec Marked 3**. Vous ne la téléchargez ni ne l’installez séparément. Elle est incluse dans les versions Direct, Mac App Store, Marked Pro et Setapp.

## Fonctionnement

Lorsque vous choisissez **Marked** dans un menu Partager, Marked s’ouvre immédiatement. Il n’y a pas de fenêtre de composition intermédiaire.

### Partager un fichier

Depuis le **Finder** (ou une autre app qui partage des fichiers), choisissez **Partager → Marked**.

Marked reçoit le chemin du fichier et l’ouvre avec le même gestionnaire d’URL `x-marked-3://open` qu’ailleurs. Le fichier s’ouvre dans Marked comme un document que vous auriez glissé sur l’icône du Dock ou ouvert avec {% appmenu File, Open... ({{cmd}}O) %}.

Les entrées prises en charge incluent les URL de fichier, les fichiers locaux et les URL web lorsque l’app source les fournit.

### Partager du texte sélectionné

Sélectionnez du texte dans une app comme **TextEdit**, **Safari** ou **Mail**, puis choisissez **Partager → Marked**.

Marked place le texte dans le presse-papiers et ouvre un **aperçu transitoire** via le gestionnaire `x-marked-3://paste`. C’est le même type d’aperçu non enregistré que {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Vous pouvez l’enregistrer plus tard avec {% appmenu File, Save Transient Preview %}.

Texte brut, HTML, RTF et Markdown sont pris en charge lorsque l’app source les fournit.

Voir [URL Handler](URL_Handler.html) pour les détails des commandes sous-jacentes.

## Utiliser le menu Partager

### Depuis le Finder

1. Cliquez avec le bouton droit sur un fichier Markdown ou texte (ou sélectionnez-le et cliquez sur **Partager** dans la barre d’outils du Finder).
2. Choisissez **Marked** dans le menu Partager.

Si **Marked** n’apparaît pas, voir [Activer l’extension Partage](#enable-the-share-extension) ci-dessous.

### Depuis une sélection de texte

1. Sélectionnez le texte à prévisualiser.
2. Ouvrez le menu **Partager** de l’app (menu Partager, bouton de la barre d’outils ou menu contextuel).
3. Choisissez **Marked**.

Marked se lance (ou passe au premier plan) avec un aperçu du contenu partagé.

## Activer l’extension Partage

Marked doit être installé dans `/Applications` (ou votre dossier Applications habituel) et lancé au moins une fois avant que macOS n’affiche son extension Partage.

### Activer Marked dans Réglages Système

1. Ouvrez **Réglages Système**.
2. Allez dans **Général → Ouverture à la connexion et extensions** (sur certaines versions de macOS : **Confidentialité et sécurité → Extensions**).
3. Cliquez sur **Extensions** (ou le bouton **ⓘ** à côté d’Extensions).
4. Sélectionnez **Partage** (ou **Sharing**).
5. Activez **Marked**.

### Ajouter Marked au menu Partager d’une app

Même lorsque l’extension est activée à l’échelle du système, chaque app choisit quelles destinations Partager afficher :

1. Ouvrez une app compatible Partager (Finder et TextEdit conviennent pour tester).
2. Ouvrez le menu **Partager**.
3. Choisissez **Modifier les extensions…** (libellé variable : **Plus…** ou **Préférences des extensions…** sur d’anciennes versions de macOS).
4. Sous **Partager**, cochez **Marked**.
5. Faites éventuellement glisser **Marked** plus haut dans la liste pour un accès plus rapide.

Les changements s’appliquent immédiatement dans la plupart des apps.

## Si Marked n’apparaît pas dans Partager

W> L’extension Partage est disponible à partir de Marked 3.1.9. Assurez-vous d’avoir mis à jour au moins vers cette version.

Essayez ces étapes dans l’ordre :

1. **Lancez Marked une fois** après installation ou mise à jour. Quittez et rouvrez Marked si vous venez de mettre à jour.
2. **Vérifiez que l’extension est activée** dans Réglages Système comme décrit ci-dessus.
3. **Personnalisez le menu Partager** dans l’app depuis laquelle vous partagez. macOS masque les destinations peu utilisées jusqu’à ce que vous les activiez.
4. **Plusieurs copies de Marked :** si les versions Direct et Mac App Store sont installées, seule la copie en cours d’exécution enregistre son extension. Supprimez ou renommez l’autre copie, puis lancez celle que vous voulez.
5. **Redémarrez le Mac** si l’extension n’apparaît toujours pas après une mise à jour. macOS met en cache l’enregistrement des extensions Partage.
6. **Réinstallez Marked** dans `/Applications` si vous testez une build copiée manuellement depuis Xcode ou une image disque. L’extension doit être intégrée dans `Marked.app/Contents/PlugIns/`.

## Conseils

- L’extension Partage convient aux aperçus rapides d’extraits web, de paragraphes d’e-mail ou de notes sans créer de fichier d’abord.
- Pour des pages entières ou des sélections complexes dans un navigateur, les [extensions de navigateur](Using_the_Browser_Extensions.html) offrent souvent plus de contrôle (sélection de section, Markdownify URL, etc.).
- Les fichiers partagés s’ouvrent comme des documents Marked normaux avec surveillance du fichier. Le texte partagé ouvre un aperçu transitoire jusqu’à enregistrement.
