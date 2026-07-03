<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane Style %}:

![Configurações: Estilo][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout e tipografia

Limitar a largura do texto na visualização
: defina uma largura máxima para o corpo da visualização usando o controle deslizante (em pixels).

Hifenização automática em parágrafos
: permite que as palavras sejam quebradas com hifenização automaticamente.

Evite viúvas em manchetes e parágrafos
: força um espaço ininterrupto entre as duas últimas palavras dos títulos e dos parágrafos para evitar que palavras únicas passem para uma nova linha.

Gere citações e pontuação tipograficamente corretas
: use SmartyPants para citações inteligentes, conversão de reticências e outros recursos de tipografia (MultiMarkdown).

Coloque marcadores de notas de rodapé com colchetes
: se marcado, use a formatação MultiMarkdown padrão para marcadores de notas de rodapé ([1]). Desmarque para retirar os colchetes.

Ativar Outline para extensões
: ativa automaticamente o modo Outline para arquivos com extensões listadas.

Use o estilo APA
: use contornos de estilo APA em vez do formato decimal padrão.

Estilize blocos textuais (código) como poesia
: Se marcado, o código recuado por tabulação, cercado ou incluído é exibido como poesia em vez de um bloco de código (sem realce de sintaxe e estilo especial dependendo do tema).

Permitir que os temas envolvam texto dentro de blocos de código
: Se marcado, os temas podem causar quebra automática dentro de `pre>code` blocos. Se desmarcado, o estouro horizontal sempre rolará.

Sempre quebrar o código
: força o agrupamento dos blocos de código, independentemente das configurações do tema (substitui o comportamento do agrupamento do tema).

Detectar e estilizar texto RTL
: Detecte o idioma por elemento no documento e estilize da direita para a esquerda de acordo.

### Tema

Gerenciar estilos
: Abre a janela [Gerenciador de Estilo](Style_Manager.html). Adicione arquivos CSS da sua unidade para que apareçam nos menus do seletor de estilo. Use o botão `Add New Style` ou arraste os arquivos CSS para esta janela. Arraste para reordenar e use as caixas de seleção para ativar ou desativar Estilos.

Mais temas
: abra a galeria de temas online para navegar e instalar estilos adicionais.

Estilo padrão
: O estilo selecionado aqui será carregado para todas as novas janelas, a menos que um [estilo específico do documento seja indicado nos metadados](Per-Document_Settings.html) (por exemplo, "Estilo Marcado: Grump").

Rastreie alterações de CSS
: quando ativado, Marked observará o estilo atual em busca de alterações no disco, auxiliando na edição de estilo personalizado e no desenvolvimento web.

CSS adicional
: CSS adicionado aqui será incluído após a folha de estilo normal com todos os temas. Entre outras coisas, você pode usá-lo para substituir configurações gerais sem editar estilos internos.
: Isso se aplica a todos os documentos e estilos. Se você deseja aplicar CSS personalizado a documentos com base em condições, use Regras Personalizadas em {% prefspane Processor %}.

### Incluir scripts

Destaque de sintaxe
: Ative destaque.js [destaque de sintaxe](Syntax_Highlighting.html) para blocos de código. Selecione um tema no menu suspenso.
: Se **Somente se o idioma especificado** estiver marcado, o realce de sintaxe só será aplicado a blocos de código protegidos com um idioma especificado.

Habilitar MathJax
: Carrega [MathJax](MathJax.html) para exibir equações MathML. Escolha **Local** (empacotado) ou **CDN** no menu suspenso.
: **Pacotes Adicionais** abre uma planilha para incluir pacotes MathJax extras (por exemplo Física e Química).
: **Configuração avançada** abre uma planilha para configuração personalizada do MathJax.

Habilitar KaTeX
: Carrega [KaTeX](Mathjax.html#katex) como uma alternativa ao MathJax. Apenas um ou outro pode ser selecionado.

Equações numéricas
: Se aplicável, Marcado adicionará números de figuras às equações renderizadas. Escolha **Lado Esquerdo** ou **Lado Direito** para numeração. Se estiver usando MathJax, você pode escolher **AMS apenas** para numerar apenas equações AMS.

Sereia
: carrega [mermaid.js](https://mermaid.js) de um CDN para ativar a diagramação no estilo Markdown. O gancho necessário para renderizar diagramas Mermaid em cada atualização de documento é incluído automaticamente.

Diagramas de panorâmica e zoom
: quando diagramas Mermaid estiverem presentes, ative o zoom com {% kbd cmd %}-rolagem e panorâmica clicando e arrastando.