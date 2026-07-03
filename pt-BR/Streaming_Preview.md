<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ao abrir {% appmenu File, New, Streaming Preview %}, Marked recebe atualizações ao vivo em uma área de trabalho nomeada em vez de assistir a um arquivo no disco. O aplicativo de origem deve ser integrado ao Marked.

[Curio](Curio.html), [Drafts](Drafts.html) e [The Archive](The_Archive.html) documentam seus próprios botões de alternância e comandos de menu. nvUltra, nvALT, Bear e outros usam o mesmo canal: abra a visualização do streaming no Marked, habilite a integração em seu editor e comece a digitar; as atualizações chegam quase em tempo real.

## Desenvolvedores

Para integrar o Streaming Preview ao seu aplicativo, você só precisa colocar o texto markdown para visualizar em uma área de transferência nomeada. Use o seguinte código (Objective-C) para atualizar, de preferência em um método didEndEditing ou em intervalos limitados:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Declarando um URL base para ativos relativos

Você também pode fornecer um URL base para a visualização do streaming, permitindo que URLs relativos em imagens e outros ativos funcionem como funcionariam no aplicativo de origem. Se o URL base incluir um nome de arquivo, seu nome e extensão serão disponibilizados para processadores personalizados, mas isso não é obrigatório. Para incluir a URL base, basta colocar um objeto NSURL na área de transferência:

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

Ou em Swift:

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Se a versão do Marked da Mac App Store estiver sendo usada e o baseURL não estiver acessível por meio de sandbox, a permissão será solicitada na primeira vez que o URL for carregado na visualização.

### Declarando o aplicativo de origem

Os aplicativos também podem se declarar como a fonte do conteúdo de visualização incluindo uma linha de metadados `source`. Isso geralmente será feito em um comentário HTML para permitir compatibilidade com processadores GFM e MultiMarkdown. Basta indicar o nome do aplicativo ou o ID do pacote:

```html
<!--
source: Bear.app
-->
```

### Abrindo a visualização do streaming programaticamente

Seu aplicativo pode abrir o Streaming Preview programaticamente usando o método manipulador de URL `x-marked-3://stream/`. Este método também aceita um parâmetro `x-success` no qual você pode passar um ID de pacote de um aplicativo para ativar após a conclusão.