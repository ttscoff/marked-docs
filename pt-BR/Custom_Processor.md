<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>


Marcado oferece controle total com regras personalizadas, texto
transformações e a capacidade de executar seus próprios comandos ou executar
processadores diferentes com base nas propriedades correspondentes do arquivo.


## Usando pré-processadores/processadores personalizados

Para adicionar processadores personalizados, vá para {% prefspane Processor %}
e clique em **Regras personalizadas**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


No Editor de regras (também conhecido como "Condutor"), você pode adicionar
regras que possuem critérios para combinar arquivos com base no nome do arquivo,
caminho, correspondências no conteúdo, metadados e até mesmo se
outros arquivos existem na mesma árvore do documento que está sendo
aberto. Quando uma regra é correspondida, as ações definidas para a
regra são executadas nesse arquivo.

> Abaixo do campo Processador, as caixas de seleção em "Novo
>documents use custom:" determina se as regras são testadas
> em absoluto para as fases de Pré-processador e Processador. Em geral,
> deixe-os marcados, mas se quiser substituir completamente
> qualquer processador personalizado, defina-o aqui.

![Editor de regras][2]

  [2]: imagens/CustomRules-800.jpg @2x width=800

Para criar uma nova regra, use o `+`
botão na parte inferior da lista de regras à esquerda. Dê o
determine um nome e defina-o como um pré-processador ou processador.

Os três pontos próximos a uma regra indicam Pré-processador, Processador e Habilitado. Apenas um Pré-processador ou Processador pode ser destacado e você pode clicar nos pontos para alterar os estados da regra.

Pré-processador
: é executado após o arquivo ser processado inicialmente, quando Marcado adiciona arquivos incluídos, lida com preferências de estilo como novas linhas do GitHub, etc., mas antes da fase de processamento. O documento ainda está Markdown bruto neste ponto e você pode fazer alterações no conteúdo para passar ao processador. Se nenhum Processador Personalizado corresponder ou nenhuma ação Executar Processador for executada em um Processador Personalizado correspondente, o processador padrão será executado.

Processador
: Um processador personalizado substitui o processador integrado definido em {% prefspane Processor %}. Ele pode lidar com todas as ações que um pré-processador pode e adiciona ações Executar Comando e Executar Processador. Isso permite que você execute um comando personalizado, por exemplo. Pandoc ou execute um processador integrado diferente em arquivos que correspondam aos critérios.

Todas as tabelas no editor de regras personalizadas podem ser reordenadas por
arrastando e soltando, para que você possa afetar a ordem em que
regras são executadas, a ordem dos critérios no predicado
editor e a ordem das ações a serem executadas em sequência.

### Editor de Predicados

![Editor de Predicado][predicado]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Depois que uma regra for adicionada, use o editor de predicados para definir
critérios que determinarão se a regra será executada por um
determinado arquivo. Use o menu suspenso do lado esquerdo para selecionar um
critério e, em seguida, use os campos comparador e valor para construir
o predicado.

- _Filename_ corresponde apenas ao nome do arquivo
- _Extension_ corresponde apenas à extensão do arquivo
- _Path_ corresponde ao caminho POSIX (Unix) completo do arquivo
- _Tree_ procura correspondências de nome de arquivo em qualquer lugar do
  árvore de diretórios do arquivo
- _Text_ corresponde ao conteúdo do texto no arquivo. Usar para frente
  barras ao redor do valor do texto para torná-lo regular
  pesquisa de expressão.
- _Arquivo inclui_ testa se o arquivo contém itens incluídos
  arquivos (usando qualquer um dos [marcados incluem
  sintaxes](Multi-File_Documents.html)).
- _Tipo de metadados_ testa se o arquivo inclui YAML,
  Metadados MultiMarkdown ou Pandoc
- _Metadados:_ campos (por exemplo _Metadados: Autor_,
  _Metadados: Data_, _Metadados: Título_) teste para específico
  chaves de metadados. Qualquer chave de metadados aparece no menu suspenso como
  _Metadados:_ seguido do nome do campo.
- _Ativado manualmente_ corresponde quando essa regra foi alterada
  ativado para a janela de visualização atual (consulte [Ativado manualmente
  regras](#manuallyenabled) abaixo). Combine-o com outros
  critérios em um grupo Todos (AND), para que a regra seja executada apenas quando
  você aceita e o arquivo corresponde às suas outras condições.

Para corresponder todos os arquivos (ou seja, um processador personalizado que sempre
é executado), defina _Nome do arquivo_ como `contains` `*`. O asterisco irá
atue como um curinga e corresponda a todos os arquivos.

[Adicionar um predicado][addpredicate]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Clique no sinal de mais (+) na linha do predicado para adicionar outro predicado. Mantenha pressionada Option enquanto clica em + para adicionar um grupo booleano que pode ser definido como Todos (AND) ou Qualquer (OR).

### Regras habilitadas manualmente [habilitadas manualmente]

Algumas regras não devem ser executadas em todos os arquivos que correspondam às suas
critérios. Adicione um critério **ativado manualmente** quando desejar
uma regra a ser executada somente depois de ativá-la para o atual
visualização.

Use o botão **Adicionar ativado manualmente** abaixo do predicado
editor para inserir este critério. Cada regra pode incluí-lo
apenas uma vez. Quando presente, a regra aparece no submenu {% appmenu
Preview, Enable Custom Rule %} dessa visualização
janela.

**Exemplo de caso de uso:** você mantém uma regra que injeta
imprime CSS, remove comentários e muda os níveis de cabeçalho para
Exportação de PDF. Você não quer essa transformação em todos
economize durante o rascunho, mas você deseja isso sob demanda. Dê o
regra de critérios normais de correspondência de arquivo mais **Ativado manualmente**,
em seguida, alterne-o no menu Visualização (ou em um atalho de gatilho)
quando estiver pronto para revisar o layout de impressão.

#### Atalho de gatilho

Quando uma regra selecionada inclui **Ativado manualmente**, um
O campo **Atalho do acionador** aparece ao lado de **Adicionar manualmente
Ativado**. Clique no gravador e pressione a tecla
combinação que você deseja. Esse atalho alterna a regra para o
visualização marcada mais à frente (ativar se estiver desativado, desativar se estiver ativado). O
o atalho é armazenado com a regra e persiste durante as inicializações.
Limpe o campo para remover o atalho.

![Aciona o gravador de atalho no Conductor][atalho manual]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### Substituições por visualização no menu Visualização

Dois submenus do menu Visualização controlam substituições para o ativo
apenas visualização. As configurações são salvas por [visualização](#multiview) quando
várias janelas mostram o mesmo arquivo.

**Ativar regra personalizada**
: lista todas as regras habilitadas que incluem **Manualmente
  critério habilitado**. Verifique uma regra para ativá-lo para isso
  visualização; desmarque para desligá-lo. A visualização é atualizada
  imediatamente.

**Substituição de regra personalizada**
: lista as regras da fase do processo. Escolha um para *fixar*: durante
  fase Processo, apenas essa regra é avaliada (outras
  As regras do processo são ignoradas). Escolha **Nenhum (automático)** para
  retornar à correspondência normal de regras. Isto é útil quando você
  deseja forçar um pipeline de processador específico para um
  visualizar sem alterar as regras personalizadas globais.

#### Botão Substituir na barra de ferramentas de visualização

Quando uma visualização tem pelo menos uma regra habilitada manualmente ou um
substituição de processo fixada, um ícone de ramificação aparece na parte inferior
barra de ferramentas (à esquerda dos controles de exportação e gaveta).
O ícone preenchido com cor de destaque significa que as substituições estão ativas;
o ícone de contorno significa que as substituições estão suspensas.

![Botão de substituição de regra personalizada na barra de ferramentas de visualização][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

Clique no botão para suspender ou reativar substituições para este
visualizar sem limpar as marcas de seleção das regras manuais ou
regra de processo fixada. As substituições suspensas são restauradas quando
você clica novamente. Isso é mais rápido do que desmarcar regras no
menu quando quiser comparar a visualização normal com o seu
substituir o pipeline.

### Ações

Use o botão *+ Ação* para adicionar ações à regra.

![Adicionar uma ação][addação]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

As ações disponíveis incluem:

Definir estilo
: defina o estilo da visualização. Qualquer estilo integrado ou estilo personalizado que você adicionou estará disponível.

Executar comando
: Isso leva um comando de linha de comando, incluindo quaisquer argumentos, e passará o conteúdo do arquivo em STDIN. O comando deve retornar a saída resultante em STDOUT.

> **Sandboxing da Mac App Store**: a versão Mac App Store (MAS) do Marked é executada em um ambiente de sandbox que restringe a execução de binários externos. Se precisar usar processadores externos como Pandoc na versão MAS, você deverá copiar o binário no pacote de aplicativos. Para fazer isso:
>
> 1. Clique com o botão direito em Marked.app → Mostrar conteúdo do pacote
> 2. Navegue até Conteúdo/Recursos/
> 3. Crie uma pasta `bin` se ela não existir
> 4. Copie seu binário (por exemplo, `pandoc`) para este
> pasta `bin`
> 5. Torne-o executável: `chmod +x` o binário
> 6. Na ação Executar Comando, referencie-o como:
>
> `YOUR_BINARY_NAME [arguments]`
> Ou use o caminho completo:
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Nota**: Scripts com shebangs externos (como scripts Python apontando para `/opt/homebrew/bin/python`) serão executados automaticamente através de interpretadores do sistema quando copiados para o pacote. A versão MAS ainda pode ter problemas para executar binários que na verdade são scripts Python ou Ruby em vez de arquivos binários.
> Você precisará copiar novamente os binários após cada atualização do aplicativo, pois as atualizações substituem todo o pacote. Alternativamente, use **Help->Crossgrade** para obter a versão sem sandbox que não possui tais restrições.

Executar script incorporado
: edite um script completo no editor de código integrado. Assim como o Run Command, isso deve receber entrada em STDIN e retornar saída em STDOUT.

Definir metadados
: adiciona ou define metadados. Forneça uma chave e um valor. Se a chave existir, seu valor será atualizado, caso contrário, será adicionado. O tipo de metadados utilizados será determinado automaticamente pelo conteúdo do arquivo (ou pelo resultado de uma ação de conversão de metadados).
: Se nenhum metadado existente for encontrado, os metadados serão adicionados no formato MultiMarkdown dentro de um comentário HTML. Marcado pode ler esses metadados, mas eles não aparecerão na sua visualização, independentemente do processador usado.

Excluir metadados
: exclua metadados com base em sua chave.

Tirar metadados
: exclua todos os metadados. Afeta os metadados YAML, MultiMarkdown e Pandoc.

Converter YAML Meta em MMD
: converte um bloco de metadados YAML na parte superior do arquivo em metadados no estilo MultiMarkdown.

Converter MMD Meta em YAML
: converte um bloco de metadados MultiMarkdown em YAML.

Pesquisar e substituir
: faça uma pesquisa e substitua o conteúdo do arquivo.
: Se a string de pesquisa estiver entre barras (por exemplo, `/Project \w+/`), ela será tratada como uma expressão regular. Você pode usar `$1`, `$2`, etc. para incluir grupos de correspondência na string de substituição.
: O campo de substituição suporta algumas sequências de escape (uma barra invertida seguida por): `\n` insere uma nova linha, `\t` insere um caractere de tabulação, `\\` insere uma barra invertida literal, `\$` insere um cifrão literal (em vez de um grupo de correspondência)
: Qualquer outra sequência `\X` é tratada apenas como `X` (a barra invertida é eliminada), então `\e` torna-se `e`. Um \ final sem nenhum caractere depois de ser preservado como uma barra invertida literal.
: use `[%key]` na string de substituição para inserir um valor de metadados de documento, variáveis ​​de ambiente ou contexto (por exemplo, `[%title]`, `[%MARKED_PATH]`). Estão disponíveis chaves definidas por ações anteriores na mesma regra ou por uma regra anterior. Chaves sem correspondência são substituídas por uma string vazia.

Inserir título H1
: Insere um H1 no documento. Isso pode ser obtido dos metadados ou do nome do arquivo.

Cabeçalhos de turno
: Ajusta os níveis do cabeçalho, de -5 a +5. Por exemplo, se você definir isso como -1, todos os H1s se tornarão H2s, H2s se tornarão H3s, etc. Defina-o como um número positivo para elevar os níveis do cabeçalho nesse valor.

Normalizar cabeçalhos
: esta ação garantirá, se possível, que haja apenas um H1 no documento e ajustará todos os níveis de cabeçalho para que estejam em ordem semântica e não pulem níveis, por exemplo. de H2 a H4. Se o documento original estiver ordenado semanticamente para começar, isso refinará bem a hierarquia.

Inserir sumário
: insira um índice. O TOC pode ir depois do primeiro H1, do primeiro H2 ou no topo do arquivo (será inserido após qualquer metadado).

Inserir arquivo
: insere um arquivo de texto selecionado em um determinado ponto do documento. Isso pode ser após o primeiro H1, primeiro H2, superior, inferior ou após uma correspondência de texto (use `/pattern/` para procurar uma expressão regular).

Inserir texto
: fornece um editor pop-up com o qual você pode incorporar texto diretamente na ação. As opções de posicionamento são iguais a _Inserir arquivo_.
: Use `[%key]` em qualquer lugar do texto inserido para extrair valores de metadados de documentos, variáveis ​​de ambiente ou contexto marcado (por exemplo, `[%author]`, `[%MARKED_PATH]`). Isso funciona independentemente de qual processador você usa, portanto você não precisa do MultiMarkdown para substituição de metadados. Valores de ações anteriores na mesma regra (como **Definir metadados**) ou de uma regra anterior são incluídos. Chaves sem correspondência são substituídas por uma string vazia.

Inserir arquivo CSS
: injeta um arquivo CSS selecionado no documento. Ele será carregado após qualquer seleção de estilo e pode ser usado para substituir estilos existentes ou adicionar novos.

Inserir CSS
: oferece um editor CSS pop-up onde você pode adicionar seu próprio CSS diretamente à ação. Este CSS será injetado no topo do documento, após quaisquer estilos existentes. A ordem dos estilos injetados corresponderá à ordem das ações na regra.

Inserir arquivo JavaScript
: injeta um arquivo JavaScript selecionado no final do documento. Observe que você precisa usar uma ação *Inserir JavaScript* com um [gancho de atualização](#updatehook) se quiser que o script seja recarregado a cada atualização.

Insira JavaScript do URL
: Use isto para inserir uma tag `<script>` vinculada a um CDN ou outro URL remoto no final do documento. Observe que você precisa usar uma ação *Inserir JavaScript* com um [gancho de atualização](#updatehook) se quiser que o script seja recarregado a cada atualização.

Insira JavaScript
: fornece um editor JavaScript pop-up com o qual você pode incorporar JavaScript personalizado diretamente na ação. Isso será injetado no final do documento, e a ordem do JavaScript executado pela regra será determinada pela sequência das ações, com a última ação adicionada por último.
: Observe que você precisa usar um [gancho de atualização](#updatehook) se quiser que os scripts sejam executados a cada atualização.

URLS de auto-link
: Converta qualquer URL simples em `<url>`, o que gerará um hiperlink em qualquer processador.

Executar atalho
: execute um atalho da Apple. Qualquer execução de atalho deve receber entrada de STDIN e retornar saída no final (Stop e Return Output). Se você quiser executar ações que não modifiquem o texto, defina a entrada como uma variável, execute suas ações e, em seguida, produza a variável de texto original no final.

Execute o serviço do sistema
: Execute qualquer serviço do sistema em `~/Library/Services`. O Serviço deve aceitar entrada e retornar saída.

Execute o fluxo de trabalho do Automator
: Execute qualquer arquivo do Automator `.workflow`. A entrada será passada em STDIN e a saída será esperada em STDOUT.

Executar regra
: execute as ações de outra regra personalizada a partir da regra atual.
  Escolha a regra de destino no pop-up. A regra invocada
  é executado na mesma fase (Pré-processador ou Processo) sem
  reavaliando seu predicado, o que o torna útil para
  regras de "ingredientes" reutilizáveis.

  **Exemplo de caso de uso:** Defina uma pequena regra chamada "Strip
  Comentários HTML" com uma ação Pesquisar e Substituir e fornecer
  é um critério **ativado manualmente** para que nunca seja executado
  automaticamente. Na sua regra principal de processamento de livros, adicione
  **Executar ações de regra** em sequência: primeiro "Normalizar cabeçalhos",
  em seguida, "Remover comentários HTML" e, em seguida, um comando Executar que chama
  Pandoc. Você mantém cada etapa passível de manutenção sem duplicação
  ações através das regras.

  **Aninhamento:** uma regra invocada por **Run Rule** não pode ser invocada
  outra regra. Se a regra de destino contiver uma **Regra de Execução**
  ação, essa ação será ignorada; todas as outras ações do
  a regra de destino ainda está em execução. Você pode adicionar várias **Regras de execução**
  ações a uma única regra e elas são executadas em ordem.

  Uma regra não pode invocar a si mesma e Marcada detecta ciclos
  (por exemplo, Regra A invocando Regra B que invoca Regra A)
  e ignora a chamada aninhada. Consulte as [Regras Personalizadas
  Log](#customprocessorlog) para ignorar mensagens.

Continuar
: por padrão, quando uma regra é correspondida, o processamento será interrompido (separadamente para pré-processadores e processadores, para que um pré-processador e um processador possam corresponder). Esta ação forçará a continuação da correspondência de regras depois que a regra executar suas ações.

### Gancho de atualização

Marcado não faz uma atualização completa a cada atualização, então se
você tem scripts que renderizam partes do DOM, eles precisam
para executar sua função de renderização usando a API Hook do Marked.

O exemplo abaixo usa Mermaid, que você nunca
precisa fazer, já que o Mermaid agora está incluído por padrão. Mas
veja como você faria isso se o incluísse manualmente.

Adicione uma ação **Inserir JavaScript** e em "Editar JS"
janela, inicialize o script e adicione o gancho:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Isso fará com que `mermaid.run()` seja executado toda vez
Marcado executa uma atualização parcial.

### Regras de teste

O botão _Regras de teste_ na lista Regras abrirá um
caixa de diálogo onde você pode selecionar qualquer arquivo Markdown e ele será
testado contra todas as suas regras. Regras que correspondam obterão
destacado com uma guia verde no lado esquerdo. Ao combinar
contra um arquivo, um botão X aparecerá que pode ser usado para
limpe o teste e desmarque as linhas.

## Arraste e solte

A janela do Conductor suporta arrastar e soltar aprimorado
recursos que detectam de forma inteligente tipos de arquivos e
forneça ações apropriadas com base no arquivo arrastado. O
a implementação inclui um sistema de sobreposição dividida para texto
arquivos que permitem aos usuários escolher entre testar o arquivo
contra regras ou adicionando-o como uma ação.

![Arraste e solte nas regras personalizadas][arraste]

[drag]: images/draganddropconductor.jpg @2x width=800

### Detecção de tipo de arquivo

O sistema detecta automaticamente diferentes tipos de arquivos e
mostra mensagens de sobreposição apropriadas:

- **Arquivos CSS** (`.css`): Mostra a sobreposição "Inserir arquivo CSS"
- **Arquivos JavaScript** (`.js`, `.javascript`): Mostra "Inserir
  Sobreposição de arquivo JS"
- **Arquivos de script** (qualquer arquivo executável)): Mostra "Executar
  Sobreposição de comando"
- **Arquivos de texto**: mostra sobreposição dividida
- **Arquivos executáveis**: Mostra a sobreposição "Executar Comando"
- **Extensões desconhecidas**: o padrão é o tipo "texto" e mostra
  sobreposição dividida

## Log do processador personalizado [customprocessorlog]

Se você estiver obtendo resultados estranhos e quiser dar uma olhada no que está acontecendo, o Registro de regras personalizadas mostrará quais regras estão sendo executadas e em que ordem. Use **Ajuda->Mostrar registro de regras personalizadas** para abri-lo. As ações de **Executar regra** invocadas e as chamadas aninhadas ignoradas também são registradas aqui.

![Registro de regras personalizadas][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Executando vários comandos

Uma regra pode ter vários comandos em sequência. A saída de
cada comando será passado para o próximo. Se você quiser ter
um comando produz algo ao mesmo tempo que o de Marked
visualizar atualizações, certifique-se de devolver o conteúdo original
para STDOUT para processar o próximo comando ou integrado
processador.

Por exemplo, se você quiser que um comando atualize um PDF
documento usando Pandoc, basta passar o caminho do arquivo original
(de variáveis de ambiente) para Pandoc com apropriado
opções de linha de comando e, em seguida, ecoe o conteúdo STDIN de volta
para STDOUT.

## Ignorando dinamicamente processadores personalizados

Se um processador personalizado retornar "NOCUSTOM" em STDOUT, marcado
encerrará o processador personalizado e retornará ao
processador interno padrão. Isso permite que você crie um
processador personalizado que pode decidir se precisa ou não
execute usando as [variáveis de ambiente](#environmentvariables)
abaixo, o nome do arquivo ou extensão do documento, correspondência de conteúdo
ou outra lógica.

Se em vez de `NOCUSTOM` um Processador Personalizado retornar
`MULTIMARKDOWN` ou `DISCOUNT` (ou `GFM`), `KRAMDOWN`, ou
`COMMONMARK`, então esse processador interno será usado para
apenas esse documento. Esta alteração não afetará o padrão
processador definido em Configurações.

## Variáveis de ambiente

A ação Executar Comando possui um editor de ambiente onde você
pode definir suas próprias variáveis de ambiente que serão
disponível para o comando ou script. Além destes
variáveis personalizadas, Marked inclui algumas próprias.

Marked executa o processador personalizado em seu próprio shell, o que significa
variáveis de ambiente padrão não são passadas automaticamente.
Você pode usar as variáveis de ambiente do Marked para aumentar seu
possuir em seus scripts. Marcado cria as seguintes variáveis
disponível para uso em seus scripts de shell:

**MARKED_ORIGIN**
: A localização (diretório base) do seu arquivo de trabalho primário (a pasta do texto de trabalho, Scrivener ou arquivo de índice).

** CAMINHO **
: Marcado define um caminho que inclui pastas executáveis padrão e anexa o diretório no `MARKED_ORIGIN` acima. Os padrões são: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. Você pode adicionar o seu próprio definindo a variável PATH conforme necessário e anexando ou substituindo o caminho de Marked (por exemplo, `PATH=/usr/local/yourfolder:$PATH`).

**CASA**
: o diretório inicial do usuário conectado. Python e outros scripts que dependem da variável HOME definida irão capturá-la automaticamente, mas estará disponível para outros usos em seus scripts.

**MARKED_EXT**
: a extensão do arquivo primário que está sendo processado. Esta variável permite criar scripts de diferentes processos com base no tipo de arquivo que está sendo visualizado. Por exemplo, se `$MARKED_EXT == "md"` execute seu processador Markdown preferido, mas se `$MARKED_EXT == "textile"` execute um processador têxtil.

**MARKED_PATH**
: Este é o caminho completo do UNIX para o arquivo principal aberto em Marcado no momento em que é carregado.

**MARKED_INCLUDES**
: Uma lista entre aspas e separada por vírgulas dos arquivos Marcados incluídos no texto que está sendo passado usando as várias [incluir sintaxes](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: será definido como "PROCESS" ou "PREPROCESS", permitindo que você use um único script para lidar com ambas as fases com base nesta variável.

**MARKED_CSS_PATH**
: O caminho completo para a folha de estilo atual

### Variáveis de ambiente de metadados

Quando a ação Executar Comando é executada no Marked's
Sistema condutor, os metadados do documento são automaticamente
extraídas e disponibilizadas como variáveis de ambiente para o
comando.

#### Como funciona

1. **Extração de Metadados**: O sistema extrai metadados do documento usando o método `extractMetaDataFromString:` existente, que suporta:
   - Matéria inicial YAML (`---` blocos)
   - Metadados MultiMarkdown (chave: linhas de valor)
   - Metadados Pandoc (`%` blocos de título)
   - Metadados de comentários HTML (`<!-- key: value -->`)

2. **Normalização de chave**: as chaves de metadados são normalizadas para uso como variáveis de ambiente:
   - Convertido para minúsculas
   - Todos os caracteres não alfanuméricos são removidos
   - Espaços e caracteres especiais são eliminados

3. **Formato de variável de ambiente**: cada chave de metadados se torna uma variável de ambiente com o prefixo `MD_`:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Exemplo

Dado um documento com estes metadados:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

As seguintes variáveis de ambiente estariam disponíveis para
comandos:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Uso em Comandos

Agora você pode usar essas variáveis de ambiente em seu Run
Ações de comando:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Ações suportadas

Esta funcionalidade variável de metadados para ambiente é
disponível em:

- **Executar comando** ações
- **Executar script incorporado** ações

Os metadados são extraídos automaticamente do documento
conteúdo e disponibilizado para qualquer comando ou script que
percorre essas ações.

## Ativando e Desativando

Os processadores personalizados podem ser ligados e desligados para
documentos individuais usando {% kbd opt cmd C %}. Você
também pode ativar um pré-processador ou processador para um documento
automaticamente [usando metadados](#perdocument) na parte superior de
o documento.

Os status atuais dos processadores para cada documento são
exibido como luzes indicadoras (visíveis apenas quando um processador
está ativado) à esquerda dos itens da barra de ferramentas na parte inferior
barra de ferramentas direita da visualização.

### Pré-processador

Se você configurar regras de pré-processador, elas serão executadas após Marcadas
lida com quaisquer tarefas específicas do Marked, como incluir
documentos e código, mas antes de executar o processador
(interno ou personalizado). Isso lhe dá a chance de renderizar
variáveis de modelo personalizadas, lidar com substituições ou injetar
seu próprio conteúdo por qualquer outro meio.

Marcado define uma variável de ambiente para o trabalho
diretório (`MARKED_ORIGIN`) para o diretório pai do
arquivo sendo visualizado. Você pode usar isso para alterar o funcionamento
diretório de um script e incluir arquivos com caminhos relativos
ao documento original. Por exemplo, em Ruby você pode
usar:

	Dir.chdir(ENV['MARKED_ORIGIN'])

Quando ativado, o pré-processador personalizado pode ser ativado e
desativado para documentos individuais usando
{% kbd ctrl opt cmd C %}.

#### Processador/Pré-processador por documento [por documento]

Processadores personalizados também podem ser definidos por documento
usando o formato de metadados para [Por Documento
configurações](Per-Document_Settings.html).

Você pode especificar se deseja usar configurações personalizadas do processador e
substituir o padrão de um documento usando [Per-Document
configurações](Per-Document_Settings.html) (`Custom Processor:`
e `Custom Preprocessor:`). Qualquer configuração diferente de "true"
ou "sim" desativará o pré/processador personalizado.

Exemplo de uso:

    Processador personalizado: verdadeiro
    Pré-processador personalizado: falso

Conforme observado no [Por Documento
Configurações](Per-Document_Settings.html#hidingmeta) página, você
pode cercar esses metadados com marcadores de comentários HTML para ocultar
do GitHub e de outros processadores que não o removem
da saída:

    <!--
    Processador personalizado: verdadeiro
    Pré-processador personalizado: verdadeiro
    -->

## Usando um processador Markdown alternativo

Qualquer tipo de Markdown que você possa renderizar na linha de comando pode
ser usado com Marcado. Ele precisa ser capaz de receber contribuições
STDIN, que é o mesmo que "canalizar" seu Markdown para ele
linha de comando, ou seja, `cat myfile.md | myprocessor`. Precisa
para retornar o HTML resultante em STDOUT, que cada
processador com o qual já trabalhei faz isso por padrão.

Use `which YOUR_PROCESSOR` no Terminal para determinar o caminho
para o executável e cole-o no caminho Executar Comando
campo ou apenas arraste o executável para a janela Regras Personalizadas
com a regra à qual você deseja adicionar a ação selecionada.

Se o seu processador exigir argumentos na linha de comando,
você precisará inseri-los no campo também. Alguns
processadores precisam de hífens para funcionar em STDIN e/ou STDOUT,
por exemplo `-o - -` geralmente sinaliza entrada de STDIN, saída para
STDOUT. Consulte a documentação do seu processador para obter detalhes.

Testei o recurso Processador Personalizado com Pandoc,
Kramdown, marcado (desconto), MultiMarkdown 6, Maruku e
vários outros sabores.

### Uma nota sobre Pandoc e Sandboxing

Pandoc (e algumas outras ferramentas de linha de comando) não serão executados em
a versão Mac App Store (em sandbox) do Marked.
Se você precisar executar o Pandoc, use **Help->Crossgrade** para obter um
licença gratuita para a versão direta (Paddle). Isso é verdade
de qualquer processador que tenha problemas de sandbox: se marcado
não puder executá-lo devido a problemas de permissão do MAS, ele irá
ofereça as etapas para fazer crossgrade. Se você estiver enfrentando problemas
e isso não está acontecendo, entre em contato comigo através do
[site de suporte](https://support.markedapp.com/questions/add).

### Pandoc como processador de descontos do exército suíço

[Pandoc](https://pandoc.org/) é de longe o mais flexível
ferramenta multifuncional para lidar com uma variedade de formatos de marcação. Por
adicionando um argumento `-f` com um dos seguintes, Pandoc pode
seja seu processador personalizado para qualquer um dos seguintes:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

E um monte de outros. Veja o [Pandoc
documentação](https://pandoc.org/MANUAL.html) para mais
informações. Para usar um deles como formato de entrada, basta adicionar o
seguinte no campo Executar comando:

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc é perfeito para escrever um script que usa o
`$MARKED_EXT` variável de ambiente para determinar qual formato
para executar o Pandoc ou usar uma série de regras com
correspondências de extensão. Se a extensão for `md`, use
`pandoc -f gfm` ou `pandoc -f markdown_mmd` (ou apenas retorne
`NOCUSTOM` em STDOUT para usar o processador padrão). Mas se for
`textile`, execute `pandoc -f textile` dentro do script. E se
é `wiki`, use um dos processadores de marcação wiki. Você consegue
a ideia.

Como os aficionados do Pandoc saberão, o Pandoc também pode lidar com
extensa bibliografia e cenários LaTeX. A maioria dos recursos
você pode acessar através da linha de comando estão disponíveis apenas
usando argumentos de passagem em Marcado.

## Usando Têxtil

Algumas pessoas perguntaram como fazer o Têxtil funcionar em
Marcado. Você precisa ter um conversor têxtil disponível em
a linha de comando. Existem algumas opções, incluindo Pandoc
(veja acima), mas se você ainda não tiver o Pandoc instalado,
duas outras opções são RedCloth para Ruby e Textile para Perl
(requer que as Ferramentas do Desenvolvedor estejam instaladas). Instalar
um ou outro:

1. Instale Têxtil de
   <https://github.com/bradchoate/text-textile> **OU**
   `sudo gem install RedCloth` no terminal
2. Use `which textile` ou `which redcloth` para determinar o
   caminho a ser usado nas configurações de caminho do processador personalizado

Now Marked é um visualizador de têxteis para você!

## Usando AsciiDoc

1. Instale [AsciiDoctor](http://asciidoctor.org/).
2. Habilite uma regra personalizada em {% prefspane Processor %} para corresponder aos seus arquivos AsciiDoc.
3. Defina a regra como um processador e adicione uma ação Executar comando
    1. Determine o caminho para `asciidoc`, que será
       algo como `/usr/bin/asciidoc` ou
       `/opt/local/bin/asciidoc`. Se não tiver certeza, use
       `which asciidoc` para localizar
    2. Digite `[PATH To asciidoc] --backend html5 -o - -` como
       o comando (o - no final envia a saída como
       STDOUT)

Isso envia o documento atual para STDIN e exibe o
HTML gerado como STDOUT.

Veja [esta essência](https://gist.github.com/mojavelinux/6324279)
de [Dan Allen](https://gist.github.com/mojavelinux) para
mais informações.