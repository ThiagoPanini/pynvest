# Coletando indicadores de ativos financeiros

## Visão Geral

| | |
| :-- | :-- |
| 🚀 **Método** | [coleta_indicadores_de_ativo()](../../mkdocstrings/scrappers/fundamentus.md/#pynvest.scrappers.fundamentus.Fundamentus.coleta_indicadores_de_ativo) |
| 📄 **Descrição** | Um método capaz de extrair uma série de indicadores fundamentalistas de ativos financeiros da bolsa de valores brasileira |
| 📦 **Acessível em** | `pynvest.scrappers.fundamentus.Fundamentus` |

## Demonstração

Com o método `coleta_indicadores_de_ativo()`, os usuários precisam necessariamente informar o *ticker* alvo da extração de indicadores para obter um DataFrame do pandas com o resultado do processo de *web scrapping* aplicado.

???+ info "Sobre os indicadores financeiros extraídos"
    O método em questão permite extrair indicadores financeiros tanto de Ações quanto de Fundos Imobiliários. Entretanto, é importante reforçar que esses dois tipos de ativos **possuem indicadores financeiros distintos** e, dessa forma, o resultado do *web scrapping* aplicado ao método `coleta_indicadores_de_ativo()` pode retornar DataFrames com diferentes colunas de acordo com o *ticker* informado pelo usuário.

    Em outras palavras, caso o usuário informa um *ticker* de uma ação (ex: "ITUB3"), o DataFrame resultante irá contemplar um conjunto de indicadores aplicados a ações.

    Caso o usuário execute o método com um *ticker* de fundo imobiliário (ex: BTLG11), então o DataFrame resultante irá conter um outro conjunto de indicadores que se aplicam apenas a FIIs.

## Obtendo Indicadores de Ações

Para obter indicadores de uma Ação listada na B3, basta instanciar um objeto da classe `Fundamentus` e executar o método `coleta_indicadores_de_ativo()` passando, como principal argumento, um *ticker* válido de uma Ação.

```python
# Importando classe
from pynvest.scrappers.fundamentus import Fundamentus

# Instanciando objeto da classe
pynvest_scrapper = Fundamentus()

# Obtendo indicadores financeiros de uma Ação
df_itub3 = pynvest_scrapper.coleta_indicadores_de_ativo("itub3")
```

???+ example "Extraindo indicadores de uma ação"
    [![Um GIF mostrando a execução do método coleta_indicadores_de_ativo() com o parâmetro "ticker" igual a uma ação (ex: "itub3")](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_acao.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_acao.gif?raw=true)


## Obtendo Indicadores de FIIs

De forma análoga, para obter indicadores fundamentalista de um Fundo Imobiliário, basta chamar o mesmo método e passar, como argumento, um *ticker* válido de um FII listado na bolsa.

```python
# Obtendo indicadores financeiros de um FII
df_xplg11 = pynvest_scrapper.coleta_indicadores_de_ativo("xplg11")
```

???+ example "Extraindo indicadores de um fundo imobiliário"
    [![Um GIF mostrando a execução do método coleta_indicadores_de_ativo() com o parâmetro "ticker" igual a um fii (ex: "xplg11")](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_fii.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_fii.gif?raw=true)


## Erros e Exceções

Ao tentar extrair um DataFrame pandas com indicadores financeiros de uma Ação ou FII não listados na B3 (seja por erro de digitação ou por qualquer outro motivo), uma exceção do tipo `TypeError` será lançada para o usuário com uma mensagem explicativa sobre o problema de escopo.

```python
# Tentando extrair indicadores de um ativo inválido dentro do escopo do método
df_foo = pynvest_scrapper.coleta_indicadores_de_ativo("foo")
```

???+ warning "Tentando coletar indicadores de um ativo não listado na B3"
    [![Um GIF mostrando a execução do método coleta_indicadores_de_ativo() com o parâmetro "ticker" não listado na B3 ou que não seja uma ação ou FII(ex: "foo")](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_foo.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_foo.gif?raw=true)


## Sobre os indicadores coletados

:material-alert-decagram:{ .mdx-pulse .warning } Para obter detalhes sobre a definição de todos os indicadores financeiros extraídos e consolidados através do processo *web scrapping* ao site Fundamentus, verifique a página de [indicadores](../../indicadores/sobre-indicadores.md).
