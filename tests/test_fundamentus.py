"""

"""


# Importando bibliotecas
import pytest


@pytest.mark.fundamentus
@pytest.mark.extracao_tickers_de_ativos
def test_extracao_de_tickers_de_acoes_retorna_um_objeto_do_tipo_lista(
    tickers_acoes: list[str]
):
    """
    G: Dado que o usuário deseja extrair todos os tickers de Ações da bolsa
    W: Quando o método extracao_tickers_de_ativos() for chamado
    T: Então o objeto resultante deve ser do tipo lista
    """

    assert isinstance(tickers_acoes, list)


