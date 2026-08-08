# <%= @title %>

Marked peut ouvrir directement des documents PDF (`.pdf`). Faites glisser un fichier vers Marked ou utilisez {% appmenu File, Open... ({{cmd}}O) %}. Le document est converti en Markdown pour prévisualisation et exportation.

L'importation PDF fonctionne mieux sur les **fichiers PDF texte plus petits** (diapositives, articles, rapports courts). Les manuels, livres et documents numérisés volumineux sont pris en charge, mais leur conversion est souvent lente ou imparfaite : voir **Limitations** ci-dessous.

Marked est toujours un outil **d'aperçu** : vous ne modifiez pas le PDF dans Marked. Utilisez {% kbd cmd E %} pour ouvrir le PDF dans **Aperçu** (ou par défaut de votre système) et Marked s'actualise lorsque le fichier change sur le disque.

## Comment fonctionne la conversion [how-conversion-works]

L'importation PDF utilise la bibliothèque [pdf22md](https://github.com/twardoch/pdf22md) (licence MIT ; voir [licence pdf22md](PDF22MD_License.html)). Marked exécute la conversion en arrière-plan tout en affichant un court avis de **Conversion**.

Le convertisseur :

- Extrait le **texte** des PDF numériques à l'aide de PDFKit
- Utilise **Vision OCR** sur les pages où le texte intégré est manquant (courant avec les numérisations)
- Détecte les **titres** à partir de la taille de la police lorsque cela est possible
- Enregistre les **images** dans un dossier `assets` à côté du Markdown généré

Marked n'active **pas** le nettoyage IA facultatif de pdf22md dans l'application. La qualité de la conversion dépend de la manière dont le PDF a été créé.

## Cache et aperçu en direct [cache-and-live-preview]

Les fichiers Markdown convertis et les images sont stockés dans le cache des observateurs de Marked (`~/Library/Caches/Marked/Watchers/PDF/`). Le chemin du PDF d'origine reste la source du document pour la surveillance des fichiers.

Lorsque vous enregistrez ou remplacez le PDF dans une autre application, Marked détecte le changement et le reconvertit automatiquement (même comportement de rechargement fusionné que [RTF](RTF_Support.html) et [Scrivener](Scrivener_Support.html)).

## Exportation et autres fonctionnalités [export-and-other-features]

Après la conversion, Marked traite le document comme les autres sources compilées : l'exportation, les statistiques et la plupart des fonctionnalités d'aperçu s'exécutent sur le Markdown généré. Les chemins d'image dans l'aperçu pointent vers les ressources mises en cache jusqu'à l'exportation.

## Limites [limitations]

Définissez vos attentes en conséquence : le PDF vers Markdown est utile, mais pas parfait.

**Ce qui fonctionne bien**

- **PDF vectoriels et basés sur du texte** avec du vrai texte intégré (exporté depuis Word, Pages, InDesign, etc.)
- **Longueur modérée** : quelques dizaines de pages sont généralement converties dans un délai raisonnable avec une bonne structure

**Qu'est-ce qui n'est pas fiable**

- **OCR (PDF numérisés)** : Vision remplit le texte manquant, mais la précision est souvent médiocre par rapport à un outil OCR dédié ; attendez-vous à des fautes de frappe, des mots brisés et des colonnes manquées
- **Tableaux** : la disposition est devinée à partir des positions du texte ; les cellules fusionnées, les tableaux imbriqués et les grilles complexes survivent rarement sous forme de tableaux Markdown propres
- **Placement de l'image** : les figures sont extraites jusqu'à `assets/`, mais l'alignement, les légendes et le texte autour des images ne sont pas préservés de manière fiable

**Taille et performances**

- Les **PDF volumineux** (guides d'utilisation, manuels scolaires, manuels longs) peuvent prendre un **très long** à convertir, utiliser une mémoire importante ou ne pas produire de Markdown utile. Marked reste réactif pendant que la conversion s'exécute en arrière-plan, mais rien ne garantit qu'un manuel de 500 pages se terminera avec succès
- Si la conversion se termine avec peu ou pas de contenu, Marked affiche une erreur plutôt que de laisser un aperçu vide

**Autres limites**

- **Les PDF protégés par mot de passe** ne sont pas pris en charge dans la v1
- **Les images PDF intégrées dans Markdown** (`![]()` faisant référence à un fichier `.pdf`) ne sont pas liées à l'importation PDF : seule l'ouverture d'un `.pdf` en tant que document principal déclenche la conversion

Pour les documents Word, utilisez [Travailler avec DOCX](Working_With_DOCX.html). Pour le texte enrichi, utilisez [Support RTF et RTFD](RTF_Support.html).

## Sujets connexes [related-topics]

- [Ouverture de fichiers](Opening_Files.html) : glisser-déposer, ouvrir récent, presse-papiers
- [Exportation](Exporting.html) : enregistrez HTML, PDF, DOCX et Markdown à partir de l'aperçu
- [Licence pdf22md](PDF22MD_License.html) : texte de licence MIT tiers
