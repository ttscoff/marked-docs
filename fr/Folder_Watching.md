# <%= @title %>

Déposez un **dossier** de notes en texte brut sur Marked. Marked ouvre une fenêtre d'aperçu qui suit toujours le fichier éligible **le plus récemment modifié** dans ce dossier (.md, .txt, .markdown, etc., correspondant aux filtres de type de fichier de Marked).

Les mises à jour s'exécutent chaque fois qu'un fichier surveillé est enregistré : si le fichier le plus récent correspond au précédent, Marked fait défiler vers la région d'édition détectée ; lorsque vous changez de document, l'intégralité de l'aperçu passe au fichier actif.

## Fonctionne bien avec nvUltra, nvALT et des outils similaires

Les applications de bloc-notes qui laissent des fichiers individuels sur le disque (bibliothèques classiques de style **nvALT**, **nvUltra**, **Notational Velocity**, dossiers Git synchronisés, dossiers de travail Dropbox, etc.) s'associent naturellement à la surveillance des dossiers : vous écrivez dans une fenêtre et gardez Marked épinglé à côté sans rouvrir manuellement les aperçus.

**nvUltra** propose également **[Aperçu du(des) fichier(s) dans Marked](nvUltra.html)** dans son menu contextuel lorsque vous souhaitez ouvrir des notes spécifiques dans Marked directement au lieu d'attacher Marked au flux d'observateur de dossier entier décrit ci-dessus.

Marked expose également le même comportement d'observateur sous d'autres noms de menu lorsque vous consolidez de nombreux petits chapitres dans ce qui ressemble à une seule expérience de lecture ; voir aussi [Documents multi-fichiers](Multi-File_Documents.html) pour les manuscrits qui fusionnent intentionnellement plusieurs sources Markdown.
