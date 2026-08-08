# <%= @title %>

Options du panneau de préférences {% prefspane Apps %} :

(Voir [Prise en charge d'applications supplémentaires](Additional_Application_Support.html))

![Paramètres : Applications][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Paramètres généraux [general-settings]

Éditeur de texte
: Sélectionnez un éditeur de texte qui recevra le document actuel lorsque vous tapez {% kbd cmd E %}.

Éditer automatiquement les nouveaux fichiers
: Lors de l'utilisation de la commande « Nouveau fichier », cette option ouvrira automatiquement le fichier créé dans l'éditeur externe choisi.

Les liens vers des fichiers texte doivent s'ouvrir dans :
: Détermine le comportement de Marked lorsqu'un lien cliqué dans une fenêtre d'aperçu mène vers un fichier texte local.

Éditeur d'images
: Sélectionnez une application à ouvrir lorsqu'un clic droit sur une image locale et « Éditer l'image » est sélectionné.

Éditeur d'annotation/de balisage d'images
: Sélectionnez une application à ouvrir lorsqu'un clic droit sur une image locale et « Annoter l'image » est sélectionné.

Si aucun éditeur n'est choisi, Marked affiche un menu des applications installées lorsque vous éditez ou annotez. Ce menu comprend les outils courants de Markdown, d'image et d'annotation présents sur votre Mac, une option **Autre…** pour choisir n'importe quelle application depuis `/Applications`, et **Toujours utiliser cette application** (activée par défaut) pour enregistrer votre choix par défaut. Utilisez le bouton d'effacement (cercle avec un X) à côté de chaque contrôle Choisir dans {% prefspane Apps %} pour supprimer une sélection et revenir au sélecteur.

### Paramètres spécifiques aux applications [application-specific-settings]

Afficher les commentaires et annotations par défaut
: Si cette case est cochée, les annotations effectuées dans les documents Scrivener, Fountain, Word et CriticMarkup apparaîtront en surbrillance dans l'aperçu. Décochez pour les masquer complètement. Elles peuvent également être activées ou désactivées pendant la lecture d'un document depuis le menu {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%}.
: Lorsque les commentaires sont activés, les commentaires et notes de bas de page apparaissent dans une barre latérale. Le survol d'un commentaire indique son emplacement dans le document.

#### DocC [docc]

[(Informations sur la prise en charge de DocC)](DocC_Support.html)

Résoudre les références d'images DocC
: À l'intérieur d'un catalogue de documentation `.docc`, résout les références sans extension `![](NomImage)` vers les images du dossier `Resources` du catalogue, y compris les variantes `~dark` et `@2x`.

Résoudre les variantes d'images sombres et @2x
: Pour les images locales possédant une extension de fichier (`images/icon.png`), détecte les fichiers `~dark` et `@2x` associés dans le même dossier et génère un balisage `<picture>` adaptatif. Fonctionne dans tout document Markdown ou HTML, pas uniquement dans les catalogues DocC. Voir [Variantes d'images](Image_Variants.html).

#### Hookmark [hookmark]

Résoudre les URL hook:// dans les images et les liens
: Marked peut lire les URL créées par Hookmark et les résoudre vers leur emplacement sur le disque.

#### Leanpub/GitBook [leanpubgitbook]

Activer la prise en charge de Leanpub
: Interprète les fichiers nommés `Book.txt` comme des fichiers d'index et gère la syntaxe spécifique à Leanpub.

Activer la prise en charge de GitBook
: Interprète les fichiers nommés `SUMMARY.md` comme des fichiers d'index pour la documentation GitBook.

#### Markdownifier [markdownifier]

Utiliser les liens en ligne
: Les documents Markdown créés par Markdownifier utiliseront des liens en ligne plutôt que des liens de référence.

#### MarsEdit [marsedit]

Inclure le titre de l'article comme en-tête Markdown (h1)
: Utilise le titre de l'article sélectionné comme en-tête Markdown.

Afficher les métadonnées sous forme de tableau
: Lorsque cette option est activée, les métadonnées telles que les catégories et les titres s'afficheront sous forme de tableau Markdown dans l'aperçu.

#### Dossiers [folders]

Prévisualiser uniquement ces extensions
: Lors de l'ouverture d'un dossier, Marked recherche le document modifié le plus récemment, en privilégiant par défaut des extensions telles que `md`, `mmd` et `html`. La liste indiquée ici remplace la liste par défaut.

#### Scrivener [scrivener]

[(Informations sur la prise en charge de Scrivener)](Scrivener_Support.html)

Inclure les titres des documents comme en-têtes Markdown
: Analyse le titre des pages et des pages imbriquées pour créer des en-têtes Markdown hiérarchiques.

Ajouter les métadonnées de compilation (titre, auteur) si absentes
: Lorsqu'un projet Scrivener ne possède pas de document `metadata` ni d'en-tête MultiMarkdown existant, ajoute le titre et l'auteur issus des réglages de compilation du projet (`Settings/compile.xml`).

Ouvrir les fichiers .scriv dans Scrivener lorsqu'ils sont ouverts dans Marked
: Lorsqu'un document Scrivener est ouvert dans Marked, l'ouvre automatiquement dans Scrivener également.

#### Word [word]

Convertir le suivi des modifications <-> CriticMarkup
: Si cette option est activée, le suivi des modifications des documents Word sera converti en CriticMarkup lors de l'importation, et CriticMarkup sera converti en suivi des modifications Word lors de l'exportation de fichiers DOCX.

#### Cartes mentales/Plans [MindMapsOutlines]

Intégrer sous forme de cartes mentales Mermaid
: Chaque case à cocher contrôle un format pris en charge. Lorsqu'elle est **activée**, le fichier concerné est converti en diagramme de carte mentale Mermaid (disposition en arbre ordonné). Lorsqu'elle est **désactivée**, Marked utilise l'alternative prévue pour ce format.
: **Cartes mentales** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Si activé : carte mentale Mermaid. Si désactivé : iThoughts intègre son image d'aperçu ; MindManager et FreeMind sont convertis en listes Markdown imbriquées.
: **Fichiers OPML** (.opml). Si activé : carte mentale Mermaid. Si désactivé : liste Markdown imbriquée.
: **Plans OmniOutliner** (.ooutline). Si activé : carte mentale Mermaid. Si désactivé : liste Markdown imbriquée (ou liste de tâches le cas échéant).
: **Plans Bike**. Si activé : carte mentale Mermaid. Si désactivé : liste Markdown imbriquée.
