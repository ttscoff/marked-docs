# <%= @title %>

**Marked Quick Look** est une application distincte du Mac App Store qui ajoute une extension d'aperçu Quick Look pour les fichiers Markdown et texte brut. Appuyez sur la barre d'espace dans le Finder (ou utilisez Quick Look partout où macOS le prend en charge) pour voir un aperçu HTML stylisé au lieu de la source brute.

Marked Quick Look n'est **pas inclus avec Marked 3**. C'est un achat séparé (**9,99 $** sur le Mac App Store). <!-- MAS link: add App Store URL here when available -->

I> Marked Quick Look et Marked 3 sont des produits indépendants. Acheter Marked n'installe pas l'extension Quick Look, et acheter Marked Quick Look n'inclut pas de licence Marked. L'aperçu inclut un bouton facultatif **Open in Marked** lorsque Marked est installé.

## Ce que vous obtenez [what-you-get]

Marked Quick Look enregistre une **extension d'aperçu Quick Look** qui restitue les fichiers `.md`, `.markdown`, `.mmd`, et de nombreux fichiers texte brut avec le même soin visuel qui a fait la réputation de Marked :

- **Traitement Apex** : propulsé par [Apex](https://github.com/ApexMarkdown/apex), un processeur Markdown open source qui prend en charge CommonMark, GitHub Flavored Markdown, MultiMarkdown, Kramdown, et un mode **Unifié** qui combine des fonctionnalités de plusieurs saveurs
- **Styles d'aperçu Marked** : neuf thèmes intégrés (GitHub par défaut) plus l'importation de CSS personnalisé
- **Coloration syntaxique**, **MathJax**, et diagrammes **Mermaid** (scripts intégrés ; aucune connexion réseau requise)
- **CriticMarkup** dans la vue de balisage
- **Open in Marked** : passez de Quick Look à l'aperçu complet de Marked lorsque Marked est installé

W> Les aperçus Quick Look sont en lecture seule. Les inclusions de fichiers (`<<[file]`, `{{file}}`, et syntaxes similaires) ne sont **pas développées** dans Quick Look. Elles apparaissent comme des espaces réservés en surbrillance (`Fichier inclus : chemin`) afin que vous puissiez voir où le contenu serait intégré. Ouvrez le document dans Marked pour un rendu multi-fichiers complet.

## Installation [installation]

1. Installez **Marked Quick Look** depuis le Mac App Store.
2. **Lancez l'application une fois** depuis `/Applications`. Cela enregistre l'extension Quick Look auprès de macOS.
3. Appuyez sur la **barre d'espace** sur un fichier Markdown dans le Finder pour le prévisualiser.

L'application conteneur inclut une fenêtre **Paramètres** ({% kbd cmd %},{% kbd , %}) où vous pouvez choisir le mode du processeur Apex, le style d'aperçu, le thème de coloration syntaxique, et les bascules pour MathJax et Mermaid.

## Apex et les saveurs de Markdown [apex-and-markdown-flavors]

Marked Quick Look utilise [Apex](https://github.com/ApexMarkdown/apex) pour tout le rendu. Apex est développé comme un processeur autonome et est également intégré dans Marked 3.

Dans Paramètres, choisissez un **mode Apex** correspondant à votre style d'écriture :

| Mode | Idéal pour |
| --- | --- |
| **Unifié** (par défaut) | Fonctionnalités Markdown mixtes entre les saveurs |
| **CommonMark** | CommonMark strict |
| **GFM** | GitHub Flavored Markdown |
| **MultiMarkdown** | Métadonnées, transclusion, notes de bas de page |
| **Kramdown** | Extensions de style Kramdown |

Le mode Unifié est le meilleur choix par défaut pour la plupart des documents. Changez de mode si un fichier a été écrit pour un processeur spécifique et que quelque chose s'affiche de manière inattendue.

## Open in Marked [open-in-marked]

Lorsque Marked 3 est installé, l'aperçu Quick Look peut afficher un bouton **Open in Marked** dans la barre d'outils. Cliquez dessus pour transférer le fichier à Marked pour un aperçu en direct, l'exportation, la relecture et le développement complet des inclusions.

Si Marked n'est pas installé, le bouton apparaît désactivé.

## Résoudre les conflits Quick Look [troubleshooting-quick-look-conflicts]

macOS permet à plusieurs applications d'enregistrer des extensions d'aperçu Quick Look pour Markdown. Une seule extension gère chaque aperçu, et **le plugin d'une autre application peut prendre le pas** sur Marked Quick Look.

### Comment savoir quelle extension est active [how-to-tell-which-extension-is-active]

Les aperçus Marked Quick Look incluent une barre d'outils **Open in Marked** lorsque cette option est activée. Si vous voyez une mise en page différente, la source brute en police à chasse fixe, ou le style d'une autre application, c'est probablement un autre gestionnaire Quick Look qui prend le dessus.

### Rétablir la priorité de Marked Quick Look [restore-marked-quick-look-precedence]

Après une installation ou une mise à jour, ou après une réinitialisation du cache Quick Look, suivez ces étapes :

1. **Lancez Marked Quick Look** une fois depuis `/Applications` (ou exécutez-le depuis Xcode si vous testez une version de développement).
2. Dans le Terminal, enregistrez et privilégiez l'extension :

```bash
pluginkit -a "/Applications/Marked Quick Look.app/Contents/PlugIns/MarkedQuickLookPreview.appex"
pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview
```

3. Réinitialisez les services Quick Look :

```bash
killall quicklookd QuickLookUIService 2>/dev/null
```

4. Appuyez à nouveau sur la **barre d'espace** sur un fichier `.md`.

Pour effacer les aperçus mis en cache :

```bash
qlmanage -r cache
```

### Désactiver temporairement une extension en conflit [temporarily-disable-a-conflicting-extension]

Pour confirmer qu'une autre application prend le pas sur Marked Quick Look, désactivez son extension avec `pluginkit -e ignore -i BUNDLE_ID`, prévisualisez un fichier, puis rétablissez-la avec `pluginkit -e default -i BUNDLE_ID`.

Exemple : désactiver l'extension Markdown de **Folder Quick Look** :

```bash
pluginkit -e ignore -i studio.appahead.AA7.Markdown-Quick-Look-Extension
```

### Applications fréquemment en conflit [common-conflicting-apps]

Ces applications (et d'autres) enregistrent des extensions d'aperçu Quick Look qui peuvent gérer les fichiers `.md` :

| Application | ID de bundle (extension d'aperçu) |
| --- | --- |
| **Folder Quick Look** | `studio.appahead.AA7.Markdown-Quick-Look-Extension` |
| **QLMarkdown** | `org.sbarex.QLMarkdown.QLExtension` |
| **Peek** | `com.bigzlabs.peek.peekextension` |
| **Highland Pro** | `com.quoteunquoteapps.highland.pro.qlplugin` |
| **Bear** | `net.shinyfrog.bear.Bear-Quicklook-Extension` |
| **Ulysses** | `com.soulmen.ulysses-setapp.quicklookextension` (Setapp) / `com.soulmen.ulysses.quicklookextension` |
| **Drafts** | `com.agiletortoise.Drafts-OSX.Drafts-OSX-QuickLookPreview` |
| **Scrivener** | `com.literatureandlatte.scrivener3.ScrivQuickLook` |
| **Black Ink** | `com.red-sweater.blackink2.quicklook` |

W> **iA Writer** ne fournit pas d'extension Quick Look Markdown dédiée, mais **Folder Quick Look**, **QLMarkdown**, et **Peek** sont des sources fréquentes de conflits car ils ciblent également `net.daringfireball.markdown`.

Lister les extensions d'aperçu enregistrées :

```bash
pluginkit -m -D -p com.apple.quicklook.preview -A -v | grep -i markdown
```

Les extensions marquées d'un `+` sont explicitement activées ; utilisez `pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview` pour placer Marked Quick Look en tête.

### Vous voyez encore du texte brut ? [still-seeing-plain-text]

Si l'aperçu affiche une **source non stylée en police à chasse fixe**, macOS se rabat peut-être sur le générateur intégré **Text.qlgenerator** parce que l'extension d'aperçu n'a pas réussi à se charger. Vérifiez **Console.app** pour des erreurs provenant de `MarkedQuickLookPreview`, puis réinstallez Marked Quick Look dans `/Applications` et lancez-le une fois.

### Versions de développement [development-builds]

Les versions de débogage compilées depuis Xcode résident dans DerivedData et **ne s'enregistrent pas automatiquement**. Exécutez l'application conteneur **Marked Quick Look** depuis Xcode (Cmd+R) après chaque build propre, puis relancez les commandes `pluginkit -a` et `pluginkit -e use` avec le chemin DerivedData vers votre `.appex`.

## Sujets connexes [related-topics]

- [Ouverture de fichiers](Opening_Files.html) : comment Marked ouvre et surveille les documents
- [Documents multi-fichiers](Multi-File_Documents.html) : syntaxe d'inclusion et développement complet dans Marked
- [Choisir un processeur](Choosing_a_Processor.html) : options de processeur dans Marked 3
- [Extension de partage](Share_Extension.html) : envoyer des fichiers à Marked depuis le menu Partage du système
