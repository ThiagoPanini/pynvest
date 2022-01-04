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
from pynvest.utils.log import log_config

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