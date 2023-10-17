# Extraindo tickers listados na bolsa brasileira

## Visão Geral

| | |
| :-- | :-- |
| 🚀 **Método** | [extracao_tickers_de_ativos()](../../mkdocstrings/scrappers/fundamentus.md/#pynvest.scrappers.fundamentus.Fundamentus.extracao_tickers_de_ativos) |
| 📄 **Descrição** | Um método que permite com que usuários obtenham uma lista com todos os ativos listados na B3 (Ações ou Fundos Imobiliários) |
| 📦 **Acessível em** | `pynvest.scrappers.fundamentus.Fundamentus` |

## Demonstração

O método em questão possui um parâmetro de nome `tipo` que define se a extração de ativos refere-se a Ações ou Fundos Imobiliários listados na B3. Este parâmetro aceita as seguintes entradas:

- "ações" (não é case sensitive, ou seja "AÇÕES" também é uma entrada válida)
- "fiis" (não é case sensitive, ou seja "FIIS" também é uma entrada válida)

Vamos ver, na prática, como a biblioteca entrega essa dinâmica.

### Listando Ações

Para obter uma lista de **ações** registradas na B3, basta utilizar o bloco de código abaixo:

```python
# Importando classe
from pynvest.scrappers.fundamentus import Fundamentus

# Instanciando objeto da classe
pynvest_scrapper = Fundamentus()

# Obtendo tickers de Ações
tickers_acoes = pynvest_scrapper.extracao_tickers_de_ativos(tipo="ações")
```

???+ example "Obtendo tickers de Ações listadas na B3"
    [![Um GIF mostrando a execução do método extracao_tickers_de_ativos() com o parâmetro "tipo" igual a "ações"](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-extracao_tickers_de_ativos_acoes.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-extracao_tickers_de_ativos_acoes.gif?raw=true)


### Listando FIIs

Para listagem de fundos imobiliários, basta alterar a chamada do método para o tipo adequado. Considerando a classe já importada e seu respectivo objeto instanciado, o bloco de código abaixo pode ser utilizado como referência para a dada listagem:

```python
# Obtendo tickers de FIIs
tickers_fiis = pynvest_scrapper.extracao_tickers_de_ativos(tipo="fiis")
```

???+ example "Obtendo tickers Fundos Imobiliários listados na B3"
    [![Um GIF mostrando a execução do método extracao_tickers_de_ativos() com o parâmetro "tipo" igual a "fiis"](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-extracao_tickers_de_ativos_fiis.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-extracao_tickers_de_ativos_fiis.gif?raw=true)


### Erros e Exceções

Por fim, caso o usuário informe um valor para o parâmetro `tipo` diferente dos aceitáveis, uma exceção será lançada:

```python
# Exemplo de entrada errada para o parâmetro tipo
tickers = pynvest_scrapper.extracao_tickers_de_ativos(tipo="foo")
```

???+ warning "Executando método com valor incorreto para parâmetro tipo"
    [![Um GIF mostrando a execução do método extracao_tickers_de_ativos() com o parâmetro "tipo" igual a "foo"](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-extracao_tickers_de_ativos_foo.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-extracao_tickers_de_ativos_foo.gif?raw=true)
