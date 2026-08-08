<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane General %}:

![Configurações: Geral][1]

[1]: images/screenshots/preferences-General.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Janela [window]

Mantenha as novas janelas no topo
: define automaticamente novas janelas para "flutuar" acima de outros aplicativos.

Aumentar janela na atualização
: quando uma alteração é detectada em um arquivo monitorado, a janela de visualização desse documento ficará acima das outras janelas da sua área de trabalho sem ativar Marcado.

Translúcido no fundo
: esmaece a janela quando ela não está focada. Use o controle deslizante para definir a opacidade.

Desative recursos que consomem muita memória em documentos grandes
: desative alguns recursos que fazem uso intensivo do processador, como títulos recolhíveis, quando os documentos tiverem mais de 100k.

Novos documentos são abertos em
: escolha **janelas**, **guias** ou **automático** (siga a configuração do sistema macOS para tabulação). Ao usar guias, navegue com {% kbd cmd shift [/] %} e o [painel Quick Open](Quick_Open.html).

Traga o documento atualizado para frente
: quando uma visualização for atualizada, selecione sua guia ou ordene sua janela para a frente **dentro de Marcado apenas**. Se outro aplicativo estiver na frente (por exemplo, seu editor de texto), Marcado permanecerá em segundo plano — a guia correta será selecionada para que esteja pronta quando você voltar para Marcado. Para exibir a visualização acima de todos os aplicativos sem ativar Marcado, use **Aumentar janela na atualização**.

Retornar o foco ao aplicativo anterior
: quando ativado, se uma ação aumentar/trazer atualização fizer com que Marcado fique em primeiro plano, o foco do teclado será retornado ao aplicativo que estava em primeiro lugar antes da atualização (como seu editor de texto). Quando desativado, Marcado nunca executa essa transferência de foco. Se Marcado não ficar na frente, esta opção não terá efeito.

### Barra de status [status-bar]

Mostrar seletor de estilo
: mostra o seletor de estilo na barra inferior da janela de visualização.

Mostrar contagem de palavras
: mostra a contagem de palavras (e o botão de estatísticas) na barra inferior da janela de visualização.

A contagem de palavras exclui
: os cálculos de contagem de palavras podem ignorar qualquer combinação de:

- **Notas de rodapé/citações**
- **Citações em bloco**
- **Blocos de código recuados** (blocos de código protegidos são sempre excluídos)
- **Legendas das imagens**

### Atalhos [shortcuts]

Clique no campo de atalho para registrar uma combinação de teclas de atalho que aciona um evento:

Ativar Marcado
: Mude para Marcado quando esta tecla de atalho for pressionada em qualquer aplicativo.

Levante a primeira janela
: eleva a janela de visualização marcada mais à frente (última ativa) para o primeiro plano sem sair do aplicativo atual.

Abrir paleta de ações
: Abra a paleta de comandos [Ações Rápidas](Quick_Actions.html) enquanto Marcado estiver ativo. Este atalho se aplica a {% appmenu File, Quick Actions… %} e funciona apenas em Marcado (não em outros aplicativos).

Redefinir alertas
: restaure quaisquer caixas de diálogo de alerta que você tenha descartado anteriormente para que possam aparecer novamente.