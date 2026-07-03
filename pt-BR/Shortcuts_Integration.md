<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado inclui ações nativas de **atalhos** (App Intents) para abrir arquivos, alterar estilos de visualização e exportar documentos. Essas ações aparecem no aplicativo Atalhos quando você pesquisa **Marcado** e estão disponíveis no **macOS 13 (Ventura)** ou posterior.

Para automação baseada em script com um modelo de objeto completo, consulte [Suporte AppleScript](AppleScript_Support.html). Para fluxos de trabalho baseados em URL do shell, consulte [Manipulador de URL](URL_Handler.html).

## Encontrando ações

1. Abra o aplicativo **Atalhos**.
2. Crie um novo atalho ou edite um existente.
3. Pesquise na biblioteca de ações por **Marcado**.

As ações estão agrupadas em **Documentos** e **Exportar**. Marcado também registra frases da Siri como “Exportar arquivo com Marcado” e “Abrir em Marcado” para atalhos rápidos.

## Visão geral das ações

| Ação | Finalidade |
| --- | --- |
| **Abrir arquivo em Marcado** | Abra um Markdown ou arquivo de texto em uma janela de visualização. |
| **Definir estilo de visualização** | Altere o tema de visualização de um documento aberto (ou abra um arquivo primeiro). |
| **Abrir e exportar arquivo** | Abra um arquivo e exporte-o para outro formato. |
| **Documento de exportação** | Exporte um documento aberto (janela frontal ou um arquivo específico). |
| **Exportar documentos abertos** | Exporte todos os documentos atualmente abertos no Marked. |

Todas as ações de exportação retornam o arquivo (ou arquivos) exportado como saída de Atalhos **Arquivo** para que você possa passá-los para a próxima etapa (Mail, Finder, outro aplicativo).

## Abrir arquivo marcado

**Parâmetro:** **Arquivo** – o documento a ser aberto (no Finder, no Share Sheet ou em uma etapa anterior de atalhos).

Marcado abre o arquivo em uma janela de visualização. Use isto quando quiser visualizar ou editar em Marcado antes de fazer qualquer outra coisa.

## Definir estilo de visualização

**Parâmetros:**

- **Estilo** – pré-visualiza o estilo a partir de um seletor (mesmos nomes do menu de estilo de pré-visualização e do Gerenciador de estilos).
- **Arquivo** (opcional) – um arquivo específico. Se omitido, Marcado utiliza o documento frontal. Se o arquivo ainda não estiver aberto, Marcado o abrirá primeiro.

Definir um estilo recarrega a visualização com esse tema (o mesmo que escolher um estilo no menu de estilos de visualização).

## Exportar ações

As ações de exportação compartilham as mesmas opções principais:

| Parâmetro | Descrição |
| --- | --- |
| **Formato** | Markdown, HTML, PDF paginado, PDF contínuo, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack ou OPML. |
| **Perfil** (opcional) | Um perfil de exportação salvo de {% prefspane Export %}. |
| **Estilo** (opcional) | Estilo de visualização a ser aplicado antes da exportação (recarregamento da visualização completa). |
| **Tamanho da página** (opcional) | Imprima o nome do tamanho da página, como `A4` ou `Letter`. |
| **Margens** (opcional) | Abreviação de margem (veja abaixo). |
| **Tamanho da fonte** (opcional) | Tamanho base da fonte em pontos para exportação de PDF, como `14` ou `12pt`. |
| **Arquivo de saída** / **Pasta de saída** (opcional) | Caminho de destino. Se omitido, Marcado grava ao lado do arquivo de origem usando a extensão correta. |

**Notas**

- **PDF paginado** usa o mesmo pipeline de layout de impressão que {% appmenu File, Export As, Save PDF (Paginated) %}. Não está disponível para documentos de visualização HTML brutos.
- A exportação **HTML** usa a visualização renderizada (o que você vê no WebView), não o arquivo de origem Markdown bruto.
- **PDF contínuo** captura o layout WebView de visualização atual.
- **Tamanho da fonte** ativa a mesma opção de tamanho de fonte de exportação/impressão personalizada de {% prefspane Export %}. Isso não afeta os documentos do Fountain.

### Abrir e exportar arquivo

Melhor para fluxos de trabalho do Finder: escolha um arquivo Markdown, abra-o em Marcado e exporte em uma única etapa.

**Parâmetros:** **Arquivo** (obrigatório), mais as opções de exportação acima.

Exemplo de uso: uma ação rápida que pega arquivos do Finder e exporta **PDF paginado** com perfil e estilo escolhidos.

### Exportar Documento

Exporte um documento que **já está aberto** em Marcado.

**Parâmetros:**

- **Arquivo** (opcional) – um arquivo aberto específico. Se omitido, Marcado exporta o documento inicial.
- Opções de exportação e **Arquivo de saída** como acima.

Use isto quando Marcado já estiver em execução e você quiser exportar a visualização atual sem reabrir o arquivo.

### Exportar documentos abertos

Exporte **todos** documentos de visualização atualmente abertos no Marked.

**Parâmetros:**

- **Formato** e opções de exportação (perfil, estilo, tamanho da página, margens, tamanho da fonte).
- **Pasta de saída** (opcional) – diretório para arquivos exportados. Se omitido, cada arquivo será exportado junto com seu documento de origem.

Útil para exportação em lote após revisar vários capítulos ou notas em Marcado.

## Abreviação de margem

Quando **Margens** estiver definido em uma ação de exportação, use uma string com uma a quatro medidas. Unidades: `in`, `cm`, `mm`, `pt` ou `"` para polegadas. Um número sem unidade é tratado como pontos.

| Valor | Significado |
| --- | --- |
| `1in` | Todos os lados |
| `1in 2in` | Superior e inferior `1in`, esquerda e direita `2in` |
| `1in 2in 1in` | Superior `1in`, esquerda e direita `2in`, inferior `1in` |
| `1in 2in 1in 2in` | Superior, direita, inferior, esquerda |

Isso corresponde à chave `margins` nos registros de exportação [AppleScript](AppleScript_Support.html#with-options-properties-record).

## Exemplos de fluxos de trabalho

### Arquivo do Finder para PDF

1. **Abrir e exportar arquivo**
2. **Arquivo** – entrada da planilha de compartilhamento ou da ação rápida do Finder.
3. **Formato** -- PDF paginado.
4. **Estilo** – tema opcional (por exemplo Amblin).
5. **Perfil** – perfil de exportação salvo opcional.
6. **Arquivo de saída** -- opcional; deixe em branco para escrever `filename.pdf` próximo à fonte.

### Exportar o que está aberto no Marked

1. **Documento de exportação**
2. Deixe **Arquivo** vazio para usar a janela frontal.
3. Escolha **Formato** e perfil ou estilo opcional.

### Exportação em lote de documentos abertos

1. **Exportar documentos abertos**
2. Escolha **Formato** (por exemplo EPUB).
3. Opcionalmente, defina **Pasta de Saída** para coletar todas as exportações em um diretório.

### Estilo e depois exportar (duas etapas)

1. **Definir estilo de visualização** - escolha um estilo (opcionalmente, direcione um **Arquivo** específico).
2. **Exportar Documento** – mesmo arquivo ou documento frontal, com o **Formato** desejado.

Você também pode passar **Style** diretamente em uma ação de exportação; Marcado aplica o tema e aguarda o recarregamento da visualização antes de exportar.

## Exportar caminhos e sandbox

- Se **Arquivo de Saída** ou **Pasta de Saída** for omitido, Marcado grava ao lado do documento de origem.
- Marcado pode criar pastas intermediárias quando o caminho de exportação estiver **dentro da pasta do documento aberto**.
- As exportações fora da pasta do documento exigem um caminho gravável que Marcado pode acessar (local do documento salvo, marcadores com escopo de segurança ou pastas que você concedeu por meio de caixas de diálogo Abrir).

Consulte [Suporte AppleScript](AppleScript_Support.html#export-paths-and-sandboxing) para obter as mesmas regras de sandbox.

## Legado `convert_to` ação

O dicionário AppleScript ainda expõe **`convert_to`** para converter texto ou arquivos Markdown sem uma visualização aberta. As ações de atalhos nativos acima são preferidas: eles abrem documentos corretamente, aguardam o carregamento da visualização e suportam exportação de PDF paginado de forma assíncrona.

Consulte [Atalhos e `convert_to` no Suporte AppleScript](AppleScript_Support.html#shortcuts-and-convert_to) para obter detalhes sobre o comando legado.

## Solução de problemas: ações não aparecem nos atalhos

Índices de atalhos **um** Instalação marcada por identificador de pacote (`com.brettterpstra.marked`). Ele prefere a cópia com o **número de compilação mais alto** (`CFBundleVersion`), não necessariamente o aplicativo que você acabou de criar no Xcode.

Se Marcado não aparecer em **Aplicativos** na biblioteca de ações do Atalhos:

1. Liste todas as cópias no disco:
   ```bash
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Remova ou renomeie cópias obsoletas (por exemplo, um `Marked.app` antigo na área de trabalho ou em `/Applications` que foi copiado de uma compilação **sem** metadados de atalhos).
3. Execute a compilação que você deseja que os atalhos usem (Xcode **Run** ou abra `.app` em DerivedData diretamente).
4. Saia e reabra o aplicativo **Atalhos**.

Uma compilação que inclui atalhos contém `Contents/Resources/Metadata.appintents`. Você pode verificar:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

Na inicialização, logs marcados `[MKShortcuts] Registering App Intents` em Console.app quando o registro é executado (macOS 13+).

## Depuração

Ative o **modo de depuração** em {% prefspane Advanced %}. Etapas de exportação de logs marcados no nível de informações com o prefixo `[AppleScript]` no Console.app e no visualizador de logs de Marked (o pipeline de exportação é compartilhado com AppleScript).

## Erros

Mensagens comuns quando uma ação falha:

- Nenhum documento marcado está disponível (nada aberto e nenhum arquivo especificado).
- Esse arquivo não está aberto em Marcado (use **Abrir Arquivo** ou **Abrir e Exportar Arquivo**).
- Perfil de exportação ou nome de estilo de visualização desconhecido.
- Tempo limite esgotado aguardando a visualização carregar ou recarregar.
- Erros de permissão de caminho de exportação ou falha na geração de PDF paginado.