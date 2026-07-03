<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado permitirá que certos atributos de um documento sejam definidos no formato de metadados MultiMarkdown (detalhado abaixo). Você pode usá-los para definir características e estilos que afetam apenas aquele documento, sem alterar as configurações padrão.

A maioria dos cabeçalhos MultiMarkdown são ignorados pela visualização, mas os seguintes são permitidos e afetam a renderização. Você pode incluir outros metadados a serem renderizados na saída final. Marcado irá apenas ignorar as chaves não listadas abaixo. Se você salvar como HTML e *não* incluir um modelo, Marcado renderizará todas as chaves de metadados conforme esperado.

## Formato de metadados

Os metadados são inseridos na parte superior do arquivo Markdown ou imediatamente após qualquer cabeçalho YAML. Eles consistem em uma chave, seguida por dois pontos, espaços ou tabulações opcionais e o valor:

	Metadados de exemplo: chave de exemplo

Múltiplas entradas de metadados devem estar em suas próprias linhas, mas sem quebras de linha entre elas. A última entrada de metadados precisa ser seguida por uma linha em branco antes do início do texto do documento.

	Primeiro: esta é a primeira entrada de metadados
	Segundo: esta é a segunda entrada
	Terceiro: a última entrada de metadados

	# O início do texto do documento

## Chaves de metadados marcadas

### Ocultando metadados para outros processadores [hidingmeta]

**Observação:** Se você estiver usando um processador personalizado ou postando seu Markdown diretamente em uma fonte que não processa esses metadados, ainda poderá usá-lo adicionando marcadores de comentários HTML antes e depois dos metadados. Ao contrário do MultiMarkdown e de outros processadores, o Marked localizará essas tags em qualquer lugar do documento e as processará/removerá da saída. Assim, o seguinte no cabeçalho fornecerá os resultados desejados em Marcado, mas não aparecerá em outro lugar:

	<!--
	Estilo Marcado: Meu Estilo Personalizado
	Processador personalizado: verdadeiro
	-->

*Apenas certifique-se de que a chave de metadados comece no início da linha, sem espaços ou tabulações, e não coloque mais nada na linha após o valor.*

### Estilos por documento

A tecla "Estilo Marcado:" definirá um estilo de visualização para o documento. O valor pode ser o nome de um estilo padrão ou um nome ou caminho para qualquer [Estilo personalizado](Custom_Styles.html) que você definiu nas configurações. Se esta chave for encontrada e corresponder a um estilo que Marked conhece, esse estilo será usado para a visualização toda vez que o documento que a contém for carregado.

**Exemplo**

	Estilo Marcado: Cidadão Honrado

### Idioma das citações

Por padrão, Marcado usa aspas no estilo inglês. Você pode modificar isso por documento com a chave "Quotes Language:". Os idiomas disponíveis são:

* holandês
* inglês
* francês
* alemão
* guilhotinas
* sueco

**Exemplo**

	Idioma das citações: francês

	Cria «aspas» no idioma francês.

### Nível base do cabeçalho

Você pode definir o nível de cabeçalho a partir do qual Marcado inicia a contagem com a tecla "Base Header Level:". Deve ser um número de 1 a 6 e modificará a maneira como os cabeçalhos "#" são renderizados. Se você definir o nível do cabeçalho como 3, o que normalmente seria um cabeçalho de primeiro nível (h1) será renderizado como um cabeçalho de terceiro nível (h3) e os cabeçalhos subsequentes na hierarquia serão aumentados em 2.

**Exemplo**

	Nível básico do cabeçalho: 3

	# Este título será renderizado como h3

	## Este título será um h4

	Renderiza como:

	<h3>Este título será renderizado como h3</h3>

	<h4>Este título será um h4</h4>

### Processadores personalizados

Conforme detalhado em [Processador Personalizado](Custom_Processor.html#preprocessor), você pode ativar ou desativar um processador personalizado e um pré-processador personalizado usando metadados:

    Processador personalizado: verdadeiro
    Pré-processador personalizado: falso

"true" ou "false" liga e desliga o pré/processador.

O valor "Processador" pode ser definido como "multimarkdown" ou "desconto" para forçar o uso de um ou outro dos processadores internos. Esta configuração por documento não alterará a configuração padrão em {% prefspane Processor %}.

### Imprimir cabeçalhos/rodapés

Você pode substituir as configurações em {% prefspane Export %} para imprimir cabeçalhos e rodapés usando as seguintes teclas:

	imprimir cabeçalho à esquerda:
	centro do cabeçalho de impressão:
	imprimir cabeçalho à direita:
	imprimir rodapé à esquerda:
	imprimir centro do rodapé:
	imprimir rodapé à direita:

Isso pode incluir [variáveis de impressão](Exporting.html#headersandfooters) como `%title`, `%page`, `%total`, etc., bem como referências a outros metadados usando `%md_[key without spaces]`.

### Imprimir margens

Defina as margens da página para impressão e saída de PDF paginado com a tecla `Margins:`. Os valores estão em pontos; sufixos como `px`, `pt` e `em` são ignorados. Forneça dois números para margens verticais e horizontais ou quatro números para superior, direita, inferior e esquerda:

	Margens: 10 20
	Margens: 10, 20, 10, 20

As margens de metadados substituem as configurações {% prefspane Export %} e os campos de margem no painel de exportação de PDF.

### Inserindo JavaScript

Este método especifica os dados incluídos na tag `<head>` do documento. Marcado ignora a maioria dos valores desta chave, exceto na saída do documento completo, mas respeitará os scripts incluídos desta maneira. As tags de script definidas aqui não estarão no cabeçalho, porém serão anexadas antes da tag de fechamento `</body>`. O jQuery já está carregado e você pode tirar vantagem disso em qualquer script que injetar.

**Exemplo**

	Cabeçalho XHTML: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		-ou-

	Cabeçalho XHTML: <script src="myfancyscript.js"></script>