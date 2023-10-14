# Visão Básica de Arquitetura

Com o objetivo de nos aprofundarmos um pouco mais no funcionamento da biblioteca `pynvest` por baixo dos panos, a imagem abaixo traz um diagrama básico da jornada do usuário ao utilizar as funcionalidades disponíveis.

![Jornada básica de construção da biblioteca](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/diagrams/pynvest-diagram.png?raw=true)


## Scrappers

Como mencionado na página inicial, a biblioteca `pynvest` entrega funcionalidades baseadas em *scrappers* que, essencialmente, podem ser definidos como módulos capazes de extrair informações financeiras de um determinado site ou portal.

Para entender melhor esse conceito, esta é a visão atual da biblitoeca em termos dos módulos disponíveis:

```bash
├───scrappers
│   │   fundamentus.py
│   └───__init__.py
│
└───utils
    │   log.py
    └───__init__.py
```

Observando essa dinâmica, percebe-se que o módulo `scrappers` tem a responsabilidade de alocar submódulos capazes de extrair e consolidar informações de ativos financeiros para diferentes sites ou portais.

???+ question "E o que temos disponível hoje?"
    Atualmente, a biblioteca conta apenas com o submódulo `fundamentus` responsável por aplicar *web scrapping* no site [Fundamentus](https://www.fundamentus.com.br/). Eventualmente, outros *scrappers* poderão ser adicionados em submódulos adicionais.


### Fundamentus

Assim, uma vez apresentada a estrutura de construção da biblioteca, as regras associadas no *scrapper* `fundamentus` consideram as seguintes etapas:

1. São realizadas requisições à diferentes URLs do site [Fundamentus](https://www.fundamentus.com.br/) conforme o propósito do método invocado
2. Como o site Fundamentus não expõe uma API, o retorno dessas requisições são dados por páginas HTML
3. O conteúdo das páginas HTML são então tratados através da biblioteca [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
4. Regras específicas são aplicadas no contéudo HTML tratado para que, em alguns casos/métodos, DataFrames do [pandas](https://pandas.pydata.org/) possam ser entregues aos usuários