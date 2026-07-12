<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Capturando palavreado problemático e destacando frases importantes.

## Destacando palavras-chave

O destaque de palavras-chave em Marcado permite capturar frases comuns que você pode querer evitar, encontrar termos alternativos ou apenas destacar para fins gerais. A lista de palavras-chave usadas para corresponder a cada categoria pode ser editada em {% prefspane Proofing %}.

Ative o realce com {% kbd shift cmd H %}, no menu de engrenagem ({% appmenu {{gear}}, Highlight Keywords %}), ou abra a gaveta de palavras-chave usando o ícone de realce no canto inferior esquerdo (próximo ao menu de engrenagem). A gaveta também pode ser aberta com o atalho de teclado {% kbd shift cmd K %}. O realce é ativado automaticamente quando a gaveta é aberta e pode ser ativado e desativado com o interruptor no lado esquerdo da gaveta.

## A gaveta de palavras-chave

![Gaveta de palavras-chave][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

A gaveta de palavras-chave revelada ao ativar o destaque fornece acesso rápido às opções de destaque, incluindo a capacidade de ativar e desativar tipos de destaque individuais. A linha vertical de rótulos coloridos no lado esquerdo corresponde aos destaques do texto. Clicar em um rótulo alterna os destaques desse tipo de palavra-chave.

À esquerda de cada rótulo há um ícone de alvo. Clicar aqui começará a rolar o documento para a próxima instância do destaque na ordem do documento. À direita do rótulo há uma contagem que mostra o número total de destaques para esse tipo.

Você pode navegar rapidamente pelos destaques usando o teclado. Digitar `[` e `]` irá inicialmente avançar e retroceder em todos os destaques. Se você clicar em um ícone de destino, `[` e `]` passarão a navegar apenas nesse tipo de destaque. `{` (Shift-[) e `}` (Shift-]) sempre navegarão por todos os destaques, independentemente do último alvo clicado.

Se uma palavra ou frase destacada for clicada, esse tipo se tornará o alvo da navegação e usar `[` ou `]` navegará a partir desse ponto no documento.

## Editando palavras-chave

![Configurações de revisão][preferências de prova]

  [proofprefs]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane

Por padrão, Marked usa a lista de palavras e frases usadas em demasia da [Campanha em inglês simples](http://www.plainenglish.co.uk). Você pode adicioná-los ou substituí-los facilmente editando-os em {% prefspane Proofing %}. Cada campo é um texto de formato livre e cada linha é interpretada como uma frase de pesquisa. Use `*` no início de uma frase ou palavra para corresponder a qualquer texto anterior e `?` para corresponder a um único caractere como curinga.

Expressões regulares podem ser usadas cercando a expressão com barras:

    /\\S*?ly/

O texto acima corresponderá a quaisquer palavras que terminem em "ly" para destaque. A sintaxe para expressões regulares no destaque de palavras-chave de Marked é [igual ao JavaScript](http://www.regular-expressions.info/javascript.html).

## Palavras-chave temporárias

Você também pode adicionar palavras-chave temporárias na gaveta de palavras-chave editando o bloco de notas. Assim como nos campos {% prefspane Proofing %}, você adiciona uma palavra-chave ou frase por linha, expressões regulares permitidas (cercadas por barras). Após editar palavras-chave temporárias, clique no botão "Atualizar" (ou pressione {% kbd cmd return  %}) para salvar as alterações e vê-las destacadas em seu documento.

Expressões regulares também funcionam no campo de palavras-chave temporárias, apenas coloque o texto com barras (`/my expression\b/`).

Palavras-chave temporárias destinam-se a situações em que a densidade de palavras-chave é importante e permitem ver rapidamente quantas vezes você usou as palavras-alvo, destacando suas localizações no documento. Uma contagem de correspondências para as palavras-chave temporárias é exibida em destaque na gaveta.

Consulte também o comando ["Visualize Word Repetition"][wordrep] para encontrar palavras usadas em excesso em seu texto.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Voz Passiva

Marcado indicará o uso de "voz passiva" no texto em inglês. Conforme [definido pela Wikipedia][passivo]:

> o sujeito gramatical expressa o tema ou paciente do verbo principal – ou seja, a pessoa ou coisa que sofre a ação ou tem seu estado alterado.

A voz passiva não é má, como você pode ler sobre [nas postagens do linguista Geoffrey K. Pullum] [gkp]. Marcado aponta passagens usando voz passiva, mas a decisão quanto à sua validade é sua.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Palavras duplicadas

Palavras duplas (por exemplo, "o o") são automaticamente destacadas em laranja quando o Destaque de palavras-chave está ativado. Atualmente, isso não é configurável, mas deve ser útil para revisão.