<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Fonte](http://fountain.io/) é uma linguagem de marcação de texto especializada projetada para escrever roteiros. Roteiristas que escrevem usando a sintaxe do Fountain podem usar Marcado para visualizar seu trabalho. 

Abrir qualquer arquivo com extensão “.fountain” ativará automaticamente o suporte do Fountain para a janela. Uma folha de estilo Fountain padrão será aplicada para visualização e exportação.

Você pode forçar qualquer documento a ser processado como Markdown abrindo o menu de engrenagem no canto inferior direito da janela de visualização e selecionando **Processar como Fountain**.

Os cabeçalhos das seções e cenas aparecerão no Índice para navegação rápida em seu roteiro.

## Roteiros [scrippets]

Você também pode usar "scriptpets" em um documento normal para que seções individuais sejam processadas e estilizadas com Fountain. Simplesmente coloque sua marcação Fountain dentro do documento principal com tags `[scrippet]`:

    [roteiro]
    O texto do seu roteiro...
    [/script]

Você também pode usar tags de estilo marcado padrão:

    <!--SCRIPPET-->
    O texto do seu roteiro...
    <!--/SCRIPPET-->