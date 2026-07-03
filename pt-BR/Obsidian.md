<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked funciona com notas do [Obsidian][obsidian-app] de duas maneiras: abra uma **pasta do cofre** para acompanhamento automático ou use o **plugin da comunidade** para uma sincronização mais precisa.

A visualização integrada do Obsidian é ideal quando você nunca sai do aplicativo. Escolha Marcado quando desejar exportação com qualidade de publicação, revisão avançada, temas CSS personalizados ou o mesmo fluxo de trabalho de visualização ao vivo em vários editores. Veja [Visualização Marcada vs Obsidian](Marked_vs_Obsidian_Preview.html) para uma comparação completa.

## Abra um cofre inteiro

Arraste a **pasta do vault** (o diretório que contém a pasta de configuração oculta do Obsidian na raiz do vault) para Marcado no Dock. Marcado observa aquela árvore, mantém a nota **editada mais recentemente** na visualização e atualiza conforme você salva no Obsidian.

Para padrões específicos do vault (estilo, processador, URL base para imagens e assim por diante), adicione uma [Regra personalizada](http://support.markedapp.com) que corresponda aos caminhos nesse vault.

## Sintaxe de texto explicativo Obsidian

Quando o processador MultiMarkdown é executado, Marked converte **textos explicativos no estilo Obsidian** comuns (o padrão `> [!note]`) em marcação de bloco estilizada para que correspondam ao restante da sua visualização.

## Plugin Obsidian marcado como 3

O [plugin Marked 3 Obsidian][plugin] pode abrir a nota atual ou todo o vault com comandos ou teclas de atalho para que a janela Marcada rastreie o que você está editando. Use a paleta de comandos (**⌘P**) e pesquise **Marcado** ou atribua teclas de atalho nas configurações de **Teclas de atalho** do Obsidian.

### Instalando a partir de plug-ins da comunidade

No Obsidian, abra **Configurações → Plug-ins da comunidade**, navegue ou pesquise **marcado** e instale **Abrir em Marcado**.

### Instalando manualmente o plugin

Se você preferir instalar do GitHub:

1. Baixe `main.js` e `manifest.json` do [latest release][plugin-releases] no GitHub (ou construa-os a partir do repositório [Marked3-obsidian][plugin]).
2. Em seu vault, crie a pasta do plugin em `plugins/` dentro do diretório de configuração do Obsidian na raiz do vault. O nome da pasta deve corresponder ao plugin `id` em `manifest.json` (veja o [plugin README][plugin] para o caminho completo).
3. Copie `main.js` e `manifest.json` para essa pasta.
4. No Obsidian, abra **Configurações → Plug-ins da comunidade**, desative o **Modo restrito** se necessário e ative **Abrir em marcados**.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest