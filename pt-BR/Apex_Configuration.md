<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Estas opções ficam na folha **Configurar Apex**. Abra-a em {% prefspane Processor %} quando o processador padrão for **Apex (beta)**. Cada opção vale só para o Apex. Matemática, Critic Markup, hashtags, inclusões de arquivo e IDs de títulos continuam nos outros ajustes do Marked.

Veja [Apex (beta)](Apex.html) para o que o Apex é e a sintaxe que ele cobre.

As caixas da folha têm prioridade sobre os mesmos ajustes de um arquivo de metadados do Apex. Caminhos de arquivo são opcionais. Um caminho que o Marked não consegue ler é ignorado, e a prévia continua.

## Arquivos [files]

CSL
: Um arquivo Citation Style Language (`.csl`) usado quando o Apex formata uma bibliografia. Deixe vazio para usar o estilo indicado no documento ou no arquivo de metadados.

Bibliografia
: Um ou mais arquivos de bibliografia. Tipos aceitos: BibTeX (`.bib`), CSL JSON (`.json`) e CSL YAML (`.yml`, `.yaml`). Clique em **Add** para outro arquivo. O Apex os consulta ao resolver citações.

Concordância
: Um ou mais arquivos de concordância (`.tsv`, `.txt` ou `.csv`) usados ao montar um índice. Clique em **Add** para outro arquivo.

Arquivo de metadados
: Um arquivo externo de metadados (`.yml`, `.yaml`, `.txt` ou `.md`) mesclado antes de o Apex rodar. Se o documento e o arquivo definirem a mesma chave, os metadados do documento prevalecem. As caixas desta folha prevalecem sobre os valores do arquivo de metadados.

## Sintaxe [syntax]

Ligadas por padrão, salvo indicação em contrário.

Tabelas
: Tabelas com barras, incluindo uma linha de cabeçalho e uma linha separadora.

Notas de rodapé
: Notas de referência (`[^id]`) e notas inline.

Listas de definição
: Listas de termo e definição (`: definição`).

Sobrescrito / subscrito
: `^super^` e `~sub~`. Desligue se um til sozinho não deve significar subscrito. O ajuste do Marked **Renderizar ~text~ como sublinhado** é separado e conflita com o subscrito.

Riscado
: `~~removido~~`.

Autolink de URLs e e-mails
: URLs `https://` e endereços de e-mail soltos viram links.

Divs cercados
: Blocos `::: nome` que envolvem uma seção em um `<div>`.

Spans entre colchetes
: Spans de atributo inline, como `[texto]{.class}`.

Listas alfabéticas
: Listas que começam com `a.` ou `A.`, além dos números.

Marcadores de lista mistos
: Uma lista pode misturar `*`, `+` e `-` e continuar sendo uma só lista.

Markdown em HTML
: Markdown dentro de tags de bloco HTML é processado. Alguma marcação ainda pode quebrar.

Transformações de metadados
: Marcadores `[%key]` são substituídos pelos metadados do documento.

## Tabelas e imagens [tables-and-images]

Tabelas em grade
: Tabelas desenhadas com `+` e `|`. Desligadas por padrão.

Tabelas relaxadas
: Tabelas com barras podem omitir as barras inicial e final. Ligadas por padrão.

Alinhamento por célula
: Marcadores de alinhamento numa célula substituem o alinhamento da coluna. Ligado por padrão.

Legendas de imagem
: O título da imagem, ou o texto alternativo se não houver título, vira uma legenda visível. Ligado por padrão.

Somente legendas de título
: Só o título da imagem é usado como legenda. O texto alternativo é ignorado. Desligado por padrão. Não tem efeito se **Legendas de imagem** estiver desligado.

## Links e índices [links-and-indexes]

Links wiki
: O Apex converte `[[links wiki]]`. Desligado por padrão. Quando está ligado, o Marked pula a própria passagem de prévia "Converter links wiki" nesse documento, e o Apex pode resolver o arquivo de destino de um jeito diferente do Marked. A extensão padrão vem dos ajustes de links wiki do Marked.

Sanear URLs de links wiki
: As URLs geradas ficam em minúsculas, apóstrofos são removidos e outros caracteres que não são letras nem números são substituídos. Desligado por padrão. Disponível só quando **Links wiki** está ligado.

Processamento de índice
: Reconhece marcadores de índice (estilos MultiMarkdown, mmark, Leanpub e textindex). Ligado por padrão.

Suprimir a saída do índice
: Ainda lê os marcadores, mas não imprime o índice gerado. Desligado por padrão.

## Chamadas (extra) [callouts-extra]

As duas ficam desligadas por padrão. Chamadas do Obsidian e do Bear (`> [!NOTE]`) são tratadas pelo Marked antes do Apex e não se controlam aqui.

Chamadas Python-Markdown (!!!)
: Chamadas no estilo `!!! note`.

Chamadas Quarto
: Blocos Quarto `::: {.callout-note}`.

## Acessibilidade [accessibility]

As duas ficam desligadas por padrão.

Rótulos ARIA
: Adiciona atributos ARIA que descrevem a estrutura do HTML emitido pelo Apex.

Âncoras de título
: Emite uma âncora `<a>` em cada título em vez de só um `id` no título.
