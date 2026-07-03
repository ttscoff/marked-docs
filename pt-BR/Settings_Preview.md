<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane Preview %}:

![Configurações: Visualização][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Comportamento de visualização

Ativar navegação no minimapa
: Gere um mapa visual do documento que aparece quando "0" é pressionado. Pode causar pequenos atrasos ao renderizar documentos grandes.

Manchetes recolhem seções
: clicar em um elemento de título recolhe a seção entre ele e o próximo título.

Requer {% kbd cmd %}‑clique
: se esta opção estiver marcada, os títulos só serão recolhidos/expandidos quando clicados com a tecla Command pressionada.

Visualização de sincronização e rolagem de origem
: quando seu editor suportar, mantenha a visualização rolada para corresponder ao local correspondente no documento de origem.

Sincronize a leitura rápida com a posição de rolagem
: Mantenha a sobreposição [Leitura rápida](Speed_Reading.html) alinhada com a posição de rolagem da visualização. Você também pode alternar isso na sobreposição de leitura rápida.

### Role para editar

Role para editar
: Ao atualizar a visualização, Marcado pode determinar o primeiro ponto onde o documento foi alterado e rolar automaticamente até ele. Isso mantém a visualização sincronizada com sua localização atual no documento que você está editando. O marcador de edição mais recente é a primeira diferença no documento desde a última atualização. Ativar "Ordem reversa de comparação" considerará a última diferença no documento (de cima para baixo) como a edição mais recente.

Mostrar marcador de edição mais recente
: Um pequeno marcador vermelho aparece no ponto da primeira edição detectada. Desligue isso para torná-lo invisível. (Requer **Role para editar**.)

Mostrar todos os marcadores de comparação
: Se estiver habilitado, todas as diferenças entre a última atualização e o conteúdo atual serão destacadas na medianiz. Você pode navegar pelas edições, rolando-as até o meio da visualização, usando <kbd>e</kbd> (avançar) e {% kbd shift E %} (retroceder).

Ordem de diferença reversa
: Se estiver habilitado, as diferenças serão marcadas na ordem inversa (de baixo para cima). Isso afeta a navegação, então <kbd>e</kbd> navegará para cima e {% kbd shift E %} navegará para baixo. A “edição mais recente” se tornará a última diferença no documento.

### Recursos adicionais

O índice rastreia a posição de rolagem
: Índice destaca a seção atual.

Estatísticas pop-up para seleção de texto
: mostra um pop-up de contagem de palavras para o texto selecionado sempre que uma seleção é feita.

Habilitar popovers de link
: mostra um menu pop-up quando links externos são clicados e mantidos pressionados antes de serem liberados.

Validar URLs automaticamente na atualização
: valide URLs no carregamento e atualização de documentos. Exibe resultados apenas se houver erros.
: Isto executa [validação de link](Link_Validation.html) toda vez que o documento é atualizado (se você tiver um número significativo de links, este pode ser um processo lento e deve ser evitado).

### Links Wiki

Converter [[Links Wiki]]
: Habilite a [navegação wiki](Wiki_Navigation.html) de Marked para a sintaxe `[[wiki link]]`.

Extensão padrão
: A extensão de nome de arquivo Marked é usada ao resolver links wiki que não incluem uma extensão (por exemplo, `md`).

### Aparência

Modo escuro
: Exibe todas as janelas no modo "Alto Contraste", com cromo escuro e, se disponível, a versão invertida do Estilo atual (pode não se aplicar a Estilos Personalizados).

Configuração do sistema de correspondência
: alterne o modo escuro automaticamente quando o modo escuro do macOS estiver ativado ou desativado em todo o sistema.

Mostrar caminho completo no título da janela
: Quando ativado, Marcado exibirá o caminho completo para o documento atual no título da janela.