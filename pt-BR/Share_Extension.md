<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O Marked inclui uma **extensão Compartilhar** do macOS que aparece no menu Compartilhar do sistema. Use-a para enviar um arquivo ou texto selecionado ao Marked sem trocar de app ou copiar URLs manualmente.

A extensão Compartilhar **vem com o Marked 3**. Você não baixa nem instala separadamente. Ela está incluída nas builds Direct, Mac App Store, Marked Pro e Setapp.

## Como funciona

Quando você escolhe **Marked** em um menu Compartilhar, o Marked abre imediatamente. Não há janela intermediária de composição.

### Compartilhar um arquivo

No **Finder** (ou outro app que compartilha arquivos), escolha **Compartilhar → Marked**.

O Marked recebe o caminho do arquivo e o abre com o mesmo manipulador de URL `x-marked-3://open` usado em outros fluxos. O arquivo abre no Marked como um documento arrastado para o ícone do Dock ou escolhido com {% appmenu File, Open... ({{cmd}}O) %}.

Entradas suportadas incluem URLs de arquivo, arquivos locais e URLs da web quando o app de origem as fornece.

### Compartilhar texto selecionado

Selecione texto em um app como **TextEdit**, **Safari** ou **Mail** e escolha **Compartilhar → Marked**.

O Marked coloca o texto na área de transferência e abre uma **visualização transitória** com o manipulador `x-marked-3://paste`. É o mesmo tipo de visualização não salva de {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Você pode salvá-la depois com {% appmenu File, Save Transient Preview %}.

Texto simples, HTML, RTF e Markdown são suportados quando o app de origem os fornece.

Consulte [URL Handler](URL_Handler.html) para detalhes dos comandos subjacentes.

## Usar o menu Compartilhar

### No Finder

1. Clique com o botão direito em um arquivo Markdown ou de texto (ou selecione-o e clique em **Compartilhar** na barra de ferramentas do Finder).
2. Escolha **Marked** no menu Compartilhar.

Se **Marked** não aparecer, veja [Ativar a extensão Compartilhar](#enable-the-share-extension) abaixo.

### A partir de seleção de texto

1. Selecione o texto que deseja visualizar.
2. Abra o menu **Compartilhar** do app (item Compartilhar, botão na barra ou menu contextual).
3. Escolha **Marked**.

O Marked inicia (ou vem para a frente) com uma visualização do conteúdo compartilhado.

## Ativar a extensão Compartilhar

O Marked deve estar instalado em `/Applications` (ou sua pasta Aplicativos usual) e ter sido aberto pelo menos uma vez antes de o macOS listar sua extensão Compartilhar.

### Ativar Marked em Ajustes do Sistema

1. Abra **Ajustes do Sistema**.
2. Vá em **Geral → Itens de login e extensões** (em algumas versões do macOS: **Privacidade e segurança → Extensões**).
3. Clique em **Extensões** (ou no botão **ⓘ** ao lado de Extensões).
4. Selecione **Compartilhamento** (ou **Sharing**).
5. Ative **Marked**.

### Adicionar Marked ao menu Compartilhar de um app

Mesmo com a extensão ativada em todo o sistema, cada app escolhe quais destinos Compartilhar exibir:

1. Abra um app com Compartilhar (Finder e TextEdit são bons testes).
2. Abra o menu **Compartilhar**.
3. Escolha **Editar extensões…** (em macOS antigos: **Mais…** ou **Preferências de extensões…**).
4. Em **Compartilhar**, marque **Marked**.
5. Opcionalmente arraste **Marked** para cima na lista para acesso mais rápido.

As alterações se aplicam imediatamente na maioria dos apps.

## Se Marked não aparecer em Compartilhar

W> A extensão Compartilhar está disponível a partir do Marked 3.1.9. Certifique-se de ter atualizado pelo menos para essa versão.

Tente estes passos em ordem:

1. **Abra o Marked uma vez** após instalar ou atualizar. Feche e reabra o Marked se acabou de atualizar.
2. **Confirme que a extensão está ativada** em Ajustes do Sistema conforme descrito acima.
3. **Personalize o menu Compartilhar** no app de onde você compartilha. O macOS oculta destinos pouco usados até você ativá-los.
4. **Várias cópias do Marked:** se as builds Direct e Mac App Store estiverem instaladas, só a cópia em execução registra sua extensão. Remova ou renomeie a outra e abra a desejada.
5. **Reinicie o Mac** se a extensão ainda não aparecer após uma atualização. O macOS armazena em cache o registro de extensões Compartilhar.
6. **Reinstale o Marked** em `/Applications` se estiver testando uma build copiada manualmente do Xcode ou de uma imagem de disco. A extensão deve estar em `Marked.app/Contents/PlugIns/`.

## Dicas

- A extensão Compartilhar é ideal para visualizações rápidas de trechos da web, parágrafos de e-mail ou notas sem criar um arquivo primeiro.
- Para páginas inteiras ou seleções complexas no navegador, as [extensões do navegador](Using_the_Browser_Extensions.html) podem oferecer mais controle (seleção de seção, Markdownify URL etc.).
- Arquivos compartilhados abrem como documentos normais do Marked com monitoramento de arquivo. Texto compartilhado abre como visualização transitória até você salvar.
