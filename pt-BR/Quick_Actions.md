<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A paleta Ações Rápidas é um iniciador de comando pesquisável para Marcado. Ele coleta ações da barra de menu principal e do **menu de engrenagem** de visualização, além de comandos de teclado somente de visualização que não aparecem nos menus (como **Rolagem automática**). Use-o quando você sabe o que quer fazer, mas não consegue lembrar qual menu o contém.

## Abrindo a paleta de ações rápidas [opening-the-quick-actions-palette]

Abra a paleta com {% kbd shift cmd P %} ou de {% appmenu File, Quick Actions… %}. O painel aparece como uma janela flutuante acima do documento atual.

Pressione o mesmo atalho novamente ou pressione **Escape** para fechar a paleta. Se a paleta já estiver aberta, escolher **Ações Rápidas…** no menu também a fecha.

## Personalizando o atalho [customizing-the-shortcut]

O atalho padrão é {% kbd shift cmd P %}. Para alterá-lo, abra {% prefspane General %} e grave uma nova combinação em **Abrir Paleta de Ações** na seção **Atalhos**.

Ao contrário de **Ativar Marcado** e **Abrir primeira janela**, o atalho de Ações Rápidas funciona apenas quando Marcado é o aplicativo ativo. Ele atualiza o atalho do menu {% appmenu File, Quick Actions… %} para corresponder à sua configuração.

## Pesquisa e filtro [search-and-filter]

Digite no campo de pesquisa na parte superior do painel para filtrar comandos em tempo real. A correspondência é confusa e indulgente:

- A ordem das palavras não importa (`view source` corresponde a **Alternar visualização da fonte**)
- As iniciais funcionam bem (`sv` corresponde a **Visualização de origem**)
- A correspondência recolhida encontra comandos sem espaços (`akdoc` corresponde a **Perguntar sobre o documento**)

Cada resultado mostra o nome do comando à esquerda e seu atalho de teclado (quando disponível) à direita em cinza. Alguns comandos também mostram um caminho de navegação (por exemplo `Preview › Autoscroll`) quando a ação vem de um submenu ou do mecanismo de visualização.

## O que aparece na lista [what-appears-in-the-list]

A paleta inclui:

- **Comandos de menu** na barra de menu principal, incluindo menus dinâmicos como **Estilo**, **Histórico** e guias abertas de **Janelas**
- Comandos do **menu de engrenagem** da janela de visualização
- **Atalhos de visualização** do mapa de teclado em visualização (os mesmos comandos mostrados no HUD de ajuda de visualização), incluindo navegação, rolagem automática, marcadores, pesquisa e outras ações somente de visualização

Quando o mesmo comando aparece em mais de um lugar, Marcado mostra o caminho de menu mais curto e mescla informações de atalho de duplicatas.

## Navegação pelo teclado [keyboard-navigation]

Navegue pela paleta Ações Rápidas inteiramente a partir do teclado:

- **↑/↓ Teclas de seta**: Percorrer a lista filtrada
- **Return**: Execute o comando selecionado
- **Escape**: Fecha a paleta
- **⌘-teclas de atalho**: Feche a paleta e execute o comando de menu correspondente (por exemplo, pressione {% kbd cmd U %} para executar **Toggle Source View** em vez de selecioná-lo na lista)

A digitação simples (sem a tecla Command) filtra o campo de pesquisa. Atalhos de tecla única somente para visualização, como `s` para rolagem automática, filtram a lista; pressione **Return** para executar o comando selecionado.

## Executando Comandos [running-commands]

Selecionar um comando de menu o despacha da mesma forma que escolhê-lo no menu, incluindo itens de menu dinâmicos e de engrenagem.

Selecionar um **atalho de visualização** executa a ação associada na visualização ativa (por exemplo, alternar a rolagem automática ou pular para o próximo cabeçalho). Esses comandos requerem um documento aberto com visualização; se nenhuma visualização estiver disponível, a paleta ainda será aberta, mas as ações somente de visualização não terão efeito.

Para a troca de arquivos relacionada, consulte [Abertura Rápida](Quick_Open.html). Para obter a referência completa do teclado de visualização, consulte [Atalhos de teclado](Keyboard_Shortcuts.html) ou pressione {% kbd h %} na visualização para mostrar o HUD de ajuda.