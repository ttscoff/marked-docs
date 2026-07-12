# <%= @title %>

Marked inclut une **extension de partage** macOS qui apparaît dans le menu Partager du système. Utilisez-la pour envoyer un fichier ou du texte sélectionné vers Marked sans changer d'application ni copier d'URL à la main.

L'extension de partage est **intégrée à Marked 3**. Vous n'avez pas besoin de la télécharger ou de l'installer séparément. Elle est fournie avec les versions Direct, Mac App Store, Marked Pro et Setapp.

## Fonctionnement

Lorsque vous choisissez **Marked** dans un menu Partager, Marked s'ouvre immédiatement. Il n'y a pas de fenêtre de composition intermédiaire.

### Partager un fichier

Depuis le **Finder** (ou une autre application permettant de partager des fichiers), choisissez **Partager → Marked**.

Marked reçoit le chemin du fichier et l'ouvre avec le même gestionnaire d'URL `x-marked-3://open` utilisé ailleurs. Le fichier s'ouvre dans Marked comme un document que vous auriez glissé sur l'icône du Dock ou ouvert avec {% appmenu File, Open... ({{cmd}}O) %}.

Les entrées prises en charge incluent les URL de fichiers, les fichiers locaux et les URL web, lorsque l'application d'envoi les fournit.

### Partager du texte sélectionné

Sélectionnez du texte dans une application comme **TextEdit**, **Safari** ou **Mail**, puis choisissez **Partager → Marked**.

Marked place le texte dans le presse-papiers et ouvre un **aperçu temporaire** à l'aide du gestionnaire `x-marked-3://paste`. Il s'agit du même type d'aperçu non enregistré que celui obtenu avec {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Vous pouvez l'enregistrer par la suite avec {% appmenu File, Save Transient Preview %}.

Le texte brut, le HTML, le RTF et les sélections Markdown sont pris en charge lorsque l'application source les fournit.

Voir [Gestionnaire d'URL](URL_Handler.html) pour plus de détails sur les commandes sous-jacentes.

## Utilisation du menu Partager

### Depuis le Finder

1. Cliquez avec le bouton droit sur un fichier Markdown ou texte (ou sélectionnez-le et cliquez sur le bouton **Partager** de la barre d'outils du Finder).
2. Choisissez **Marked** dans le menu Partager.

Si **Marked** n'apparaît pas, consultez [Activer l'extension de partage](#enable-the-share-extension) ci-dessous.

### Depuis une sélection de texte

1. Sélectionnez le texte que vous souhaitez prévisualiser.
2. Ouvrez le menu **Partager** de l'application (élément **Partager** de la barre de menus, bouton Partager de la barre d'outils, ou menu contextuel du clic droit).
3. Choisissez **Marked**.

Marked se lance (ou passe au premier plan) avec un aperçu du contenu partagé.

## Activer l'extension de partage {#enable-the-share-extension}

Marked doit être installé dans `/Applications` (ou votre dossier Applications habituel) et lancé au moins une fois avant que macOS ne liste son extension de partage.

### Activer Marked dans Réglages Système

1. Ouvrez **Réglages Système**.
2. Accédez à **Général → Éléments de connexion et extensions** (sur certaines versions de macOS, cela apparaît sous **Confidentialité et sécurité → Extensions**).
3. Cliquez sur **Extensions** (ou sur le bouton **ⓘ** à côté d'Extensions).
4. Sélectionnez **Partage** (ou **Partager**).
5. Activez **Marked**.

### Ajouter Marked au menu Partager d'une application

Même lorsque l'extension est activée pour l'ensemble du système, chaque application vous permet de choisir les destinations de partage qui apparaissent :

1. Ouvrez une application prenant en charge le partage (le Finder et TextEdit sont de bons exemples pour tester).
2. Ouvrez le menu **Partager**.
3. Choisissez **Modifier les extensions…** (le libellé peut être **Plus…** ou **Préférences des extensions…** sur les anciennes versions de macOS).
4. Sous **Partager**, cochez **Marked**.
5. Vous pouvez éventuellement faire glisser **Marked** plus haut dans la liste pour y accéder plus facilement.

Les modifications s'appliquent immédiatement à ce menu Partager dans la plupart des applications.

## Si Marked n'apparaît pas dans le menu Partager

W> L'extension de partage est disponible depuis Marked 3.1.9. Assurez-vous d'avoir mis à jour vers au moins cette version.

Essayez les étapes suivantes, dans l'ordre :

1. **Lancez Marked une fois** après l'installation ou la mise à jour. Quittez et rouvrez Marked si vous venez de faire une mise à jour.
2. **Vérifiez que l'extension est activée** dans Réglages Système, comme décrit ci-dessus.
3. **Personnalisez le menu Partager** dans l'application depuis laquelle vous partagez. macOS masque les destinations de partage peu utilisées jusqu'à ce que vous les activiez.
4. **Vérifiez la présence de plusieurs copies de Marked.** Si une version Direct et une version Mac App Store sont toutes deux installées, seule la copie que vous exécutez enregistre son extension. Supprimez ou renommez la copie que vous n'utilisez pas, puis lancez celle que vous souhaitez utiliser.
5. **Redémarrez le Mac** si l'extension n'apparaît toujours pas après une mise à jour. macOS met en cache l'enregistrement des extensions de partage et a parfois besoin d'un redémarrage pour l'actualiser.
6. **Réinstallez Marked** dans `/Applications` si vous testez une version copiée manuellement depuis Xcode ou une image disque. L'extension de partage doit être intégrée dans le bundle de l'application, à l'emplacement `Marked.app/Contents/PlugIns/`.

## Astuces

- L'extension de partage est idéale pour prévisualiser rapidement des extraits web, des paragraphes d'e-mail ou des notes sans avoir à créer un fichier au préalable.
- Pour des pages entières ou des sélections complexes depuis un navigateur, les [extensions de navigateur](Using_the_Browser_Extensions.html) peuvent offrir plus de contrôle (sélection de section, Markdownify d'URL, etc.).
- Les fichiers partagés s'ouvrent comme des documents Marked normaux, avec la surveillance de fichier activée. Le texte partagé s'ouvre comme un aperçu temporaire jusqu'à ce que vous l'enregistriez.
