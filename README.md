<div align="center">
    <br><img src="https://github.com/ThiagoPanini/pynvest/blob/v0.1.x/docs/assets/imgs/logo-v2.png?raw=true" width=150 alt="pynvest-logo">
</div>

<div align="center">  
  <br>
  
  [![PyPI](https://img.shields.io/pypi/v/pynvest?style=flate&logo=python&logoColor=FFFFFF&color=22C7FF)](https://pypi.org/project/pynvest/)
  ![PyPI - Downloads](https://img.shields.io/pypi/dm/pynvest?logo=pypi&logoColor=FFFFFF&color=22C7FF)
  ![CI workflow](https://img.shields.io/github/actions/workflow/status/ThiagoPanini/pynvest/ci-main.yml?label=ci&logo=github&logoColor=FFFFFF)
  [![codecov](https://codecov.io/github/ThiagoPanini/pynvest/branch/main/graph/badge.svg?token=L4KO1RM63H)](https://codecov.io/github/ThiagoPanini/pynvest)
  [![Documentation Status](https://readthedocs.org/projects/pynvest/badge/?version=latest)](https://pynvest.readthedocs.io/en/latest/?badge=latest)

  [![Python](https://img.shields.io/badge/python-grey?style=for-the-badge&logo=python&logoColor=22C7FF)](https://www.python.org/)
  [![Pytest](https://img.shields.io/badge/pytest-grey?style=for-the-badge&logo=pytest&logoColor=22C7FF)](https://www.python.org/)
  [![Mkdocs](https://img.shields.io/badge/mkdocs-grey?style=for-the-badge&logo=markdown&logoColor=22C7FF)](https://www.mkdocs.org/)
  [![Read the Docs](https://img.shields.io/badge/readthedocs-grey?style=for-the-badge&logo=readthedocs&logoColor=22C7FF)](https://readthedocs.org/)
  [![GitHub](https://img.shields.io/badge/github-grey?style=for-the-badge&logo=github&logoColor=22C7FF)](https://github.com/)

</div>

___

<div align="center">
  <br>
</div>


## Visão Geral

A biblioteca `pynvest` foi criada para facilitar o processo de extração e análise de indicadores financeiros da bolsa de valores brasileira (B3). Isto é obtido através de *web scrappings* aplicados a plataformas/sites financeiros para extração de atributos e valores capazes de proporcionar, aos usuários, uma jornada interessante de análise de dados.

## Quickstart

A instalação da biblioteca pode ser feita através de qualquer gerenciador de pacotes Python, como o [pip](https://pip.pypa.io/en/stable/), por exemplo:

```python
pip install pynvest
```

A partir deste ponto, os usuários poderão utilizar *scrappers* capazes de entregar indicadores financeiros em formatos amigáveis (como DataFrames do [pandas](https://pandas.pydata.org/docs/index.html), por exemplo).

```python
# Importando classe
from pynvest.scrappers.fundamentus import Fundamentus

# Instanciando objeto da classe
pynvest_scrapper = Fundamentus()

# Obtendo indicadores financeiros de uma Ação
df_itub3 = pynvest_scrapper.coleta_indicadores_de_ativo("itub3")
```

<details>
  <summary>📽️ Demonstração de método de extração de indicadores financeiros</summary>

  [![Um GIF mostrando a execução do método coleta_indicadores_de_ativo() com o parâmetro "ticker" igual a uma ação (ex: "itub3")](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_acao.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_acao.gif?raw=true)
  
</details>

## Readthedocs

🚨 Reforçando pois vale o reforço: existe uma [página oficial de documentação da biblitoeca](https://pynvest.readthedocs.io/pt/latest/) criada com carinho e dedicação para todos os interessados em saber mais a respeito da solução. Viva o open source!


## Entre em Contato

- GitHub: [@ThiagoPanini](https://github.com/ThiagoPanini)
- LinkedIn: [Thiago Panini](https://www.linkedin.com/in/thiago-panini/)
- Hashnode: [panini-tech-lab](https://panini.hashnode.dev/)
- DevTo: [thiagopanini](https://dev.to/thiagopanini)