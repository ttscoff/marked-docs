<!-- MT-DRAFT: machine translation; human review required -->

# Permissões personalizadas do processador na versão MAS

Devido a restrições de sandbox, a versão do Marked na Mac App Store não é capaz de executar certos tipos de ferramentas binárias como processadores personalizados. Se você se deparar com essa limitação, existem algumas etapas que você pode tentar.

1. Certifique-se de ter entrado em Configurações **Marcadas** ({% kbd cmd , %}), no painel **Avançado** e clicado em "Atualizar Permissões". Isso tentará conceder acesso marcado a toda a sua unidade padrão, resolvendo problemas com scripts e utilitários que precisam acessar pastas temporárias e locais não padrão.
2. Tente usar um script. Faça referência ao utilitário que você deseja executar (multimarkdown, kramdown, etc.) em um script de shell. Pode ser um script bash, Ruby, Perl ou Python. Em seguida, defina o processador em Configurações avançadas para o shell ou executável relacionado e os parâmetros para o local do script. Por exemplo, posso criar um script bash salvo em ~/scripts/mmd_wrapper.sh:

        #!/bin/bash
        gato | /usr/local/bin/multimarkdown

    Em seguida, torne-o executável (`chmod a+x ~/scripts/mmd_wrapper.sh`) e defina minhas configurações de processador personalizado:

        Processador: /bin/bash
        Argumentos: /Users/me/scripts/mmd_wrapper.sh
3. Alguns executáveis (especialmente o Pandoc) simplesmente não funcionam no sandbox. Neste caso, entre em contato comigo através da janela de erro que aparece durante a execução para receber uma licença crossgrade para a versão direta.