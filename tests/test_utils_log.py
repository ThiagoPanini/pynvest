"""Test cases for features defined on cloudgeass.utils.log module.

___
"""

# Importing libraries
import pytest
import logging

from pynvest.utils.log import log_config


@pytest.mark.utils_log
@pytest.mark.log_config
def test_log_config_function_returns_a_logger_object():
    """
    G: Dado que os usuários desejam obter um objeto Logger pré configurado
    W: Quando a função log_config() for invocada
    T: Então o retorno obtido deve ser um objeto do tipo logging.Logger
    """

    logger = log_config()
    assert isinstance(logger, logging.Logger)
