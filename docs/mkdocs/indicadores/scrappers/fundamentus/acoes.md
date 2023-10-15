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
| P/EBIT | vlr_ind_p_sobre_ebit | Preço da ação (P) dividido pelo EBIT. O EBIT é uma aproximação do resultado operacional da empresa. O EBIT é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas |
| PSR | vlr_ind_psr | Também conhecido como *Price Sales Ratio*, este indicador é definido como o preço da ação dividido pela receita líquida por ação |
| P/Ativos | vlr_ind_p_sobre_ativ | Preço da ação (P) dividido pelos ativos totais por ação |
| P/Cap. Giro | vlr_ind_p_sobre_cap_giro | Preço da ação (P) dividido pelo capital de giro por ação. O capital de giro é o ativo circulante subtraído do passivo circulante |
| P/Ativ Circ Liq | vlr_ind_p_sobre_ativ_circ_liq |
| Div. Yield | vlr_ind_div_yield |
| EV / EBITDA | vlr_ind_ev_sobre_ebitda |
| EV / EBIT | vlr_ind_ev_sobre_ebit |
| Cres. Rec (5a) | pct_cresc_rec_liq_ult_5a |
| LPA | vlr_ind_lpa |
| VPA | vlr_ind_vpa |
| Marg. Bruta | vlr_ind_margem_bruta |
| Marg. EBIT | vlr_ind_margem_ebit |
| Marg. Líquida | vlr_ind_margem_liq |
| EBIT / Ativo | vlr_ind_ebit_sobre_ativo |
| ROIC | vlr_ind_roic |
| ROE | vlr_ind_roe |
| Liquidez Corr | vlr_liquidez_corr |
| Div Br/ Patrim | vlr_ind_divida_bruta_sobre_patrim |
| Giro Ativos | vlr_ind_giro_ativos |
| Ativo | vlr_ativo |
| Disponibilidades | vlr_disponibilidades |
| Ativo Circulante | vlr_ativ_circulante |
| Dív. Bruta | vlr_divida_bruta |
| Dív. Líquida | vlr_divida_liq |
| Patrim. Líq | vlr_patrim_liq |
| Receita Líquida_1 | vlr_receita_liq_ult_12m |
| EBIT_1 | vlr_ebit_ult_12m |
| Lucro Líquido_1 | vlr_lucro_liq_ult_12m |
| Receita Líquida | vlr_receita_liq_ult_3m |
| EBIT | vlr_ebit_ult_3m |
| Lucro Líquido | vlr_lucro_liq_ult_3m |
