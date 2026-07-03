<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A velocidade geral de renderização e o desempenho do Marked podem variar muito com base nas configurações e no tipo de conteúdo do documento. Existem vários fatores que podem levar a uma renderização lenta ou a longos atrasos:

* **Time Machine.** Se o Time Machine estiver em execução e seu sistema estiver enfrentando muita atividade de disco, você poderá achar que Marked é mais lento para responder às alterações em seu documento. A velocidade de processamento não é afetada, apenas o tempo de reação.
* **Renderizando um documento Markdown contendo muito HTML.** Isso sempre levará mais tempo para ser processado. O Discount lida com isso um pouco melhor do que o MultiMarkdown, então, se isso for uma necessidade, você pode considerar alterar o processador padrão (**Advertência:** você perderá notas de rodapé e alguns outros recursos do MultiMarkdown).
* **Usando muitas inclusões.** Sejam inclusões de código ou um arquivo de mesclagem de índice, coletar todas as peças leva um segundo. O mesmo se aplica a documentos grandes do Scrivener. Não há muito que você possa fazer para corrigir isso, o Marked apenas fará o possível para acompanhar a maneira como você escolhe estruturar seu documento.
* **Condição do disco rígido.** Se o seu disco rígido estiver quase cheio, o índice do Spotlight estiver corrompido ou suas permissões não forem reparadas há algum tempo, o Marked pode ter mais dificuldade em captar as alterações no arquivo que está monitorando. Otimizar sua unidade reparando permissões geralmente ajuda, e reconstruir o índice Spotlight costuma ser uma solução para problemas marcados.