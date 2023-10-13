"""
Este módulo comporta funções responsáveis por auxiliar usuários a aprimorar
suas respectivas jornadas de logs nas aplicações desenvolvidas. Os componentes
aqui disponibilizados podem ser utilizados em funcionalidades dentro ou fora
da biblioteca em questão.

___
"""

# Importando bibliotecas
import logging


# Criando um objeto Logger pré configurado
def log_config(
    logger_name: str = __file__,
    logger_level: int = logging.INFO,
    logger_date_format: str = "%Y-%m-%d %H:%M:%S"
) -> logging.Logger:
    """Cria, configura e disponibiliza um objeto Logger.

    Esta função pode ser utilizada em qualquer aplicação Python para aprimorar
    processos de log com objetivo de aumentar os níveis de observabilidade dos
    códigos desenvolvidos. Ela utiliza o pacote Python logging para criar e
    retornar ao usuário um objeto de Logger com algumas configurações básicas
    pré estabelecidas, evitando possíveis overheads de configuração.

    Args:
        logger_name (str): O nome do objeto Logger criado
        logger_level (int): O nível de log considerado
        logger_date_format (str): Formato de data desejado da mensagem de log

    Returns:
        Um objeto Logger pré configurado.

    Examples:
        ```python
        # Importando a função
        from package.utils.log import log_config

        # Criando e obtendo um objeto Logger pré configurado
        logger = log_config(logger)
        ```
    """

    # Criando um objeto Logger e estabelecendo seu nível
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    # Configurando o formato da mensagem
    log_format = "%(levelname)s;%(asctime)s;%(filename)s;"
    log_format += "%(lineno)d;%(message)s"
    formatter = logging.Formatter(log_format,
                                  datefmt=logger_date_format)

    # Configurando stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
