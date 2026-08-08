<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Quick Open fornece acesso rápido aos seus documentos abertos e arquivos recentes.

## Abrindo Abertura Rápida [opening-quick-open]

Acesse o painel Quick Open usando {% kbd shift cmd O %} ou no menu {% appmenu File, Quick Open %}. O painel aparece como uma janela flutuante acima do documento atual, permitindo alternar rapidamente entre documentos abertos ou arquivos recentes.

![Painel de abertura rápida][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Seções do documento [document-sections]

O painel Quick Open organiza documentos em seções claras:

### Abrir documentos [open-documents]

No topo da lista, você verá todos os documentos abertos no momento. Os documentos são agrupados visualmente por sua janela:

- **Janelas com guias**: documentos em janelas com guias mostram "Janela com X guias" como subtítulo, indicando quantas guias existem naquele grupo de janelas
- **Windows autônomos**: documentos em janelas individuais mostram "Janela" como legenda

Cada documento aberto exibe:
- O nome do arquivo do documento como título principal
- A janela agrupando informações como legenda
- Um ícone de documento

### Documentos recentes [recent-documents]

Abaixo dos documentos abertos, um separador “Documentos Recentes” divide a lista. A seção de documentos recentes mostra até 10 dos arquivos abertos mais recentemente que não estão abertos no momento. Cada documento recente exibe:

- O nome do arquivo do documento como título principal
- "Recente" como legenda
- Um ícone de documento

### Abrir outro [open-other]

No final da lista, a opção “Abrir outro…” permite abrir o seletor de arquivos padrão do macOS para selecionar qualquer arquivo. Esta opção exibe:

- "Open Other…" como título principal
- "Abrir um arquivo ou pasta" como legenda
- Um ícone de pasta

## Pesquisa e filtro [search-and-filter]

Digite no campo de pesquisa na parte superior do painel para filtrar a lista em tempo real. A pesquisa corresponde a:

- Nomes de arquivos de documentos
- Caminhos completos de arquivos

À medida que você digita, a lista é atualizada imediatamente para mostrar apenas os documentos correspondentes. A opção "Abrir outro..." permanece sempre visível na parte inferior dos resultados filtrados.

## Navegação pelo teclado [keyboard-navigation]

Navegue no painel Quick Open inteiramente com o teclado:

- **↑/↓ Teclas de seta**: Mover para cima e para baixo na lista
- **Retornar**: Abra o documento ou opção selecionada
- **Escape**: feche o painel Quick Open
- **Comando (⌘)**: Segure para revelar os caminhos dos arquivos (veja abaixo)

## Visualizando caminhos de arquivos [viewing-file-paths]

Mantenha pressionada a tecla **Command (⌘)** enquanto o painel Quick Open estiver aberto para ver o caminho completo do arquivo de cada documento na área de legenda. Os caminhos em seu diretório inicial são exibidos usando a abreviatura `~` (por exemplo, `~/Documents/file.md`). Solte a tecla Command para retornar à visualização normal mostrando o agrupamento de janelas ou informações "Recentes".

Isso é particularmente útil quando você tem vários arquivos com o mesmo nome abertos ou quando precisa verificar a localização exata de um documento.

## Abrindo Documentos [opening-documents]

- **Documentos abertos**: selecionar um documento aberto traz sua janela para o primeiro plano e alterna para a guia desse documento se ele estiver em uma janela com guias
- **Documentos recentes**: selecionar um documento recente abre-o em uma nova janela ou adiciona-o como uma guia (dependendo da sua preferência "Abrir documentos em guias" em {% prefspane General %})
- **Abrir outro...**: selecionar esta opção abre a caixa de diálogo padrão do seletor de arquivos do macOS