# Visão Básica de Arquitetura

Com o objetivo de nos aprofundarmos um pouco mais no funcionamento da biblioteca `pynvest` por baixo dos panos, a imagem abaixo traz um diagrama básico da jornada do usuário ao utilizar as funcionalidades disponíveis.

![Jornada básica de construção da biblioteca](./assets/diagrams/pynvest-diagram.png)

Em essência, alguns pontos podem ser destacados:

1. As funcionalidades presentes baseam-se em requisições realizadas ao site [Fundamentus](https://www.fundamentus.com.br/)
2. Como o site Fundamentus não expõe uma API, o retorno dessa requisição é dado por uma página HTML
3. O conteúdo desta página HTML é então tratado através da biblioteca [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
4. Regras específicas são aplicadas no contéudo HTML tratado para que, em alguns casos/métodos, DataFrames do [pandas](https://pandas.pydata.org/) possam ser entregues aos usuários