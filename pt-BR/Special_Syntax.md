<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Chamadas

## Urso/Obsidiana ##

Marcado oferece suporte a textos explicativos com a sintaxe usada por Obsidian e Bear, que é uma citação em bloco especialmente formatada:

	> [!NOTE] Título da nota
	> Texto adicional

A "NOTA" em `[!NOTE]` não diferencia maiúsculas de minúsculas. Pode ser qualquer um dos seguintes:

- NOTA
- RESUMO, RESUMO, TLDR
- INFORMAÇÕES
- TODO
- DICA, DICA, IMPORTANTE
- SUCESSO, VERIFIQUE, FEITO
- PERGUNTA, AJUDA, FAQ
- AVISO, CUIDADO, ATENÇÃO
- FALHA, FALHA, FALTA
- PERIGO, ERRO
- ERRO
- EXEMPLO
- CITAÇÃO, CITAÇÃO

Isso criará blocos especialmente formatados.

Você pode usar `+` ou `-` para tornar o texto explicativo recolhível. Um sinal de mais (`+`) significa que o texto explicativo pode ser recolhido, mas o padrão é aberto. Um sinal de menos (`-`) significa que o texto explicativo pode ser recolhido, mas o padrão é fechado.

  ![Chamadas marcadas][chatas]

[callouts]: images/callouts-800.jpg @2x width=800

### Parque Xcode ###

Ao visualizar arquivos do Xcode Playground, Marked oferece suporte à sintaxe de chamada nativa do Xcode Playground:

	- Atenção: Título opcional
	O conteúdo da frase de destaque vai aqui.

O tipo de texto explicativo (por exemplo, "Atenção") não diferencia maiúsculas de minúsculas e pode ser qualquer um dos seguintes tipos de texto explicativo do Xcode Playground:

- **Atenção** - Estilizado como texto explicativo informativo
- **Autor** - Chamada de metadados
- **Autores** - Chamada de metadados
- **Bug** - Chamada de erro/perigo
- **Complexidade** - Texto explicativo em estilo de nota
- **Direitos autorais** - Chamada de metadados
- **Chamada personalizada** - Chamada de exemplo
- **Data** - Chamada de metadados
- **Exemplo** - Exemplo de texto explicativo
- **Experiência** - Chamada estilo dica
- **Importante** - Texto explicativo em estilo informativo
- **Invariante** - Texto explicativo em estilo de nota
- **Nota** - Nota explicativa
- **Pré-condição** - Texto explicativo em estilo de nota
- **Pós-condição** - Texto explicativo em estilo de nota
- **Observação** - Texto explicativo em estilo de nota
- **Requer** - Texto explicativo em estilo de nota
- **Veja também** - Texto explicativo em estilo informativo
- **Desde** - Chamada de metadados
- **Versão** - Chamada de metadados
- **Aviso** - Texto explicativo de aviso

O título opcional após os dois pontos será usado como título da frase de destaque. Se nenhum título for fornecido, o nome do tipo de texto explicativo será usado como título.

O conteúdo da frase de destaque segue imediatamente na próxima linha (não é necessária linha em branco). O conteúdo continua até uma linha em branco, a próxima chamada, um bloco de código protegido ou o final do documento.

Exemplo:

````remarcação
- Importante: Nota de Desempenho
Este algoritmo tem complexidade O(n log n).

- Exemplo: classificação rápida
Veja como implementá-lo:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

Você também pode omitir totalmente o título:

	- Aviso
	Este é um aviso sem título personalizado.

Essas frases de destaque são convertidas automaticamente para o formato de frase de destaque do Marked e estilizadas adequadamente. O tipo de texto explicativo original é preservado no atributo `data-callout`, permitindo estilo CSS personalizado, se desejado.

> Este recurso só funciona ao visualizar arquivos do Xcode Playground (`.playground`). Arquivos markdown regulares não processarão esta sintaxe.


## Índice

Você pode especificar onde no documento o Índice deve aparecer usando `<!--TOC-->`. Se estiver definido, ele substituirá a opção em Preferências e sempre será exibido na janela de visualização, bem como ao salvar e imprimir. O Índice será exibido apenas uma vez, mesmo se houver vários especificadores `<!--TOC-->` no conteúdo.

Se você adicionar `max#` à tag acima (onde # é um dígito de 1 a 5), ​​ele controlará a profundidade do Índice exibido. Por exemplo, `<!--TOC max2-->` exibirá apenas cabeçalhos de primeiro e segundo nível na lista. Você também pode especificar um nível mínimo de cabeçalho com `<!--TOC min2-->`. Os máximos e mínimos são baseados nos níveis reais do título, não nos níveis de aninhamento. Máximo e mínimo podem ser usados ​​juntos.

Marked também reconhece o estilo MultiMarkdown `{{TOC}}` e o estilo Pandoc `{{TOC:2-6}}`, onde `2-6` é o intervalo de níveis mínimo e máximo de cabeçalhos a serem incluídos.

Por padrão, o Índice será impresso na primeira página do documento se "Imprimir Índice" estiver habilitado em {% prefspane Export %}. Se existir um marcador no documento, ele será colocado nesse ponto.

I> Você pode especificar o tipo de numeração ou letras de cada nível de uma hierarquia de índice aninhado em {% prefspane Export %}.

## Quebras de página

Você pode forçar uma quebra de página para saída impressa/PDF usando a sintaxe:

```html
<!--BREAK-->
```

Coloque o token sozinho em uma linha e ele gerará uma marcação que forçará uma nova página naquele ponto. Marked também entende o formato Leanpub:

	{::pagebreak /}

## A rolagem automática pausa [pausa]

Marked pode funcionar como um Teleprompter usando o recurso [Autoscroll](Autoscroll.html) (você deve adicionar o [estilo Teleprompter](https://markedapp.com/styles/preview?style=teleprompter)). Ao fazer isso, pode ser útil incluir pausas no documento. Faça isso usando:

```html
<!--PAUSE:X-->
```

Onde `X` é o número de segundos durante os quais Marcado deve pausar. Portanto, inserir `<!--PAUSE:15-->` proporcionaria uma pausa de 15 segundos quando esse ponto do documento atingir o meio da tela.

## Arquivo inclui

O conteúdo de arquivos adicionais pode ser inserido usando a sintaxe:

	<<[pasta/nome do arquivo]

O caminho para o arquivo pode ser relativo ao arquivo de índice ou absoluto. As inclusões podem ser aninhadas; você pode usar essa mesma sintaxe dentro de um arquivo incluído. Se você estiver usando caminhos relativos, as inclusões em arquivos aninhados deverão ser relativas a esse arquivo. ***No entanto,*** o MultiMarkdown processará tudo com base na localização do primeiro arquivo aberto, portanto, todos os caminhos de imagem ou outras incorporações devem ser relativos ao primeiro arquivo pai, mesmo quando existirem em documentos filhos.

Os metadados MultiMarkdown e os cabeçalhos YAML são automaticamente removidos dos arquivos incluídos antes da renderização. Isso impedirá que os cabeçalhos apareçam no documento, mas esteja ciente de que metadados como "nível de cabeçalho básico" serão ignorados nos documentos incluídos.

T> Observe que ao visualizar documentos com arquivos incluídos, você pode digitar “I” (shift-i) para ver qual arquivo incluído está na área visível.

Consulte ["Documentos com vários arquivos"][ext] para obter mais informações.

[ext]: Multi-File_Documents.html

## Incluindo código

Marcado pode incluir arquivos externos como código usando uma sintaxe semelhante ao arquivo inclui acima:

	<<(pasta/nome do arquivo)

Observe os parênteses em vez dos colchetes. Para compatibilidade com a sintaxe Leanpub, Marked também reconhecerá um conjunto anterior de colchetes contendo um título, mas no momento nada é feito com ele em Marked:

	<<[Título do código](pasta/nome do arquivo)

O conteúdo do arquivo especificado será inserido dentro de um bloco de pré-código em seu documento e estará disponível para realce automático de sintaxe se estiver habilitado. Os blocos de código não podem ser aninhados e não serão processados ​​com MultiMarkdown. Os processadores personalizados ainda serão executados no bloco de pré-código criado.

## Incluindo texto ou HTML não processado

E> **Nota:** Este recurso é para usuários avançados.

Se você deseja incluir HTML bruto ou outro texto que não deve ser processado pelo MultiMarkdown (ou pelo seu processador personalizado), você pode usar chaves (`{}`) para incluir um arquivo *após* processar o resto do documento:

	<<{folder/raw_file.html}

Nenhuma sintaxe de inclusão será reconhecida nesses arquivos (sem aninhamento) e o conteúdo **bruto** do arquivo será inserido na saída HTML final. Isso é ótimo para inserir HTML sem atrapalhar o processador de texto ou ter coisas convertidas/escapadas quando você não deseja, mas tenha cuidado, pois há poucas salvaguardas para garantir que a formatação do documento seja preservada em torno do que você insere.