# <%= @title %>

La version Mac App Store (MAS) de Marked s'exécute dans un environnement sandbox qui restreint certaines opérations pour des raisons de sécurité. Cela peut affecter certaines fonctionnalités, en particulier lors de l'utilisation de processeurs personnalisés avec des binaires ou scripts externes.

## Restrictions courantes du sandbox

### Binaires de la commande Exécuter

Le problème le plus courant rencontré par les utilisateurs est que les binaires externes ne peuvent pas être exécutés directement dans la version MAS. Cela affecte :

- les **processeurs externes** comme Pandoc, Kramdown, ou d'autres outils en ligne de commande
- les **scripts personnalisés** qui dépendent de binaires externes
- les **utilitaires système** qui ne sont pas accessibles depuis le sandbox

### Solutions de contournement

#### Copier des binaires dans le bundle de l'application

Si vous devez utiliser des processeurs externes comme Pandoc dans la version MAS, vous pouvez copier le binaire dans le bundle de l'application :

1. Clic droit sur Marked.app → **Afficher le contenu du paquet**
2. Accédez à **Contents/Resources/**
3. Créez un dossier `bin` s'il n'existe pas
4. Copiez votre binaire (par exemple, `pandoc`) dans ce dossier `bin`
5. Rendez-le exécutable : `chmod +x` sur le binaire
6. Dans l'action Exécuter la commande, référencez-le comme :
   - `YOUR_BINARY_NAME [arguments]`
   - Ou utilisez le chemin complet : `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Remarque** : les scripts avec des shebangs externes (comme les scripts Python pointant vers `/opt/homebrew/bin/python`) seront automatiquement exécutés via les interpréteurs système lorsqu'ils seront copiés dans le bundle. La version MAS peut encore avoir des difficultés à exécuter des binaires qui sont en réalité des scripts Python ou Ruby plutôt que des fichiers binaires.

**Important** : vous devrez recopier les binaires après chaque mise à jour de l'application, car les mises à jour remplacent l'intégralité du bundle.

#### Utiliser des scripts intégrés

Plutôt que d'exécuter des commandes externes, vous pouvez utiliser l'action **Exécuter le script intégré** dans les Règles personnalisées. Cela vous permet d'écrire des scripts directement dans l'éditeur de code de Marked, qui peut accéder aux interpréteurs système disponibles dans le sandbox.

## Passer à la version sans sandbox [crossgrade]

Si vous avez fréquemment besoin d'utiliser des binaires externes ou si vous rencontrez d'autres limitations liées au sandboxing, vous pourriez vouloir passer à la version sans sandbox de Marked. La version sans sandbox n'a aucune de ces restrictions et peut exécuter n'importe quel outil ou script en ligne de commande que vous avez installé.

### Pour les utilisateurs d'abonnement

Si vous avez un abonnement Mac App Store actif :

1. **Annulez votre abonnement MAS** dans Réglages Système → Identifiant Apple → Média et achats → Abonnements
2. **Téléchargez l'essai gratuit** depuis [https://markedapp.com](https://markedapp.com)
3. **Démarrez un abonnement Paddle** directement via l'application ou le site web

La version Paddle offre les mêmes fonctionnalités sans les restrictions liées au sandboxing.

### Pour les détenteurs d'un déverrouillage permanent

Si vous avez acheté un déverrouillage permanent ou une licence à vie via le Mac App Store, veuillez [envoyer un e-mail au développeur](mailto:marked@brettterpstra.com?subject=Crossgrade%20de%20licence%20Marked&body=Veuillez%20inclure%20votre%20UUID%20%28Aide-%3ECopier%20l%27UUID%20dans%20Marked%29%20dans%20cet%20e-mail%20pour%20la%20v%C3%A9rification%20du%20re%C3%A7u.) pour demander une licence Paddle gratuite à vie.

**Important** : pour vérifier votre achat, veuillez inclure l'un des éléments suivants dans votre e-mail :

- votre **identifiant utilisateur** (UUID) : utilisez **Aide → Copier l'UUID** pour le copier dans votre presse-papiers, puis collez-le dans votre e-mail
- votre **ID de transaction** depuis votre reçu App Store (vous pouvez le trouver dans votre historique d'achats dans l'application App Store)

Le Mac App Store ne communique pas votre adresse e-mail aux développeurs, donc nous vérifions les achats à l'aide des ID de transaction ou des identifiants utilisateur stockés sur notre serveur. Inclure ces informations nous aidera à vérifier rapidement votre achat et à générer votre licence Paddle gratuite.

### Version Setapp

Autrement, si vous avez un abonnement Setapp, vous pouvez utiliser la version Setapp de Marked, qui n'est également pas sandboxée et dispose d'un accès complet aux ressources système.

## Ressources supplémentaires

Pour plus d'informations sur les processeurs personnalisés et leurs capacités, voir [Processeur personnalisé](Custom_Processor.html).
