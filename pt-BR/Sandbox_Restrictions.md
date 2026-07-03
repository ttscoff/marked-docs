<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A versão Mac App Store (MAS) do Marked é executada em um ambiente de área restrita que restringe certas operações por motivos de segurança. Isso pode afetar alguns recursos, principalmente ao usar processadores personalizados com binários ou scripts externos.

## Restrições comuns de sandbox

### Executar binários de comando

O problema mais comum que os usuários encontram é que os binários externos não podem ser executados diretamente na versão MAS. Isso afeta:

- **Processadores externos** como Pandoc, Kramdown ou outras ferramentas de linha de comando
- **Scripts personalizados** que dependem de binários externos
- **Utilitários do sistema** que não podem ser acessados no sandbox

### Soluções alternativas

#### Copiando binários para o pacote de aplicativos

Se precisar usar processadores externos como Pandoc na versão MAS, você pode copiar o binário no pacote de aplicativos:

1. Clique com o botão direito em Marked.app → **Mostrar conteúdo do pacote**
2. Navegue até **Conteúdo/Recursos/**
3. Crie uma pasta `bin` se ela não existir
4. Copie seu binário (por exemplo, `pandoc`) para esta pasta `bin`
5. Torne-o executável: `chmod +x` o binário
6. Na ação Executar Comando, referencie-o como:
   - `YOUR_BINARY_NAME [arguments]`
   - Ou use o caminho completo: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Nota**: Scripts com shebangs externos (como scripts Python apontando para `/opt/homebrew/bin/python`) serão executados automaticamente através de interpretadores do sistema quando copiados para o pacote. A versão MAS ainda pode ter problemas para executar binários que na verdade são scripts Python ou Ruby em vez de arquivos binários.

**Importante**: você precisará copiar novamente os binários após cada atualização do aplicativo, pois as atualizações substituem todo o pacote.

#### Usando scripts incorporados

Em vez de executar comandos externos, você pode usar a ação **Run Embedded Script** em Regras Personalizadas. Isso permite que você escreva scripts diretamente no editor de código do Marked, que pode acessar interpretadores de sistema disponíveis na sandbox.

## Mudando para a versão sem sandbox [crossgrade]

Se você precisa usar binários externos com frequência ou encontrar outras limitações de sandbox, você pode querer mudar para a versão sem sandbox do Marked. A versão sem sandbox não tem tais restrições e pode executar qualquer ferramenta ou script de linha de comando que você tenha instalado.

### Para usuários assinantes

Se você tiver uma assinatura ativa da Mac App Store:

1. **Cancele sua assinatura MAS** em Configurações do sistema → ID Apple → Mídia e compras → Assinaturas
2. **Baixe a avaliação gratuita** em [https://markedapp.com](https://markedapp.com)
3. **Inicie uma assinatura do Paddle** diretamente pelo aplicativo ou site

A versão Paddle oferece os mesmos recursos sem restrições de sandbox.

### Para detentores de desbloqueio permanente

Se você adquiriu um desbloqueio permanente ou uma licença vitalícia através da Mac App Store, envie um e-mail para desenvolvedor](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Por favor%20include%20your%20UUID%20%28Help-%3ECopy%20UUID%20in%20Marked%29%20in%20this%20email%20for%20receipt%20verification.) para solicite uma licença vitalícia gratuita do Paddle.

**Importante**: Para verificar sua compra, inclua um dos seguintes itens em seu e-mail:

- Seu **identificador de usuário** (UUID) - use **Ajuda->Copiar UUID** para copiá-lo para sua área de transferência e cole-o em seu e-mail
- Seu **ID de transação** no recibo da App Store (você pode encontrá-lo em seu histórico de compras no aplicativo App Store)

A Mac App Store não fornece seu endereço de e-mail aos desenvolvedores, por isso verificamos as compras usando IDs de transação ou identificadores de usuário armazenados em nosso servidor. A inclusão dessas informações nos ajudará a verificar rapidamente sua compra e gerar sua licença Paddle gratuita.

### Versão do Setapp

Como alternativa, se você tiver uma assinatura do Setapp, poderá usar a versão Setapp do Marked, que também não está em sandbox e tem acesso total aos recursos do sistema.

## Recursos Adicionais

Para obter mais informações sobre Processadores Personalizados e seus recursos, consulte [Processador Personalizado](Custom_Processor.html).