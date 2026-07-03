<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A ferramenta de linha de comando `mk` fornece acesso fácil aos recursos do Marked a partir do terminal, permitindo automação do fluxo de trabalho e integração com scripts de shell e outras ferramentas de linha de comando.

## Instalação

A maneira recomendada de instalar `mk` é com Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Se você não usa Homebrew, baixe e instale o pacote assinado:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

Após baixar `mk.pkg`, clique duas vezes nele e siga as instruções do instalador.

## Uso Básico

### Abrindo arquivos

Abra um arquivo markdown em Marcado na linha de comando:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Transmissão de conteúdo do STDIN

Transmita conteúdo diretamente para a visualização de streaming do Marked:

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

A janela Streaming Preview será aberta e exibirá o conteúdo em tempo real à medida que é transmitido por outros comandos.

## Referência de comando

### Operações de arquivo

**`mk [file]`** — Abra um arquivo markdown em Marked

**`mk [file] --raise`** — Abra o arquivo e eleve a janela acima de todas as outras

### STDIN e streaming

**`mk`** ou **`mk -`** — Leia do STDIN e abra a visualização do streaming

**`mk --stream`** — Abra a janela de visualização de streaming sem ler STDIN

### Gerenciamento de visualização

**`mk --refresh`** — Atualize a janela de visualização mais à frente

**`mk --refresh all`** — Atualize todas as janelas de visualização abertas

**`mk --refresh file.md`** — Atualize a visualização de um arquivo específico (se aberto)

### Preferências

**`mk --pref`** — Abra as preferências marcadas (página Geral)

**`mk --pref Advanced`** — Abra as preferências em uma página específica

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — Definir preferências do usuário (vários pares permitidos)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Gerenciamento de estilo

**`mk --style NAME`** — Defina o estilo de visualização para janelas abertas

**`mk --add-style FILE`** — Adicione um arquivo CSS como estilo personalizado ao Marcado

```bash
mk --add-style ~/Styles/custom.css
```

### Execução de JavaScript

**`mk --dojs "JAVASCRIPT_COMMAND"`** — Execute JavaScript na janela frontal

**`mk --dojs "SCRIPT" all`** — Execute JavaScript em todas as janelas

**`mk --dojs "SCRIPT" file.md`** — Execute JavaScript em arquivo(s) específico(s)

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Extração e importação de conteúdo

**`mk --extract URL`** — Extraia o conteúdo do URL e abra em Marked

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** — Abra a janela URL de importação (opcionalmente com URL)

**`mk --stylestealer [URL]`** — HUD do Style Stealer aberto (opcionalmente com URL)

### Comandos utilitários

**`mk --paste`** — Crie um novo documento da área de transferência

**`mk --preview TEXT`** — Visualize o texto diretamente em um novo documento

**`mk --dingus`** — Abra Markdown Dingus para testar processadores

**`mk --help`** ou **`mk -h`** — Mostrar informações de uso

**`mk --version`** ou **`mk -v`** — Mostrar informações da versão

## Exemplos

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## Integração

### Aliases de shell

Adicione ao seu `~/.zshrc` ou `~/.bash_profile`:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Roteiros

Use `mk` em scripts shell para automação:

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Fluxos de trabalho

Combine com outras ferramentas:

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

## Código aberto

A ferramenta de linha de comando `mk` é de código aberto e está disponível no GitHub:

**https://github.com/ttscoff/mk**

Você pode:
- Veja o código fonte
- Contribuir com melhorias
- Relatar problemas
- Construa a partir da fonte, se necessário

A ferramenta é escrita em Swift e pode ser compilada usando Xcode. Veja o [README](https://github.com/ttscoff/mk) para instruções de construção.

## Versão

Verifique sua versão `mk` instalada com:

```bash
mk --version
```

## Recursos relacionados

- Consulte [URL Handler](URL_Handler) para obter mais informações sobre o esquema de URL do Marked
- Consulte [Streaming Preview](Streaming_Preview) para obter detalhes sobre o recurso de visualização de streaming
- Consulte [Integração de fluxo de trabalho](Workflow_Integration) para exemplos de automação