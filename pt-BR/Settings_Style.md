# <%= @title %>

Opções em {% prefspane Style %}:

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout e tipografia [layout-and-typography]

Limitar largura do texto na visualização
: Define uma largura máxima para o corpo da visualização usando o controle deslizante (em pixels).

Hifenizar automaticamente nos parágrafos
: Permite que as palavras sejam divididas automaticamente com hifenização.

Impedir palavras viúvas em títulos e parágrafos
: Força um espaço inseparável entre as duas últimas palavras de títulos e parágrafos para impedir que uma palavra isolada passe para a linha seguinte.

Gerar aspas e pontuação tipograficamente corretas
: Usa o SmartyPants para aspas inteligentes, conversão de reticências e outros recursos tipográficos (MultiMarkdown).

Envolver marcadores de notas de rodapé em colchetes
: Se marcado, usa a formatação padrão do MultiMarkdown para marcadores de notas de rodapé ([1]). Desmarque para remover os colchetes.

Ativar Estrutura de Tópicos para extensões
: Ativa automaticamente o modo Estrutura de Tópicos para arquivos com as extensões listadas.

Usar Estilo APA
: Usa estruturas de tópicos no estilo APA em vez do formato Decimal padrão.

Estilizar blocos verbatim (código) como poesia
: Se marcado, código com indentação por tabulação, delimitado por cercas ou incluído é exibido como poesia em vez de bloco de código (sem destaque de sintaxe, com estilo especial dependendo do tema).

Permitir que os temas quebrem o texto dentro de blocos de código
: Se marcado, os temas podem causar quebra de linha dentro de blocos `pre>code`. Se desmarcado, o excesso horizontal sempre será rolável.

Sempre quebrar linha no código
: Força a quebra de linha nos blocos de código independentemente das configurações do tema (substitui o comportamento de quebra definido pelo tema).

Detectar e estilizar texto RTL
: Detecta o idioma de cada elemento do documento e aplica o estilo da direita para a esquerda (RTL) conforme necessário.

### Tema [theme]

Gerenciar Estilos
: Abre a janela do [Gerenciador de Estilos](Style_Manager.html). Adicione arquivos CSS do seu disco para que apareçam nos menus de seleção de Estilo. Use o botão `Add New Style` ou arraste arquivos CSS para esta janela. Arraste para reordenar e use as caixas de seleção para ativar ou desativar Estilos.

Mais Temas
: Abre a galeria de temas on-line para procurar e instalar estilos adicionais.

Estilo padrão
: O estilo selecionado aqui será carregado em todas as novas janelas, a menos que um [estilo específico do documento seja indicado nos metadados](Per-Document_Settings.html) (por exemplo, "Marked Style: Grump").

Monitorar alterações no CSS
: Quando ativado, o Marked observa o Estilo atual em busca de alterações no disco, o que ajuda na edição de estilos personalizados e no desenvolvimento web.

CSS adicional
: O CSS adicionado aqui é anexado após a folha de estilo normal de cada tema. É uma sobreposição parcial, não um substituto completo do tema.
: O Marked reescreve os seletores neste campo (por exemplo, regras de impressão devem usar `body.mkprinting #wrapper …`). Não há limite de tamanho nem verificação de validade --- veja [Criando CSS Personalizado](Writing_Custom_CSS.html#additional-css-settings).
: Isso se aplica a todos os documentos e todos os estilos, incluindo exportação em HTML quando os estilos estão incluídos. Se quiser aplicar CSS personalizado a documentos com base em condições, use Regras Personalizadas em {% prefspane Processor %}.

### Incluir Scripts [include-scripts]

Destaque de Sintaxe
: Ativa o [destaque de sintaxe](Syntax_Highlighting.html) do highlight.js para blocos de código. Selecione um tema no menu suspenso.
: Se **Apenas se a linguagem for especificada** estiver marcado, o destaque de sintaxe só será aplicado a blocos de código delimitados por cercas com uma linguagem especificada.

Ativar MathJax
: Carrega o [MathJax](MathJax.html) para exibir equações MathML. Escolha **Local** (incluído) ou **CDN** no menu suspenso.
: **Pacotes Adicionais** abre uma folha para incluir pacotes extras do MathJax (por exemplo, Física e Química).
: **Configuração Avançada** abre uma folha para configuração personalizada do MathJax.

Ativar KaTeX
: Carrega o [KaTeX](MathJax.html#katex) como alternativa ao MathJax. Apenas um dos dois pode ser selecionado.

Numerar equações
: Quando aplicável, o Marked adiciona numeração às equações renderizadas. Escolha **Lado Esquerdo** ou **Lado Direito** para a numeração. Se estiver usando o MathJax, você pode escolher **Somente AMS** para numerar apenas as equações AMS.

Mermaid
: Carrega o [mermaid.js](https://mermaid.js) de uma CDN para habilitar a criação de diagramas em estilo Markdown. O hook necessário para renderizar diagramas Mermaid a cada atualização do documento é incluído automaticamente.

Diagramas com pan e zoom
: Quando há diagramas Mermaid presentes, ative o zoom com {% kbd cmd %}-scroll e a movimentação (pan) clicando e arrastando.
