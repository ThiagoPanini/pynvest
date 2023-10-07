"""Módulo: pynvest.fundamentus

Este módulo proporciona uma série de funcionalidades específicas para extrair
indicadores financeiros do site Fundamentus.

___
"""

# Importando bibliotecas
import logging
from pynvest.utils.log import log_config

import requests
from bs4 import BeautifulSoup

from datetime import datetime


""" -------------------------------------------------
    VARIÁVEIS
    Definindo variáveis de requisição ao site
------------------------------------------------- """

# URL para extração de todos os tickers de ações e FIIs
URL_TICKERS_ACOES = "https://www.fundamentus.com.br/resultado.php"
URL_TICKERS_FIIS = "https://www.fundamentus.com.br/fii_resultado.php"

# URL básica para extração de informações de ações
URL_INFO_TICKERS = "https://www.fundamentus.com.br/detalhes.php?papel="

# Header da requisição
REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) "
                  "Gecko/20100101 Firefox/50.0"
}

# Atributos temporais extraídos do site
CUSTOM_HEADINGS = [
    "Dia", "Mês", "30 dias", "12 meses"
] + [str(datetime.now().year-i) for i in range(6)]


class Fundamentus:
    """Classe responsável por extrair informações do site Fundamentus.

    Estas classe contém atributos e métodos capazes de proporcionar uma jornada
    completa de extração de dados do site Fundamentus que, por sua vez, é
    especializado em consolidar e disponibilizar informações fundamentalistas
    de empresas e fundos imobiliários listados na B3.

    Para um melhor esclarecimento sobre as reais informações disponibilizadas
    pelo portal alvo de extração deste módulo Python, consulte o site
    [Fundamentus](https://www.fundamentus.com.br/.)

    Examples:
        ```python
        # Importando classe
        from pynvest.fundamentus import Fundamentus

        # Em construção
        ```

    Args:
        Em construção
    """

    def __init__(
        self,
        logger_level: int = logging.INFO,
        url_tickers_acoes: str = URL_TICKERS_ACOES,
        url_tickers_fiis: str = URL_TICKERS_FIIS,
        request_header: dict = REQUEST_HEADER
    ) -> None:
        # Configurando objeto de logger
        self.logger_level = logger_level
        self.logger = log_config(logger_level=self.logger_level)

        # Definindo URLs de extração de nomes de ativos
        self.url_tickers_acoes = url_tickers_acoes
        self.url_tickers_fiis = url_tickers_fiis

        # Definindo informações das requisições realizadas
        self.request_header = request_header

    def extracao_tickers_de_ativos(self, tipo: str = "ações") -> list[str]:
        """
        Extrai uma lista formada por tickers de ações ou FIIs listados na B3.

        Este método é responsável por extrair uma lista de tickers (siglas) de
        Ações ou Fundos Imobiliários listados na Bolsa brasileira (B3). Para
        isso, os seguintes passos são realizados em tempo de execução:

        1. Faz-se uma requisição à URLs específicas disponibilizada pelo
        site Fundamentus de acordo com tipo definido pelo usuário (tickers
        de Ações ou tickers de FIIs)
        2. O resultado é obtido em formato HTML e tratado através da
        biblioteca BeautifulSoup
        3. Com o conteúdo tratado, extai-se uma lista ordenada de tickers
        de Ações ou de FIIs.

        Note: Sobre os tickers de Ações ou Fundos Imobiliários
            De acordo com a dinâmica do próprio portal Fundamentus, existem
            URLs diferentes para visualização dos tickers de Ações e de FIIs.

            - [Ações]("https://www.fundamentus.com.br/resultado.php")
            - [FIIs]("https://www.fundamentus.com.br/fii_resultado.php")

            A requisição via requests e o web scrapping via BeautifulSoup é o
            mesmo para ambas as URLs. Entretanto, pelo fato de existirem URLs
            distintas para cada cenário, o usuário precisa informar, em tempo
            de chamada do método, se deseja extrair tickers de Ações ou FIIs.
            Isto pode ser feito pelo parâmetro `tipo` do método.

        Args:
            tipo (str):
                Define que tipo de listagem de tickers da B3 o usuário deseja
                obter. Os valores possíveis são "ações" ou "fiis". Dentro do
                método, existem tratativas em strings para transformar este
                input do usuário em letras minúsculas e sem espaços ao final.
        
        Returns:
            Uma lista de strings contendo as siglas das Ações ou FIIs.

        Raises:
            Exception: exceção genérica ao tentar realizar a requisição para \
                a URL alvo da extração dos tickers.

        Examples:
            ```python
            # Importando classe
            from pynvest.fundamentus import Fundamentus

            # Instanciando objeto da classe
            fund = Fundamentus()

            # Obtendo tickers de ações
            tickers_acoes = fund.extracao_tickers_de_ativos(tipo="ações")
            # ['AALR3', 'ABCB3', 'ABCB4', 'ABEV3', 'ABYA3', 'ACES3', ...]
            ```
        """

        # Validando se o usuário forneceu o tipo adequado
        tipo_prep = tipo.strip().lower()
        if tipo_prep not in ("ações", "fiis"):
            raise TypeError(f"Tipo inválido para o método (tipo={tipo}). "
                            "Opções válidas: 'ações' ou 'fiis'.")

        # Verificando se o usuário deseja extrair tickers de ações
        if tipo_prep == "ações":
            url = self.url_tickers_acoes
            self.logger.debug("Extraindo lista de tickers de ações da B3")
        else:
            # Usuário deseja extrair tickers de FIIs
            url = self.url_tickers_fiis
            self.logger.debug("Extraindo lista de tickers de FIIs da B3")

        # Coletando conteúdo da requisição em HTML e tratando
        try:
            html_content = requests.get(url, headers=self.request_header).text
            soup = BeautifulSoup(html_content, "lxml")

        except Exception as e:
            self.logger.error(f"Erro de requisição à URL {url}. "
                              f"Exception: {e}")
            raise e

        # Tratando conteúdo e listando tickers
        tickers = [
            row.find_all("a")[0].text.strip()
            for row in soup.find_all("tr")[1:]
        ]
        self.logger.info("Processo de extração finalizado com sucesso com "
                         f"{len(tickers)} encontrados")

        return sorted(tickers)
