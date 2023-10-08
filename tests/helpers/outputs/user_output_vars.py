"""Centralizando todos os outputs dos usuários usados em testes.

A ideia deste arquivo é consolidar variáveis definidas por usuários com a
intenção de centralizar todos os valores esperados em testes unitários.

Com isso, sempre que uma validação específica precisar ser feita em um caso de
teste, como por exemplo, validar se o retorno de um método é igual a um objeto
pré definido, então este "objeto pré definido" pode ser definido neste arquivo

___
"""

# Importando biblitoecas
import os


# Lendo arquivo HTML com mock de resposta à URL de tickers de Ações
expected_tickers_acoes_filepath = os.path.join(
    os.path.dirname(__file__),
    "tickers_acoes.txt"
)

with open(expected_tickers_acoes_filepath, "r", encoding="utf-8") as f:
    EXPECTED_TICKERS_ACOES = f.read().split(",")


# Lendo arquivo HTML com mock de resposta à URL de tickers de FIIs
expected_tickers_fiis_filepath = os.path.join(
    os.path.dirname(__file__),
    "tickers_fiis.txt"
)

with open(expected_tickers_fiis_filepath, "r", encoding="utf-8") as f:
    EXPECTED_TICKERS_FIIS = f.read().split(",")
