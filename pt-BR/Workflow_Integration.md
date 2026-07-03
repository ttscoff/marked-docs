<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## AppleScript

Marked inclui um [dicionário AppleScript](AppleScript_Support.html) completo para abrir arquivos, controlar a visualização (recarregar, rolar, realçar, rolagem automática, leitura rápida), ler estatísticas, configurar processadores, copiar HTML ou RTF, alterar estilos de visualização e exportar para Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF e OPML. **A visualização dos títulos/índice** via AppleScript está [documentada como trabalho em andamento](AppleScript_Support.html#table-of-contents-work-in-progress) e ainda não é confiável.

Você pode direcionar o aplicativo, uma janela específica ou um documento. Os comandos do aplicativo incluem **abrir visualização de streaming**, **visualizar área de transferência** e **fechar tudo**. Os comandos de documento incluem **obter estatísticas** e **imprimir com perfil**. Os comandos de exportação aceitam um **perfil** de exportação opcional ou um registro **`with`** para opções como visualização **estilo**, **pageSize** e **margens**. Por exemplo:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Consulte [Suporte AppleScript](AppleScript_Support.html) para obter a lista de comandos, abreviações de margem, notas de sandbox e dicas de depuração.

A integração AppleScript também permite que aplicativos como Tags.app funcionem diretamente no Marked.

{% note %}
## Atalhos

Marcado inclui [ações de atalhos](Shortcuts_Integration.html) nativas no macOS 13 ou posterior. Use **Abrir e exportar arquivo** para fluxos de trabalho do Finder para PDF, **Exportar documento** para o que já estiver aberto no Marcado ou **Definir estilo de visualização** para alterar os temas antes da exportação. As ações de exportação aceitam **perfis**, **estilos** de visualização e opções como **tamanho da página**, **margens** e **tamanho da fonte** (mesma semântica dos registros AppleScript `with`).

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## Manipulador de URL

O [manipulador de URL marcado] [urlhandler] permite integração extensiva simplesmente chamando URLs, seja de AppleScript ou com um comando `open` básico em um script de shell.

## Pacote de bônus marcado

O Marked Bonus Pack é uma coleção de scripts, comandos e serviços. Alguns trabalham com vários editores, alguns são específicos para determinados editores. Os Serviços geralmente funcionarão com qualquer editor que possua os recursos necessários. O restante é organizado em pastas com base no aplicativo com o qual trabalha.

Você pode baixar o Bonus Pack e encontrar instruções para instalá-lo e usá-lo neste [artigo da base de conhecimento](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html