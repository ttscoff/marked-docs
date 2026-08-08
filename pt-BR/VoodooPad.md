<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[VoodooPad][vp] agrupa cada página em um único arquivo de banco de dados. Arraste o `.vpdoc` para Marcado para visualizar a página que está atualmente em primeiro lugar no VoodooPad; use {% kbd cmd S %} no VoodooPad sempre que precisar do Marked para recarregar do disco.

Marcado monitora o documento no disco e troca a visualização quando você muda de página dentro do VoodooPad.

## Imagens incorporadas [embedded-images]

Quando você faz referência a imagens com Markdown ou HTML e o binário reside **dentro** do banco de dados VoodooPad, Marked pode extraí-lo para visualização. Imagens que são apenas **aliases** (arquivos arrastados por referência) não são armazenadas no pacote — aponte para aquelas com caminhos absolutos ou caminhos relativos ao `.vpdoc` no disco para que Marcado possa resolvê-los.

[vp]: https://www.voodoopad.com/