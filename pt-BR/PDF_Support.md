<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado pode abrir documentos PDF (`.pdf`) diretamente. Arraste um arquivo para Marcado ou use {% appmenu File, Open... ({{cmd}}O) %}. O documento é convertido em Markdown para visualização e exportação.

A importação de PDF funciona melhor em **PDFs menores baseados em texto** (slides, artigos, relatórios curtos). Manuais grandes, livros e documentos digitalizados são suportados, mas muitas vezes a conversão é lenta ou imperfeita. Consulte **Limitações** abaixo.

Marcado ainda é uma ferramenta de **visualização**: você não edita o PDF dentro do Marcado. Use {% kbd cmd E %} para abrir o PDF em **Visualização** (ou no padrão do sistema) e Marcado como atualizado quando o arquivo é alterado no disco.

## Como funciona a conversão

A importação de PDF usa a biblioteca [pdf22md](https://github.com/twardoch/pdf22md) (Licença MIT; consulte [Licença pdf22md](PDF22MD_License.html)). Marcado executa a conversão em segundo plano enquanto mostra um breve aviso de **Conversão**.

O conversor:

- Extrai **texto** de PDFs digitais usando PDFKit
- Usa **Vision OCR** em páginas onde falta texto incorporado (comum em digitalizações)
- Detecta **títulos** do tamanho da fonte quando possível
- Salva **imagens** em uma pasta `assets` próxima ao Markdown gerado

Marcado **não** habilita a limpeza opcional de IA do pdf22md no aplicativo. A qualidade da conversão depende de como o PDF foi criado.

## Cache e visualização ao vivo

O Markdown convertido e as imagens são armazenados no cache do Marked's Watchers (`~/Library/Caches/Marked/Watchers/PDF/`). O caminho original do PDF permanece a origem do documento para visualização de arquivos.

Quando você salva ou substitui o PDF em outro aplicativo, o Marked detecta a alteração e reconverte automaticamente (mesmo comportamento de recarga unida de [RTF](RTF_Support.html) e [Scrivener](Scrivener_Support.html)).

## Exportação e outros recursos

Após a conversão, Marked trata o documento como outras fontes compiladas: exportação, estatísticas e a maioria dos recursos de visualização são executados no Markdown gerado. Os caminhos da imagem na visualização apontam para os ativos armazenados em cache até você exportar.

## Limitações

Defina suas expectativas de acordo – PDF-to-Markdown é útil, não perfeito.

**O que funciona bem**

- **PDFs vetoriais e baseados em texto** com texto real incorporado (exportado do Word, Pages, InDesign, etc.)
- **Comprimento moderado** — algumas dezenas de páginas geralmente são convertidas em um tempo razoável com boa estrutura

**O que não é confiável**

- **OCR (PDFs digitalizados)** — O Vision preenche texto ausente, mas a precisão geralmente é baixa em comparação com uma ferramenta de OCR dedicada; espere erros de digitação, palavras quebradas e colunas perdidas
- **Tabelas** — o layout é adivinhado a partir das posições do texto; células mescladas, tabelas aninhadas e grades complexas raramente sobrevivem como tabelas Markdown limpas
- **Posicionamento da imagem** — as figuras são extraídas para `assets/`, mas o alinhamento, as legendas e o texto em torno das imagens não são preservados de forma confiável

**Tamanho e desempenho**

- **PDFs grandes** (guias do usuário, livros didáticos, manuais longos) podem levar **muito tempo** para serem convertidos, usar memória substancial ou não produzir Markdown útil. Marcado permanece responsivo enquanto a conversão é executada em segundo plano, mas não há garantia de que um manual de 500 páginas será concluído com sucesso
- Se a conversão for concluída com pouco ou nenhum conteúdo, Marcado mostra um erro em vez de deixar uma visualização em branco

**Outros limites**

- **PDFs protegidos por senha** não são suportados na v1
- **Imagens PDF incorporadas no Markdown** (`![]()` referenciando um arquivo `.pdf`) não estão relacionadas à importação de PDF — apenas abrir um `.pdf` quando o documento principal aciona a conversão

Para documentos do Word, use [Trabalhando com DOCX](Working_with_DOCX.html). Para Rich Text, use [Suporte RTF e RTFD](RTF_Support.html).

## Tópicos relacionados

- [Abrindo arquivos](Opening_Files.html) — arrastar e soltar, Abrir recente, área de transferência
- [Exportando](Exporting.html) — salve HTML, PDF, DOCX e Markdown da visualização
- [Licença pdf22md](PDF22MD_License.html) — texto da licença MIT de terceiros