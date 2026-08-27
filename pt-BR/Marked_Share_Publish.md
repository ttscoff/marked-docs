<!-- MT draft for pt-BR — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** é o serviço de publicação online da Marked em [share.markedapp.com](https://share.markedapp.com). Conecte seu Mac uma vez e publique o documento frontal como um * *TextPack** com imagens e destaques opcionais do Modo de Leitura. Qualquer pessoa com o link pode visualizar o documento na web.

Este recurso é separado da * * Extensão de compartilhamento * * do macOS (menu Compartilhamento do sistema). Consulte [Using the Share Extension](Share_Extension.html) para enviar ficheiros ou seleções para Marcado a partir de outras aplicações.

## Associe a sua conta [connect-your-account]

Antes da sua primeira publicação, conecte-se Marcado à sua conta do Share:

1. Escolha {% appmenu Arquivo, Publicar, Conectar conta… %}.
2. Marcado abre o seu navegador predefinido para iniciar sessão em share.markedapp.com.
3. Depois de aprovar a ligação, o navegador volta a Marcado com um link de início de sessão seguro. Confirme o rótulo da conta mostrado na caixa de diálogo.

Marcado armazena o token da API e a chave do dispositivo no Chaveiro do macOS neste Mac. As credenciais não são gravadas em logs ou relatórios de falhas.

Para desligar, escolha {% appmenu Arquivo, Publicar, Desconectar conta… %}. Os documentos publicados permanecem online; revogue o acesso a qualquer momento em share.markedapp.com, se necessário.

## Publique um documento [publish-a-document]

Com um documento aberto na pré-visualização, escolha {% appmenu Arquivo, Publicar, Publicar… %}.

Na primeira vez que você publica um documento, Marked mostra uma pequena folha de opções:

- **Título** — mostrado no Compartilhamento (o padrão é o nome do documento sem sua extensão).
- **Visibilidade** — Privado, Não Anunciado ou Público. Novas publicações padrão para **Não anunciado** (acessível por link, não listado publicamente).
- **Incluir destaques e comentários** — incorpora destaques do Modo de Leitura no TextPack. O padrão é em quando o documento tem destaques.
- **Permitir que outros remixem** — quando ativado, os visualizadores podem bifurcar o documento no Compartilhar.

Marcado cria um TextPack em segundo plano (Markdown, assets e ⟦P0 opcional⟧), carrega-o e grava o URL de partilha neste Mac.

### Atualizar uma publicação existente [update-an-existing-publish]

Depois que um documento é vinculado ao Compartilhar, o item de menu lê **Atualizar documento publicado ** em vez de **Publicar…**. Escolha-o para carregar uma nova versão do TextPack. Marcado envia o hash de conteúdo do servidor para que edições simultâneas de outro Mac ou da web sejam detectadas.

Se outra pessoa atualizou o documento no Share primeiro, Marked pergunta se deve **Substituir** com a versão deste Mac, **Abrir na Web** ou **Cancelar**.

## Depois de publicar [after-publishing]

Quando uma publicação termina, a Marked confirma o sucesso e oferece:

- **Copiar link de compartilhamento ** — {% appmenu Arquivo, Publicar, Copiar link do Share %}
- **Abrir na Web** — {% appmenu Arquivo, Publicar, Abrir na web %}

Esses comandos se aplicam ao documento frontal quando ele tem um registro de publicação vinculado.

## Janela Documentos publicados [published-documents-window]

Escolha {% appmenu Arquivo, Publicar, Documentos publicados… %} para abrir uma lista de documentos publicados a partir deste Mac e sincronizados a partir da sua conta Share.

Para cada entrada, você pode:

- **Abrir** o arquivo local quando Marcado ainda tem um link para ele no disco.
- **Importar** um TextPack quando não houver nenhum arquivo local (salve-o em qualquer lugar e abra-o em Marcado).
- **Abrir na Web** ou **Copiar link** para o URL de compartilhamento.
- **Revelar no Finder** quando um caminho local for conhecido.
- **Esquecer** remove o registro deste Mac sem excluir o documento online.

A lista é atualizada a partir de Partilhar quando está ligado. Se estiver offline ou desligado, Marked mostra registos em cache e pode pedir-lhe para voltar a ligar.

## O que pode publicar [what-you-can-publish]

Você pode publicar qualquer documento que Marked possa renderizar, incluindo:

- Markdown e ficheiros de texto guardados
- Visualizações transitórias (área de transferência, streaming ou documentos não salvos)
- TextBundles e outros formatos suportados

Apenas uma operação de publicação é executada de cada vez por janela de documento; o item de menu é desativado enquanto um carregamento está em andamento.

## Dicas [tips]

- A publicação inclui imagens referenciadas pela visualização. Pacotes muito grandes podem ser rejeitados antes do upload; reduza os ativos incorporados se atingir um limite de tamanho.
- Os destaques exportados no TextPack utilizam o formato JSON de destaque da Marked. Consulte [Reading Mode](Reading_Mode.html) para criar e exportar destaques.
- O Marked Share está disponível nas versões Direct, Mac App Store, Setapp e Marked Pro. Nenhuma assinatura separada é necessária para publicar.
