# Arquitetura

## Arquitetura Básica de Funcionamento

O funcionamento da biblioteca `pynvest` é relativamente simples e pode ser ilustrado através do diagrama abaixo:

![Diagrama de arquitetura básico ilustrando o funcionamento da biblitoeca pynvest](assets/imgs/arquitetura-basica.svg){ width=750px height=750px }

No modelo proposto, existem basicamente 7 grandes etapas que resumem todas as principais funcionalidades na biblioteca. São elas:

1. Usuários interessados em obter indicadores financeiros utilizam a biblioteca em suas aplicações
2. Os métodos da biblioteca realizam requisições à sites contendo indicadores financeiros através de [módulos de scrappers](#scrappers)
3. Respostas às requisições são obtidas
4. Em geral, as respostas chegam no formato HTML puro
5. O conteúdo HTML é tratado através da biblioteca [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
6. O tratamento do conteúdo normalmente é convertido em um [DataFrame do pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
7. O usuário então recebe um DataFrame pandas contendo os indicadores financeiros de ativos

## Scrappers

Neste contexto, as funcionalidades de coleta de indicadores financeiros da `pynvest` estão totalmente baseada no conceito de *scrappers* que, essencialmente, são módulos personalizados para cada site ou fonte da informação onde dados precisam ser coletados e tratados. Em outras palavras, existe uma relação de 1 para 1 entre *scrapper* e site/portal de indicadores financeiros.

???+ question "Quais scrappers estão atualmente disponíveis na biblioteca?"
    Até o presente momento, a biblitoeca conta apenas com *scrapper* `fundamentus` responsávei por aplicar processos de *web scrapping* no portal [Fundamentus](https://www.fundamentus.com.br/). No futuro, outros *scrappers* podem ser adicionados para proporcionar uma experiência cada vez mais vasta ao usuário.

## Módulos e Submódulos

Apresentada a estratégia de funcionamento, a biblioteca possui essa árvore de módulos e submódulos onde os usuários podem interagir diretamente via código.

```bash
├───scrappers
│   │   fundamentus.py
│   └───__init__.py
│
└───utils
    │   log.py
    └───__init__.py
```

<small>
  :octicons-light-bulb-16:
  **Dica:** Aqui, é possível entender claramente a relação entre *scrappers* e portais de indicadores financeiros. O submódulo `fundamentus.py` contém funções, classes e métodos especialmente construídos para contemplar toda a dinâmica de extração e tratamento de dados contidos no site Fundamentus.
</small>
