"""
---------------------------------------------------
------------- SCRIPT: analise_ativos --------------
---------------------------------------------------
Neste script, é proposto o consumo da classe 
AtivosFundamentus construída no módulo fundamentus
deste pacote. O principal objetivo é extrair 
informações detalhadas de ativos financeiros
da bolsa de valores, permitindo assim um melhor
gerenciamento de investimentos por parte dos usuários.

Table of Contents
---------------------------------------------------
1. Configurações Iniciais
    1.1 Importando bibliotecas
2. Gerando Indicadores Financeiros
    2.1 Importando classe e executando método
---------------------------------------------------
"""

# Author: Thiago Panini
# Date: 23/08/2021


"""
---------------------------------------------------
------------ 1. CONFIGURAÇÕES INICIAIS ------------
            1.1 Importando bibliotecas
---------------------------------------------------
"""

# Módulo fundamentus
from pynvest.fundamentus import AtivosFundamentus

# Bibliotecas gerais
import os
import pandas as pd

# Logging
import logging


"""
---------------------------------------------------
------------ 1. CONFIGURAÇÕES INICIAIS ------------
               1.2 Configurando log
---------------------------------------------------
"""

# Definindo função para configurar objeto de log do código
def log_config(logger, level=logging.DEBUG, 
               log_format='%(levelname)s;%(asctime)s;%(filename)s;%(module)s;%(lineno)d;%(message)s',
               log_filepath=os.path.join(os.getcwd(), 'exec_log/execution_log.log'),
               flag_file_handler=False, flag_stream_handler=True, filemode='a'):
    """
    Função que recebe um objeto logging e aplica configurações básicas ao mesmo
    
    Parâmetros
    ----------
    :param logger: objeto logger criado no escopo do módulo [type: logging.getLogger()]
    :param level: level do objeto logger criado [type: level, default=logging.DEBUG]
    :param log_format: formato do log a ser armazenado [type: string]
    :param log_filepath: caminho onde o arquivo .log será armazenado 
        [type: string, default='exec_log/execution_log.log']
    :param flag_file_handler: define se será criado um arquivo de armazenamento de log
        [type: bool, default=False]
    :param flag_stream_handler: define se as mensagens de log serão mostradas na tela
        [type: bool, default=True]
    :param filemode: tipo de escrita no arquivo de log [type: string, default='a' (append)]
    
    Retorno
    -------
    :return logger: objeto logger pré-configurado
    """

    # Setting level for the logger object
    logger.setLevel(level)

    # Creating a formatter
    formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')

    # Creating handlers
    if flag_file_handler:
        log_path = '/'.join(log_filepath.split('/')[:-1])
        if not os.path.isdir(log_path):
            os.makedirs(log_path)

        # Adding file_handler
        file_handler = logging.FileHandler(log_filepath, mode=filemode, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if flag_stream_handler:
        # Adding stream_handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)    
        logger.addHandler(stream_handler)

    return logger

# Instanciando e configurando objeto de log
logger = logging.getLogger(__file__)
logger = log_config(logger)


"""
---------------------------------------------------
------- 2. GERANDO INDICADORES FINANCEIROS --------
    2.1 Importando classe e executando método
---------------------------------------------------
"""

# Definindo variáveis do projeto
PROJECT_PATH = os.getcwd()
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
BANNER = """
                                .  
                               _|_ 
    .,-. .  ..--..    ._.-. .--.|  
    |   )|  ||  | \  / (.-' `--.|  
    |`-' `--|'  `- `'   `--'`--'`-'
    |       ;                      
    '    `-'                       

Análise de indicadores de ativos da bolsa!
"""

# Início do programa
print(BANNER)

# Importando classe e extraindo indicadores
ativos = AtivosFundamentus()
df_indicadores_acoes = ativos.analise_financeira_ativos(tipo='Ações', save=True)
df_indicadores_fiis = ativos.analise_financeira_ativos(tipo='FIIs', save=True)

logger.info(f'Dimensões da base de ações gerada: {df_indicadores_acoes.shape}')
logger.info(f'Dimensões da base de FIIs gerada: {df_indicadores_fiis.shape}')