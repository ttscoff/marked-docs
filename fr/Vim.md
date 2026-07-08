# <%= @title %>

[vim-marked][vimrepo] est un plugin Vim qui ouvre le buffer Markdown actuel dans Marked. Il ajoute les commandes `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` et `:MarkedPreview`, afin de pouvoir envoyer le fichier (ou une plage) vers Marked sans quitter l'éditeur.

## Installation

Installez-le avec votre gestionnaire de plugins ; consultez le [README du projet][vimrepo] pour `vim-plug` et les autres options. Le réglage par défaut de `g:marked_filetypes` inclut `markdown` et les variantes courantes ; étendez la liste si vous utilisez un `filetype` personnalisé.

## macOS et nom de l'application

Marked est exclusif à macOS, le plugin ne se charge donc pas sur les autres systèmes. Le nom d'application par défaut est **Marked 2** ; si votre copie de Marked est installée sous un nom ou un chemin différent, définissez `g:marked_app` en conséquence (par exemple un chemin complet vers le bundle de l'application). Le README détaille le comportement de fermeture, de fermeture automatique et de focus.

I> Ce sujet d'aide ne fait pas partie du projet vim-marked ; pour les commandes et options les plus récentes, consultez le [dépôt GitHub][vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked
