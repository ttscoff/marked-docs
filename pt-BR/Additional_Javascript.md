<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Você pode incluir seu próprio JavaScript de CDNs ou colando código bruto.

## Uma nota sobre o condutor marcado

A maneira mais fácil de implementar JavaScript personalizado que varia entre tipos de documentos e locais é com o [Marked Conductor][conductor]. Ele permite que você use uma configuração YAML para anexar scripts usando “filtros”. Confira a [página do Conductor][condutor] para obter detalhes e veja [configuração de amostra][configuração de amostra] para obter exemplos.

[conductor]: https://brettterpstra.com/projects/conductor/
[sample config]: https://github.com/ttscoff/conductor-config/

## Adicionando JavaScript de CDNs [cdns]

![][1]

   [1]: imagens/capturas de tela/AdditionalJavascript.jpg @2x width=592px height=576px class=center

Você pode adicionar URLs JavaScript CDN na janela "Scripts adicionais", acessível em {% prefspane Style %}. Insira URLs CDN, um por linha. Não inclua nenhuma tag `<script>`, apenas o URL:

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
https://cdn.jsdelivr.net/npm/micromark-extension-gfm-strikethrough@2.1.0/lib/html.min.js
```

> Observe que o jQuery já está incluído na janela de visualização.

Esses scripts serão inseridos no final da visualização, antes da tag do documento. Se você precisar chamar uma função init ou atualizar sempre que a visualização for feita, consulte [Incluindo JavaScript bruto](#rawjs). Para inspecionar o DOM e depurar esses scripts em uma visualização marcada ao vivo, você pode anexar o Web Inspector do Safari conforme descrito em [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).


### Incluindo JavaScript bruto [rawjs]

No campo de texto inferior da janela Scripts Adicionais, você pode inserir JavaScript bruto. Isso será incluído em um par `<script></script>`, portanto não inclua isso na entrada. Este campo pode conter qualquer comando JavaScript necessário para inicializar uma biblioteca incluída, realizar alterações no DOM ou qualquer coisa que você queira fazer em uma visualização do WebKit. jQuery já está incluído para conveniência de manipulação de DOM.

Esses scripts só serão executados quando a janela for carregada pela primeira vez. Quando a visualização é atualizada, isso é feito substituindo partes do DOM, portanto, os scripts que precisam agir no conteúdo atualizado devem fazê-lo usando [Hooks](Embedding_Scripts.html#hooks).

Inclua no campo JavaScript bruto uma chamada como esta:

```javascript
Marked.hooks.register('update', function() { myCustomFunction(); });
```
