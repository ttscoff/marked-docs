<!-- MT draft for pt-BR — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** é o serviço de publicação online de Marked em [share.markedapp.com](https://share.markedapp.com). Conecte seu Mac uma vez e publique o documento inicial como **TextPack** com imagens e destaques opcionais no modo de leitura. Qualquer pessoa com o link pode visualizar o documento na web.

Este recurso é separado da **extensão Compartilhar** do macOS (menu Compartilhar do sistema). Consulte [Using the Share Extension](Share_Extension.html) para enviar arquivos ou seleções para Marked de outros aplicativos.

## Conecte sua conta [connect-your-account]

Antes de sua primeira publicação, conecte Marked à sua conta Share:

1. Escolha {% appmenu Arquivo, Publicar, Conectar conta… %}.
2. Marked abre seu navegador padrão para fazer login em share.markedapp.com.
3. Depois de aprovar a conexão, o navegador retorna para Marked com um link de login seguro. Confirme o rótulo da conta mostrado na caixa de diálogo.

Marked armazena o token API e a chave do dispositivo no macOS Keychain neste Mac. As credenciais não são gravadas em logs ou relatórios de falhas.

Para desconectar, escolha {% appmenu Arquivo, Publicar, Desconectar conta… %}. Os documentos publicados permanecem online; revogue o acesso a qualquer momento em share.markedapp.com, se necessário.

## Publicar um documento [publish-a-document]

Com um documento aberto na visualização, escolha {% appmenu Arquivo, Publicar, Publicar… %}.

Na primeira vez que você publica um documento, Marked mostra uma pequena folha de opções:

- **Título** — mostrado em Compartilhar (o padrão é o nome do documento sem sua extensão).
- **Visibilidade** — Privado, Não listado ou Público. O padrão de novas publicações é **Não listado** (acessível por link, não listado publicamente).
- **Estilo de leitura** — Editorial, Manuscrito, Suíço, Contraste, Máquina de escrever ou **Nenhum**. O padrão é o estilo de visualização do documento, quando possível. Compartilhar usa isso como sugestão; os leitores podem substituí-lo. Escolha **Nenhum** para publicar sem um estilo sugerido.
- **Incluir destaques e comentários** — incorpora destaques do Modo de Leitura no TextPack. O padrão é ativado quando o documento tem destaques.
- **Permitir que outras pessoas façam remixes** — quando ativado, os visualizadores podem bifurcar o documento no Compartilhar.

Marked cria um TextPack em segundo plano (Markdown, ativos e `highlights.json` opcional), carrega-o e registra o URL de compartilhamento neste Mac.

### Atualizar uma publicação existente [update-an-existing-publish]

Depois que um documento é vinculado ao Compartilhar, o item de menu exibe **Atualizar documento publicado** em vez de **Publicar…**. Escolha-o para fazer upload de uma nova versão TextPack. Marked envia o hash de conteúdo do servidor para que edições simultâneas de outro Mac ou da web sejam detectadas.

Se outra pessoa atualizou o documento no Compartilhar primeiro, Marked pergunta se deseja **Substituir** pela versão deste Mac, **Abrir na Web** ou **Cancelar**.

## Depois de publicar [after-publishing]

Quando uma publicação termina, Marked confirma o sucesso e oferece:

- **Copiar link de compartilhamento** — {% appmenu Arquivo, Publicar, Copiar link do Share %}
- **Aberto na Web** — {% appmenu Arquivo, Publicar, Abrir na web %}

Esses comandos se aplicam ao documento inicial quando ele possui um registro de publicação vinculado.

## Janela Documentos Publicados [published-documents-window]

Escolha {% appmenu Arquivo, Publicar, Documentos publicados… %} para abrir uma lista de documentos publicados neste Mac e sincronizados com sua conta Share.

Para cada entrada você pode:

- **Abra** o arquivo local quando Marked ainda tiver um link para ele no disco.
- **Importar** um TextPack quando não houver arquivo local (salve-o em qualquer lugar e abra-o em Marked).
- **Abrir na Web** ou **Copiar link** para o URL de compartilhamento.
- **Revelar no Finder** quando um caminho local é conhecido.
- **Forget** remove o registro deste Mac sem excluir o documento online.

A lista é atualizada em Compartilhar quando você está conectado. Se você estiver off-line ou desconectado, Marked mostrará registros em cache e poderá solicitar que você se reconecte.

## O que você pode publicar [what-you-can-publish]

Você pode publicar qualquer documento que Marked possa renderizar, incluindo:

- Markdown e arquivos de texto salvos
- Visualizações transitórias (área de transferência, streaming ou documentos não salvos)
- TextBundles e outros formatos suportados

Apenas uma operação de publicação é executada por vez em cada janela do documento; o item de menu fica desabilitado enquanto um upload está em andamento.

## Dicas [tips]

- A publicação inclui imagens referenciadas pela visualização. Pacotes muito grandes podem ser rejeitados antes do upload; reduza os ativos incorporados se você atingir um limite de tamanho.
- Os destaques exportados em TextPack usam o formato JSON de destaque de Marked. Consulte [Reading Mode](Reading_Mode.html) para criar e exportar destaques.
- Marked Share está disponível nas versões Direct, Mac App Store, Setapp e Marked Pro. Nenhuma assinatura separada é necessária para publicação.
