# <%= @title %>

[MarsEdit][me] stocke les publications dans sa base de données, et non sous forme de fichiers libres sur le disque. Marked utilise donc un flux de travail de prévisualisation dédié qui communique avec l'application MarsEdit en cours d'exécution.

## Fenêtre d'aperçu de MarsEdit [marsedit-preview-window]

Choisissez {% appmenu File, New, MarsEdit Preview %}. Marked demande à AppleScript de lire le **message au premier plan dans MarsEdit** (les identifiants de bundle de Red Sweater pour direct, Mac App Store, Setapp et MarsEdit 4/5 sont reconnus). Gardez MarsEdit en cours d'exécution avec un document ouvert pendant que vous travaillez.

- **Actualisation manuelle :** enregistrez depuis l'aperçu de Marked si vous souhaitez forcer une mise à jour.
- **Mises à jour automatiques :** activez la surveillance pour que Marked s'actualise à chaque sauvegarde automatique de MarsEdit.

Si aucune publication n'est disponible, Marked fait apparaître une courte erreur dans l'aperçu au lieu d'un texte obsolète.

### Messages étendus [extended-posts]

Le contenu du champ **étendu** de MarsEdit est séparé dans l'aperçu et la source de Marked à l'aide d'un séparateur `<!--more-->` de style WordPress afin que les sites orientés pagination (WordPress, Jekyll, etc.) voient toujours la rupture. Le commentaire est inoffensif ailleurs.

### Balises et catégories dans les métadonnées [tags-and-categories-in-metadata]

Les balises et catégories de MarsEdit sont exposées dans le bloc de métadonnées MultiMarkdown. Avec le processeur MultiMarkdown ({% prefspane Processor %}), vous pouvez les référencer comme :

    Étiqueté : [%tags]
    Publié dans : [%categories]

[me]: https://www.red-sweater.com/marsedit/
