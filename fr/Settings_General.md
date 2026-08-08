# <%= @title %>

Options du panneau de préférences {% prefspane General %} :

![Paramètres : Général][1]

[1]: images/screenshots/preferences-General.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Fenêtre [window]

Conserver les nouvelles fenêtres au premier plan
: Configure automatiquement les nouvelles fenêtres pour qu'elles « flottent » au-dessus des autres applications.

Faire remonter la fenêtre lors d'une mise à jour
: Lorsqu'une modification est détectée dans un fichier surveillé, la fenêtre d'aperçu de ce document remonte au-dessus des autres fenêtres de votre bureau, sans activer Marked.

Translucide en arrière-plan
: Estompe la fenêtre lorsqu'elle n'est pas au premier plan. Utilisez le curseur pour régler l'opacité.

Désactiver les fonctionnalités gourmandes en mémoire sur les documents volumineux
: Désactive certaines fonctionnalités gourmandes en ressources du processeur, telles que les titres repliables, lorsque les documents dépassent 100 000 caractères.

Les nouveaux documents s'ouvrent dans
: Choisissez **fenêtres**, **onglets**, ou **automatique** (suit le réglage système macOS pour la gestion des onglets). Lors de l'utilisation des onglets, naviguez avec {% kbd cmd shift [/] %} et le [panneau Ouverture rapide](Quick_Open.html).

Amener le document mis à jour au premier plan
: Lorsqu'un aperçu est mis à jour, sélectionne son onglet ou place sa fenêtre au premier plan **au sein de Marked uniquement**. Si une autre application est au premier plan (votre éditeur de texte, par exemple), Marked reste en arrière-plan : l'onglet approprié est sélectionné afin d'être prêt lorsque vous revenez à Marked. Pour faire apparaître l'aperçu au-dessus de toutes les applications sans activer Marked, utilisez plutôt **Faire remonter la fenêtre lors d'une mise à jour**.

Restaurer le focus à l'application précédente
: Lorsque cette option est activée, si une action de remontée ou de mise au premier plan lors d'une mise à jour amène Marked au premier plan, le focus clavier revient à l'application qui était au premier plan avant la mise à jour (votre éditeur de texte, par exemple). Lorsqu'elle est désactivée, Marked n'effectue jamais ce transfert de focus. Si Marked ne passe pas au premier plan, cette option n'a aucun effet.

### Barre d'état [status-bar]

Afficher le sélecteur de style
: Affiche le sélecteur de style dans la barre inférieure de la fenêtre d'aperçu.

Afficher le nombre de mots
: Affiche le nombre de mots (ainsi que le bouton des statistiques) dans la barre inférieure de la fenêtre d'aperçu.

Le nombre de mots exclut
: Le calcul du nombre de mots peut ignorer n'importe quelle combinaison des éléments suivants :

- **Notes de bas de page/Citations**
- **Citations en bloc**
- **Blocs de code indentés** (les blocs de code délimités sont toujours exclus)
- **Légendes d'images**

### Raccourcis [shortcuts]

Cliquez dans le champ de raccourci pour enregistrer une combinaison de touches qui déclenche un événement :

Activer Marked
: Bascule vers Marked lorsque ce raccourci est utilisé dans n'importe quelle application.

Faire remonter la première fenêtre
: Fait remonter au premier plan la fenêtre d'aperçu Marked la plus récemment active, sans quitter l'application en cours.

Ouvrir la palette d'actions
: Ouvre la palette de commandes [Actions rapides](Quick_Actions.html) lorsque Marked est actif. Ce raccourci correspond à {% appmenu File, Quick Actions… %} et ne fonctionne qu'au sein de Marked (pas depuis d'autres applications).

Réinitialiser les alertes
: Restaure toutes les boîtes de dialogue d'alerte que vous avez précédemment masquées, afin qu'elles puissent réapparaître.
