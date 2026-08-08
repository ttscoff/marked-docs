<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O Custom Style Generator é uma ferramenta baseada na web que permite criar estilos personalizados para Marked sem escrever CSS manualmente. Ele fornece uma interface visual com controles de tipografia, cores, espaçamento e muito mais, com uma visualização ao vivo que é atualizada conforme você faz alterações.

## Acessando o Gerador [accessing-the-generator]

O Gerador de estilo está disponível em [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/). Você pode usá-lo diretamente em seu navegador – não é necessária instalação.

![Gerador de estilo][gerador de estilo img]

  [img-style-generator]: images/style-generator-800.jpg @2x width=800 class=center

## Primeiros passos [getting-started]

Ao abrir o gerador pela primeira vez, você verá:

- **Painel de visualização** (esquerda): uma visualização ao vivo do seu estilo aplicado ao conteúdo de redução de amostra
- **Painel de controles** (à direita): todos os controles de estilo organizados em seções
- **Barra de ferramentas** (topo): título do estilo, seletor de tema base e opção de importação de CSS

### Escolhendo um tema base [choosing-a-base-theme]

Comece selecionando um **Tema Base** no menu suspenso. Isso fornece uma base para o seu estilo – você pode personalizar cada aspecto dele. As opções populares incluem Em Branco (para começar do zero), Padrão e vários temas integrados.

### Importando CSS Existente [importing-existing-css]

Se você tiver um arquivo CSS existente que gostaria de usar como ponto de partida, clique em **Importar CSS** e selecione seu arquivo. O gerador carregará esses estilos e você poderá modificá-los usando os controles.

## Controles de estilo [style-controls]

O gerador organiza os controles em seções lógicas:

### Tipografia básica [base-typography]

Controle as configurações fundamentais de tipografia:

- **Usar ritmo**: quando ativado, usa uma escala tipográfica matemática para tamanhos e espaçamentos de cabeçalho consistentes
- **Tamanho base da fonte**: o tamanho da fonte raiz (normalmente 16px)
- **Altura da Linha**: O espaçamento entre linhas de texto
- **Proporção de escala**: a proporção usada para a escala tipográfica (afeta os tamanhos dos títulos)

###Layout

Ajuste o espaçamento e o recuo:

- **Preenchimento do wrapper**: espaço ao redor da área de conteúdo
- **Recuo de parágrafo**: recuo de primeira linha para parágrafos
- **Recuo da lista**: recuo para listas
- **Blockquote Indent**: Margem esquerda para blockquotes

### Fontes [layout]

Configure famílias e pesos de fontes:

- **Fontes de cabeçalho**: lista de fontes separadas por vírgulas para títulos (por exemplo, "Geórgia, serif")
- **Body Fonts**: lista de fontes separadas por vírgulas para o corpo do texto
- **Peso do cabeçalho**: Peso da fonte para títulos (100–900)
- **Peso Corporal**: Peso da fonte para o corpo do texto
- **Espessura em negrito**: Peso da fonte para texto em negrito
- **Espaçamento entre letras**: espaçamento entre caracteres para cabeçalhos e corpo do texto

### Fontes do Google [fonts]

Adicione Google Fonts ao seu estilo:

1. Digite um nome de fonte no campo de pesquisa (aparecem sugestões de preenchimento automático)
2. Opcionalmente, especifique estilos (por exemplo, "400.400i,700" para regular, itálico, negrito)
3. Clique em **Adicionar** para incluí-lo
4. Use **Procurar Google Fonts** para explorar o catálogo completo com visualizações

As fontes adicionadas aparecem em uma lista abaixo dos controles – clique no × para removê-las.

### Cores [google-fonts]

Defina cores para vários elementos:

- **Plano de fundo**: cor de fundo da página
- **Texto Base**: Cor do texto padrão
- **Cor do cabeçalho**: cor para todos os títulos (pode ser substituída por nível de título)
- **Cor do corpo**: cor do texto do corpo
- **Cor do link**: Cor dos links
- **Cor de ênfase**: Cor para texto enfatizado (`<em>`)
- **Cor forte**: Cor para texto forte (`<strong>`)
- **Marcar fundo**: cor de fundo do texto destacado (`<mark>`)

As cores de cabeçalho individuais (H1–H6) podem ser definidas separadamente — use **Redefinir** para limpar uma substituição e retornar à cor do cabeçalho.

### Modo escuro [colors]

Ative o **Modo escuro** para visualizar e configurar as cores do modo escuro. Quando ativado, você verá controles de cores separados para variantes do modo escuro. Os estilos de modo escuro se aplicam quando `.inverted` está definido no elemento body em Marcado.

Use **Gerar cores** para criar automaticamente uma paleta de modo escuro com base nas cores do modo claro.

### Imagens [dark-mode]

Controlar a aparência da imagem:

- **Largura máxima**: largura máxima para imagens (por exemplo, "100%", "800px")
- **Border Radius**: Cantos arredondados (por exemplo, "8px", "0")
- **Alinhamento**: Padrão do documento, Esquerda, Centro ou Direita

### Citações em bloco [images]

Citações de estilo:

- **Largura da borda esquerda**: Espessura da borda esquerda
- **Cor da borda esquerda**: Cor da borda esquerda
- **Cor de fundo**: Cor de fundo para citações em bloco
- **Estilo da fonte**: Normal ou Itálico
- **Margem Esquerda**: Espaçamento da borda esquerda
- **Margem esquerda aninhada**: espaçamento para citações em bloco aninhadas (pode ser "herdado")

Controles separados estão disponíveis para citações em bloco no modo escuro.

### Listas [blockquotes]

Configurar a aparência da lista:

- **Posição do estilo de lista**: Interior ou Exterior (onde aparecem marcadores/números)
- **Margem Esquerda**: Espaçamento da borda esquerda
- **Margem esquerda aninhada**: espaçamento para listas aninhadas (pode ser "herdado")

### Listas de definições [lists]

Listas de definição de estilo (`<dl>`, `<dt>`, `<dd>`):

- **Recuo DL**: recuo geral
- Configurações de **DT** (termo): tamanho, peso e estilo da fonte
- Configurações de **DD** (definição): tamanho da fonte, peso, estilo e recuo

### Tabelas [definition-lists]

Estilo de mesa abrangente:

- **Cor de fundo**: fundo da tabela
- **Cor da borda**: cor da borda das células
- **Cor do texto da tabela**: cor padrão do texto nas tabelas
- **Linhas/colunas alternadas**: habilite listras de zebra com cores personalizadas
- **Borda**: Mostrar/ocultar o contorno da tabela
- **Grade**: Mostrar/ocultar linhas de grade internas
- **Alinhamento**: Esquerda ou Centro
- **Raio da borda**: cantos arredondados
- **Largura Máxima**: Largura máxima da tabela
- **Preenchimento celular**: espaçamento interno
- Configurações de **cabeçalho**: peso, tamanho e estilo da fonte
- Configurações de **Legenda**: Peso da fonte, tamanho, estilo e cor do texto

Controles separados estão disponíveis para tabelas no modo escuro.

### Blocos de código [tables]

Blocos de código de estilo e código embutido:

- **Família de fontes de código**: pilha de fontes monoespaçadas
- **Fundo**: Cor de fundo
- **Cor da borda**: Cor da borda
- **Raio da borda**: cantos arredondados
- **Modo Wrap**: Sem wrap (pré), Preservar + wrap (pré-wrap) ou Normal (wrap)
- **Preenchimento de código**: espaçamento interno

Controles separados estão disponíveis para blocos de código no modo escuro.

### Notas de rodapé [code-blocks]

Notas de rodapé de estilo:

- **Cor do marcador**: cor dos marcadores de notas de rodapé
- **Cor do texto**: cor do texto da nota de rodapé
- **Estilo da fonte do texto**: Normal ou Itálico

Controles separados estão disponíveis para notas de rodapé no modo escuro.

### Sombra projetada [footnotes]

Adicione sombras projetadas aos elementos:

1. Escolha a sombra **Força**: Suave, Média ou Forte
2. Selecione em quais elementos aplicar sombras:
   - Imagens
   - Blocos de código
   - Citações em bloco
   - Tabelas

##CSS personalizado

Para personalização avançada além dos controles disponíveis, use o botão **CSS personalizado** para abrir um editor de código. Qualquer CSS que você adicionar aqui será anexado ao estilo gerado e automaticamente definido para funcionar dentro da estrutura do documento do Marked.

O editor inclui destaque e validação de sintaxe – CSS inválido será sinalizado com mensagens de erro.

## Visualização ao vivo [custom-css]

O painel de visualização mostra seu estilo aplicado ao conteúdo de markdown de amostra, incluindo:

- Títulos (H1–H6)
- Parágrafos com várias formatações embutidas
- Tabelas
- Blocos de código
- Imagens
- Listas (ordenadas e não ordenadas)
- Citações em bloco
- Listas de definição
- Notas de rodapé
- Listas de tarefas

As alterações são atualizadas em tempo real conforme você ajusta os controles.

## Salvando e compartilhando [live-preview]

Quando estiver satisfeito com seu estilo, você terá várias opções:

### Ver CSS

Clique em **Ver CSS** para ver o CSS gerado completo em um popover. Você pode copiá-lo para a área de transferência ou revisá-lo antes de salvá-lo.

### Salvar CSS

Clique em **Salvar CSS** para baixar seu estilo como um arquivo CSS. Você será solicitado a inserir metadados (título, autor, descrição) antes de fazer o download.

### Adicionar aos Marcados

Clique em **Adicionar ao Marcado** para adicionar diretamente o estilo à sua instalação Marcada. Isso requer que o Marked esteja em execução e abrirá uma caixa de diálogo para confirmar o nome do estilo e as informações do autor.

### Compartilhar estilo

Clique em **Compartilhar estilo** para publicar seu estilo na [Galeria de estilos marcados](https://markedapp.com/styles) para que outras pessoas possam usá-lo. Você precisará fornecer:

- Título do estilo
- Seu nome
- URL do autor (opcional)
- Descrição
- Nota (opcional)

Uma prévia do seu estilo aparecerá na caixa de diálogo de compartilhamento antes de publicar.

## Metadados [saving-and-sharing]

Use a seção de metadados (expansível por meio do botão de seta próximo ao título do estilo) para definir:

- **Autor**: Seu nome (persiste em todas as sessões)
- **URL do autor**: URL do seu site ou perfil
- **Descrição**: Uma descrição do estilo
- **Nota**: Notas adicionais (não incluídas em estilos compartilhados)

Esses metadados são incluídos no cabeçalho do arquivo CSS e usados ao compartilhar estilos.

## Dicas [metadata]

- Comece com um tema base próximo ao que você deseja e depois personalize
- Use o tema **Em branco** se quiser controle total do zero
- Ative o **Ritmo** para uma tipografia matematicamente consistente
- Teste seu estilo com o botão **Modo Escuro** se você planeja apoiá-lo
- Use **CSS personalizado** com moderação — a maioria das necessidades pode ser atendida com os controles integrados
- Visualize seu estilo com vários tipos de conteúdo antes de compartilhar

## Compatibilidade do navegador [tips]

O Style Generator funciona melhor em navegadores modernos (Chrome, Firefox, Safari, Edge). Requer que o JavaScript esteja ativado.