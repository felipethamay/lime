# Lime

O Lime é capaz de explicar qualquer classificador de caixa preta, com duas ou mais classes. É necessário que o classificador implemente uma função que receba um texto bruto ou um array numpy e produza uma probabilidade para cada classe. O suporte para classificadores scikit-learn é integrado.

<br>

O Lime é baseado no trabalho apresentado [neste artigo](https://arxiv.org/abs/1602.04938) ([bibtex here for citation](https://github.com/marcotcr/lime/blob/master/citation.bib)). Aqui está um link para o vídeo promocional:

<a href="https://www.youtube.com/watch?v=hUnRCxnydCc" target="_blank"><img src="https://raw.githubusercontent.com/marcotcr/lime/master/doc/images/video_screenshot.png" width="450" alt="KDD promo video"/></a>

<br>
<br>

## Notebooks
Nos notebooks é aplicado os conceitos de análise e compreensão de texto, mais especificamente, em dados de filmes. Existem diversas técnicas para realizar análise de texto, neste utilizamos algumas técnicas de vetorização e processamento de dados para poder classificar como positiva ou negativa as avaliações do IMDB sobre filmes. IMBD significa Internet Movie Database (do portugues, Banco de dados de filmes da Internet), onde é uma base de dados online de informação sobre música, cinema, filmes, programas e comerciais para televisão e jogos de computador, hoje pertencente à Amazon.

Descrição dos dados:

- id: Atributo identificador
- text_en: Texto sobre o filme em inglês
- text_p: Texto sobre o filme em portugues
- sentiment: Variável alvo referente a classificação como positiva ou negativa

<br>
<br>

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
