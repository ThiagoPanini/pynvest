"""Módulo: pynvest.scrappers.fundamentus

Este módulo proporciona uma série de funcionalidades específicas para extrair
indicadores financeiros do site Fundamentus.

___
"""

# Importando bibliotecas
import logging
from pynvest.utils.log import log_config

import requests
from bs4 import BeautifulSoup

from datetime import datetime, timezone, timedelta

import pandas as pd


""" -------------------------------------------------
    VARIÁVEIS
    Definindo variáveis de requisição ao site
------------------------------------------------- """

# URL para extração de todos os tickers de ações e FIIs
URL_TICKERS_ACOES = "https://www.fundamentus.com.br/resultado.php"
URL_TICKERS_FIIS = "https://www.fundamentus.com.br/fii_resultado.php"

# URL básica para extração de informações de ações
URL_KPIS_TICKER = "https://www.fundamentus.com.br/detalhes.php?papel="

# Header da requisição
REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) "
                  "Gecko/20100101 Firefox/50.0"
}

# Lista de indicadores de variação temporal não presentes na regra de extração
VARIATION_HEADINGS = [
    "Dia", "Mês", "30 dias", "12 meses"
] + [str(datetime.now().year - i) for i in range(6)]

# Estabelecendo indicadores financeiros de ações
METADATA_COLS_ACOES = {
    "Papel": "nome_papel",
    "Tipo": "tipo_papel",
    "Empresa": "nome_empresa",
    "Setor": "nome_setor",
    "Subsetor": "nome_subsetor",
    "Cotação": "vlr_cot",
    "Data últ cot": "dt_ult_cot",
    "Min 52 sem": "vlr_min_52_sem",
    "Max 52 sem": "vlr_max_52_sem",
    "Vol $ méd (2m)": "vol_med_neg_2m",
    "Valor de mercado": "vlr_mercado",
    "Valor da firma": "vlr_firma",
    "Últ balanço processado": "dt_ult_balanco_proc",
    "Nro. Ações": "num_acoes",
    "Dia": "pct_var_dia",
    "Mês": "pct_var_mês",
    "30 dias": "pct_var_30d",
    "12 meses": "pct_var_12m",
    "2023": "pct_var_2023",
    "2022": "pct_var_2022",
    "2021": "pct_var_2021",
    "2020": "pct_var_2020",
    "2019": "pct_var_2019",
    "2018": "pct_var_2018",
    "P/L": "vlr_ind_p_sobre_l",
    "P/VP": "vlr_ind_p_sobre_vp",
    "P/EBIT": "vlr_ind_p_sobre_ebit",
    "PSR": "vlr_ind_psr",
    "P/Ativos": "vlr_ind_p_sobre_ativ",
    "P/Cap. Giro": "vlr_ind_p_sobre_cap_giro",
    "P/Ativ Circ Liq": "vlr_ind_p_sobre_ativ_circ_liq",
    "Div. Yield": "vlr_ind_div_yield",
    "EV / EBITDA": "vlr_ind_ev_sobre_ebitda",
    "EV / EBIT": "vlr_ind_ev_sobre_ebit",
    "Cres. Rec (5a)": "pct_cresc_rec_liq_ult_5a",
    "LPA": "vlr_ind_lpa",
    "VPA": "vlr_ind_vpa",
    "Marg. Bruta": "vlr_ind_margem_bruta",
    "Marg. EBIT": "vlr_ind_margem_ebit",
    "Marg. Líquida": "vlr_ind_margem_liq",
    "EBIT / Ativo": "vlr_ind_ebit_sobre_ativo",
    "ROIC": "vlr_ind_roic",
    "ROE": "vlr_ind_roe",
    "Liquidez Corr": "vlr_liquidez_corr",
    "Div Br/ Patrim": "vlr_ind_divida_bruta_sobre_patrim",
    "Giro Ativos": "vlr_ind_giro_ativos",
    "Ativo": "vlr_ativo",
    "Disponibilidades": "vlr_disponibilidades",
    "Ativo Circulante": "vlr_ativ_circulante",
    "Dív. Bruta": "vlr_divida_bruta",
    "Dív. Líquida": "vlr_divida_liq",
    "Patrim. Líq": "vlr_patrim_liq",
    "Receita Líquida_1": "vlr_receita_liq_ult_12m",
    "EBIT_1": "vlr_ebit_ult_12m",
    "Lucro Líquido_1": "vlr_lucro_liq_ult_12m",
    "Receita Líquida": "vlr_receita_liq_ult_3m",
    "EBIT": "vlr_ebit_ult_3m",
    "Lucro Líquido": "vlr_lucro_liq_ult_3m"
    # "Cart. de Crédito": "vlr_cart_de_cred",
    # "Depósitos": "vlr_depositos",
    # "Patrim. Líq": "vlr_patrim_liq",
    # "Result Int Financ_1": "vlr_result_int_financ_ult_12m",
    # "Rec Serviços_1": "vlr_rec_servicos_ult_12m",
    # "Lucro Líquido_1": "vlr_lucro_liq_ult_12m",
    # "Result Int Financ": "vlr_result_int_financ_ult_3m",
    # "Rec Serviços": "vlr_rec_servicos_ult_3m"
}

# Estabelecendo indicadores financeiros de ações
METADATA_COLS_FIIS = {
    "FII": "fii",
    "Nome": "nome_fii",
    "Mandato": "tipo_mandato",
    "Segmento": "segmento",
    "Gestão": "tipo_gestao",
    "Cotação": "vlr_cot",
    "Data últ cot": "data_ult_cot",
    "Min 52 sem": "min_52_sem",
    "Max 52 sem": "max_52_sem",
    "Vol $ méd (2m)": "vol_med_neg_2m",
    "Valor de mercado": "vlr_mercado",
    "Nro. Cotas": "num_cotas",
    "Relatório": "dt_ult_relat_ger",
    "Últ Info Trimestral": "dt_ult_informe_trim",
    "Dia": "pct_var_dia",
    "Mês": "pct_var_mes",
    "30 dias": "pct_var_30d",
    "12 meses": "pct_var_12m",
    "2023": "pct_var_2023",
    "2022": "pct_var_2022",
    "2021": "pct_var_2021",
    "2020": "pct_var_2020",
    "2019": "pct_var_2019",
    "2018": "pct_var_2018",
    "FFO Yield": "vlr_ffo_yield",
    "FFO/Cota": "vlr_ffo_sobre_cota",
    "Div. Yield": "vlr_div_yield",
    "Dividendo/cota": "vlr_dividendo_sobre_cota",
    "P/VP": "vlr_p_sobre_vp",
    "VP/Cota": "vlr_vp_sobre_cota",
    "Receita_1": "vlr_rec_bruta_ult_12m",
    "Venda de ativos_1": "vlr_vend_ativ_ult_12m",
    "FFO_1": "vlr_ffo_ult_12m",
    "Rend. Distribuído_1": "vlr_rendim_distr_ult_12m",
    "Receita": "vlr_rec_bruta_ult_3m",
    "Venda de ativos": "vlr_vend_ativ_ult_3m",
    "FFO": "vlr_ffo_ult_3m",
    "Rend. Distribuído": "vlr_rendim_distr_ult_3m",
    "Ativos": "vlr_ativos",
    "Patrim Líquido": "vlr_patrim_liq",
    "Qtd imóveis": "qtd_imoveis",
    "Qtd Unidades": "qtd_unidades",
    "Imóveis/PL do FII": "vlr_imoveis_sobre_pl",
    "Área (m2)": "total_area_m2",
    "Aluguel/m2": "vlr_aluguel_por_m2",
    "Preço do m2": "vlr_do_m2",
    "Cap Rate": "vlr_cap_rate",
    "Vacância Média": "vlr_vacancia_media",
}


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
        from pynvest.scrappers.fundamentus import Fundamentus

        # Instanciando objeto da classe
        pynvest_scrapper = Fundamentus()

        # Extraindo tickers de Ações e FIIs da bolsa
        tickers_acoes = pynvest_scrapper.extracao_tickers_de_ativos()
        tickers_fiis = pynvest_scrapper.extracao_tickers_de_ativos(tipo="fiis")

        # Extraindo indicadores de uma Ação ou FII da bolsa
        df_itsa4 = pynvest_scrapper.coleta_indicadores_de_ativo("itsa4")
        df_xplg11 = pynvest_scrapper.coleta_indicadores_de_ativo("xplg11")
        ```

    Args:
        logger_level (int, optional):
            Nível do objeto de log a ser configurado

        url_tickers_acoes (str, optional):
            URL utilizada para extrair todos os tickers de Ações listadas na
            B3 através do site Fundamentus. No momento de construção da lib,
            a URL necessária para tal ação foi mapeada e registrada na
            variável URL_TICKERS_ACOES acessível no módulo fundamentus.py.

        url_tickers_acoes (str, optional):
            URL utilizada para extrair todos os tickers de FIIs listados na
            B3 através do site Fundamentus. No momento de construção da lib,
            a URL necessária para tal ação foi mapeada e registrada na
            variável URL_TICKERS_FIIS acessível no módulo fundamentus.py.

        url_kpis_ticker (str, optional):
            URL utilizada para extrair indicadores fundamentalistas de ativos
            (Ações e B3) através do site Fundamentus. No momento de construção
            da lib, a URL necessária para tal ação foi mapeada e registrada na
            variável URL_KPIS_TICKER acessível no módulo fundamentus.py.

        request_header (dict, optional):
            Dicionário contendo header para configuração das requisições
            realizadas ao site Fundamentus. No momento de construção
            da lib, o header da requisição necessário para tal ação foi
            mapeado e registrao na variável REQUEST_HEADER acessível no módulo
            fundamentus.py.

        variation_headings (list, optional):
            Lista de indicadores de variação que precisam ser manualmente
            definidos por conta da dificuldade de captura automática no
            processo de Web Scrapping e parse do HTML resultante da requisição.
            Em linhas gerais, os indicadores fundamentalistas dos ativos contam
            com tabelas de oscilações que mostram a variação do determinado
            ativo ao longo do tempo (períodos diários, mensais e até anuais).
            Tais atributos de variação fogem à regra de extração automática
            por conta da própria construção do site Fundamentus. Dessa forma,
            a única forma de extrair e assimilar tais indicadores de variação
            é associando-os manualmente em um atributo da classe para que os
            mesmos possam ser considerados no ato da extração. Na visão do
            usuário da biblioteca, nenhuma ação é requerida, visto que essa
            "associação manual" é feita diretamente no módulo e não exige
            nenhum tipo de atualização (a não ser que o próprio site
            Fundamentus sobre alterações bruscas).

        metadata_cols_acoes (dict, optional):
            Ao extrair indicadores financeiros de Ações da B3, uma série de
            atributos podem ser analisados e consolidados. Para garantir que
            as extrações, estas baseadas no parse de uma página HTML, tenham
            uma padronização pré definida em termos da nomenclatura e da
            ordem na qual os atributos/indicadores são extraídos, este
            atributo considera a presença de um dicionário de mapeamento
            contendo o nome original do atributo/indicador financeiro
            presente no site e seu respectivo nome já preparado conforme
            algumas regras e boas práticas de armazenamento de dados, como
            por exemplo, a remoção de caracteres especiais, espaços, etc.
            Este processo já é definido previamente no próprio módulo e
            acessível através da variável METADATA_COLS_ACOES.

        metadata_cols_fiis (dict, optional):
            Existe uma diferença entre os indicadores oferecidos para Ações
            e para Fundos Imobiliários. Isto faz total sentido, pois tratam-se
            de ativos totalmente diferentes. Assim, por conta disso, um
            dicionário de mapeamento de nomes de colunas para FIIs se faz
            necessário (nos mesmos moldes do atributo metadata_cols_acoes).
            Assim como no caso mencionado, este processo já é definido
            previamente no próprio módulo e acessível através da variável
            METADATA_COLS_FIIS.

    Tip: Preparação dos atributos da classe Fundamentus
        Você deve ter notado que, em essência, todos os atributos da classe
        são opcionais. Isto foi pensado para aliviar ao máximo o lado do
        usuário ao consumir a solução, não exigindo que nenhuma configuração
        adicional seja fornecida (se o usuário assim entender que faça
        sentido).

        Em outras palavras, para começar a utilizar a classe Fundamentus,
        basta inicializá-la em seu modo padrão e executar seus métodos.
    """

    def __init__(
        self,
        logger_level: int = logging.INFO,
        url_tickers_acoes: str = URL_TICKERS_ACOES,
        url_tickers_fiis: str = URL_TICKERS_FIIS,
        url_kpis_ticker: str = URL_KPIS_TICKER,
        request_header: dict = REQUEST_HEADER,
        variation_headings: list = VARIATION_HEADINGS,
        metadata_cols_acoes: dict = METADATA_COLS_ACOES,
        metadata_cols_fiis: dict = METADATA_COLS_FIIS
    ) -> None:
        # Configurando objeto de logger
        self.logger_level = logger_level
        self.logger = log_config(logger_level=self.logger_level)

        # Definindo URLs de requisição ao site
        self.url_tickers_acoes = url_tickers_acoes
        self.url_tickers_fiis = url_tickers_fiis
        self.url_kpis_ticker = url_kpis_ticker

        # Definindo informações das requisições realizadas
        self.request_header = request_header

        # Definindo lista de indicadores financeiros de variação
        self.variation_headings = variation_headings

        # Definindo colunas de indicadores de ativos
        self.metadata_cols_acoes = metadata_cols_acoes
        self.metadata_cols_fiis = metadata_cols_fiis

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
            from pynvest.scrappers.fundamentus import Fundamentus

            # Instanciando objeto da classe
            pynvest_scrapper = Fundamentus()

            # Obtendo tickers de Ações
            tickers_acoes = pynvest_scrapper.extracao_tickers_de_ativos()
            # ['AALR3', 'ABCB3', 'ABCB4', 'ABEV3', 'ABYA3', 'ACES3', ...]

            # Obtendo tickers de Fundos Imobiliários
            tickers_fiis = pynvest_scrapper.extracao_tickers_de_ativos(
                tipo="fiis"
            )
            # ['AAZQ11', 'ABCP11', 'AEFI11', 'AFCR11', 'AFHI11', ...]
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
        self.logger.debug("Processo de extração finalizado com sucesso com "
                          f"{len(tickers)} encontrados")

        return sorted(list(set(tickers)))

    def coleta_indicadores_de_ativo(self, ticker: str) -> pd.DataFrame:
        """
        Extrai indicadores de um ativo específico em um formato de DataFrame.

        Este método é responsável por realizar uma requisição à página
        Funtamentus através de uma URL capaz de entregar indicadores gerais
        sobre um determinado ativo, seja ele um ticker de Ação ou de um FII.
        O resultado é então tratado através de uma série de regras pré
        estabelecidas de acordo com a dinâmica de resposta da requisição e,
        enfim, o retorno ao usuário se dá a partir de um DataFrame do pandas
        pré configurado com os mais variados indicadores do ativo selecionado.

        Em linhas gerais, os passos consolidados no método são:

        1. Faz-se uma requisição à uma URL específica do site Fundamentus para
        expor indicadores fundamentalistas de um determinado ativo (parâmetro
        ticker é substituído como um placeholder na URL antes da requisição).
        2. O resultado é obtido em formato HTML e tratado através da
        biblioteca BeautifulSoup.
        3. Laços de repetição são realizados para iterar sobre todas as
        tabelas do conteúdo HTML obtido em busca da extração dos indicadores.
        4. Um DataFrame pandas é gerado com colunas pré definidas e valores
        extraídos como resultado do tratamento proposto.

        Question: Quais indicadores são extraídos e entregues de fato?
            Considerando o conteúdo presente no site Fundamentus, a URL para
            visualizar indicadores de Ações e FIIs é a mesma, com a diferença
            do ticker substituído como placeholder antes da requisição.

            Entretanto, requisitar indicadores de uma Ação (ex: ITUB3) traz
            resultados diferentes de uma requisição de indicadores de um FII
            (ex: BTLG11). Isto é totalmente plausível, visto que tratam-se de
            ativos completamente diferentes em termos financeiros.

            Dessa forma, para entregar DataFrames adequados para cada tipo de
            ativo, dois mappers distintos foram considerados como variáveis
            estáticas do módulo como dicionários Python contendo todos os
            nomes de colunas/indicadores de Ações e também de FIIs. Tais
            mappers são representados pelas variáveis:

            - METADATA_COLS_ACOES para requisições à indicadores de Ações
            - METADATA_COLS_FIIS para requisições à indicadores de FIIs

            O usuário não precisa informar previamente à execução do método
            se a requisição de indicadores é de uma Ação ou de um FII. Isto é
            feito automaticamente dentro do método através de validações de
            conteúdos das páginas obtidas em cada cenário. Em outras palavras,
            regras internas do próprio método definem quais colunas associar
            ao DataFrame resultante (Ações ou FIIs).

        Args:
            ticker (str):
                Referência do ticker do papel (Ação) ou FII a ser alvo da
                extração de indicadores.

        Returns:
            DataFrame pandas com indicadores financeiros do ativo escolhido.

        Raises:
            KeyError: exceção lançada quando há uma tentativa inválida de \
                mapear colunas pré definidas em uma lista ao DataFrame \
                resultante do processo de requisição e tratamento de \
                indicadores financeiros, indicando assim um mismatch entre \
                o conteúdo do site e o conteúdo previamente mapeado e validado

        Examples:
            ```python
            # Importando classe
            from pynvest.scrappers.fundamentus import Fundamentus

            # Instanciando objeto da classe
            pynvest_scrapper = Fundamentus()

            # Obtendo indicadores financeiros de uma Ação
            df_itub3 = pynvest_scrapper.coleta_indicadores_de_ativo("itub3")

            # Ou também, obtendo indicadores financeiros de um FII
            df_btlg11 = pynvest_scrapper.coleta_indicadores_de_ativo("btlg11")
            ```
        """

        # Concatenando URL básica de extração com nome do ativo (ticker)
        url = self.url_kpis_ticker + ticker.strip().upper()

        # Realizando requisição e tratando conteúdo via BeautifulSoup
        html_content = requests.get(url=url, headers=self.request_header).text
        soup = BeautifulSoup(html_content, "lxml")

        # Obtendo todas as tabelas da página de indicadores do ativo
        tables = soup.find_all("table", attrs={'class': 'w728'})

        # Iterando sobre todas as tabelas da página
        financial_data_raw = []
        for table in tables:
            # Extraindo linhas da tabela
            table_row = table.find_all("tr")

            # Iterando sobre linhas da tabela
            for table_data in table_row:
                # Extraindo lista de células da linha
                cells_list = table_data.find_all("td")

                # Coletando headings de células (atributos)
                headings = [
                    cell.text.replace("?", "").strip()
                    for cell in cells_list
                    if "?" in cell.text or cell.text in self.variation_headings
                ]

                # Iterando por headings para procurar por elementos duplicados
                for header in headings:
                    if headings.count(header) > 1:
                        new_header_name = header + "_1"
                        headings[headings.index(header)] = new_header_name

                # Coletando valores das células (indicadores)
                values = [
                    cell.text.strip() for cell in cells_list
                    if ("?" not in cell.text) and (cell.text not in headings)
                ]

                # Gerando dicionário com os elementos das linhas
                table_data_dict = {
                    header: value for header, value in zip(headings, values)
                }

                # Adicionando dicionários que possuem dados válidos extraídos
                if table_data_dict != {}:
                    financial_data_raw.append(table_data_dict)

        # Preparando dicionário único a partir de lista de dicionários extraída
        financial_data = {
            name: value for dictionary in financial_data_raw
            for name, value in dictionary.items()
        }

        # Validando se a extração do ativo é de uma Ação ou de um FII
        if "Papel" in financial_data:
            # Ação: devemos assumir os metadados/indicadores de FIIs
            metadata_cols = self.metadata_cols_acoes
        elif "FII" in financial_data:
            # FII: devemos assumir os metadados/indicadores de Ações
            metadata_cols = self.metadata_cols_fiis
        else:
            raise TypeError("Não foram encontradas informações financeiras "
                            f"para o ticker '{ticker}'. Verifique se o mesmo "
                            "refere-se a uma Ação ou Fundo Imobiliário.")

        # Criando DataFrame pandas com indicadores financeiros do ativo
        df_ativo_raw = pd.DataFrame(financial_data, index=[0])

        # Renomeando atributos/indicadores para melhor análise
        df_indicadores_ativo = df_ativo_raw.rename(
            columns=metadata_cols,
            errors="ignore"
        )

        # Reordenando colunas com base em dicionário de metadados pré definido
        try:
            dataset_cols = list(metadata_cols.values())
            df_indicadores_ativo = df_indicadores_ativo[dataset_cols]

        except KeyError as ke:
            self.logger.debug("Ocorreu um erro ao tentar mapear as colunas "
                              "dos indicadores financeiros no DataFrame "
                              "resultante do processo de web scrapping para "
                              f"o ticker {ticker}.\n\n"
                              "Existem uma série de motivos capazes de "
                              "ocasionar esta falha no mapeamento, como por "
                              "exemplo:\n\n"
                              "1. Alteração no layout do portal Fundamentus.\n"
                              "2. Diferença entre indicadores entre ativos "
                              "distintos.\n\n"
                              "Por experiências de consumo, o layout do site "
                              "não costuma sofrer alterações, sendo mais "
                              "provável a segunda hipótese que defende que "
                              "diferentes ativos podem apresentar diferentes "
                              "indicadores.\n\n"
                              "Pesquise manualmente no site Fundamentus pelos "
                              "ativos 'ITUB3' e 'ITSA4' e veja como os dados "
                              "do balanço patrimonial e do demonstrativo de "
                              "resultados possuem indicadores diferentes.\n\n"
                              f"Exception: {ke}")

            self.logger.debug("Iterando sobre colunas mapeadas e validando "
                              "quais delas não estão presentes no DataFrame "
                              f"resultante para o ticker {ticker}.")
            for col in dataset_cols:
                if col not in list(df_indicadores_ativo.columns):
                    df_indicadores_ativo[col] = None

        # Reordenando DataFrame agora que todas as colunas existem
        df_indicadores_ativo = df_indicadores_ativo[dataset_cols]

        # Adicionando informação de data e hora de processamento
        now = datetime.now(timezone(timedelta(hours=-3)))
        date_exec = now.strftime("%d-%m-%Y")
        datetime_exec = now.strftime("%d-%m-%Y %H:%M:%S")
        df_indicadores_ativo.loc[:, ["date_exec"]] = date_exec
        df_indicadores_ativo.loc[:, ["datetime_exec"]] = datetime_exec

        return df_indicadores_ativo
