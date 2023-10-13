"""

"""


# Importando bibliotecas
import pytest

from pynvest.scrappers.fundamentus import Fundamentus

from tests.helpers.outputs.user_output_vars import (
    EXPECTED_TICKERS_ACOES,
    EXPECTED_TICKERS_FIIS
)


@pytest.mark.fundamentus
@pytest.mark.extracao_tickers_de_ativos
def test_erro_ao_selecionar_um_tipo_invalido_de_extracao_de_tickers(
    pynvest_scrapper: Fundamentus
):
    """
    G: Dado que o usuário deseja extrair todos os tickers de Ações da bolsa
    W: Quando o método extracao_tickers_de_ativos() for chamado com o
       parâmetro tipo inserido de forma inválida (ex: tipo="foo")
    T: Então uma exceção do tipo TypeError deve ser lançada
    """

    with pytest.raises(TypeError):
        pynvest_scrapper.extracao_tickers_de_ativos(tipo="foo")


@pytest.mark.fundamentus
@pytest.mark.extracao_tickers_de_ativos
def test_extracao_de_tickers_de_acoes_retorna_um_objeto_do_tipo_lista(
    tickers_acoes: list[str]
):
    """
    G: Dado que o usuário deseja extrair todos os tickers de Ações da bolsa
    W: Quando o método extracao_tickers_de_ativos() for chamado com o
       parâmetro tipo="ações"
    T: Então o objeto resultante deve ser do tipo lista
    """

    assert isinstance(tickers_acoes, list)


@pytest.mark.fundamentus
@pytest.mark.extracao_tickers_de_ativos
def test_extracao_de_tickers_de_acoes_retorna_uma_lista_de_tickers_esperado(
    tickers_acoes: list[str],
    expected_tickers_acoes: list[str] = EXPECTED_TICKERS_ACOES
):
    """
    G: Dado que o usuário deseja extrair todos os tickers de Ações da bolsa
    W: Quando o método extracao_tickers_de_ativos() for chamado com o
       parâmetro tipo="ações"
    T: Então a lista resultante deve conter os todos os tickers esperados
    """

    assert tickers_acoes == expected_tickers_acoes


@pytest.mark.fundamentus
@pytest.mark.extracao_tickers_de_ativos
def test_extracao_de_tickers_de_fiis_retorna_um_objeto_do_tipo_lista(
    tickers_fiis: list[str]
):
    """
    G: Dado que o usuário deseja extrair todos os tickers de FIIs da bolsa
    W: Quando o método extracao_tickers_de_ativos() for chamado com o
       parâmetro tipo="fiis"
    T: Então o objeto resultante deve ser do tipo lista
    """

    assert isinstance(tickers_fiis, list)


@pytest.mark.fundamentus
@pytest.mark.extracao_tickers_de_ativos
def test_extracao_de_tickers_de_fiis_retorna_uma_lista_de_tickers_esperado(
    tickers_fiis: list[str],
    expected_tickers_fiis: list[str] = EXPECTED_TICKERS_FIIS
):
    """
    G: Dado que o usuário deseja extrair todos os tickers de FIIs da bolsa
    W: Quando o método extracao_tickers_de_ativos() for chamado com o
       parâmetro tipo="fiis"
    T: Então a lista resultante deve conter os todos os tickers esperados
    """

    assert tickers_fiis == expected_tickers_fiis
