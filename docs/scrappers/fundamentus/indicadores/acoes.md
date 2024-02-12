# Fundamentus: Indicadores de Ações

De forma objetiva, a tabela abaixo contempla uma lista de indicadores financeiros (e suas respectivas definições/descrições) disponíveis no site e obtidos como resultado do método [coleta_indicadores_de_ativo()](../../../mkdocstrings/scrappers/fundamentus.md/#pynvest.scrappers.fundamentus.Fundamentus.coleta_indicadores_de_ativo).

| **Nome Original** | **Atributo DataFrame** | **Descrição** |
| :-- | :-- | :-- |
| Papel | nome_papel | Código da ação |
| Tipo | tipo_papel | Tipo de ação (ON = ordinária, PN = preferencial, PNA = preferencial tipo A, etc) |
| Empresa | nome_empresa | Nome comercial da empresa |
| Setor | nome_setor | Classificação setorial da empresa |
| Subsetor | nome_subsetor | Classificação por segmento de atuação |
| Cotação | vlr_cot | Cotação de fechamento da ação no último pregão |
| Data últ cot | dt_ult_cot | Data do último pregão onde o ativo foi negociado |
| Min 52 sem | vlr_min_52_sem | Menor cotação da ação nos últimos 12 meses |
| Max 52 sem | vlr_max_52_sem | Maior cotação da ação nos últimos 12 meses |
| Vol $ méd (2m) | vol_med_neg_2m | Volume médio de negociação da ação nos últimos 2 meses |
| Valor de mercado | vlr_mercado | Valor de mercado da empresa calculado através da multiplicação entre o preço da ação e o número total de ações |
| Valor da firma | vlr_firma | Também conhecido como *Enterprise value*, este indicador é calculado somando o valor de mercado da empresa e sua dívida líquida |
| Últ balanço processado | dt_ult_balanco_proc | Data do último balanço divulgado pela empresa que consta no banco de dados do site Fundamentus. Todos os indicadores são calculados considerando os últimos 12 meses finalizados na data do balanço |
| Nro. Ações | num_acoes | Número total de ações somadas todas as espécies (ON, PN, etc) |
| Dia | pct_var_dia | Percentual de variação/oscilação da ação no dia |
| Mês | pct_var_mês | Percentual de variação/oscilação da ação no mês |
| 30 dias | pct_var_30d | Percentual de variação/oscilação da ação nos últimos 30 dias |
| 12 meses | pct_var_12m | Percentual de variação/oscilação da ação nos últimos 12 meses |
| 2023 | pct_var_2023 | Percentual de variação/oscilação da ação em 2023 |
| 2022 | pct_var_2022 | Percentual de variação/oscilação da ação em 2022 |
| 2021 | pct_var_2021 | Percentual de variação/oscilação da ação em 2021 |
| 2020 | pct_var_2020 | Percentual de variação/oscilação da ação em 2020 |
| 2019 | pct_var_2019 | Percentual de variação/oscilação da ação em 2019 |
| 2018 | pct_var_2018 | Percentual de variação/oscilação da ação em 2018 |
| P/L | vlr_ind_p_sobre_l | Preço da ação (P) dividido pelo lucro da ação (L). O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes |
| P/VP | vlr_ind_p_sobre_vp | Preço da ação (P) dividido pelo valor patrimonial (VP). Este indicador informa o quanto o mercado está disposto a pagar sobre o patrimônio líquido da empresa |
| P/EBIT | vlr_ind_p_sobre_ebit | Preço da ação (P) dividido pelo EBIT (*Earnings Before Interest and Taxes*). O EBIT é uma aproximação do resultado operacional da empresa. O EBIT é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas |
| PSR | vlr_ind_psr | Também conhecido como *Price Sales Ratio*, este indicador é definido como o preço da ação dividido pela receita líquida por ação |
| P/Ativos | vlr_ind_p_sobre_ativ | Preço da ação (P) dividido pelos ativos totais por ação |
| P/Cap. Giro | vlr_ind_p_sobre_cap_giro | Preço da ação (P) dividido pelo capital de giro por ação. O capital de giro é o ativo circulante subtraído do passivo circulante |
| P/Ativ Circ Liq | vlr_ind_p_sobre_ativ_circ_liq | Preço da ação (P) dividido pelos ativos circulantes líquidos. A informação de ativo circulante líquido é obtido através da subtração entre os ativos circulantes e as dívidas de curto e longo prazo. Em outras palavras, este indicador remete à visão dos ativos mais líquidos da empresa (caixa, estoque, etc) após o pagamento de todas as dívidas |
| Div. Yield | vlr_ind_div_yield | Dividendo pago por ação dividido pelo preço da ação. Trata-se do rendimento gerado para o dono da ação através do pagamento de dividendos |
| EV / EBITDA | vlr_ind_ev_sobre_ebitda | Valor da firma (*Enterprise Value* ou EV) dividido pelo EBITDA. O EBITDA é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas + Depreciação e Amortização |
| EV / EBIT | vlr_ind_ev_sobre_ebit | Valor da firma (*Enterprise Value* ou EV) dividido pelo EBIT. O EBIT é uma aproximação do resultado da empresa e calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas |
| Cres. Rec (5a) | pct_cresc_rec_liq_ult_5a | Percentual de crescimento da receita líquida nos últimos 5 anos |
| LPA | vlr_ind_lpa | Lucro por ação |
| VPA | vlr_ind_vpa | Valor patrimonial por ação: valor do patrimônio líquido dividido pelo número total de ações |
| Marg. Bruta | vlr_ind_margem_bruta | Lucro bruto dividido pela receita líquida: indica a porcentagem de cada "R$1" de venda que sobrou após o custo dos produtos/serviços vendidos |
| Marg. EBIT | vlr_ind_margem_ebit | EBIT dividido pela receita líquida: indica a porcentagem de cada "R$1" de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas gerais e administrativas |
| Marg. Líquida | vlr_ind_margem_liq | Lucro líquido dividido pela receita líquida |
| EBIT / Ativo | vlr_ind_ebit_sobre_ativo | EBIT dividido pelos ativos totais |
| ROIC | vlr_ind_roic | Retorno sobre o capital investido: calculado através da divisão entre o EBIT (Ativos - Fornecedores - Caixa) sobre o capital total aplicado |
| ROE | vlr_ind_roe | Retorno sobre o patrimônio líquido: lucro líquido dividido pelo patrimônio líquido |
| Liquidez Corr | vlr_liquidez_corr | Ativo circulante dividido pelo passivo circulante: reflete a capacidade de pagamento da empresa no curto prazo |
| Div Br/ Patrim | vlr_ind_divida_bruta_sobre_patrim | Dívida bruta total (Dívida + Debêntures) sobre o patrimônio líquido |
| Giro Ativos | vlr_ind_giro_ativos | Receita líquida dividida pelos ativos totais: indica a eficiência com a qual a empresa usa seus ativos para gerar vendas |
| Ativo | vlr_ativo | Todos os bens, direitos e valores a receber de uma entidade |
| Disponibilidades | vlr_disponibilidades | Contas que representam bens numerários (dinheiro) |
| Ativo Circulante | vlr_ativ_circulante | Bens ou direitos que podem ser convertidos em dinheiro no curto prazo |
| Dív. Bruta | vlr_divida_bruta | A dívida bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo |
| Dív. Líquida | vlr_divida_liq | Subtração entre a dívida bruta e o valor de disponibilidades. Se este valor é negativo, então a empresa possui caixa líquido positivo |
| Patrim. Líq | vlr_patrim_liq | O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, o patrimônio líquido é dado como  diferença entre o valor dos ativos, dos passivos e do resultado de exercícios futuros. Basicamente, é o valor contábil devido pela pessoa jurídica aos sócios e acionistas |
| Receita Líquida_1 | vlr_receita_liq_ult_12m | Valor da receita líquida dos últimos 12 meses. A receita líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos |
| EBIT_1 | vlr_ebit_ult_12m | Também conhecido como *Earnings Before Interest and Taxes*, este valor representa o lucro antes dos impostos e juros. É uma forma aproximada de tentar representar o lucro operacional da empresa. Seu cálculo é dado por Lucro Bruto - Despesa de Vendas - Despesas Administrativas. Valor referente aos últimos 12 meses |
| Lucro Líquido_1 | vlr_lucro_liq_ult_12m | O que sobrou das vendas após a dedução de todas as depesas. Valor referente aos últimos 12 meses |
| Receita Líquida | vlr_receita_liq_ult_3m | Valor da receita líquida dos últimos 3 meses. A receita líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos |
| EBIT | vlr_ebit_ult_3m | Também conhecido como *Earnings Before Interest and Taxes*, este valor representa o lucro antes dos impostos e juros. É uma forma aproximada de tentar representar o lucro operacional da empresa. Seu cálculo é dado por Lucro Bruto - Despesa de Vendas - Despesas Administrativas. Valor referente aos últimos 3 meses |
| Lucro Líquido | vlr_lucro_liq_ult_3m | O que sobrou das vendas após a dedução de todas as depesas. Valor referente aos últimos 3 meses |
