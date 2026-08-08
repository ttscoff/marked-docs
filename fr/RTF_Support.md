# <%= @title %>

Marked peut ouvrir directement des documents Rich Text Format (`.rtf`) et RTFD (`.rtfd`). Faites glisser un fichier vers Marked ou utilisez {% appmenu File, Open... ({{cmd}}O) %}. Le document est converti en Markdown pour l'aperçu et l'exportation.

Cela fonctionne bien avec les documents provenant de **Pages**, **TextEdit**, **Word**, et d'autres applications qui enregistrent au format RTF ou RTFD. Marked reste un outil **d'aperçu** : vous modifiez dans l'application d'origine et Marked se met à jour lorsque vous enregistrez.

## Comment fonctionne la conversion [how-conversion-works]

Marked convertit le RTF en HTML à l'aide du moteur de texte système, puis en Markdown. Le convertisseur :

- Associe les **grandes tailles de police de paragraphe** à des niveaux de titre (par rapport à la taille de corps la plus courante dans le document)
- Préserve le **gras**, l'*italique*, et les liens lorsque c'est possible
- Extrait les **images** des bundles RTFD et des pièces jointes intégrées
- Ne traite **pas** les noms de fichiers RTF comme des légendes d'image (voir Images ci-dessous)

Le même pipeline de conversion est utilisé pour la compilation RTF de Scrivener et pour les fichiers RTF inclus dans d'autres documents.

## Aperçu en direct [live-preview]

Lorsque vous enregistrez le fichier RTF ou RTFD dans une autre application, Marked détecte le changement et actualise l'aperçu automatiquement.

## Images [images]

Le RTF ne définit pas de champ « légende » séparé de la manière dont Cocoa l'exporte en HTML. Ce qui ressemble à une légende dans votre mise en page est généralement du **texte normal** dans le paragraphe suivant, et Marked le conserve comme texte du corps.

Les images intégrées et les images à l'intérieur des bundles RTFD (par exemple `pastedGraphic.png` dans un export Pages) sont copiées dans un dossier de cache sous `~/Library/Caches/Marked/Watchers/`. Les chemins d'image de l'aperçu pointent vers ces fichiers mis en cache jusqu'à ce que vous exportiez.

Marked n'utilise **pas** le nom de fichier de l'image comme texte alternatif ou comme légende de figure MultiMarkdown. Vous ne devriez pas voir `pastedGraphic.png` sous l'image, sauf si vous avez tapé ce texte dans le document.

## Exportation et autres fonctionnalités [export-and-other-features]

Après la conversion, Marked traite le document comme les autres sources compilées (de manière similaire à [Scrivener](Scrivener_Support.html) et [DOCX](Working_With_DOCX.html)) : l'exportation, les statistiques et la plupart des fonctionnalités d'aperçu s'exécutent sur le Markdown généré stocké dans le cache des observateurs.

## Limitations [limitations]

La qualité de la conversion dépend de l'application source. En général :

- Les **titres** sont déduits de la taille de police, pas des styles de plan Word/Pages
- Les **mises en page complexes** (tableaux multi-colonnes utilisés uniquement pour le positionnement, zones de texte) peuvent ne pas se convertir proprement en Markdown
- Les **équations** en RTF ne sont pas prises en charge dans l'aperçu (voir [MathJax](MathJax.html) pour les mathématiques en Markdown)
- Le **format `.doc` hérité** (Word binaire) n'est pas pris en charge ; enregistrez d'abord au format DOCX ou RTF

Pour un collage ponctuel sans enregistrer de fichier, utilisez plutôt [Aperçu du presse-papiers](Opening_Files.html#from-the-clipboard).

## Sujets connexes [related-topics]

- [Support PDF](PDF_Support.html) : ouvrir des documents PDF comme sources Markdown
- [Travailler avec DOCX](Working_With_DOCX.html) : documents Word avec suivi des modifications et commentaires
- [Ouverture de fichiers](Opening_Files.html) : glisser-déposer, Ouvrir récent, presse-papiers
- [Exportation](Exporting.html) : Copier le texte enrichi et enregistrer en RTFD (exportation), différent de l'ouverture d'un RTF comme fichier source
