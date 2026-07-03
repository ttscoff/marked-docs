<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

### Modo de depuração

Você pode ativar o registro de depuração abrindo {% prefspane Advanced %} e marcando a caixa de seleção **Modo de Depuração** na parte inferior do painel. Isso exibirá um menu suspenso onde você pode definir o nível de registro que deseja ver:

- **Somente erros**: Somente erros graves serão registrados
- **Erros e avisos**: exibe adicionalmente avisos menos urgentes
- **Todos**: exibe erros, avisos e mensagens de depuração em nível de informação. Esta é a configuração recomendada para solução de problemas.

{% note %}
TODO: Isso ainda funciona?
Você também pode acessar essas opções mantendo pressionada a tecla {% kbd opt  %} ao abrir {% appmenu Help %} na barra de menu.
{% endnote %}

### Visualizando o registro

Com o **Modo de Depuração** ativado, você pode abrir o menu {% appmenu Help %} e selecionar Abrir Log de Depuração. Isso abrirá o log do Marked no Console.app, que será atualizado ao vivo à medida que mensagens de log forem adicionadas ao usar o Marked.

### Solução de problemas de regras personalizadas

[Pré-processadores e processadores personalizados](Custom_Processor.html) obtêm sua própria interface de log. Selecione {% appmenu Help, Show Custom Rules Log %} para abrir a janela. Esta janela exibirá um log colorido mostrando quais regras correspondem e quais comandos elas executam.

### Relatando um problema

Use {% appmenu Help, Report an Issue %} para abrir uma janela que mostra suas configurações para as chaves mais comuns e um modelo para criar um relatório de bug. Use o botão "Copiar para área de transferência" para copiar o conteúdo da janela e clique em "Abrir site de suporte" para abrir [o formulário de nova pergunta](https://support.markedapp.com/questions/add) onde você pode colar seu relatório. Tento responder aos relatos em até 48 horas.