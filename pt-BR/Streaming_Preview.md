<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ao abrir {% appmenu File, New, Streaming Preview %}, Marked recebe atualizações ao vivo em uma área de trabalho nomeada em vez de assistir a um arquivo no disco. O aplicativo de origem deve ser integrado ao Marked.

[Curio](Curio.html), [Drafts](Drafts.html) e [The Archive](The_Archive.html) e [Traverse](Traverse.html) documentam seus próprios botões de alternância e comandos de menu. nvUltra, nvALT, Bear e outros usam o mesmo canal: abra a visualização do streaming no Marked, habilite a integração em seu editor e comece a digitar; as atualizações chegam quase em tempo real.

## Desenvolvedores [developers]

Para integrar o Streaming Preview ao seu aplicativo, você só precisa colocar o texto markdown para visualizar em uma área de transferência nomeada. Use o seguinte código (Objective-C) para atualizar, de preferência em um método didEndEditing ou em intervalos limitados:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Declarar o app de origem e o formato [declaring-the-origin-app-and-format]

Coloque uma palavra-chave `source` ou `format` em um comentário HTML no início do texto enviado. O Marked lê o comentário e o remove da visualização, então a nota continua compatível com os processadores GFM e MultiMarkdown. O espaço depois dos dois-pontos é opcional (`source:Bear.app` e `source: Bear.app` são iguais), e a palavra-chave ignora maiúsculas e minúsculas.

Os dois valores são livres. O Marked tem um comportamento embutido para alguns deles, e todo valor fica disponível no [Custom Processor](Custom_Processor.html) (Conductor) como **Origem da visualização em streaming** e **Formato da visualização em streaming**. Esses critérios aceitam **é**, **não é**, **contém** e **não contém**.

**`source: APP_NAME`** nomeia o app de origem, pelo nome do app ou pelo bundle id. O Marked usa isso para acrescentar um tratamento especial para esse app. `source: Bear.app` e `source: Drafts.app` ligam o comportamento de visualização desses apps. Qualquer outro nome ainda pode ser comparado por uma regra do Conductor, para você executar suas próprias ações para esse app:

```html
<!--source:Bear.app-->
```

**`format: fountain`** liga o tratamento de [Fountain](Fountain_for_Screenwriters.html), então o fluxo é visualizado como um roteiro em vez de Markdown. Qualquer outro valor de formato não muda o processador. Ele existe para uma regra do Conductor comparar, por exemplo **Formato da visualização em streaming** `é` `fountain`.

```html
<!--format:fountain-->
```

Um comentário pode levar as duas palavras-chave:

```html
<!--
source: Bear.app
format: fountain
-->
```

### Abrindo a visualização do streaming programaticamente [opening-the-streaming-preview-programatically]

Seu aplicativo pode abrir o Streaming Preview programaticamente usando o método manipulador de URL `x-marked-3://stream/`. Este método também aceita um parâmetro `x-success` no qual você pode passar um ID de pacote de um aplicativo para ativar após a conclusão.