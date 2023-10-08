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
acoes_url_html_filename = os.path.join(
    os.path.dirname(__file__),
    "acoes_url_content.html"
)

with open(acoes_url_html_filename, "r", encoding="utf-8") as f:
    ACOES_TICKERS_HTML_MOCKED_RESPONSE = f.read()
