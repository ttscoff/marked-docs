<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked usa muito JavaScript para fornecer os recursos que oferece na visualização. Por esse motivo, podem surgir algumas complicações quando os scripts são incluídos no corpo do documento.

## Scripts externos

Você pode incluir alguns scripts externos usando uma linha de metadados "CSS Header:" na parte superior do seu documento. Esses scripts serão inseridos não no cabeçalho, mas no rodapé depois que os scripts do jQuery e do Marked já tiverem sido carregados. Isso é ideal na maioria dos casos. Você ainda poderá enfrentar um comportamento inesperado, pois o Marked não pode compensar todos os possíveis conflitos de script. As alterações no DOM podem ser especialmente problemáticas.

    Cabeçalho CSS: <script src="file.js"></script>

## Inline inclui

Existem muitos aplicativos para que o JavaScript apareça no corpo de um documento, como geradores de gráficos ou outras ferramentas do Canvas. Dependendo das definições de configuração e do processador que você está usando, eles geralmente ficam confusos. A solução é colocar seu script e elementos DOM extras em um arquivo externo e usar a sintaxe do Marked para [arquivos de inclusão "brutos"] [sintaxe]. Esses arquivos não são processados ​​de forma alguma; seu conteúdo é adicionado ao arquivo após a conclusão do restante do processamento.

    Texto de redução.

    <<{arquivo.html}

    Mais texto Markdown...

Para experimentar e depurar o JavaScript executado na visualização do Marked, você pode anexar o Web Inspector do Safari à janela de visualização usando as etapas em [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml