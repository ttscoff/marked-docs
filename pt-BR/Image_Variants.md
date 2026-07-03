<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O Marked pode criar automaticamente elementos `<picture>` responsivos para imagens locais quando os arquivos complementares **modo escuro** e **Retina** ficam próximos à imagem que você refere. Isso usa as mesmas convenções de nomenclatura dos catálogos de documentação DocC da Apple, mas funciona para **qualquer documento Markdown ou HTML** com caminhos de imagem normais que incluem uma extensão de arquivo.

Veja também [Suporte DocC](DocC_Support.html) para referências de catálogo sem extensão dentro de pacotes `.docc`.

## Habilitando variantes de imagem

Em {% prefspane Apps %}, ative **Resolver variantes de imagem escura e @2x** (ativado por padrão) nas configurações de DocC.

Esta preferência é separada de **Resolver referências de imagens DocC**, que se aplica apenas dentro dos catálogos `.docc`. Você pode usar um, ambos ou nenhum, dependendo do seu projeto.

## Convenção de nomenclatura

Coloque os arquivos variantes na **mesma pasta** da imagem principal. Marcado procura quatro combinações baseadas no nome base:

| Função | Exemplo de nome de arquivo |
|------|------------------|
| Luz (1x) | `icon.png` |
| Escuro (1x) | `icon~dark.png` |
| Luz (2x) | `icon@2x.png` |
| Escuro (2x) | `icon~dark@2x.png` |

A ordem dos sufixos é flexível — `icon@2x~dark.png` e `icon~dark@2x.png` são tratados da mesma maneira.

Extensões suportadas: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` e `pdf`.

## O que é reescrito

Marcado digitaliza seu documento **antes** da renderização da visualização final:

- **Marcação:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

Se existirem pelo menos **dois** arquivos variantes correspondentes no disco, a referência será substituída por um bloco `<picture>`. Um único arquivo extra é suficiente – você não precisa de todas as quatro variantes.

Exemplo de saída quando arquivos claros, escuros e @2x estão presentes:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

A visualização (e a exportação de HTML) segue a aparência do sistema do usuário para variantes escuras e a densidade de pixels do dispositivo para ativos @2x.

## O que é ignorado

Marcado **não** reescreve:

- URLs remotos (`http://`, `https://`, `data:`)
- Referências que já apontam para um arquivo `~dark`
- Tags `<img>` já dentro de um elemento `<picture>` existente
- Nomes sem extensão como `![Diagram](diagram)` — use [Suporte DocC](DocC_Support.html) para referências de estilo de catálogo

## Visualização ao vivo e visualização de arquivos

Quando variantes são detectadas, Marked adiciona **todos os arquivos de variantes existentes** à sua lista de observação junto com o documento principal. Salvar `icon~dark.png` em um editor externo aciona o mesmo recarregamento de imagem ao vivo que a edição `icon.png`.

## Dicas

- Faça referência à imagem **light 1x** em sua fonte quando possível (`icon.png`, não `icon~dark.png`). Marked descobre irmãos desse caminho.
- Se você tiver apenas ativos `@2x`, inclua pelo menos uma outra variante (normalmente `~dark`) ou Marcado deixará a referência inalterada.
- A resolução variante usa caminhos **relativos ao documento** (ou à pasta do arquivo incluído para inclusões aninhadas), as mesmas regras de caminho base de [Documentos com vários arquivos](Multi-File_Documents.html).

## Tópicos relacionados

- [Suporte DocC](DocC_Support.html) — nomes de imagens sem extensão dentro de catálogos `.docc`
- [Configurações: Aplicativos](Settings_Apps.html) — alterna preferências para DocC e variantes de imagem
- [Pré-visualização](Previewing.html) — visualização ao vivo e atualizações de arquivos