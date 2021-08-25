<h1 align="center">
  <img src="https://i.imgur.com/dZbJrh1.png", alt="pynvest logo">
</h1>
<div align="center">
  <strong>:moneybag: Aplicando web scrapping para extração de indicadores fundamentalistas de ativos :moneybag:</strong>
</div>
<br/>

## Table of content

- [Sobre o pynvest](#sobre-o-pynvest)
- [Instalação](#instalação)
  - [Criação de Ambiente Virtual](#criação-de-ambiente-virtual)
  - [Clonando repositório](#clonando-repositório)
  - [Instalando o Pacote](#instalando-o-pacote)
- [Utilização Prática](#utilização-prática)

___

## Sobre o pynvest

Já pensou em uma forma rápida, fácil e direta de gerenciar seus investimentos a partir da análise de uma série de indicadores fundamentalistas? As funcionalidades do _pynvest_ contemplam extrações sistêmicas dos mais variados parâmetros de ativos financeiros para que o usuário, em posse de tais informações, possa usufruir uma visão completa de ações e fundos imobiliários listados na bolsa de valores (ou em uma carteira específica) com o objetivo de **tomar melhores decisões** seguindo critérios pessoais de análise.

Baseado em processos de [web scrapping](https://www.tecmundo.com.br/internet/215525-web-scraping-conheca-tecnica-coleta-dados.htm) construídos em [python](https://www.python.org/), o _pynvest_ fornece classes, métodos e funções que permitem:

* Extração de indicadores fundamentalistas, oscilações, balanços patrimoniais e demonstrativos de resultados de **ações** listadas na B3
* Extração de indicadores fundamentalistas, oscilações, balanços patrimoniais e demonstrativos de resultados de **fundos imobiliários** listados na B3
* Listar todos os [_tickers_](https://carteirasa.com.br/ticker-entenda-o-que-e-e-como-funciona-o-codigo-das-acoes-na-b3/) presentes na B3 para ações e fundos imobiliários
* Muito mais...

Como principal fonte, o _pynvest_ utiliza o site [Fundamentus](https://www.fundamentus.com.br/index.php) para extração de indicadores de ativos da bolsa. Neste cenário, o módulo `fundamentus.py` contempla a classe `AtivosFundamentus` contendo, por sua vez, métodos específicos para o alcance dos objetivos aqui listados dentro do contexto do site Fundamentus.

Para facilitar o acompanhamento das execuções, a construção das ferramentas contidas no pacote _pynvest_ contém elementos de [_logging_](https://docs.python.org/pt-br/3/howto/logging.html) que informam ao usuário o status de alguns pontos estratégicos dos códigos.

___

## Instalação

### Criação de Ambiente Virtual
Seguindo as boas práticas de consumo de soluções python, recomenda-se a criação de um [ambiente virtual](https://docs.python.org/pt-br/3/tutorial/venv.html) para a instalação das dependências (pacotes e bibliotecas) da ferramenta a ser utilizada. Para tal, em um diretório de escolha própria no sistema operacional de uso, basta executar os comandos abaixo para criar e ativar um ambiente virtual (exemplos para SOs Linux e Windows):

```bash
# Criando e ativando venv no Linux
$ python -m venv <nome_venv>
$ source <nome_venv>/bin/activate

# Criando e ativcando venv no Windows
$ python -m venv <nome_venv>
$ <nome_venv>/Scripts/activate
```

### Clonando Repositório
Para obter o código fonte do projeto _pynvest_, pode-se [clonar](https://www.gitkraken.com/learn/git/git-clone) o repositório utilizando os protocolos HTTPS ou SSH. Assim, em um diretório de escolha própria, basta selecionar executar um dos comandos abaixo de acordo com o protocolo de utilização:

```bash
# Clonando repositório via HTTPS
$ git clone https://github.com/ThiagoPanini/pynvest.git

# Clonando repositório via SSH
$ git clone git@github.com:ThiagoPanini/pynvest.git
```

### Instalando o Pacote
Com o ambiente virtual criado ativo e o repositório alvo devidamente clonado, para obter os insumos do pacote _pynvest_, basta navegar até o diretório do projeto realizar a instalação do módulo em modo de edição através do comando:

```bash
$ (nome_venv) cd pynvest/
$ (nome_venv) pip install -e .
```

___

## Utilização Prática
Após toda a preparação detalhada na seção anterior, é possível encontrar, no diretório `scripts/` do projeto, alguns exemplos práticos de utilização das funcionalidades propostas pelo pacote _pynvest_. Para ilustrar uma aplicação do pacote, o script `analise_ativos.py` é responsável por extrair todos os tickers de ações e fundos imobiliários listados na B3 e gerar indicadores estratégicos para cada um dos ativos obtidos.

```bash
$ (nome_venv) python scripts/analise_ativos.py
```

* _Prompt de comando_
Como mencionado anteriormente, as funcionalidades contidas nos módulos `pynvest` contemplam a utilização de logs para facilitar o gerenciamento do estado de execução do código. Abaixo, as mensagens no prompt de comando permitem acompanhar a extração de indicadores para todas as **ações** e **fundos imobiliários** listados na B3.
<h1 align="center">
  <img src="https://i.imgur.com/Pokg1cH.png", alt="ex_analise_ativos">
</h1>

* _Arquivos gerados_
Como resultado, o script `analise_ativos.py` salva, em um diretório nominado `data/` no sistema operacional (caso o diretório não exista, é realizada a criação automática do mesmo)
