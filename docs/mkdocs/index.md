# Um jeito fácil de obter indicadores financeiros

<div align="center">
    <br><img src="https://github.com/ThiagoPanini/pynvest/blob/v0.0.x/docs/assets/gifs/logo-animated-intro.gif?raw=true" alt="pynvest-animated-intro" width="900" height="400">
</div>

## Visão Geral

Bem-vindos à página de documentação da `pynvest`, a sua biblioteca Python para extração e análise de indicadores financeiros da B3.

Atualmente, a biblioteca conta com funcionalidades de *web scrapping* aplicadas ao site [Fundamentus](https://www.fundamentus.com.br/) para retornar DataFrames pandas com indicadores fundamentalistas pré estabelecidos, abrindo uma série de possibilidades analíticas e de acompanhamento aos seus usuários.

## Features

- 💸 Listagem de todos os *tickers* de Ações da B3
- 🧱 Listagem de todos os *tickers* de Fundos Imobiliários da B3
- 💰 Extração de indicadores financeiros de ativos (Ação ou FII)
- *E muito mais...*

## Primeiros Passos

Para iniciar sua jornada utilizando a `pynvest`, basta realizar sua instalação através do comando:

```python
pip install pynvest
```

Eventualmente, você pode querer realizar este processo em um [ambiente virtual Python](https://docs.python.org/3/library/venv.html) criado para seu projeto de análise. Se quiser mais informações sobre essa dinâmica de criação de *virtual envs*, este [excelente artigo](https://realpython.com/python-virtual-environments-a-primer/) pode ajudar a desbravar esse conhecimento.

Uma vez instalada a biblioteca, você poderá importar seus módulos e classes em qualquer script de aplicação. No exemplo abaixo, um dos métodos disponíveis é chamado para extrair indicadores de um determinado ativo financeiro:

```python
# Importando classe
from pynvest.fundamentus import Fundamentus

# Instanciando objeto da classe
fundamentus = Fundamentus()

# Obtendo indicadores financeiros de uma Ação
df_itub3 = fundamentus.coleta_indicadores_de_ativo("itub3")
```

## Navegando pela Doc

- A página de [arquitetura](./arquitetura.md) contempla um diagrama de funcionamento da bibioteca
- Em [documentação oficial](./mkdocstrings/fundamentus.md) você poderá encontrar todas as docs de classes e métodos

???+ warning "Páginas em construção"
    - Página de demonstração de funcionalidades com GIFs acessíveis
    - Página de contribuição para novos colaboradores
    - FAQ com perguntas mais frequentes sobre a biblioteca

## Entre em Contato

- :fontawesome-brands-github: [@ThiagoPanini](https://github.com/ThiagoPanini)
- :fontawesome-brands-linkedin: [Thiago Panini](https://www.linkedin.com/in/thiago-panini/)
- :fontawesome-brands-hashnode: [panini-tech-lab](https://panini.hashnode.dev/)
- :fontawesome-brands-dev: [thiagopanini](https://dev.to/thiagopanini)
