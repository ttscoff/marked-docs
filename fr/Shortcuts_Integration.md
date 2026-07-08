# <%= @title %>

Marked inclut des actions natives **Raccourcis** (App Intents) pour ouvrir des fichiers, changer le style d'aperçu et exporter des documents. Ces actions apparaissent dans l'application Raccourcis lorsque vous recherchez **Marked**, et sont disponibles sous **macOS 13 (Ventura)** ou une version ultérieure.

Pour de l'automatisation par script avec un modèle d'objets complet, voir [Prise en charge d'AppleScript](AppleScript_Support.html). Pour des flux de travail basés sur des URL depuis le shell, voir le [Gestionnaire d'URL](URL_Handler.html).

## Rechercher des actions

1. Ouvrez l'application **Raccourcis**.
2. Créez un nouveau raccourci ou modifiez-en un existant.
3. Recherchez **Marked** dans la bibliothèque d'actions.

Les actions sont regroupées sous **Documents** et **Export**. Marked enregistre également des phrases Siri telles que « Exporter un fichier avec Marked » et « Ouvrir dans Marked » pour des raccourcis rapides.

## Aperçu des actions

| Action | Objectif |
| --- | --- |
| **Ouvrir un fichier dans Marked** | Ouvre un fichier Markdown ou texte dans une fenêtre d'aperçu. |
| **Définir le style d'aperçu** | Change le thème d'aperçu d'un document ouvert (ou ouvre d'abord un fichier). |
| **Ouvrir et exporter un fichier** | Ouvre un fichier, puis l'exporte vers un autre format. |
| **Exporter le document** | Exporte un document ouvert (fenêtre au premier plan ou fichier spécifique). |
| **Exporter les documents ouverts** | Exporte tous les documents actuellement ouverts dans Marked. |

Toutes les actions d'export renvoient le ou les fichiers exportés en sortie **Fichier** de Raccourcis, afin que vous puissiez les transmettre à l'étape suivante (Mail, Finder, une autre application).

## Ouvrir un fichier dans Marked

**Paramètre :** **Fichier** -- le document à ouvrir (depuis le Finder, la feuille de partage ou une étape précédente de Raccourcis).

Marked ouvre le fichier dans une fenêtre d'aperçu. Utilisez cette action lorsque vous souhaitez prévisualiser ou éditer dans Marked avant toute autre étape.

## Définir le style d'aperçu

**Paramètres :**

- **Style** -- style d'aperçu choisi dans un sélecteur (mêmes noms que dans le menu de style d'aperçu et le Gestionnaire de styles).
- **Fichier** (facultatif) -- un fichier spécifique. S'il est omis, Marked utilise le document au premier plan. Si le fichier n'est pas déjà ouvert, Marked l'ouvre d'abord.

Définir un style recharge l'aperçu avec ce thème (comme si vous choisissiez un style depuis le menu de style d'aperçu).

## Actions d'export

Les actions d'export partagent les mêmes options de base :

| Paramètre | Description |
| --- | --- |
| **Format** | Markdown, HTML, PDF paginé, PDF continu, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack, ou OPML. |
| **Profil** (facultatif) | Un profil d'export enregistré depuis {% prefspane Export %}. |
| **Style** (facultatif) | Style d'aperçu à appliquer avant l'export (rechargement complet de l'aperçu). |
| **Taille de page** (facultatif) | Nom de la taille de page d'impression, comme `A4` ou `Letter`. |
| **Marges** (facultatif) | Notation abrégée des marges (voir ci-dessous). |
| **Taille de police** (facultatif) | Taille de police de base en points pour l'export PDF, comme `14` ou `12pt`. |
| **Fichier de sortie** / **Dossier de sortie** (facultatif) | Chemin de destination. S'il est omis, Marked écrit à côté du fichier source avec l'extension appropriée. |

**Remarques**

- **PDF paginé** utilise le même pipeline de mise en page d'impression que {% appmenu File, Export As, Save PDF (Paginated) %}. Non disponible pour les documents d'aperçu HTML brut.
- L'export **HTML** utilise l'aperçu rendu (ce que vous voyez dans la WebView), et non le fichier source Markdown brut.
- **PDF continu** capture la mise en page actuelle de la WebView d'aperçu.
- **Taille de police** active la même option de taille de police personnalisée pour l'export/impression que dans {% prefspane Export %}. N'affecte pas les documents Fountain.

### Ouvrir et exporter un fichier

Idéal pour les flux de travail depuis le Finder : sélectionnez un fichier Markdown, ouvrez-le dans Marked et exportez-le en une seule étape.

**Paramètres :** **Fichier** (requis), plus les options d'export ci-dessus.

Exemple d'utilisation : une Action rapide qui prend des fichiers depuis le Finder et les exporte en **PDF paginé** avec un profil et un style choisis.

### Exporter le document

Exporte un document **déjà ouvert** dans Marked.

**Paramètres :**

- **Fichier** (facultatif) -- un fichier ouvert spécifique. S'il est omis, Marked exporte le document au premier plan.
- Options d'export et **Fichier de sortie** comme ci-dessus.

Utilisez cette action lorsque Marked est déjà lancé et que vous souhaitez exporter l'aperçu actuel sans rouvrir le fichier.

### Exporter les documents ouverts

Exporte **tous** les documents d'aperçu actuellement ouverts dans Marked.

**Paramètres :**

- **Format** et options d'export (profil, style, taille de page, marges, taille de police).
- **Dossier de sortie** (facultatif) -- répertoire pour les fichiers exportés. S'il est omis, chaque fichier est exporté à côté de son document source.

Utile pour un export par lots après avoir consulté plusieurs chapitres ou notes dans Marked.

## Notation abrégée des marges

Lorsque **Marges** est défini sur une action d'export, utilisez une chaîne comportant une à quatre mesures. Unités : `in`, `cm`, `mm`, `pt`, ou `"` pour les pouces. Un nombre sans unité est traité comme des points.

| Valeur | Signification |
| --- | --- |
| `1in` | Tous les côtés |
| `1in 2in` | Haut et bas `1in`, gauche et droite `2in` |
| `1in 2in 1in` | Haut `1in`, gauche et droite `2in`, bas `1in` |
| `1in 2in 1in 2in` | Haut, droite, bas, gauche |

Cela correspond à la clé `margins` des enregistrements d'export [AppleScript](AppleScript_Support.html#with-options-properties-record).

## Exemples de flux de travail

### Fichier du Finder vers PDF

1. **Ouvrir et exporter un fichier**
2. **Fichier** -- entrée depuis la feuille de partage ou une Action rapide du Finder.
3. **Format** -- PDF paginé.
4. **Style** -- thème facultatif (par exemple Amblin).
5. **Profil** -- profil d'export enregistré facultatif.
6. **Fichier de sortie** -- facultatif ; laissez vide pour écrire `nomfichier.pdf` à côté du fichier source.

### Exporter ce qui est ouvert dans Marked

1. **Exporter le document**
2. Laissez **Fichier** vide pour utiliser la fenêtre au premier plan.
3. Choisissez le **Format** et éventuellement un profil ou un style.

### Export par lots des documents ouverts

1. **Exporter les documents ouverts**
2. Choisissez le **Format** (par exemple EPUB).
3. Définissez éventuellement un **Dossier de sortie** pour rassembler tous les exports dans un même répertoire.

### Style puis export (deux étapes)

1. **Définir le style d'aperçu** -- choisissez un style (en ciblant éventuellement un **Fichier** spécifique).
2. **Exporter le document** -- même fichier ou document au premier plan, avec le **Format** souhaité.

Vous pouvez également transmettre le **Style** directement sur une action d'export ; Marked applique le thème et attend le rechargement de l'aperçu avant d'exporter.

## Chemins d'export et bac à sable

- Si **Fichier de sortie** ou **Dossier de sortie** est omis, Marked écrit à côté du document source.
- Marked peut créer des dossiers intermédiaires lorsque le chemin d'export se trouve **à l'intérieur du dossier du document ouvert**.
- Les exports en dehors du dossier du document nécessitent un chemin accessible en écriture par Marked (emplacement du document enregistré, signets à portée de sécurité, ou dossiers que vous avez autorisés via les boîtes de dialogue d'ouverture).

Voir [Prise en charge d'AppleScript](AppleScript_Support.html#export-paths-and-sandboxing) pour les mêmes règles de bac à sable.

## Action historique `convert_to`

Le dictionnaire AppleScript expose toujours **`convert_to`** pour convertir du texte ou des fichiers Markdown sans aperçu ouvert. Les actions natives Raccourcis ci-dessus sont à privilégier : elles ouvrent correctement les documents, attendent le chargement de l'aperçu et prennent en charge l'export PDF paginé de manière asynchrone.

Voir [Raccourcis et `convert_to` dans Prise en charge d'AppleScript](AppleScript_Support.html#shortcuts-and-convert_to) pour plus de détails sur cette commande historique.

## Dépannage : les actions n'apparaissent pas dans Raccourcis

Raccourcis indexe **une seule** installation de Marked par identifiant de bundle (`com.brettterpstra.marked`). Il privilégie la copie avec le **numéro de build le plus élevé** (`CFBundleVersion`), pas nécessairement l'application que vous venez de compiler dans Xcode.

Si Marked n'apparaît pas sous **Applications** dans la bibliothèque d'actions de Raccourcis :

1. Listez toutes les copies présentes sur le disque :
   ```bash
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Supprimez ou renommez les copies obsolètes (par exemple un ancien `Marked.app` sur le Bureau ou dans `/Applications`, copié depuis une version **sans** métadonnées Raccourcis).
3. Exécutez la version que vous souhaitez que Raccourcis utilise (**Exécuter** dans Xcode, ou ouvrez directement le `.app` dans DerivedData).
4. Quittez et rouvrez l'application **Raccourcis**.

Une version incluant Raccourcis contient `Contents/Resources/Metadata.appintents`. Vous pouvez le vérifier ainsi :

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

Au lancement, Marked consigne `[MKShortcuts] Registering App Intents` dans Console.app lorsque l'enregistrement s'effectue (macOS 13+).

## Débogage

Activez le **Mode débogage** dans {% prefspane Advanced %}. Marked consigne les étapes d'export au niveau Info avec le préfixe `[AppleScript]` dans Console.app et dans le visualiseur de journaux de Marked (le pipeline d'export est partagé avec AppleScript).

## Erreurs

Messages courants en cas d'échec d'une action :

- Aucun document Marked disponible (rien d'ouvert et aucun fichier spécifié).
- Ce fichier n'est pas ouvert dans Marked (utilisez **Ouvrir un fichier** ou **Ouvrir et exporter un fichier**).
- Nom de profil d'export ou de style d'aperçu inconnu.
- Délai d'attente dépassé pour le chargement ou le rechargement de l'aperçu.
- Erreurs de permission sur le chemin d'export ou échec de génération du PDF paginé.
