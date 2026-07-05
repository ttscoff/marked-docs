# Autorisations de processeur personnalisées dans la version MAS

En raison des restrictions du sandboxing, la version Mac App Store de Marked n'est pas en mesure d'exécuter certains types d'outils binaires en tant que processeurs personnalisés. Si vous rencontrez cette limitation, vous pouvez essayer quelques étapes.

1. Assurez-vous d'être allé dans Paramètres **Marked** ({% kbd cmd , %}), dans le volet **Avancé** et d'avoir cliqué sur « Mettre à jour les autorisations ». Cela tentera d'accorder à Marked un accès à l'intégralité de votre lecteur par défaut, résolvant ainsi les problèmes liés aux scripts et aux utilitaires qui doivent accéder aux dossiers temporaires et aux emplacements non par défaut.
2. Essayez d'utiliser un script. Référencez l'utilitaire que vous souhaitez exécuter (multimarkdown, kramdown, etc.) dans un script shell. Il peut s'agir d'un script bash, Ruby, Perl ou Python. Définissez ensuite le processeur dans les paramètres avancés sur le shell ou l'exécutable associé, et les paramètres sur l'emplacement du script. Par exemple, je peux créer un script bash enregistré dans ~/scripts/mmd_wrapper.sh :

        #!/bin/bash
        cat | /usr/local/bin/multimarkdown

    Rendez-le ensuite exécutable (`chmod a+x ~/scripts/mmd_wrapper.sh`) et configurez vos paramètres de processeur personnalisé :

        Processeur : /bin/bash
        Arguments : /Users/me/scripts/mmd_wrapper.sh
3. Certains exécutables (en particulier Pandoc) ne fonctionneront tout simplement pas dans le sandboxing. Dans ce cas, veuillez me contacter via la fenêtre d'erreur qui apparaît lors de l'exécution pour recevoir une licence crossgrade vers la version directe.
