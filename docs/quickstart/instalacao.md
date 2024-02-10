# Facilitando a Extração de Indicadores Financeiros



## Instalação

Para iniciar sua jornada no `pynvest`, basta realizar a instalação da biblioteca utilizando um gerenciador de pacotes de sua preferência (como por exemplo, o [pip](https://pypi.org/project/pip/)):

```python
pip install pynvest
```

???+ tip "Sobre ambientes virtuais Python"
    Eventualmente, você pode querer realizar este processo de instalação em um [ambiente virtual Python](https://docs.python.org/3/library/venv.html). Para mais infromações a respeito, este [excelente artigo](https://realpython.com/python-virtual-environments-a-primer/) pode ajudar a desbravar esse conhecimento.

Uma vez instalada a biblioteca, a dinâmica de uso sob a ótica do usuário pode ser resumida a:

1. Usuário importa uma classe de um dos *scrappers* disponíveis
2. Usuário cria um objeto dessa classe importada
3. Usuário chamada os métodos disponíveis para obter indicadores financeiros

Abaixo é possível visualizar um exemplo de chamada do método [coleta_indicadores_de_ativo()]() para obtenção de um DataFrame pandas com indicadores financeiros de um determinado ativo:

```python
# Importando classe
from pynvest.scrappers.fundamentus import Fundamentus

# Instanciando objeto da classe
pynvest_scrapper = Fundamentus()

# Obtendo indicadores financeiros de uma Ação
df_itub3 = pynvest_scrapper.coleta_indicadores_de_ativo("itub3")
```

???+ example "Exemplo de funcionamento prático de um dos métodos da biblioteca"
    [![Um GIF mostrando a execução do método coleta_indicadores_de_ativo() com o parâmetro "ticker" igual a uma ação (ex: "itub3")](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_acao.gif?raw=true)](https://github.com/ThiagoPanini/pynvest/blob/docs/atualizacao-de-documentacao/docs/assets/gifs/pynvest-coleta_indicadores_de_ativo_acao.gif?raw=true)

## Navegando pela Doc

Nesta página de documentação, você encontrará todos os detalhes relacionados à biblitoeca `pynvest`, da sua concepção até dicas fundamentais de usabilidade.