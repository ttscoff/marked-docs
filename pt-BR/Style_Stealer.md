<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Extraia e roube estilos de qualquer site.

## O que é o ladrão de estilo? [what-is-the-style-stealer]

O Style Stealer é uma ferramenta que permite extrair estilos CSS de qualquer site e aplicá-los aos seus documentos Markdown como [Estilos personalizados](Custom_Styles.html). É perfeito para:

- **Blogueiros** que desejam combinar o estilo de seus sites favoritos
- **Escritores** que precisam criar documentos que correspondam a uma marca ou publicação específica
- **Desenvolvedores** que desejam criar protótipos rapidamente com sistemas de design existentes
- **Qualquer pessoa** que queira capturar a aparência de qualquer site bem projetado

> O Style Stealer depende de um site relativamente bem organizado e com divisões de marcação claras. Não funcionará em todos os sites, mas deverá funcionar bem na maioria.

> Para obter os melhores resultados, insira uma página que contenha o máximo de conteúdo de texto possível. Por exemplo, para extrair estilos de um blog, abra diretamente em um artigo ou postagem, não na página de índice principal.

## Como usar o ladrão de estilo [how-to-use-the-style-stealer]

### Passo 1: Abra o Style Stealer [step-1-open-the-style-stealer]

Acesse o Style Stealer através de **Ajuda** → **Style Stealer**.

### Etapa 2: insira um URL [step-2-enter-a-url]

No campo URL, insira o endereço do site do qual deseja extrair os estilos. O Style Stealer funciona com qualquer site de acesso público. Se o site estiver atrás de um acesso pago, talvez seja necessário fazer login para poder extrair o conteúdo.

![Visualização do Style Stealer][visualização]

  [visualização]: images/style-stealer-preview.jpg @2x width=800

### Etapa 3: carregar e navegar [step-3-load-and-navigate]

Clique em **Extrair** ou pressione {% kbd return  %} para carregar o site. Depois de carregado, você pode:

- **Navegue** no site usando Command+Clique nos links
- **Passe o mouse** sobre as áreas de conteúdo para vê-las destacadas
- **Clique** na área de conteúdo principal da qual deseja extrair estilos

A área de conteúdo principal selecionada deve conter apenas títulos, parágrafos, listas, etc. Não selecione uma área de conteúdo que contenha menus, barras laterais ou outro conteúdo estranho. Freqüentemente, o título estará em um contêiner separado do conteúdo normal do parágrafo. Nestes casos, tente primeiro selecionar o menor contêiner que ainda contenha ambos. Se os resultados forem ruins, clique em **Extrair** novamente e selecione novamente apenas o contêiner que contém os parágrafos.

### Etapa 4: extrair estilos [step-4-extract-styles]

Ao clicar na área de conteúdo, os estilos que se aplicam a essa área serão extraídos. A visualização será recarregada com uma página genérica que mostra todos os elementos HTML comuns e como os estilos extraídos serão aplicados a eles.

Você pode então salvar esse estilo personalizado em sua pasta CSS personalizado para usar em qualquer documento. Clique no botão **Salvar** ou pressione {% kbd cmd S %} para salvar. O estilo será nomeado com base no domínio do URL que você inseriu.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## O que é extraído [what-gets-extracted]

O Style Stealer captura um conjunto abrangente de estilos, incluindo:

### Tipografia [typography]

- **Famílias de fontes** e tamanhos para todos os níveis de título (H1-H6)
- Estilo de **parágrafo** incluindo altura e espaçamento da linha
- **Cores do texto** e cores de fundo
- **Espessuras de fonte** e estilos (negrito, itálico, etc.)

### Layout e espaçamento [layout-and-spacing]

- **Margens e preenchimento** para todos os elementos
- **Estilos e cores de borda**
- **Cores de fundo** incluindo planos de fundo corporais para temas escuros

### Elementos interativos [interactive-elements]

- **Estilos de links** incluindo estados visitados e de foco
- **Botão** e estilo de elemento de formulário
- **Lista** estilo (marcadores, números, recuo)

### Recursos especiais [special-features]

- **Primeiro parágrafo** estilo
- Formatação **Blockquote**
- **Código** e estilo de texto pré-formatado
- **Mesa** estilo
- **Fontes personalizadas** e fontes da web

## Recursos avançados [advanced-features]

### Bloqueio de mídia [media-blocking]

O Style Stealer bloqueia automaticamente o conteúdo de mídia (vídeos, imagens, áudio) para evitar travamentos e focar no estilo do texto. Isso garante um processo de extração tranquilo, mesmo em sites com muita mídia.

### Suporte a pseudo-seletor [pseudo-selector-support]

A ferramenta captura pseudo-seletores CSS como:

- `:hover` estados para links e botões
- `:visited` estados de link
- `:first-child` estilo de parágrafo
- `::first-letter` para letras maiúsculas

### Filtragem Inteligente [smart-filtering]

O Style Stealer filtra de forma inteligente:

- Estilos de navegador padrão
- Prefixos de fornecedores desnecessários
- Regras conflitantes ou redundantes
- Estilos que tornariam o texto ilegível

### Modo de depuração [debug-mode]

Ative o modo de depuração no Style Stealer para ver o registro detalhado do processo de extração. Isso é útil para solucionar problemas ou entender quais estilos estão sendo capturados.

## Dicas para melhores resultados [tips-for-best-results]

### Escolha a área de conteúdo correta [choose-the-right-content-area]

- Clique na **área de conteúdo principal** da página, não nos cabeçalhos, barras laterais ou rodapés
- Procure a área que contém o texto do artigo, postagem do blog ou conteúdo principal
- Evite áreas com JavaScript pesado ou conteúdo dinâmico

### Lidar com temas escuros [handle-dark-themes]

O Style Stealer captura automaticamente as cores de fundo do corpo, tornando-o perfeito para extrair estilos de temas escuros. A visualização mostrará a aparência do seu conteúdo com o estilo escuro extraído.

### Considerações sobre fontes [font-considerations]

- **Fontes da Web** são capturadas e incluídas nos estilos extraídos
  - As fontes carregadas de um URL remoto (por exemplo, Google Fonts) manterão esse URL. As fontes carregadas de URLs de dados serão duplicadas na folha de estilo gerada.
- **Fontes do sistema** funcionarão normalmente em sistemas diferentes
- **O carregamento da fonte** pode demorar um pouco na visualização

### Testando seus estilos [testing-your-styles]

Depois de salvar os estilos extraídos:

1. Aplique-os a um documento de teste
2. Verifique a aparência deles com seu conteúdo real
3. Faça ajustes:
   1. Abra o {% prefspane Style %}
   2. Selecione o novo estilo na tabela Estilos personalizados
   3. Clique em Revelar para mostrar o arquivo no Finder
   4. Abra o arquivo em qualquer editor de texto simples (o TextEdit funcionará no modo de texto simples) e faça os ajustes necessários

## Solução de problemas [troubleshooting]

### O site não carrega [website-wont-load]

- Verifique se o URL está correto e acessível publicamente
- Alguns sites podem bloquear o acesso automatizado
- Experimente uma página diferente no mesmo site

### Os estilos parecem diferentes [styles-look-different]

- Os estilos extraídos são baseados no conteúdo específico selecionado
- Alguns sites usam CSS complexo que pode não ser traduzido perfeitamente
- Use CSS adicional ou edite a folha de estilo para fazer ajustes finos

### Estilos ausentes [missing-styles]

- Certifique-se de ter selecionado a área de conteúdo principal, não uma barra lateral ou cabeçalho
- Alguns estilos podem ser aplicados via JavaScript e não serão capturados
- Verifique o console de depuração para obter informações detalhadas sobre extração

## Atalhos de teclado [keyboard-shortcuts]

- {% kbd return  %} - Carregar URL para extração
- {% kbd cmd S %} - Salve o estilo extraído em um arquivo CSS de estilo personalizado
- {% kbd cmd  %}-Click - Navegue pelos links durante a visualização

## Integração com estilos personalizados [integration-with-custom-styles]

Os estilos extraídos são salvos em sua pasta CSS personalizada e podem ser:

- **Aplicado** a qualquer documento através do menu Estilo
- **Modificado** usando qualquer editor de texto
- **Compartilhado** com outras pessoas copiando o arquivo CSS
- **Combinado** com outros estilos personalizados

O Style Stealer facilita a construção de uma biblioteca de belos estilos inspirados nos sites mais bem projetados da Internet.