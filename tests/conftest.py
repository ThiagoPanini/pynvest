"""Arquivo de configuração de testes para criação de fixtures.

Este arquivo gerencia componentes fundamentais para a construção e erealização
de testes unitários para todas as funcionalidades da biblioteca. Aqui, será
possível consolidar fixtures e outros elementos capazes de facilitar a jornada
de testagem.

___
"""

# Biblioteca de testagem
import pytest

# Bibliotecas para mockagem e realização de rquisições
import requests_mock

# Recursos pynvest
from pynvest.fundamentus import Fundamentus
from pynvest.fundamentus import (
    URL_TICKERS_ACOES,
    URL_TICKERS_FIIS
)

# Elementos de entrada de usuários para testagem
from tests.helpers.inputs.user_input_vars import (
    REQUEST_MOCKED_RESPONSE_TICKERS_ACOES,
    REQUEST_MOCKED_RESPONSE_TICKERS_FIIS
)


""" -------------------------------------------------
    FIXTURES: classe Fundamentus
    Fixtures para pynvest.fundamentus.Fundamentus
------------------------------------------------- """


# Objeto da classe Fundamentus utilizado para execuçãod os métodos
@pytest.fixture
def fundamentus() -> Fundamentus:
    return Fundamentus()


# Retorno mockado do método de extração de tickers de Ações
@pytest.fixture
@requests_mock.Mocker(kw="mocker")
def tickers_acoes(
    fundamentus: Fundamentus,
    url: str = URL_TICKERS_ACOES,
    mocked_text: str = REQUEST_MOCKED_RESPONSE_TICKERS_ACOES,
    **kwargs
) -> list[str]:
    # Mockando resposta da requisição
    mocker = kwargs["mocker"]
    mocker.get(url=url, text=mocked_text)

    # Realizando requisição através do método oficial da classe
    return fundamentus.extracao_tickers_de_ativos(tipo="ações")


# Retorno mockado do método de extração de tickers de FIIs
@pytest.fixture
@requests_mock.Mocker(kw="mocker")
def tickers_fiis(
    fundamentus: Fundamentus,
    url: str = URL_TICKERS_FIIS,
    mocked_text: str = REQUEST_MOCKED_RESPONSE_TICKERS_FIIS,
    **kwargs
) -> list[str]:
    # Mockando resposta da requisição
    mocker = kwargs["mocker"]
    mocker.get(url=url, text=mocked_text)

    # Realizando requisição através do método oficial da classe
    return fundamentus.extracao_tickers_de_ativos(tipo="fiis")
