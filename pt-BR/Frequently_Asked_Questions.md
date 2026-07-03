<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %> [toc]

## O código de licença já foi utilizado [license_code_has_already_been_utilized]

Se você fizer uma nova instalação do Marked 2 e receber o erro "O código de licença já foi utilizado" ao inserir sua licença, <a href="mailto:me@brettterpstra.com">entre em contato comigo</a> solicitando uma nova licença. **Inclua o endereço de e-mail com o qual você se registrou e/ou seu código de licença atual.**

As primeiras licenças geradas para Marked tinham um limite de uso em vez de um limite de máquina, portanto, 3 instalações - mesmo na mesma máquina - consumiriam ativações. Esses limites foram corrigidos em licenças geradas mais recentemente. A compra de uma licença Marked 2 permite que você instale o Marked 2 em qualquer máquina de sua propriedade, portanto, não hesite em solicitar uma substituição se tiver problemas.

[Índice](#toc)

## Licenças de sites e descontos educacionais [site_licenses_and_educational_discounts]

Licenças de site/em massa com desconto estão disponíveis para Marcado 2. Para solicitar um link de compra, entre em contato com <a href="mailto:me@brettterpstra.com">Brett</a> e especifique o número de licenças que deseja comprar.

**Descontos**

- 5-9: **10% de desconto**
- 10-19: **12% de desconto**
- 20-49: **15% de desconto**
- 50+: **20% de desconto**

Um desconto educacional também está disponível para as versões direta e Mac App Store. Para a Mac App Store, os descontos educacionais padrão da Apple estão habilitados. Para adquirir uma versão direta com desconto educacional, <a href="mailto:me@brettterpstra.com">entre em contato comigo</a> e solicite um cupom.

[Índice](#toc)

## Um URL não valida ou retorna "Desconhecido" [a_url_wont_validate_or_returns_unknown]

A [validação de link](http://marked2app.com/help/Link_Validation.html) de Marked usa uma solicitação HEAD básica para determinar se um link é válido. Qualquer resultado diferente de 200 (sucesso) resultará em um erro desconhecido ou se for um código de erro comum, como 404 (não encontrado) ou 500 (erro do servidor). URLs por trás da autenticação (como URLs de desenvolvedores da Apple ou qualquer coisa que exija login para acesso) retornarão um "desconhecido", assim como certos sites como Amazon.com, onde o servidor retorna códigos de resposta bizarros. Não há muito que Marked possa fazer sobre isso.

[Índice](#toc)

## Permissões personalizadas do processador na versão MAS [custom_processor_permissions_in_mas_version]

Devido a restrições de sandbox, a versão Mac App Store do Marked 2 não é capaz de executar certos tipos de ferramentas binárias como processadores personalizados. Se você se deparar com essa limitação, existem algumas etapas que você pode tentar.

1. Certifique-se de ter acessado **Marcado 2** Preferências (⌘,), no painel **Avançado** e clicado em "Atualizar permissões". Isso tentará conceder acesso marcado a toda a sua unidade padrão, resolvendo problemas com scripts e utilitários que precisam acessar pastas temporárias e locais não padrão.
2. Tente usar um script. Faça referência ao utilitário que você deseja executar (multimarkdown, kramdown, etc.) em um script de shell. Pode ser um script bash, Ruby, Perl ou Python. Em seguida, defina o processador nas preferências Avançadas para o shell ou executável relacionado e os parâmetros para o local do script. Por exemplo, posso criar um script bash salvo em ~/scripts/mmd_wrapper.sh:
    
        #!/bin/bash
        gato | /usr/local/bin/multimarkdown
    
    Em seguida, torne-o executável (`chmod a+x ~/scripts/mmd_wrapper.sh`) e configure minhas preferências de processador personalizado:

        Processador: /bin/bash
        Argumentos: /Users/me/scripts/mmd_wrapper.sh
3. Alguns executáveis (especialmente o Pandoc) simplesmente não funcionam no sandbox. Neste caso, entre em contato comigo através da janela de erro que aparece durante a execução para receber uma licença crossgrade para a versão direta.

[Índice](#toc)

## Links intradocumentos em PDFs exportados [intra-document_links_in_exported_pdfs]

A exportação de PDF do Marked atualmente usa os recursos de impressão do WebKit. Uma consequência disso é que os links intradocumento (internos), incluindo aqueles em um Índice, não irão para outros pontos do documento. Isso não parece ser algo que a Apple tenha intenção de consertar na versão do WebKit que o Marked 2 usa.

Em alguns casos, você pode obter bons resultados exportando HTML com estilo incorporado e depois usando seu navegador para imprimir em PDF. Você não obterá todos os recursos de exportação do Marked, mas normalmente obterá um PDF com links internos funcionais. É uma troca por enquanto.

[Índice](#toc)

## Caminhos relativos em arquivos incluídos [relative_paths_in_included_files]

Arquivos incluídos usando [sintaxe de inclusão][include] do Marked, bem como [arquivos do Scrivener][scriv], podem usar caminhos relativos para referenciar outros arquivos. (_**Nota:** isso não se aplica a arquivos incluídos usando a sintaxe `/file` do IA Writer ou arquivos CSV_). A partir de versões recentes (2.5.10+), esses caminhos são _relativos ao arquivo incluído_, não ao arquivo base.

Dada uma estrutura de arquivo/pasta como esta:

    - arquivo_base.md
    - subpasta
        - arquivo_incluído.md
    - imagens
        - imagem1.jpg

Se `included_file.md` faz referência a image1.jpg por meio de um caminho relativo, ele precisa ser escrito como `../images/image1.jpg`, _não_ `images/image1.jpg`. (`..` indica o diretório pai).

[include]: http://marked2app.com/help/Multi-File_Documents.html
[scriv]: http://marked2app.com/help/Scrivener_Support.html

[Índice](#toc)

## Como faço para recuperar uma licença perdida (versão direta) [how_do_i_retrieve_a_lost_license_direct_version]

Se você perdeu uma licença comprada para Marcado 2 através do Paddle, você pode recuperá-la em [my.paddle.com](https://my.paddle.com/). Se você tiver algum problema para fazer login, você pode solicitar uma consulta por meio de uma solicitação privada no [site de suporte](http://support.markedapp.com).

[Índice](#toc)

## Problemas de compra no aplicativo (Error Domain=Paddle Code=0 "(null)") [in-app_purchase_issues_error_domainpaddle_code0_null]

Paddle me informou recentemente que os IAPs estão quebrados e que eles não planejam consertá-los porque poucos desenvolvedores os implementaram. (O que é tão frustrante para mim quanto para você.) A parte verdadeiramente frustrante é que eles não pararam de permitir pagamentos, então preciso reembolsar manualmente as compras até que algo seja feito sobre a forma como as licenças são tratadas. Supostamente, um novo sistema será lançado nas próximas semanas, então, se você estiver disposto a esperar, farei tudo o que puder para garantir que todas as compras atuais do IAP de Ortografia/Gramática sejam honradas por meio de qualquer sistema fornecido a seguir.

Se você preferir um reembolso, basta <a href="mailto:me@brettterpstra.com">enviar-me um e-mail diretamente</a> com a conta de e-mail usada para licenciar ou o ID da transação contido no recibo.

**Atualização:** Paddle anunciou oficialmente a nova solução IAP e ela será implementada assim que estiver disponível publicamente. As licenças atuais de compra no aplicativo (ortografia/gramática) serão migradas automaticamente e um novo código de cupom será fornecido. Isso deve acontecer em breve.

[Índice](#toc)

## Blocos de código protegidos dentro de blocos de código recuados [fenced_code_blocks_inside_indented_code_blocks]

Em circunstâncias bastante raras, você pode querer mostrar as cercas de um bloco de código protegido. Normalmente, isso poderia ser feito no Markdown recuando o código protegido, forçando um bloco "literal" recuado contendo o bloco de código protegido, que então não seria processado. Marcado lida com código protegido de maneira diferente (como parte de sua capacidade de trabalhar com múltiplas opções de sintaxe), portanto, para fazer isso, você precisa usar uma barreira dupla. Como você pode usar qualquer número de crases ou tils para isolar um bloco de código (desde que a contagem de abertura e fechamento corresponda, você pode usar apenas duas barreiras de comprimentos diferentes. Por exemplo

    `````
    ```
    Código protegido real
    ```
    `````

[Índice](#toc)