<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked inclui um sistema de navegação wiki que permite alternar rapidamente entre arquivos de texto relacionados usando links `[[wiki]]` simples. Este sistema foi projetado para uma navegação contínua e funciona melhor quando configurado para abrir links na janela atual.

## Configurações ideais

Para usar links wiki, habilite **Convert `[[wiki links]]`** em {% prefspane Preview %} e defina a extensão padrão que Marked usará ao procurar por arquivos correspondentes.

Para obter a melhor experiência, defina **"Links para arquivos de texto devem abrir em:"** para *"a janela atual"* em {% prefspane Apps %}. Isso garante que a navegação pareça natural e a história seja preservada.

Se **Realçar erros de sintaxe do Markdown** estiver habilitado em {% prefspane Proofing %}, a sintaxe `[[wiki link]]` que não corresponde a um nome de arquivo no diretório atual será destacada em vermelho para indicar que um arquivo referenciado não existe. Esses destaques serão atualizados à medida que os arquivos forem adicionados, mas somente depois que o arquivo atual for salvo ou recarregado. Clicar em um link de arquivo ausente destacado oferecerá a criação de um novo arquivo para você, acrescentando a extensão padrão, se necessário. O novo arquivo vazio será aberto em Marcado, e se Editar Novos Documentos estiver habilitado, seu editor será aberto com o novo arquivo.

## Como funcionam os links Wiki

- **Links Wiki** usam o formato: `[[wiki link]]`.
- Quando você clica em um link wiki, o Marked irá procurar um arquivo correspondente no **mesmo diretório** do documento atual.
- O arquivo deve ter a extensão especificada nas configurações do Marked (por exemplo, `.md`), a menos que você forneça um nome de arquivo completo com extensão no link (por exemplo, `[[notes.txt]]`).
- Se você quiser usar um texto para o link diferente do nome do arquivo, adicione-o após uma barra vertical (`|`) no link, por exemplo. `[[wiki linking|A note about linking]]`, que será exibido como `[A note about linking](wiki-link.md)`.
- Se um link wiki começar com `#`, ele será visto como um link âncora na mesma página. Os nomes das âncoras são normalizados por letras minúsculas e substituindo todos os espaços por travessões. Para processadores que criam IDs de cabeçalho sem travessões (como MultiMarkdown), por exemplo. `## wiki links` recebe um id de `wikilinks`, esta navegação pode falhar. Nesses casos, especifique o ID do link correto, com uma barra vertical e um título, se necessário, por exemplo. `[[#wikilinks|#wiki links]]`.

### Nomes de arquivos correspondentes

Quando você usa um link como `[[wiki link]]`, Marked irá procurar por um arquivo com qualquer um dos seguintes nomes (assumindo que sua extensão padrão seja `.md`):

- `wiki link.md`
- `WikiLink.md`
- `wiki-link.md`
- `Wiki-Link.md`
- `wiki_link.md`
- `Wiki_Link.md`
- `wikilink.md`
- `WikiLink.md`
- (e outras combinações de espaços, travessões, sublinhados e InterCaps)

**Todas as correspondências não diferenciam maiúsculas de minúsculas e são flexíveis com separadores.**
Se você especificar uma extensão no link (por exemplo, `[[notes.txt]]`), Marcado procurará exatamente esse arquivo.

## Backlinks

Quando um arquivo de texto é aberto e a navegação wiki está habilitada, o restante dos arquivos no diretório será verificado em `[[links]]` para o arquivo atual. Isso acontecerá em segundo plano e o documento aberto será atualizado com uma lista de backlinks, se algum for encontrado. Para visualizar os backlinks, a barra lateral de comentários deve estar aberta. Se estiver fechado, use o menu de engrenagem (**Revisão->Mostrar comentários**) ou pressione {% kbd ^@c %} para abri-lo.


## Histórico de navegação

Marcado rastreia sua navegação por meio de links wiki, permitindo que você retroceda e avance** no histórico de arquivos, como um navegador da web.

- **Voltar:** {% kbd @[ %}
- **Avançar:** {% kbd @] %}

Você também pode usar o menu **Histórico** para acessar qualquer arquivo visitado anteriormente.