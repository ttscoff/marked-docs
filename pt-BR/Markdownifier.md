<!-- MT-DRAFT: machine translation; human review required -->

# Markdownifier [markdownifier]

O Markdownifier é uma ferramenta que extrai automaticamente conteúdo de páginas da web e o converte para um formato Markdown limpo. Ele processa de forma inteligente o conteúdo da web para fornecer apenas texto e estrutura significativos, filtrando anúncios, elementos de navegação e outros itens desnecessários.

![URL do Markdownify][importurl]

  [importurl]: import-url@2x.jpg width=800 class=center

## Como funciona [how-it-works]

O Markdownifier usa algoritmos avançados de extração de conteúdo para:

1. **Busque e analise** o conteúdo da página da web
2. **Identifique o artigo principal** texto e estrutura
3. **Limpe e formate** o conteúdo em Markdown adequado
4. **Filtrar** anúncios, navegação e outros elementos que não sejam de conteúdo
5. **Preservar** formatações importantes como cabeçalhos, listas e links

## Abrindo o Markdownifier [opening-the-markdownifier]

Para acessar o Markdownifier, abra {% appmenu File, New, Markdownify URL (@~k) %}. Digite o URL que deseja Markdownify e pressione Return ({% kbd return %}).

## Usando o Markdownifier [using-the-markdownifier]

### Uso Básico [basic-usage]

1. **Abra o Markdownifier** usando qualquer um dos métodos acima
2. **Insira um URL** no campo de texto
3. **Clique em "Automático"** ou pressione `Return` para extrair o conteúdo
4. O conteúdo extraído será **aberto automaticamente** em um novo documento marcado

### Seleção manual de conteúdo [manual-content-selection]

Se a extração automática não capturar o conteúdo desejado:

1. Clique no botão **"Manual"** para carregar a página em uma visualização web
2. **Navegue e role** para encontrar o conteúdo desejado
3. **Clique no botão "Extrair Conteúdo"** que aparece na página da web
4. O conteúdo selecionado será convertido para Markdown e aberto em Marked

### Integração da área de transferência [clipboard-integration]

O Markdownifier detecta automaticamente URLs na sua área de transferência quando aberto:

- Se um URL for encontrado, ele será **pré-preenchido** no campo URL
- Você ainda precisa clicar em **"Automático"** ou pressionar `Return` para processá-lo
- Isso evita o processamento acidental de URLs da área de transferência

## Processamento de conteúdo [content-processing]

### Validação automática de conteúdo [automatic-content-validation]

O Markdownifier valida de forma inteligente o conteúdo extraído para garantir que contenha texto significativo:

- **Retira metadados** (frontmatter YAML, cabeçalhos MultiMarkdown)
- **Remove definições de link** e links de estilo de referência
- **Filtra** URLs independentes e elementos de navegação
- **Compacta espaços em branco** para avaliação precisa do comprimento
- **Requer no mínimo 200 caracteres** de conteúdo real

Se o conteúdo extraído for muito curto ou parecer composto principalmente de navegação/anúncios, o Markdownifier retornará automaticamente ao modo de seleção manual.

### Formatação de conteúdo [content-formatting]

O conteúdo extraído é formatado como Markdown limpo com:

- **Link da fonte** no topo: `[source](original-url)`
- **Inserção de título H1** quando necessário
- **Listas preservadas** (ordenadas e não ordenadas)
- **Links mantidos** e formatação de ênfase
- **Parágrafos limpos** com espaçamento adequado

## Recursos de segurança [safety-features]

### Prevenção de acidentes [crash-prevention]

O Markdownifier inclui diversas medidas de segurança para evitar travamentos:

- **Bloqueia URLs problemáticos** (redes de anúncios, serviços de rastreamento, conteúdo relacionado a criptografia)
- **Filtros imagens corrompidas** que podem causar problemas de renderização
- **Desativa recursos avançados da web** que podem causar instabilidade
- **Recuperação automática de falhas** com fallback no modo de segurança

### Proteção de privacidade [privacy-protection]

- **Modo de navegação privada** evita rastreamento e cookies
- **Sem plug-ins ou execução Java** para segurança
- **JavaScript limitado** com bloqueio de API de criptografia
- **Filtragem de recursos** bloqueia rastreamento e conteúdo do anúncio

## Solução de problemas [troubleshooting]

### Conteúdo não extraído [content-not-extracted]

Se a extração automática falhar:

1. **Tente a seleção manual** usando o botão "Manual"
2. **Verifique se o site requer JavaScript** – alguns sites precisam de carregamento manual
3. **Verifique se o URL** está acessível e contém o conteúdo do artigo
4. **Procure paywalls ou requisitos de login** que possam bloquear o acesso

### Problemas de WebView [webview-issues]

Se a visualização da web ficar instável:

1. O Markdownifier **entrará automaticamente no modo de segurança**
2. **JavaScript será desativado** para evitar travamentos
3. **Use o botão "Converter"** em vez da seleção manual
4. **Feche e reabra** o Markdownifier para redefinir

### Conteúdo ausente [missing-content]

Se faltar conteúdo importante na extração:

1. O **algoritmo automático** pode ter filtrado
2. **Use a seleção manual** para escolher o conteúdo específico que você deseja
3. **Verifique o HTML de origem** para ver se o conteúdo é carregado dinamicamente
4. **Tente um URL diferente** se o site tiver uma estrutura complexa

## Dicas para melhores resultados [tips-for-best-results]

### Seleção de URL [url-selection]

- **Use URLs de artigos** em vez de páginas iniciais ou de categorias
- **Evite URLs com parâmetros de rastreamento** quando possível

### Qualidade do conteúdo [content-quality]

- **Artigos mais longos** geralmente extraem melhor do que postagens curtas
- **Conteúdo bem estruturado** com títulos adequados funciona melhor
- **Evite sites com JavaScript pesado** para extração automática

### Seleção Manual [manual-selection]

- **Aguarde a página carregar totalmente** antes de extrair
- **Percorra o conteúdo** para garantir que tudo esteja carregado
- **Passe o mouse sobre as áreas** para selecionar a menor caixa azul que contém todo o conteúdo que você deseja extrair
- **Clique** quando encontrar o conteúdo desejado

## Recursos avançados [advanced-features]

### Processamento em lote [batch-processing]

Embora o Markdownifier processe um URL por vez, você pode:

- **Enfileirar vários URLs** abrindo o Markdownifier várias vezes
- **Use a integração de serviços** para processar URLs de outros aplicativos
- **Copie o conteúdo extraído** e cole em documentos marcados existentes

### Integração com Marcado [integration-with-marked]

O conteúdo extraído abre em Marcado com:

- **Nomeação automática de arquivos** com base no título do artigo
- **Preservação do URL de origem** nos metadados do documento
- **Recursos totalmente marcados** para leitura e exportação)

## Detalhes Técnicos [technical-details]

### Tipos de conteúdo suportados [supported-content-types]

- **Artigos HTML** com marcação padrão
- **Postagens de blogs** e artigos de notícias
- **Documentação** e páginas de ajuda
- **Postagens no fórum** e conteúdo de discussão

### Limitações [limitations]

- **Sites com acesso pago** podem exigir login e extração manual
- **Sites com uso intenso de JavaScript** podem exigir seleção manual
- **Conteúdo dinâmico** carregado após o carregamento da página pode ser perdido, mas a extração manual pode capturá-lo
- **Layouts complexos** podem incluir elementos de navegação indesejados

O Markdownifier foi projetado para tornar a extração de conteúdo da web o mais simples e confiável possível, ao mesmo tempo que fornece opções de fallback para sites complexos ou problemáticos.