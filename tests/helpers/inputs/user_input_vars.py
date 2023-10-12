"""Centralizando todos os inputs dos usuários usados em testes.

A ideia deste arquivo é consolidar variáveis definidas por usuários com a
intenção de facilitar a construção de testes unitários e de integração.

Essencialmente, qualquer elemento utilizado múltiplas vezes em processos de
testagem, sejam eles em fixtures ou em casos de testes propriamente ditos, são
fortes candidatos a serem centralizados neste arquivo.

___
"""

# Importando biblitoecas
import os


# Lendo arquivo HTML com mock de resposta à URL de tickers de Ações
request_content_tickers_acoes_filepath = os.path.join(
    os.path.dirname(__file__),
    "request_content_tickers_acoes.html"
)

with open(request_content_tickers_acoes_filepath, "r", encoding="utf-8") as f:
    REQUEST_MOCKED_RESPONSE_TICKERS_ACOES = f.read()


# Lendo arquivo HTML com mock de resposta à URL de tickers de FIIs
request_content_tickers_fiis_filepath = os.path.join(
    os.path.dirname(__file__),
    "request_content_tickers_fiis.html"
)

with open(request_content_tickers_fiis_filepath, "r", encoding="utf-8") as f:
    REQUEST_MOCKED_RESPONSE_TICKERS_FIIS = f.read()
