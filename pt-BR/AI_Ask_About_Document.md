<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O Ask About Document usa o **Apple Intelligence** e o modelo de linguagem do dispositivo integrado às versões recentes do macOS para resumir a visualização do Markdown e responder a perguntas sobre seu conteúdo. Todo o processamento acontece no seu Mac; o texto do documento não é enviado aos servidores da Marked ou aos serviços de IA de terceiros para este recurso.

## O que a Apple Intelligence oferece [what-apple-intelligence-provides]

Apple Intelligence é o sistema da Apple para recursos geradores no dispositivo. O Marked usa a estrutura **Foundation Models** da Apple para acessar o mesmo modelo no dispositivo que alimenta as ferramentas de gravação do sistema, exposto diretamente dentro do Marked para tarefas focadas em documentos.

Marcado envia o texto simples do seu documento (sintaxe do Markdown removida para maior clareza) para este modelo local. O modelo gera resumos, esboços e respostas em um painel flutuante ao lado da janela de visualização. Como o modelo é executado localmente, ele funciona off-line assim que o Apple Intelligence é configurado e o download do modelo do sistema é concluído.

O Apple Intelligence é melhor em tarefas linguísticas, como resumo, delineamento, extração de pontos-chave e resposta a perguntas sobre o texto fornecido. Não é um assistente de codificação ou calculadora geral, e documentos muito longos são tratados em seções para que os resultados permaneçam dentro dos limites de contexto do modelo.

## Compatibilidade do sistema [system-compatibility]

Pergunte sobre o documento aparece apenas quando o seu Mac pode executar o recurso.

**Obrigatório:**

- **macOS 26 (Tahoe)** ou posterior
- Um **Mac com suporte Apple Intelligence** (Macs Apple Silicon que atendem aos requisitos de dispositivos da Apple)
- **Apple Intelligence ativado** nas configurações do sistema

**Não suportado:**

- Macs Intel e outros Macs marcados como inelegíveis para Apple Intelligence
- Versões do macOS anteriores ao Tahoe 26
- **Pré-visualizações HTML** brutas (o recurso é para Markdown e fluxos de trabalho de documentos baseados em texto)

Se o seu Mac estiver qualificado, mas o item de menu estiver faltando, confirme se o Apple Intelligence está ativado e se você está executando uma versão atual do Marked que inclui esse recurso. O menu fica totalmente oculto em sistemas não suportados, em vez de ser mostrado desativado.

## Ativando a inteligência da Apple [enabling-apple-intelligence]

1. Abra **Configurações do sistema**.
2. Acesse **Apple Intelligence e Siri** (ou **Apple Intelligence**, dependendo da versão do seu macOS).
3. Ative o **Apple Intelligence** e conclua todas as etapas de configuração solicitadas pela Apple.
4. Aguarde até que o download do modelo no dispositivo seja concluído, se solicitado. Até que o modelo esteja pronto, Marcado pode mostrar o item de menu, mas exibir uma mensagem de que o Apple Intelligence ainda está se preparando.

Marcado não inclui uma preferência separada para esse recurso. A disponibilidade segue o status do modelo do sistema relatado pelo macOS.

## Abrindo o documento Pergunte sobre [opening-ask-about-document]

Abra o painel usando qualquer um destes métodos:

- **Visualizar> Perguntar sobre o documento…**
- Atalho de teclado {% kbd shift ctrl cmd I %} (enquanto um documento de visualização do Markdown é a janela ativa)

O painel é encaixado no lado esquerdo da janela do documento. Você precisa de um documento aberto com texto legível; um documento vazio ou uma visualização somente HTML não oferecerá o comando.

## O painel Perguntar sobre o documento [the-ask-about-document-panel]

O painel é organizado como uma visualização simples de bate-papo:

- **Ações predefinidas** na parte superior para tarefas comuns
- Uma **área de resposta** no meio onde aparecem resumos e respostas (streaming à medida que são gerados)
- Um **campo de pergunta** na parte inferior onde você digita perguntas personalizadas, com botões **Perguntar** e **Cancelar**

Após a conclusão de uma resposta, o foco retorna ao campo de pergunta para que você possa fazer um acompanhamento sem clicar.

### Ações predefinidas [preset-actions]

| Ação | O que faz |
| :-- | :-- |
| **Resumir documento** | Produz um breve resumo coeso do documento completo. Documentos longos são resumidos em seções e combinados. |
| **Resumir seleção** | Resume apenas o texto atualmente selecionado na visualização. Selecione o texto primeiro; caso contrário, Marcado solicita que você faça uma seleção ou use Resumir Documento. |
| **Esboço** | Constrói um esboço hierárquico da estrutura do documento usando títulos e marcadores. |
| **Pontos-chave** | Lista os pontos mais importantes do documento como uma lista com marcadores. |

As ações predefinidas não requerem texto no campo de pergunta. Clique em um botão e aguarde a resposta no painel acima.

### Fazendo suas próprias perguntas [asking-your-own-questions]

1. Digite uma pergunta no campo na parte inferior do painel, por exemplo “Que problema este documento resolve?” ou "Quem é o público-alvo?"
2. Pressione **Retornar** ou clique em **Perguntar**.
3. Leia a resposta à medida que ela chega à área de resposta.

Para perguntas sobre uma passagem específica, **selecione o texto na visualização** antes de perguntar. Marcado envia a seleção como contexto em vez de todo o documento quando uma seleção está ativa.

Clique em **Cancelar** para interromper uma solicitação em andamento.

## Exemplos [examples]

### Visão geral rápida de um artigo longo [quick-overview-of-a-long-article]

Abra uma postagem de blog ou relatório extenso em Marcado, escolha **Visualizar > Perguntar sobre o documento…** e clique em **Resumir documento**. Use o resumo para decidir se deseja ler o artigo completo ou refrescar a memória depois de um tempo longe do rascunho.

### Notas sobre um parágrafo selecionado [notes-on-a-selected-paragraph]

Destaque um parágrafo denso na visualização, abra Pergunte sobre o documento e clique em **Resumir seleção**. Útil quando você precisa apenas de uma versão mais curta de uma seção.

### Revisão estrutural [structural-review]

Clique em **Esboço** em um rascunho com muitos títulos para ver se o argumento flui logicamente ou use **Pontos-chave** antes de enviar um documento a outra pessoa para verificar se as ideias principais estão claras.

### Perguntas direcionadas [targeted-questions]

Sem seleção ativa, digite perguntas como:

- "Quais são as três recomendações principais?"
- "Este documento menciona licenciamento?"
- "Liste quaisquer datas ou prazos mencionados."

Com uma seleção ativa, faça perguntas mais restritas, como “O que este parágrafo pressupõe sobre o leitor?” ou "Reescreva esta ideia em uma frase" (o modelo responde sobre a seleção; ele não edita seu arquivo fonte).

## Dicas e limitações [tips-and-limitations]

- **Privacidade:** O processamento usa o modelo no dispositivo da Apple. Marcado ainda lê o texto do seu documento localmente para fornecer conteúdo a esse modelo; trate o material sensível adequadamente.
- **Precisão:** Verifique fatos importantes em relação à sua fonte. Os resumos de IA podem omitir detalhes ou interpretar mal passagens ambíguas.
- **Comprimento:** Documentos extremamente longos são processados ​​em partes. Resumos e respostas refletem indiretamente o texto completo; para obter precisão em uma seção, selecione-a primeiro.
- **Idioma:** Os resultados seguem os recursos de idioma do modelo Apple Intelligence do sistema no seu Mac.
- **Recusas:** O sistema pode recusar algumas solicitações com base nas políticas de segurança da Apple.

Se Perguntar sobre o documento não estiver disponível, verifique o status das Configurações do sistema para Apple Intelligence e verifique se você está visualizando um documento Markdown em um Mac compatível executando macOS 26 ou posterior.