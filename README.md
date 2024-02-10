<div align="center">
    <br><img src="https://github.com/ThiagoPanini/pynvest/blob/v0.1.x/docs/assets/imgs/logo/logo-com-nome.png?raw=true" width=200 alt="pynvest-logo">
</div>

<div align="center">  
  <br>

  <a href="https://pypi.org/project/pynvest/">
    <img src="https://img.shields.io/pypi/v/pynvest?style=flate&logo=python&logoColor=FFFFFF&color=22C7FF" alt="PyPi shield">
  </a>

  <a href="">
    <img src="https://img.shields.io/pypi/dm/pynvest?logo=pypi&logoColor=FFFFFF&color=B252D0">
  </a>
  
  <a href="">
    <img src="https://img.shields.io/github/actions/workflow/status/ThiagoPanini/pynvest/ci-main.yml?label=ci&logo=github&logoColor=FFFFFF">
  </a>

  <a href="https://codecov.io/github/ThiagoPanini/pynvest">
    <img src="https://codecov.io/github/ThiagoPanini/pynvest/branch/main/graph/badge.svg?token=L4KO1RM63H">
  </a>

  <a href="https://pynvest.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/pynvest/badge/?version=latest">
  </a>

  <br>

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-grey?style=for-the-badge&logo=python&logoColor=22C7FF">
  </a>

  <a href="https://docs.pytest.org/">
    <img src="https://img.shields.io/badge/pytest-grey?style=for-the-badge&logo=pytest&logoColor=22C7FF">
  </a>

  <a href="https://www.mkdocs.org/">
    <img src="https://img.shields.io/badge/mkdocs-grey?style=for-the-badge&logo=markdown&logoColor=22C7FF">
  </a>

  <a href="https://readthedocs.org/">
    <img src="https://img.shields.io/badge/readthedocs-grey?style=for-the-badge&logo=readthedocs&logoColor=22C7FF">
  </a>

  <a href="https://github.com/">
    <img src="https://img.shields.io/badge/github-grey?style=for-the-badge&logo=github&logoColor=22C7FF">
  </a>

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

📚 Para saber mais sobre essa iniciativa, acesse a [página oficial de documentação da biblitoeca](https://pynvest.readthedocs.io/pt/latest/) criada com carinho e dedicação para todos os interessados na solução. Viva o open source!


## Entre em Contato

- GitHub: [@ThiagoPanini](https://github.com/ThiagoPanini)
- LinkedIn: [Thiago Panini](https://www.linkedin.com/in/thiago-panini/)
- Hashnode: [panini-tech-lab](https://panini.hashnode.dev/)
- DevTo: [thiagopanini](https://dev.to/thiagopanini)