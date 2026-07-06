<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>


Marked vous donne un contrôle total avec des règles personnalisées, du texte
transformations et la possibilité d'exécuter vos propres commandes ou d'exécuter
différents processeurs en fonction des propriétés de fichier correspondantes.


## Utilisation de préprocesseurs/processeurs personnalisés

Pour ajouter des processeurs personnalisés, accédez au {% prefspane Processor %}
et cliquez sur **Règles personnalisées**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


Dans l'éditeur de règles (AKA "Conducteur"), vous pouvez ajouter des
des règles qui ont des critères pour faire correspondre les fichiers en fonction du nom de fichier,
chemin, correspondances dans le contenu, métadonnées et même si
d'autres fichiers existent dans la même arborescence que le document en cours
ouvert. Lorsqu'une règle correspond, les actions définies pour la
la règle est exécutée sur ce fichier.

> Sous le champ Processeur, les cases à cocher dans "Nouveau
> les documents utilisent la personnalisation :" détermine si les règles sont testées
> pas du tout pour les phases Préprocesseur et Processeur. En général,
> laissez-les cochés, mais si vous souhaitez les ignorer complètement
> tous les processeurs personnalisés, définissez-le ici.

![Éditeur de règles][2]

  [2] : images/CustomRules-800.jpg @2x largeur=800

Pour créer une nouvelle règle, utilisez le `+`
en bas de la liste des règles de gauche. Donnez le
attribuez un nom et définissez-le comme préprocesseur ou processeur.

Les trois points à côté d'une règle indiquent Préprocesseur, Processeur et Activé. Un seul préprocesseur ou processeur peut être mis en surbrillance et vous pouvez cliquer sur les points pour modifier les états de la règle.

Préprocesseur
: s'exécute après le traitement initial du fichier, lorsque Marked ajoute les fichiers inclus, gère les préférences de style telles que les nouvelles lignes de GitHub, etc., mais avant la phase de traitement. Le document est encore en Markdown brut à ce stade et vous pouvez apporter des modifications au contenu à transmettre au processeur. Si aucun processeur personnalisé ne correspond ou si aucune action Exécuter le processeur n'est exécutée dans un processeur personnalisé correspondant, le processeur par défaut sera exécuté.

Processeur
: Un processeur personnalisé remplace le processeur intégré défini dans le {% prefspane Processor %}. Il peut gérer toutes les actions qu'un préprocesseur peut effectuer et ajoute les actions Exécuter la commande et Exécuter le processeur. Cela vous permet d'exécuter une commande personnalisée, par ex. Pandoc, ou exécutez un autre processeur intégré sur les fichiers correspondant aux critères.

Tous les tableaux de l'éditeur de règles personnalisées peuvent être réorganisés en
glisser-déposer, afin que vous puissiez modifier l'ordre dans lequel
les règles sont exécutées, l'ordre des critères dans le prédicat
éditeur et l'ordre des actions à exécuter en séquence.

### Éditeur de prédicats

![Éditeur de prédicat][prédicat]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Une fois une règle ajoutée, utilisez l'éditeur de prédicats pour définir
critères qui détermineront si la règle est exécutée pendant une période
fichier donné. Utilisez le menu déroulant de gauche pour sélectionner un
critère, puis utilisez les champs comparateur et valeur pour créer
le prédicat.

- _Filename_ correspond uniquement au nom du fichier
- _Extension_ correspond uniquement à l'extension du fichier
- _Path_ correspond au chemin POSIX (Unix) complet du fichier
- _Tree_ recherche les correspondances de nom de fichier n'importe où dans le
  arborescence des répertoires du fichier
- _Text_ correspond au contenu du texte dans le fichier. Utiliser en avant
  des barres obliques autour de la valeur du texte pour en faire un texte régulier
  recherche d'expressions.
- _File include_ teste si le fichier contient des éléments inclus
  fichiers (en utilisant l'un des [Marked's include
  syntaxes](Multi-File_Documents.html)).
- _Metadata type_ teste si le fichier inclut YAML,
  Métadonnées MultiMarkdown ou Pandoc
- Champs _Metadata:_ (par exemple _Metadata: Author_,
  _Métadonnées : Date_, _Métadonnées : Titre_) test pour des
  clés de métadonnées. Toute clé de métadonnées apparaît dans la liste déroulante sous la forme
  _Métadonnées :_ suivi du nom du champ.
- _Activé manuellement_ correspond lorsque cette règle a été activée
  activé pour la fenêtre d'aperçu actuelle (voir [Activation manuelle
  règles](#manuallyenabled) ci-dessous). Combinez-le avec d'autres
  critères dans un groupe Tous (AND) afin que la règle ne s'exécute que lorsque
  vous vous inscrivez et le fichier correspond à vos autres conditions.

Pour faire correspondre tous les fichiers (c'est-à-dire un processeur personnalisé qui toujours
s'exécute), définissez _Filename_ sur `contains` `*`. L'astérisque sera
agir comme un caractère générique et faire correspondre tous les fichiers.

[Ajouter un prédicat][ajouterun prédicat]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Cliquez sur le signe plus (+) sur la ligne du prédicat pour ajouter un autre prédicat. Maintenez Option enfoncée tout en cliquant sur le + pour ajouter un groupe booléen qui peut être défini sur Tout (ET) ou Tout (OU).

### Règles activées manuellement [manuallyenabled]

Certaines règles ne doivent pas s'exécuter sur tous les fichiers correspondant à leur
critères. Ajoutez un critère **Activé manuellement** lorsque vous le souhaitez
une règle à exécuter uniquement après l'avoir activée pour le courant
aperçu.

Utilisez le bouton **Ajouter manuellement activé** sous le prédicat
éditeur pour insérer ce critère. Chaque règle peut l'inclure
une seule fois. Lorsqu'elle est présente, la règle apparaît dans le sous-menu {% appmenu
Preview, Enable Custom Rule %} de cet aperçu
fenêtre.

**Exemple de cas d'utilisation :** Vous gérez une règle qui injecte
imprimer le CSS, supprimer les commentaires et décaler les niveaux d'en-tête pour
Exportation PDF. Vous ne voulez pas cette transformation à chaque fois
enregistrez lors de la rédaction, mais vous le souhaitez sur demande. Donnez le
règle les critères de correspondance de fichiers normaux plus **Activé manuellement**,
puis basculez-le depuis le menu Aperçu (ou un raccourci de déclenchement)
lorsque vous êtes prêt à vérifier la mise en page d'impression.

#### Raccourci de déclenchement

Lorsqu'une règle sélectionnée inclut **Activé manuellement**, un
Le champ **Raccourci de déclenchement** apparaît à côté de **Ajouter manuellement
Activé**. Cliquez sur l'enregistreur, puis appuyez sur la touche
combinaison que vous voulez. Ce raccourci change la règle pour le
Aperçu marqué au premier plan (activer si désactivé, désactiver si activé). Le
le raccourci est stocké avec la règle et persiste lors des lancements.
Effacez le champ pour supprimer le raccourci.

![Déclencher l'enregistreur de raccourcis dans Conductor][manualshortcut]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### Remplacements par aperçu dans le menu Aperçu

Deux sous-menus du menu Aperçu contrôlent les remplacements pour le
aperçu uniquement. Les paramètres sont enregistrés par [vue](#multiview) lorsque
plusieurs fenêtres affichent le même fichier.

**Activer la règle personnalisée**
 : Répertorie toutes les règles activées qui incluent un ** Manuellement
  critère activé**. Cochez une règle pour l'activer pour cela
  aperçu ; décochez-la pour l'éteindre. L'aperçu est actualisé
  immédiatement.

**Remplacement de règle personnalisée**
: Répertorie les règles de phase de processus. Choisissez-en un pour l'*épingler* : pendant
  la phase de processus, seule cette règle est évaluée (les autres
  Les règles de processus sont ignorées). Choisissez **Aucun (automatique)** pour
  revenir à la correspondance normale des règles. Ceci est utile lorsque vous
  souhaitez forcer un pipeline de processeur spécifique pour un
  aperçu sans modifier les règles personnalisées globales.

#### Bouton Remplacer dans la barre d'outils d'aperçu

Lorsqu'un aperçu comporte au moins une règle activée manuellement ou un
épinglé Remplacement du processus, une icône de branche apparaît en bas
barre d'outils (à gauche des contrôles d'exportation et de tiroir).
L'icône remplie et colorée signifie que les remplacements sont actifs ;
l'icône de contour signifie que les remplacements sont suspendus.

![Bouton de remplacement de règle personnalisée dans la barre d'outils d'aperçu][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

Cliquez sur le bouton pour suspendre ou réactiver les remplacements pour cela
prévisualiser sans décocher vos coches de règles manuelles ou
Règle de processus épinglée. Les remplacements suspendus sont restaurés lorsque
vous cliquez à nouveau. C'est plus rapide que de décocher les règles dans le
menu lorsque vous souhaitez comparer l'aperçu normal avec votre
remplacer le pipeline.

### Actions

Utilisez le bouton *+ Action* pour ajouter des actions à la règle.

![Ajouter une action][addaction]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Les actions disponibles incluent :

Définir le style
: définissez le style pour l'aperçu. Tout style intégré ou style personnalisé que vous avez ajouté est disponible.

Exécuter la commande
: Cela prend une commande de ligne de commande, incluant tous les arguments, et transmettra le contenu du fichier sur STDIN. La commande doit renvoyer la sortie résultante sur STDOUT.

> **Mac App Store Sandboxing** : la version Mac App Store (MAS) de Marked s'exécute dans un environnement sandbox qui restreint l'exécution de binaires externes. Si vous devez utiliser des processeurs externes comme Pandoc dans la version MAS, vous devez copier le binaire dans le bundle d'applications. Pour ce faire :
>
> 1. Cliquez avec le bouton droit sur Marked.app → Afficher le contenu du package
> 2. Accédez à Contenu/Ressources/
> 3. Créez un dossier `bin` s'il n'existe pas
> 4. Copiez votre binaire (par exemple, `pandoc`) dans ce
> Dossier `bin`
> 5. Rendre le exécutable : `chmod +x` le binaire
> 6. Dans l'action Exécuter la commande, référencez-la comme :
>
> `YOUR_BINARY_NAME [arguments]`
> Ou utilisez le chemin complet :
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Remarque** : Les scripts avec des shebangs externes (comme les scripts Python pointant vers `/opt/homebrew/bin/python`) seront automatiquement exécutés via les interpréteurs système lorsqu'ils seront copiés dans le bundle. La version MAS peut encore avoir des difficultés à exécuter des binaires qui sont en réalité des scripts Python ou Ruby au lieu de fichiers binaires.
> Vous devrez recopier les binaires après chaque mise à jour de l'application, car les mises à jour remplacent l'intégralité du bundle. Vous pouvez également utiliser **Aide->Crossgrade** pour obtenir la version sans bac à sable qui n'a pas de telles restrictions.

Exécuter le script intégré
: Modifiez un script complet dans l'éditeur de code intégré. Comme Run Command, cela devrait prendre une entrée sur STDIN et renvoyer une sortie sur STDOUT.

Définir les métadonnées
: ajoute ou définit des métadonnées. Fournissez une clé et une valeur. Si la clé existe, sa valeur sera mise à jour, sinon elle sera ajoutée. Le type de métadonnées utilisé sera automatiquement déterminé par le contenu du fichier (ou le résultat d'une action de conversion de métadonnées).
: Si aucune métadonnée existante n'est trouvée, les métadonnées seront ajoutées au format MultiMarkdown à l'intérieur d'un commentaire HTML. Marked peut lire ces métadonnées, mais elles n'apparaîtront pas dans votre aperçu, quel que soit le processeur utilisé.

Supprimer les métadonnées
: Supprime une métadonnée en fonction de sa clé.

Supprimer les métadonnées
: Supprimez toutes les métadonnées. Affecte les métadonnées YAML, MultiMarkdown et Pandoc.

Convertir les méta YAML en MMD
: convertit un bloc de métadonnées YAML en haut du fichier en métadonnées de style MultiMarkdown.

Convertir les méta MMD en YAML
: convertit un bloc de métadonnées MultiMarkdown en YAML.

Rechercher et remplacer
: Effectuez une recherche et un remplacement sur le contenu du fichier.
: Si la chaîne de recherche est entourée de barres obliques (par exemple `/Project \w+/`), elle sera traitée comme une expression régulière. Vous pouvez utiliser `$1`, `$2`, etc. pour inclure des groupes de correspondance dans la chaîne de remplacement.
: Le champ de remplacement prend en charge quelques séquences d'échappement (une barre oblique inverse suivie de) : `\n` insère une nouvelle ligne, `\t` insère un caractère de tabulation, `\\` insère une barre oblique inverse littérale, `\$` insère un signe dollar littéral (au lieu d'un groupe de correspondance)
: Toute autre séquence `\X` est traitée comme simplement `X` (la barre oblique inverse est supprimée), donc `\e` devient `e`. Un \ final sans caractère après est conservé sous la forme d'une barre oblique inverse littérale.
: Utilisez `[%key]` dans la chaîne de remplacement pour insérer une valeur à partir des métadonnées du document, des variables d'environnement ou du contexte (par exemple `[%title]`, `[%MARKED_PATH]`). Les clés définies par des actions antérieures dans la même règle ou par une règle précédente sont disponibles. Les clés sans correspondance sont remplacées par une chaîne vide.

Insérer le titre H1
: Insère un H1 dans le document. Cela peut être extrait des métadonnées ou du nom du fichier.

En-têtes de décalage
: Ajustez les niveaux d'en-tête, de -5 à +5. Par exemple, si vous définissez ce paramètre sur -1, alors tous les H1 deviennent des H2, les H2 deviennent des H3, etc. Réglez-le sur un nombre positif pour augmenter les niveaux d'en-tête de ce montant.

Normaliser les en-têtes
: Cette action garantira, si possible, qu'il n'y a qu'un seul H1 dans le document et ajustera tous les niveaux d'en-tête afin qu'ils soient dans un ordre sémantique et ne sautent pas de niveaux, par ex. de H2 à H4. Si le document original est sémantiquement ordonné au départ, cela affinera bien la hiérarchie.

Insérer la table des matières
: Insérer une table des matières. La table des matières peut être placée après le premier H1, le premier H2 ou en haut du fichier (sera insérée après toute métadonnée).

Insérer un fichier
: Insère un fichier texte sélectionné à un endroit donné du document. Cela peut être après le premier H1, le premier H2, le haut, le bas ou après une correspondance de texte (utilisez `/pattern/` pour rechercher une expression régulière).

Insérer du texte
: Fournit un éditeur contextuel avec lequel vous pouvez intégrer du texte directement dans l'action. Les options de positionnement sont les mêmes que pour _Insérer un fichier_.
: Utilisez `[%key]` n'importe où dans le texte inséré pour extraire les valeurs des métadonnées du document, des variables d'environnement ou du contexte marqué (par exemple `[%author]`, `[%MARKED_PATH]`). Cela fonctionne quel que soit le processeur que vous utilisez, vous n'avez donc pas besoin de MultiMarkdown pour la substitution des métadonnées. Les valeurs d'actions antérieures dans la même règle (telles que **Définir les métadonnées**) ou d'une règle précédente sont incluses. Les clés sans correspondance sont remplacées par une chaîne vide.

Insérer un fichier CSS
: Injecte un fichier CSS sélectionné dans le document. Celui-ci sera chargé après toute sélection de style et pourra être utilisé pour remplacer les styles existants ou en ajouter de nouveaux.

Insérer du CSS
: Propose un éditeur CSS contextuel dans lequel vous pouvez ajouter votre propre CSS directement à l'action. Ce CSS sera injecté en haut du document, après les styles existants. L’ordre des styles injectés correspondra à l’ordre des actions dans la règle.

Insérer un fichier JavaScript
: Injecte un fichier JavaScript sélectionné à la fin du document. Notez que vous devez utiliser une action *Insérer JavaScript* avec un [update hook](#updatehook) si vous souhaitez que le script se recharge à chaque mise à jour.

Insérer du JavaScript à partir de l'URL
: Utilisez ceci pour insérer une balise `<script>` liée à un CDN ou à une autre URL distante à la fin du document. Notez que vous devez utiliser une action *Insérer JavaScript* avec un [update hook](#updatehook) si vous souhaitez que le script se recharge à chaque mise à jour.

Insérer du JavaScript
: Fournit un éditeur JavaScript contextuel avec lequel vous pouvez intégrer du JavaScript personnalisé directement dans l'action. Celui-ci sera injecté à la fin du document, et l'ordre du JavaScript exécuté par la règle sera déterminé par la séquence des actions, la dernière action étant ajoutée en dernier.
: Notez que vous devez utiliser un [update hook](#updatehook) si vous souhaitez que les scripts s'exécutent à chaque mise à jour.

URL d'auto-lien
 : convertissez toutes les URL nues en `<url>`, ce qui générera un lien hypertexte dans n'importe quel processeur.

Exécuter le raccourci
: Exécutez un raccourci Apple. Toute exécution de raccourci doit prendre l'entrée de STDIN et renvoyer la sortie à la fin (Stop and Return Output). Si vous souhaitez effectuer des actions qui ne modifient pas le texte, définissez l'entrée sur une variable, exécutez vos actions, puis affichez la variable de texte d'origine à la fin.

Exécuter le service système
: Exécutez n'importe quel service système dans `~/Library/Services`. Le service doit accepter les entrées et renvoyer la sortie.

Exécuter le flux de travail Automator
: Exécutez n’importe quel fichier Automator `.workflow`. L'entrée sera transmise sur STDIN et la sortie est attendue sur STDOUT.

Exécuter la règle
 : exécute les actions d'une autre règle personnalisée à partir de la règle actuelle.
  Choisissez la règle cible dans la fenêtre contextuelle. La règle invoquée
  s'exécute dans la même phase (préprocesseur ou processus) sans
  réévaluer son prédicat, ce qui le rend utile pour
  règles sur les « ingrédients » réutilisables.

  **Exemple de cas d'utilisation :** Définissez une petite règle nommée "Strip
  Commentaires HTML" avec une action Rechercher et Remplacer, et donner
  c'est un critère **Activé manuellement** donc il ne s'exécute jamais
  automatiquement. Dans votre règle principale de traitement des livres, ajoutez
  Actions **Exécuter la règle** dans l'ordre : d'abord "Normaliser les en-têtes",
  puis "Supprimer les commentaires HTML", puis une commande Exécuter qui appelle
  Pandoc. Vous gardez chaque étape maintenable sans duplication
  actions à travers les règles.

  **Imbrication :** Une règle invoquée par **Run Rule** ne peut pas être invoquée.
  une autre règle. Si la règle cible contient une **Run Rule**
  action, cette action est ignorée ; toutes les autres actions dans le
  la règle cible est toujours exécutée. Vous pouvez ajouter plusieurs **Run Rule**
  actions à une seule règle et elles s’exécutent dans l’ordre.

  Une règle ne peut pas s'appeler elle-même et Marked détecte les cycles
  (par exemple, la règle A invoquant la règle B qui invoque la règle A)
  et ignore l'appel imbriqué. Voir les [Règles personnalisées
  Log](#customprocessorlog) pour ignorer les messages.

Continuer
: Par défaut, une fois qu'une règle correspond, le traitement s'arrêtera (séparément pour les préprocesseurs et les processeurs, afin qu'un préprocesseur et un processeur puissent correspondre). Cette action forcera la correspondance des règles à continuer une fois que la règle aura effectué ses actions.

### Crochet de mise à jour

Marqué n'effectue pas une actualisation complète à chaque mise à jour, donc si
vous avez des scripts qui restituent des parties du DOM, ils ont besoin
pour exécuter leur fonction de rendu à l'aide de l'API Hook de Marked.

L'exemple ci-dessous utilise Mermaid, que vous n'avez jamais réellement utilisé.
ce que vous devez faire, car Mermaid est désormais inclus par défaut. Mais
voici comment vous procéderiez si vous l'incluiez manuellement.

Ajoutez une action **Insérer JavaScript**, et dans le champ "Modifier JS".
fenêtre, initialisez le script et ajoutez le hook :

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Cela entraînera l'exécution de `mermaid.run()` à chaque fois
Marqué effectue une mise à jour partielle.

### Règles de test

Le bouton _Test Rules_ sous la liste des règles ouvrira un
boîte de dialogue où vous pouvez sélectionner n'importe quel fichier Markdown et il sera
testé par rapport à toutes vos règles. Les règles qui correspondent seront
mis en évidence par un onglet vert sur le côté gauche. Lors de la correspondance
contre un fichier, un bouton X apparaîtra qui peut être utilisé pour
effacez le test et désélectionnez les lignes.

## Glisser-déposer

La fenêtre Conductor prend en charge le glisser-déposer amélioré
des capacités qui détectent intelligemment les types de fichiers et
fournir des actions appropriées en fonction du fichier déplacé. Le
la mise en œuvre comprend un système de superposition divisée pour le texte
fichiers qui permettent aux utilisateurs de choisir entre tester le fichier
contre les règles ou en l'ajoutant comme une action.

![Glisser-déposer dans les règles personnalisées][glisser]

[drag]: images/draganddropconductor.jpg @2x width=800

### Détection du type de fichier

Le système détecte automatiquement différents types de fichiers et
affiche les messages de superposition appropriés :

- **Fichiers CSS** (`.css`) : affiche la superposition "Insérer un fichier CSS"
- **Fichiers JavaScript** (`.js`, `.javascript`) : affiche "Insérer
  Superposition "Fichier JS"
- **Fichiers de script** (n'importe quel fichier exécutable)) : affiche "Exécuter
  Superposition "Commandes"
- **Fichiers texte** : affiche la superposition divisée
- **Fichiers exécutables** : affiche la superposition "Exécuter la commande"
- **Extensions inconnues** : la valeur par défaut est le type "texte" et s'affiche
  superposition divisée

## Journal du processeur personnalisé [customprocessorlog]

Si vous obtenez des résultats étranges et souhaitez voir ce qui se passe, le journal des règles personnalisées vous montrera quelles règles sont exécutées dans quel ordre. Utilisez **Aide->Afficher le journal des règles personnalisées** pour l'ouvrir. Les actions **Exécuter la règle** invoquées et les appels imbriqués ignorés sont également enregistrés ici.

![Journal des règles personnalisées][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Exécuter plusieurs commandes

Une règle peut avoir plusieurs commandes en séquence. La sortie de
chaque commande sera transmise à la suivante. Si tu veux avoir
une commande génère quelque chose en même temps que celui de Marked
prévisualisez les mises à jour, assurez-vous de renvoyer le contenu original
vers STDOUT pour traiter la commande suivante ou intégré
processeur.

Par exemple, si vous souhaitez qu'une commande mette à jour un PDF
document utilisant Pandoc, transmettez simplement le chemin du fichier d'origine
(à partir des variables d'environnement) vers Pandoc avec les
options de ligne de commande, puis renvoyer le contenu STDIN
vers STDOUT.

## Contournement dynamique des processeurs personnalisés

Si un processeur personnalisé renvoie "NOCUSTOM" sur STDOUT, marqué
mettra fin au processeur personnalisé et reviendra au
processeur interne par défaut. Cela vous permet de créer un
processeur personnalisé qui peut décider s'il doit ou non
exécuter en utilisant les [variables d'environnement](#environmentvariables)
ci-dessous, le nom de fichier ou l'extension du document, la correspondance du contenu
ou autre logique.

Si au lieu de `NOCUSTOM` un processeur personnalisé renvoie
`MULTIMARKDOWN` ou `DISCOUNT` (ou `GFM`), `KRAMDOWN`, ou
`COMMONMARK`, alors ce processeur interne sera utilisé pour
juste ce document. Ce changement n'affectera pas la valeur par défaut
processeur défini dans Paramètres.

## Variables d'environnement

L'action Exécuter la commande possède un éditeur d'environnement dans lequel vous
pouvez définir vos propres variables d'environnement qui seront
disponible pour la commande ou le script. En plus de ceux-ci
variables personnalisées, Marked en inclut certaines.

Marked exécute le processeur personnalisé dans son propre shell, ce qui signifie
les variables d'environnement standard ne sont pas automatiquement transmises.
Vous pouvez utiliser les variables d'environnement de Marked pour augmenter votre
posséder dans vos scripts. Marqué crée les variables suivantes
disponible pour une utilisation dans vos scripts shell :

**MARKED_ORIGIN**
: L'emplacement (répertoire de base) de votre fichier de travail principal (le dossier du texte de travail, Scrivener ou fichier d'index).

**CHEMIN**
: Marked définit un chemin qui inclut les dossiers exécutables par défaut et ajoute le répertoire dans le `MARKED_ORIGIN` ci-dessus. Les valeurs par défaut sont : `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. Vous pouvez ajouter le vôtre en définissant la variable PATH selon vos besoins et en ajoutant ou en écrasant le chemin de Marked (par exemple `PATH=/usr/local/yourfolder:$PATH`).

**ACCUEIL**
: Le répertoire personnel de l'utilisateur connecté. Python et d'autres scripts qui dépendent de la définition de la variable HOME le récupéreront automatiquement, mais il est disponible pour d'autres utilisations dans vos scripts.

**MARKED_EXT**
: L'extension du fichier principal en cours de traitement. Cette variable vous permet de scripter différents processus en fonction du type de fichier affiché. Par exemple, si `$MARKED_EXT == "md"` exécutez votre processeur Markdown préféré, mais si `$MARKED_EXT == "textile"` exécutez un processeur Textile.

**MARKED_PATH**
: Il s'agit du chemin UNIX complet vers le fichier principal ouvert dans Marked au moment de son chargement.

**MARKED_INCLUDES**
: Une liste entre guillemets, séparés par des virgules, des fichiers marqués inclus dans le texte transmis en utilisant les différentes [syntaxes d'inclusion](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: Celui-ci sera défini sur "PROCESS" ou "PREPROCESS", vous permettant d'utiliser un seul script pour gérer les deux phases en fonction de cette variable.

**MARKED_CSS_PATH**
: Le chemin complet vers la feuille de style actuelle

### Variables d'environnement de métadonnées

Lorsque l'action Exécuter la commande est exécutée dans l'espace de travail de Marked
Système conducteur, les métadonnées du document sont automatiquement
extrait et mis à disposition en tant que variables d'environnement au
commande.

#### Comment ça marche

1. **Extraction de métadonnées** : le système extrait les métadonnées du document à l'aide de la méthode `extractMetaDataFromString:` existante, qui prend en charge :
   - Matière première YAML (`---` blocs)
   - Métadonnées MultiMarkdown (clé : lignes de valeur)
   - Métadonnées Pandoc (`%` cartouches)
   - Métadonnées des commentaires HTML (`<!-- key: value -->`)

2. **Normalisation des clés** : les clés de métadonnées sont normalisées pour être utilisées comme variables d'environnement :
   - Converti en minuscule
   - Tous les caractères non alphanumériques sont supprimés
   - Les espaces et les caractères spéciaux sont supprimés

3. **Format de variable d'environnement** : Chaque clé de métadonnées devient une variable d'environnement avec le préfixe `MD_` :
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Exemple

Étant donné un document avec ces métadonnées :

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

Les variables d'environnement suivantes seraient disponibles pour
commandes :

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Utilisation dans les commandes

Vous pouvez désormais utiliser ces variables d'environnement dans votre Run
Actions de commande :

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Actions prises en charge

Cette fonctionnalité de métadonnées à variable d'environnement est
disponible en :

- Actions **Exécuter la commande**
- Actions **Exécuter le script intégré**

Les métadonnées sont automatiquement extraites du document
contenu et mis à la disposition de toute commande ou script qui
traverse ces actions.

## Activation et désactivation

Les processeurs personnalisés peuvent être activés et désactivés pendant
documents individuels en utilisant {% kbd opt cmd C %}. Vous
peut également activer un préprocesseur ou un processeur pour un document
automatiquement [à l'aide de métadonnées](#perdocument) en haut de
le document.

Les statuts actuels des processeurs pour chaque document sont
affichés sous forme de voyants (visibles uniquement lorsqu'un processeur
est activé) à gauche des éléments de la barre d'outils en bas
barre d'outils droite de l'aperçu.

### Préprocesseur

Si vous configurez des règles de préprocesseur, elles sont exécutées après Marqué
gère toutes les tâches spécifiques à Marked, telles que l'inclusion de
documents et code, mais avant d'exécuter le processeur
(interne ou personnalisé). Cela vous donne une chance de rendre
variables de modèle personnalisées, gérer les substitutions ou injecter
votre propre contenu par tout autre moyen.

Marqué définit une variable d'environnement pour le travail
répertoire (`MARKED_ORIGIN`) vers le répertoire parent du
fichier en cours de prévisualisation. Vous pouvez l'utiliser pour modifier le fonctionnement
répertoire d'un script et inclure des fichiers avec des chemins relatifs
au document original. A titre d'exemple, dans Ruby, vous pouvez
utiliser :

	Dir.chdir(ENV['MARKED_ORIGIN'])

Lorsqu'il est activé, le préprocesseur personnalisé peut être activé et
désactivé pour les documents individuels en utilisant
{% kbd ctrl opt cmd C %}.

#### Processeur/Pré-processeur par document [pardocument]

Des processeurs personnalisés peuvent également être définis pour chaque document.
en utilisant le format de métadonnées pour [Par-Document
paramètres](Per-Document_Settings.html).

Vous pouvez spécifier s'il faut utiliser des paramètres de processeur personnalisés et
remplacer la valeur par défaut d'un document à l'aide de [Par-Document
paramètres](Per-Document_Settings.html) (`Custom Processor:`
et `Custom Preprocessor:`). Tout paramètre autre que "vrai"
ou "oui" désactivera le pré/processeur personnalisé.

Exemple d'utilisation :

    Processeur personnalisé : vrai
    Préprocesseur personnalisé : faux

Comme indiqué dans le [Par-Document
Paramètres](Per-Document_Settings.html#hidingmeta) page, vous
peut entourer ces métadonnées de marqueurs de commentaires HTML pour les masquer
depuis GitHub et d'autres processeurs qui ne le suppriment pas
de la sortie :

    <!--
    Processeur personnalisé : vrai
    Préprocesseur personnalisé : vrai
    -->

## Utilisation d'un processeur Markdown alternatif

Toute version Markdown que vous pouvez restituer à partir de la ligne de commande peut
être utilisé avec Marked. Il doit pouvoir donner son avis sur
STDIN, ce qui revient à "transférer" votre Markdown vers celui-ci.
ligne de commande, c'est-à-dire `cat myfile.md | myprocessor`. Il a besoin
pour renvoyer le HTML résultant sur STDOUT, qui chaque
le processeur avec lequel j'ai déjà travaillé le fait par défaut.

Utilisez `which YOUR_PROCESSOR` dans Terminal pour déterminer le chemin
à l'exécutable, puis collez-le dans le chemin d'accès à la commande Exécuter
ou faites simplement glisser l'exécutable vers la fenêtre Règles personnalisées
avec la règle à laquelle vous souhaitez ajouter l'action sélectionnée.

Si votre processeur nécessite des arguments sur la ligne de commande,
vous devrez également les saisir dans le champ. Certains
les processeurs ont besoin de tirets pour fonctionner sur STDIN et/ou STDOUT,
par ex. `-o - -` signale souvent l'entrée de STDIN, la sortie vers
STDOUT. Consultez la documentation de votre processeur pour plus de détails.

J'ai testé la fonctionnalité Custom Processor avec Pandoc,
Kramdown, marqué (remise), MultiMarkdown 6, Maruku et
diverses autres saveurs.

### Une note sur Pandoc et Sandboxing

Pandoc (et certains autres outils de ligne de commande) ne fonctionnera pas dans
la version Mac App Store (sandbox) de Marked.
Si vous devez exécuter Pandoc, utilisez **Aide->Crossgrade** pour obtenir un
licence gratuite pour la version directe (Paddle). C'est vrai
de tout processeur rencontrant des problèmes de sandboxing : s'il est marqué
ne peut pas l'exécuter en raison de problèmes d'autorisations MAS, il le fera
proposer les étapes de crossgrade. Si vous rencontrez des problèmes
et cela ne se produit pas, veuillez me contacter via le
[site d'assistance](https://support.markedapp.com/questions/add).

### Pandoc en tant que processeur de démarques de l'armée suisse

[Pandoc](https://pandoc.org/) est de loin le plus flexible
outil polyvalent pour gérer une gamme de formats de balisage. Par
en ajoutant un argument `-f` avec l'un des éléments suivants, Pandoc peut
soyez votre sous-traitant personnalisé pour l’un des :

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

Et bien d'autres. Voir le [Pandoc
documentation](https://pandoc.org/MANUAL.html) pour en savoir plus
infos. Pour utiliser l'un d'entre eux comme format d'entrée, ajoutez simplement le
suivant dans votre champ Exécuter la commande :

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc est parfait pour écrire un script qui utilise le
`$MARKED_EXT` variable d'environnement pour déterminer quel format
pour parcourir Pandoc, ou utiliser une série de règles avec
correspondances d’extension. Si l'extension est `md`, utilisez
`pandoc -f gfm` ou `pandoc -f markdown_mmd` (ou retournez simplement
`NOCUSTOM` sur STDOUT pour utiliser le processeur par défaut). Mais si c'est
`textile`, exécutez `pandoc -f textile` dans le script. Et si
il est `wiki`, utilisez l'un des processeurs de balisage wiki. Vous obtenez
l'idée.

Comme les aficionados de Pandoc le savent, Pandoc peut également gérer
bibliographie complète et scénarios LaTeX. La plupart des fonctionnalités
vous pouvez accéder via la ligne de commande sont disponibles uniquement
en utilisant des arguments passants dans Marked.

## Utilisation de textiles

Quelques personnes ont demandé comment faire fonctionner le textile en
Marqué. Vous devez disposer d'un convertisseur textile disponible auprès de
la ligne de commande. Il existe quelques options, dont Pandoc
(voir ci-dessus), mais si Pandoc n'est pas déjà installé,
deux autres options sont RedCloth pour Ruby et Textile pour Perl
(nécessite que les outils de développement soient installés). Installer
l'un ou l'autre :

1. Installez Textile à partir de
   <https://github.com/bradchoate/text-textile> **OU**
   `sudo gem install RedCloth` dans le terminal
2. Utilisez `which textile` ou `which redcloth` pour déterminer le
   chemin à utiliser dans les paramètres du chemin du processeur personnalisé

Marked est désormais un aperçu textile pour vous !

## Utilisation d'AsciiDoc

1. Installez [AsciiDoctor](http://asciidoctor.org/).
2. Activez une règle personnalisée dans {% prefspane Processor %} pour correspondre à vos fichiers AsciiDoc.
3. Définissez la règle sur un processeur et ajoutez une action Exécuter la commande.
    1. Déterminez le chemin vers `asciidoc`, qui sera
       quelque chose comme `/usr/bin/asciidoc` ou
       `/opt/local/bin/asciidoc`. En cas de doute, utilisez
       `which asciidoc` pour localiser
    2. Entrez `[PATH To asciidoc] --backend html5 -o - -` comme
       la commande (le - à la fin envoie la sortie comme
       STDOUT)

Cela envoie le document actuel à STDIN et affiche le
HTML généré en tant que STDOUT.

Voir [cet résumé](https://gist.github.com/mojavelinux/6324279)
de [Dan Allen](https://gist.github.com/mojavelinux) pour
plus d'informations.