# <%= @title %>

Options du panneau de préférences {% prefspane Preview %} :

![Paramètres : Aperçu][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Comportement de l'aperçu

Activer la navigation par mini-carte
: Génère une carte visuelle du document, qui s'affiche lorsque vous appuyez sur « 0 ». Peut entraîner de courts délais lors du rendu de documents volumineux.

Les titres replient les sections
: Cliquer sur un élément de titre replie la section comprise entre celui-ci et le titre suivant.

Exiger un {% kbd cmd %}&#8209;clic
: Si cette option est cochée, les titres ne se replieront/déplieront qu'en cas de clic avec la touche Commande maintenue enfoncée.

Synchroniser le défilement de l'aperçu et de la source
: Lorsque votre éditeur le prend en charge, maintient l'aperçu défilé à l'emplacement correspondant dans le document source.

Synchroniser la lecture rapide avec la position de défilement
: Maintient l'incrustation [Lecture rapide](Speed_Reading.html) alignée sur la position de défilement de l'aperçu. Vous pouvez également activer/désactiver cette option depuis l'incrustation Lecture rapide.

### Défilement vers la modification

Défilement vers la modification
: Lors de la mise à jour de l'aperçu, Marked peut déterminer le premier point où le document a changé et y faire défiler automatiquement la vue. Cela permet de garder l'aperçu synchronisé avec votre position actuelle dans le document en cours d'édition. Le marqueur de modification le plus récent correspond à la première différence détectée dans le document depuis la dernière actualisation. Activer « Ordre inversé des différences » fera au contraire considérer la dernière différence du document (de haut en bas) comme la modification la plus récente.

Afficher le marqueur de modification la plus récente
: Un petit marqueur rouge apparaît à l'endroit de la première modification détectée. Désactivez cette option pour le rendre invisible. (Nécessite l'option **Défilement vers la modification**.)

Afficher tous les marqueurs de différence
: Si cette option est activée, toutes les différences entre la dernière actualisation et le contenu actuel seront mises en évidence dans la marge. Vous pouvez naviguer entre les modifications, qui défilent jusqu'au centre de la vue, à l'aide de <kbd>e</kbd> (en avant) et {% kbd shift E %} (en arrière).

Ordre inversé des différences
: Si cette option est activée, les différences seront repérées dans l'ordre inverse (de bas en haut). Cela affecte la navigation : <kbd>e</kbd> naviguera vers le haut et {% kbd shift E %} naviguera vers le bas. La « modification la plus récente » deviendra alors la dernière différence du document.

### Fonctionnalités supplémentaires

La table des matières suit la position de défilement
: La table des matières met en évidence la section actuelle.

Statistiques contextuelles pour la sélection de texte
: Affiche une info-bulle avec le nombre de mots pour le texte sélectionné dès qu'une sélection est effectuée.

Activer les info-bulles de liens
: Affiche un menu contextuel lorsqu'un lien externe est cliqué et maintenu avant d'être relâché.

Valider automatiquement les URL lors de la mise à jour
: Valide les URL au chargement du document et lors des actualisations. N'affiche des résultats qu'en cas d'erreurs.
: Cette option exécute la [validation des liens](Link_Validation.html) à chaque mise à jour du document (si vous avez un grand nombre de liens, cela peut ralentir le processus et il est préférable de l'éviter).

### Liens wiki

Convertir les [[liens wiki]]
: Active la [navigation wiki](Wiki_Navigation.html) de Marked pour la syntaxe `[[lien wiki]]`.

Extension par défaut
: L'extension de fichier que Marked utilise lors de la résolution des liens wiki qui n'en incluent pas (par exemple, `md`).

### Apparence

Mode sombre
: Affiche toutes les fenêtres en mode « Contraste élevé », avec une interface sombre et, si disponible, la version inversée du style actuel (peut ne pas s'appliquer aux styles personnalisés).

Suivre le réglage système
: Active ou désactive automatiquement le mode sombre lorsque le mode sombre de macOS est activé ou désactivé au niveau du système.

Afficher le chemin complet dans le titre de la fenêtre
: Lorsque cette option est activée, Marked affiche le chemin complet du document actuel dans le titre de la fenêtre.
