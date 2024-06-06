# 📊🎥 Dashboard com o ranking de filmes IMDb 

Este repositório contém a implementação de um dashboard com o ranking de filmes de acordo com o IMDb. Foi desenvolvido para fins de aprendizado, requisitado este pelo Desafio Python do [Projeto Desenvolve](http://projetodesenvolve.com.br).

## Instruções de Uso
Este projeto foi desenvolvido usando a versão 3.12.3 do Python. Para execução do script, além da instalação do Python, se certifique que as dependências (em `requirements.txt`) foram devidamente instaladas. <br>
O dashboard pode ser executado através do seguinte comando no terminal:
```
streamlit run dashboards.py
```
A execução iniciará o servidor local do Streamlit e abrirá o dashboard no seu navegador padrão.

## Tecnologias Utilizadas
O código (disponível em `script.py`) foi feito usando a linguagem Python junto com a biblioteca `Pandas` para leitura e processamento de dados, além da biblioteca `Plotly` para criação e vizualização de dados. Por fim, foi utilizado o framework `Streamlit` para a visualização web.

### Dados
O arquivo `imdb_top_1000.csv` (em `\data`) é uma base de dados com os 1000 filmes com a avaliação mais alta do período de 1920 a 2020, em que cada linha é um filme. Dentre as colunas da base de dados original (retirada do [Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)), as colunas relevantes para o painel estão explicitadas a seguir.
* Series_Title: Nome do filme
* Released_Year: Ano de lançamento do filme
* Genre: Gênero(s) presente(s) na classificação oficial do filme
* IMDB_Rating: Classificação do filme no IMDb, de 0 a 10
* Meta_score: Classificação do filme no Metacritic, site que reune diversas críticas de jornais, revistas e profissionais.
* Director: Diretor do filme.
* Star1: Ator ou Atriz que atuou como o(a) protagonista do filme.
* Gross: Lucro obtido pelo filme.
