<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Existem várias maneiras de incorporar JavaScripts adicionais no Marked.

## Incluindo JavaScript por documento [including-javascript-per-document]

Você pode incluir scripts em um único documento usando tags `<script>` no próprio conteúdo. Isso pode ser útil para bibliotecas como [D3](https://d3js.org/) para visualizações de dados que você só precisa em documentos específicos:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Se estiver usando MultiMarkdown como processador, você pode incluir scripts nos metadados e eles serão inseridos no documento. Como Marked produz apenas "snippet", a chave `XHTML Header` não é ideal. Em vez disso, use `CSS Header` e os scripts serão inseridos na parte inferior do documento.

	Cabeçalho CSS: <script src="file.js"></script>

Para fazer com que os scripts incluídos sejam atualizados quando o conteúdo for alterado, consulte [Hooks](#hooks).

## Incluindo JavaScript [including-javascript]

Você pode incluir seu próprio JavaScript de arquivos locais, CDNs ou colando código bruto. Para acessá-lo, abra {% prefspane Style %} e clique no botão *Regras Personalizadas*.

Configure uma nova regra personalizada ou adicione scripts a uma já existente. Para adicionar scripts a cada arquivo, defina o predicado como "nome do arquivo contém *".

O editor de ações para uma regra personalizada tem três opções para incluir scripts:

Inserir arquivo JavaScript
: Permite selecionar um arquivo local para inserir no final do documento

Insira JavaScript do URL
: permite incluir uma CDN ou outra URL remota, que criará uma tag `<script>` no final do documento com a URL vinculada

Insira JavaScript
: Abre um editor de código onde você pode escrever/colar seu próprio código JavaScript

Esses scripts serão inseridos no final da visualização, antes da tag do documento. Se você precisar chamar uma função init ou atualizar sempre que a visualização for atualizada, consulte [Incluindo JavaScript bruto](Embedding_Scripts.html#hooks) e familiarize-se com os [hooks](#hooks) do Marked.

## Sereia e outros scripts [mermaid]

jQuery está incluído por padrão e você pode usá-lo em qualquer script adicionado ao Marked usando qualquer um dos métodos abaixo.

[Sereia](https://mermaid.js.org/intro/) para diagramação do tipo Markdown agora está incluída por padrão em todos os documentos. Qualquer bloco de código protegido com a linguagem `mermaid` será automaticamente renderizado como um diagrama.

Na parte inferior de {% prefspane Style %}, uma caixa de seleção para "Diagramas panorâmicos e de zoom" está disponível quando o conteúdo do Mermaid está presente. Marcar esta caixa fará com que os diagramas sejam ampliados com rolagem {% kbd cmd %} e panoramizados clicando e arrastando. O script para esse recurso está incluído em um CDN e requer uma conexão com a Internet.

Se houver uma biblioteca específica que você gostaria de ver incluída por padrão, informe-me no [fórum BrettTerpstra.com](https://forum.brettterpstra.com/) ou através do [site de suporte](https://support.markedapp.com/questions/add).

## Ganchos [hooks]

A partir de versões recentes, Marked não executa mais uma atualização completa da página ao atualizar o conteúdo, mas injeta o novo conteúdo no DOM sem exigir o carregamento da página. Isso significa que os scripts incluídos que são acionados no carregamento da página não serão acionados novamente quando o conteúdo for atualizado. Marcado fornece um recurso de "ganchos" para acomodar isso. Para registrar um gancho, você precisa incluir um segundo bloco de script chamando a [função `Marked.hooks.register()`](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor), que aceita um gatilho, neste caso 'update', e uma função para executar.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

Todas as [funcionalidades da API](https://markedapp.com/jsapi/) do Marked podem ser usadas neste campo. (Você também pode usar a API em qualquer script carregado.) Para depuração interativa e experimentação com a API em uma visualização ao vivo, consulte a seção [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) para obter detalhes sobre como usar o menu Desenvolver do Safari com Marcado.

Agora, sempre que uma atualização for realizada (sempre que o arquivo fonte monitorado for salvo), a função passada será executada. Contanto que o script que você está executando tenha algum tipo de função init ou render, você pode chamá-lo com um gancho e renderizá-lo sempre que seu documento for salvo e uma atualização for acionada.



*[CDN]: Rede de distribuição de conteúdo