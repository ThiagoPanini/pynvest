"""
---------------------------------------------------
--------------- MÓDULO: fundamentus ---------------
---------------------------------------------------
Neste módulo, será proposta a construção de classes
e funções capazes de extrair uma gama de indicadores
financeiros de empresas/ativos da bolsa de valores
a partir do processo de web scrapping na plataforma 
Fundamentus (https://www.fundamentus.com.br/).  

Como informação principal de pesquisa e cruzamento,
será utilizada a sigla do papel/ativo na bolsa de
valores (exemplo: "ITSA4" para Itaúsa), permitindo
assim a extração de indicadores fundamentalistas ou
até mesmo de oscilações da cotação do referido ativo.

Table of Contents
---------------------------------------------------
1. Configurações Iniciais
    1.1 Importando bibliotecas
    1.2 Configurando logs
    1.3 Funções auxiliares para uso interno
2. Web Scrapping de Indicadores
    2.1 Classe encapsulada
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

# Bibliotecas gerais 
import os
import pandas as pd
from datetime import datetime

# Requisições e tratamento de conteúdo
import requests
from bs4 import BeautifulSoup

# Logging
import logging

from requests.api import head


"""
---------------------------------------------------
------------ 1. CONFIGURAÇÕES INICIAIS ------------
               1.2 Configurando logs
---------------------------------------------------
"""

# Definindo função para gerenciamento de logs
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
------------ 1. CONFIGURAÇÕES INICIAIS ------------
     1.3 Funções auxiliares para uso interno
---------------------------------------------------
"""

# Definindo função para salvamento de arquivos .csv
def save_data(df, output_path, filename):
    """
    Método responsável por centralizar a ação de salvamento
    de arquivos em formato csv em diretórios locais do
    sistema operacional de trabalho. Adicionalmente, o método
    é composto por lógicas adicionais que são capazes de 
    verificar a existência de um diretório passado para que,
    em caso de inexistência da referência, seja possível
    criar a pasta em questão.

    Parâmetros
    ----------
    :param df:
        Objeto DataFrame do pandas a ser salvo.
        [type: pd.DataFrame]

    :param output_path:
        Referência de diretório destino do arquivo. Caso o caminho
        não exista no sistema operacional de trabalho, uma nova
        pasta com o mesmo nome será criada para alocar o arquivo.
        [type: string]

    :param filename:
        Referência do nome do arquivo a ser salvo. Para este
        argumento, é importante passar o nome do arquivo com
        a devida extensão em formato .csv (ou .txt, em alguns
        casos)
        [type: string]
    """

    # Verificando se o diretório passado existe
    if not os.path.isdir(output_path):
        logger.warning(f'Diretório {output_path} não existe no SO. Criando uma nova pasta com a mesma referência')
        try:
            os.makedirs(output_path)
        except Exception as e:
            logger.error(f'Erro ao tentar criar o diretório {output_path}. Exception: {e}')
            return
    
    # Salvando arquivo
    try:
        output_file = os.path.join(output_path, filename)
        df.to_csv(output_file, index=False, encoding='utf-8')
        logger.debug(f'Arquivo {filename} salvo com sucesso no diretório especificado')
    except Exception as e:
        logger.error(f'Erro ao salvar arquivo {filename}. Exception: {e}')


"""
---------------------------------------------------
--------- 2. WEB SCRAPPING DE INDICADORES ---------
               2.1 Classe Encapsulada
---------------------------------------------------
"""

class AtivosFundamentus:
    """
    Classe responsável por propor análises detalhadas sobre
    ativos financeiros a partir de consulta a uma URL do
    site Fundamentus, permitindo assim a construção de uma
    série de métodos capazes de receber uma lista de ações
    da bolsa de valores e extrair uma série de indicadores
    financeiros dos ativos selecionados, como por exemplo, 
    as cotações atualizadas, variações de época, lucros, 
    margens, P/L, P/VP, entre outros.
    
    Com essa classe, o usuário poderá aprimorar o 
    gerenciamento de investimentos financeiros realizados
    na bolsa de valores brasileria através de uma análise
    específica em uma série de ativos.
    
    Atributos da classe
    -------------------
    :attr basic_url:
        URL básica de consulta utilizada para extração de
        informações de um ativo no site Fundamentus. Para
        a devida pesquisa de um ativo, este template de 
        url deve ser concatenado com a referência ou sigla
        do papel a ser analisado.
        [type: string,
         default='https://www.fundamentus.com.br/detalhes.php?papel=']

    :attr tickers_url_acoes:
        URL de consulta para extração de todos os tickers de ações
        presentes na bolsa de valores. Para validação desta
        rota, basta acessar o site Fundamentus, clicar em pesquisa
        avançada de ações e seguir com o botão "Exibir" sem 
        preencher nenhuma informação. O resultado será uma 
        lista detalhada de todas as ações presentes na bolsa.
        [type: string, 
         default='https://www.fundamentus.com.br/resultado.php']

    :attr tickers_url_fiis:
        URL de consulta para extração de todos os tickers de FIIs
        presentes na bolsa de valores. Para validação desta
        rota, basta acessar o site Fundamentus, clicar em pesquisa
        avançada de FIIs e seguir com o botão "Exibir" sem 
        preencher nenhuma informação. O resultado será uma 
        lista detalhada de todas as ações presentes na bolsa.
        [type: string, 
         default='https://www.fundamentus.com.br/fii_resultado.php']
        
    :attr headers:
        Cabeçalho da requisição a ser passado como parâmetro
        da chamada. Em alguns sistemas operacionais ou em
        alguns sites alvo, este parâmetro é essencial para 
        evitar erros de permissão (código 403).
        [type: dict,
         default={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}]
        
    :attr custom_headings:
        Dentro da proposta de extração de indicadores, as
        tabelas fornecidas no site Fundamentus possuem
        algumas particularidades que precisam ser gerenciadas
        dentro da lógica construída nos métodos dessa classe.
        Uma das particularidades envolve as informações de
        variação na cotação do ativo em determinados 
        intervalos de análise. Este atributo tem como objetivo
        pontuar algumas referências de colunas que possuem
        tais particularidades de posicionamento para que o 
        código escrito possa tratar estes casos de maneira
        especial de modo a coletar as informações corretas
        para cada bloco de informação.
        [type: list,
         default=['Dia', 'Mês', '30 dias', '12 meses'] + [str(datetime.now().year-i) for i in range(6)]]
        
    :attr columns:
        Colunas a serem consideradas na base final gerada
        após a extração dos indicadores do site Fundamentus.
        Este atributo funciona como um filtro colunar aplicado
        a base completa extraída.
        [type: list
         default=['Papel', 'Empresa', 'Setor', 'Subsetor', 'Cotação', 'Data últ cot', 'Min 52 sem', 'Max 52 sem'] + \
                 CUSTOM_HEADINGS[:7] + ['P/L', 'P/VP', 'LPA', 'VPA', 'EV / EBITDA', 'Div. Yield', 'ROE', 'ROIC', 
                                        'Marg. Bruta', 'Marg. EBIT', 'Marg. Líquida', 'Lucro Líquido']]
    """
    
    def __init__(self, 
                 basic_url='https://www.fundamentus.com.br/detalhes.php?papel=',
                 tickers_url_acoes='https://www.fundamentus.com.br/resultado.php',
                 tickers_url_fiis='https://www.fundamentus.com.br/fii_resultado.php',
                 headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'},
                 custom_headings=['Dia', 'Mês', '30 dias', '12 meses'] + [str(datetime.now().year-i) for i in range(6)]
                 ):
        self.basic_url = basic_url
        self.tickers_url_acoes = tickers_url_acoes
        self.tickers_url_fiis = tickers_url_fiis
        self.headers = headers
        self.custom_headings = custom_headings
        
        # Definindo colunas a serem filtradas da base analítica de ações
        self.cols_filter_acoes = ['Papel', 'Empresa', 'Setor', 'Subsetor', 'Cotação', 'Data últ cot', 'Min 52 sem', 'Max 52 sem'] + \
                                  self.custom_headings[:7] + ['P/L', 'P/VP', 'LPA', 'VPA', 'EV / EBITDA', 'Div. Yield', 'ROE', 'ROIC', 
                                                              'Marg. Bruta', 'Marg. EBIT', 'Marg. Líquida', 'Lucro Líquido']

        # Definindo colunas a serem filtradas da base analítica de FIIs
        self.cols_filter_fiis = ['FII', 'Nome', 'Segmento', 'Mandato', 'Cotação', 'Data últ cot', 'Min 52 sem', 'Max 52 sem'] + \
                                 self.custom_headings[:7] + ['Div. Yield', 'Dividendo/cota', 'FFO Yield', 'FFO/Cota', 'P/VP', 'VP/Cota',
                                                             'Receita', 'Venda de ativos', 'FFO', 'Rend. Distribuído', 'Ativos', 
                                                             'Patrim Líquido', 'Qtd imóveis', 'Qtd Unidades', 'Imóveis/PL do FII',
                                                             'Área (m2)', 'Aluguel/m2', 'Preço do m2', 'Cap Rate', 'Vacância Média']
        
        # Definindo colunas finais da base de ações
        self.cols_rename_acoes = ['Papel', 'Empresa', 'Setor', 'Subsetor', 'Cotação', 'Data últ cot', 'Min 13M', 'Max 13M', 'Var Dia',
                                  'Var Mês', 'Var 30D', 'Var 12M', 'Var 2021', 'Var 2020', 'Var 2019', 'P/L', 'P/VP', 'LPA', 'VPA', 
                                  'EV / EBITDA', 'DY', 'ROE', 'ROIC', 'Marg. Bruta', 'Marg. EBIT', 'Marg. Líquida', 'Lucro Líquido']

        # Definindo colunas finais da base de fiis
        self.cols_rename_fiis = ['FII', 'Nome', 'Segmento', 'Mandato', 'Cotação', 'Data últ cot', 'Min 13M', 'Max 13M', 'Var Dia',
                                 'Var Mês', 'Var 30D', 'Var 12M', 'Var 2021', 'Var 2020', 'Var 2019', 'DY', 'Dividendo/cota', 
                                 'FFO Yield', 'FFO/Cota', 'P/VP', 'VP/Cota', 'Receita', 'Venda de ativos', 'FFO', 'Rend. Distribuído', 
                                 'Ativos', 'Patrim Líquido', 'Qtd imóveis', 'Qtd Unidades', 'Imóveis/PL do FII', 'Área (m2)', 
                                 'Aluguel/m2', 'Preço do m2', 'Cap Rate', 'Vacância Média']
    
    def extracao_tickers_bolsa(self, tipo='Ações'):
        """
        Método responsável por extrair todos os tickers (siglas)
        de ações listadas na bolsa de valores brasileira. Para
        tal, foi utilizado um processo de web scrapping no site
        Fundamentus a partir de uma url personalizada alcançada
        a partir de uma pesquisa vazia na página de pesquisa
        avançada de ações.

        Este método não recebe nenhum argumento externo e se
        utiliza os atributo "tickers_url_acoes" e "headers" 
        da classe.

        Parâmetros
        ----------
        :param tipo:
            Informação sobre o tipo de url a ser utilizada para
            a extração dos tickers. Visto que o site Fundamentus
            possui uma rota específica para cada tipo (Ações ou FIIs),
            é preciso informar esse dado para realizar uma atribuição
            interna no método sobre qual url a ser utilizada. O proceso
            de extração de tickers é idêntico para ambos os casos.

            Caso o usuário informe um valor diferente de "Ações" ou
            "FIIs", será considerada a url para a extração de tickers
            de "Ações".
            [type: string, default="Ações"]

        Retorno
        -------
        :return tickers:
            Lista com todos os tickers extraídos do site fundamentus,
            sejam estes relacionados a ações ou fiis
            [type: list]
        """
        
        # Determinando url de pesquisa de acordo com tipo de extração
        if tipo.lower().strip() == 'ações':
            url = self.tickers_url_acoes
            logger.debug(f'Extraindo todos os tickers de ações listadas na B3')
        elif tipo.lower().strip() == 'fiis':
            url = self.tickers_url_fiis
            logger.debug(f'Extraindo todos os tickers de FIIs listados na B3')
        else:
            logger.warning(f'Argumento tipo {tipo} inválido. Selecione entre "Ações" ou "FIIs"')
            logger.info(f'Considerando url de extração de tickers de "Ações"')
            url = self.tickers_url_acoes

        # Coletando conteúdo em html e transformando com BeautifulSoup
        try:
            html_content = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_content, 'lxml')
        except Exception as e:
            logger.error(f'Erro de requisição para a url {url}. Exception: {e}')
            exit()

        # Extraindo todos os tickers listados na requisição
        tickers = [row.find_all('a')[0].text.strip() for row in soup.find_all('tr')[1:]]
        logger.info(f'Processo de extração finalizado com {len(tickers)} siglas encontradas')
        
        return sorted(tickers)
    
    def analise_financeira_ativos(self, tipo='Ações', ativos='Todos', **kwargs):
        """"
        Método responsável por coletar os atributos da classe
        e iniciar um processo de extração de indicadores
        financeiros a partir de webscrapping no site
        Fundamentus. Neste método, são analisadas tabelas
        específicas contidas no site geradas a partir da
        pesquisa de ativos. Para isso, são utilizada as
        funcionalidades da biblioteca BeautifulSoup a
        serem implementadas no resultado bruto do HTML
        gerado a partir da requisição de pesquisa feita 
        no site. Com os resultados devidamente tratados,
        é proposta a construção de um objeto DataFrame
        com a disponibilização dos indicadores selecionados.

        Parâmetros
        ----------
        :param ativos:
            Lista de ativos, em formato de siglas, a ser
            utilizada dentro de um laço de repetição para
            a extração de indicadores. Este argumento do
            método é de extrema importância pois, em resumo,
            direciona toda a extração de ativos do código.
            Como aplicações práticas, é possível passar:
                * Uma lista com um único ativo para análises pontuais
                * Uma lista com uma série de ativos que compõem uma carteira
                * Uma lista completa de todos os ativos da bolsa para análises mais complexas
            [type: list]

        Argumentos adicionais
        ---------------------
        :kwarg verbose:
            Indicador para o fornecimento de mensagens de log
            ao usuário durante a execução do código.
            [type: bool, default=True]

        :kwarg ind_verbose:
            Em casos de extração de indicadores para uma lista
            relativamente grande de ativos, pode ser necessário
            um acompanhamento das chamadas logs durante o laço
            de repetição. Para isso, este argumento adicional
            funciona como uma espécie de "me informe o status
            a cada <ind_verbose> iterações do laço". Por via
            de regras, este argumento tem efeito somente se
            o argumento "verbose" estiver configurado como True
            [type: int, default=10]

        :kwarg save:
            Flag booleano que indica o salvamento do resultado
            gerado em um arquivo csv.
            [type: bool, default=False]

        :kwarg output_path:
            Referência de destino do arquivo final a ser salvo,
            caso o argumento save esteja configurado como True.
            [type: string, default=os.path.join(os.getcwd(), 'data')]

        :kwarg filename:
            Nome do arquivo a ser salvo localmente em formato csv.
            [type: string, default='indicadores_financeiros.csv']

        Retorno
        -------
        :return df_ind_financeiros:
            Objeto DataFrame do pandas contendo todos os indicadores
            de ativos extraídos e devidamente tratados de acordo
            com a lógica implementada dentro do método.
            [type: pd.DataFrame]
        """
        
        # Definindo parâmetros iniciais do código
        df_ind_financeiros = pd.DataFrame()
        i = 0
        verbose = kwargs['verbose'] if 'verbose' in kwargs else True
        ind_verbose = kwargs['ind_verbose'] if 'ind_verbose' in kwargs else 100
        tipo = tipo.lower().strip()

        # Validando tipo de análise
        if tipo not in ['ações', 'fiis']:
            logger.error(f'Tipo {tipo} inválido. Por favor, escolha entre "Ações" ou "FIIs"')
            return None

        # Extraindo tickers da bolsa caso o parâmetro não seja definido explicitamente
        if ativos.lower().strip() == 'todos':
            ativos = self.extracao_tickers_bolsa(tipo=tipo)

        # Iterando sobre a lista de ativos alvo da análise financeira
        logger.debug(f'Iniciando a extração de indicadores para {len(ativos)} tickers de {tipo} listados')
        for ativo in ativos:
            # Comunicando usuário (se aplicável)
            i += 1
            if verbose and (i % ind_verbose == 0):
                logger.debug(f'Extração realizada para {i} de {len(ativos)} {tipo}. Próximo da lista: {ativo}')

            # Criando url de requisição do ativo
            url = self.basic_url + ativo

            # Coletando e transformando conteúdo em HTML com BeautifulSoup
            html_content = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(html_content.text, 'lxml')

            # Encontrando tabelas de classe específica com indicadores financeiros do ativo
            invest_table = soup.find_all('table', attrs={'class': 'w728'})

            # Extraindo dados para todas as tabelas de análise
            financial_tables = []
            for table in invest_table:
                table_data = table.find_all('tr')
                # Iterando sobre as tabelas internas
                for td_data in table_data:

                    # Extraindo tabelas e listas específicas de colunas e valores
                    td = td_data.find_all('td')
                    headings = [h.text.replace('?', '').strip() for h in td if (('?' in h.text) or (h.text in self.custom_headings))]
                    contents = [c.text.strip() for c in td if ('?' not in c.text) and (c.text not in headings)]

                    # Gerando dicionário com os elementos e adicionando na lista geral de indicadores
                    table_data = {k: v for k, v in zip(headings, contents)}
                    if table_data != {}:
                        financial_tables.append(table_data)

            # Juntando em dicionário único e transformando em DataFrame
            financial_data = dict(pair for dictionary in financial_tables for pair in dictionary.items())
            df_ativo = pd.DataFrame(financial_data, index=[0])

            # Atribuindo colunas de filtro e de renomação de acordo com o tipo de extração
            if tipo == 'ações':
                cols_filter = self.cols_filter_acoes
                cols_rename = self.cols_rename_acoes
            elif tipo == 'fiis':
                cols_filter = self.cols_filter_fiis
                cols_rename = self.cols_rename_fiis

            # Filtrando indicadores
            try:
                df_ativo = df_ativo.loc[:, cols_filter]
            except KeyError as ke:
                continue
                
            # Adicionando ao DataFrame final
            df_ind_financeiros = df_ind_financeiros.append(df_ativo)

        # Renomenado colunas
        df_ind_financeiros.columns = cols_rename
            
        # Verificando salvamento do arquivo
        if 'save' in kwargs and bool(kwargs['save']):
            output_path = kwargs['output_path'] if 'output_path' in kwargs else os.path.join(os.getcwd(), 'data')
            if tipo == 'ações':
                output_filename = kwargs['output_filename'] if 'output_filename' in kwargs else 'detalhe_acoes_bolsa.csv'
            elif tipo == 'fiis':
                output_filename = kwargs['output_filename'] if 'output_filename' in kwargs else 'detalhe_fiis_bolsa.csv'
            
            save_data(df_ind_financeiros, output_path=output_path, filename=output_filename)
        
        logger.info(f'Extração de indicadores de ativos de {tipo} finalizada')
        
        return df_ind_financeiros

