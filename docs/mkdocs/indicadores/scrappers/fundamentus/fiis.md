# Fundamentus: Indicadores de FIIs

No portal Fundamentus, Fundos Imobiliários possuem seus próprios indicadores fundamentalistas. A tabela abaixo traz a visão daquilo que também é obtido pela chamada do método [coleta_indicadores_de_ativo()](../../../mkdocstrings/scrappers/fundamentus.md/#pynvest.scrappers.fundamentus.Fundamentus.coleta_indicadores_de_ativo) com *tickers* de FIIs.

| **Nome Original** | **Atributo DataFrame** | **Descrição** |
| :-- | :-- | :-- |
| FII | fii | Código do Fundo Imobiliário |
| Nome | nome_fii | Nome do Fundo Imobiliário |
| Mandato | tipo_mandato | Tipo de mandato do fundo. Pode ser: desenvolvimento para renda, desenvolvimento para venda, híbrido, renda, títulos e valores imobiliários |
| Segmento | segmento | Segmento dos imóveis que compõem o fundo |
| Gestão | tipo_gestao | Tipo de gestão do fundo (ativa ou passiva) |
| Cotação | vlr_cot | Cotação de fechamento do ativo no último pregão |
| Data últ cot | data_ult_cot | Data do último pregão onde o ativo foi negociado |
| Min 52 sem | min_52_sem | Menor cotação da ação nos últimos 12 meses |
| Max 52 sem | max_52_sem | Maior cotação da ação nos últimos 12 meses |
| Vol $ méd (2m) | vol_med_neg_2m | Volume médio diário de negociação do fundo nos últimos 2 meses |
| Valor de mercado | vlr_mercado | Valor de mercado do FII calculado multiplicando a cotação do papel pelo número total de cotas |
| Nro. Cotas | num_cotas | Número total de cotas |
| Relatório | dt_ult_relat_ger | Data do último relatório gerencial do fundo |
| Últ Info Trimestral | dt_ult_informe_trim | Data do último informe trimestral processado |
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
| FFO Yield | vlr_ffo_yield | FFO (*Funds From Operation*) é o lucro líquido ajustado do FII. Seu cálculo é dado por: Lucro Líquido - Ganhos com a (des)valorização dos imóveis - Ganhos (perdas) na venda de ativos. FFO Yield é o FFO sobre o valor de mercado |
| FFO/Cota | vlr_ffo_sobre_cota | FFO sobre a cota |
| Div. Yield | vlr_div_yield | Rendimento distribuído dividido pelo valor do FII. É o rendimento gerado para o dono da ação pelo pagamento de dividendos |
| Dividendo/cota | vlr_dividendo_sobre_cota | Rendimento distribuído por cota nos últimos 12 meses |
| P/VP | vlr_p_sobre_vp | Preço dividido pelo valor patrimonial |
| VP/Cota | vlr_vp_sobre_cota | Valor patrimonial por cota |
| Receita_1 | vlr_rec_bruta_ult_12m | Receita bruta recebida pelo fundo proveniente dos alugueis dos imóveis, distribuição de rendimentos dos seus FIIs e juros das aplicações financeiras. Valor referente aos últimos 12 meses |
| Venda de ativos_1 | vlr_vend_ativ_ult_12m | Receita da venda de imóveis mais resultado da venda de FIIs e aplicações financeiras. Valor referente aos últimos 12 meses |
| FFO_1 | vlr_ffo_ult_12m | FFO dos últimos 12 meses |
| Rend. Distribuído_1 | vlr_rendim_distr_ult_12m | Rendimento distribuído nos últimos 12 meses |
| Receita | vlr_rec_bruta_ult_3m | Receita bruta recebida pelo fundo proveniente dos alugueis dos imóveis, distribuição de rendimentos dos seus FIIs e juros das aplicações financeiras. Valor referente aos últimos 3 meses |
| Venda de ativos | vlr_vend_ativ_ult_3m | Receita da venda de imóveis mais resultado da venda de FIIs e aplicações financeiras. Valor referente aos últimos 3 meses |
| FFO | vlr_ffo_ult_3m | FFO dos últimos 3 meses |
| Rend. Distribuído | vlr_rendim_distr_ult_3m | Rendimento distribuído nos últimos 3 meses |
| Ativos | vlr_ativos | Ativos |
| Patrim Líquido | vlr_patrim_liq | Patrimônio líquido calculado como a subtração entre ativos e passivos |
| Qtd imóveis | qtd_imoveis | Quantidade de imóveis do fundo |
| Qtd Unidades | qtd_unidades | Número total de unidades do fundo |
| Imóveis/PL do FII | vlr_imoveis_sobre_pl | Porcentagem do patrimônio líquido do FII composto por imóveis físicos |
| Área (m2) | total_area_m2 | Área total de todos os imóveis em metros quadrados |
| Aluguel/m2 | vlr_aluguel_por_m2 | Aluguel anual por metro quadrado (em R$) |
| Preço do m2 | vlr_do_m2 | Valor de mercado do FII multiplicado pela porcentagem do patrimônio líquido do FII composto por imóveis físicos dividido pelo total de metros quadrados |
| Cap Rate | vlr_cap_rate | Aluguel dos imóveis dividido pelo valor de mercado do fundo |
| Vacância Média | vlr_vacancia_media | Vacância média dos imóveis ponderada pela área |