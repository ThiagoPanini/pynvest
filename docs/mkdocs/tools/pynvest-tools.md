# Pynvest Tools

Você já imaginou ter todo um conjunto de serviços AWS implantados em seu ambiente para obter, atualizar e analisar recorrentemente **indicadores financeiros** de ativos da B3?

Conheça o [pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools), o seu módulo [Terraform](https://www.terraform.io/) para obter tudo isso com pouquíssimas linhas de código.

## O que é o pynvest-tools?

Como já mencionado, o *pynvest-tools* é um módulo Terraform capaz de fornecer uma experiência única de implantação de toda uma arquitetura AWS provisionada para garantir a obtenção e uma recorrente atualização de indicadores financeiros utilizando a biblioteca [pynvest](../index.md).

???+ tip "Quais os benefícios ao utilizar o módulo pynvest-tools?"
    Como principal *outcome*, os usuários que chamarem o módulo pynvest-tools em seus projetos Terraform terão, entre outros insumos:

    - ✅ Processo agendado para obtenção de dados de indicadores financeiros de ativos
    - ✅ Arquitetura *serverless*, resiliente e de baixo custo
    - ✅ Tabelas atualizadas diariamente no Glue Data Catalog
    - ✅ Possibilidade de realizar as mais variadas análises financeiras via queries do Athena
    - ✅ Possibilidade de criar *dashboards* no Quicksight utilizando dados financeiros

## Arquitetura

Toda a solução foi desenhada dentro dos propósitos de uma arquitetura [serverless](https://aws.amazon.com/serverless/) utilizando serviços nativos da AWS que interagem entre si de forma [altamente desacoplada](https://aws.amazon.com/blogs/compute/decoupling-larger-applications-with-amazon-eventbridge/) e através de eventos.

![[](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/docs/drawio/pynvest-tool-diagram.png?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/docs/drawio/pynvest-tool-diagram.png?raw=true)

??? example "Passo a passo do processo de obtenção e atualização de indicadores"

    Considerando as etapas destacadas pelos números no desenho de arquitetura, temos:

    **1 -** O [Eventbridge](https://aws.amazon.com/pt/eventbridge/) engatilha a primeira função [Lambda](https://aws.amazon.com/pt/lambda/) através de uma expressão cron. Por padrão, a execução ocorre de segunda à sexta-feira às 19h (UTC-3).

    **2 -** A primeira função Lambda valida no [Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) e no [S3](https://aws.amazon.com/s3/) a existência de partições relacionadas à data de execução do processo. Caso as partições existam nas tabelas geradas, a função se encarrega de eliminá-las para evitar duplicidades eventualmente causadas por múltiplas execuções em um único dia.

    **3 -** Após executada com sucesso, a primeira função Lambda engatilha, de forma [assíncrona](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html), uma segunda função Lambda para continuidade no processo.

    **4 -** Essa função Lambda tem a responsabilidade de coletar os *tickers* (códigos) de ativos financeiros (Ações e Fundos Imobiliários) através do método [Fundamentus.coleta_indicadores_de_ativo()](../../mkdocstrings/scrappers/fundamentus.md/#pynvest.scrappers.fundamentus.Fundamentus.coleta_indicadores_de_ativo).

    **5 -** Os *tickers* coletados são então enviados para diferentes filas SQS de acordo com seu tipo (Ações ou Fundos Imobiliários).

    **6 -** As filas SQS servem como gatilho para execução de outras duas funções Lambda responsáveis, respectivamente, por coletar indicadores financeiros de Ações e Fundos Imobiliários. O processo de coleta de indicadores financeiros é feito através do método [Fundamentus.extracao_tickers_de_ativos()](../../mkdocstrings/scrappers/fundamentus.md/#pynvest.scrappers.fundamentus.Fundamentus.extracao_tickers_de_ativos).

    **7 -** Após coletar os indicadores em [DataFrames do pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), os dados [SoR](https://en.wikipedia.org/wiki/System_of_record) são então disponibilizados no S3 e catalogados no Glue Data Catalog via [AWS SDK for pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/index.html) em duas tabelas:

    - `tbl_fundamentus_indicadores_acoes` contendo indicadores financeiros específicos de Ações listadas na B3
    - `tbl_fundamentus_indicadores_fiis` contendo indicadores financeiros específicos de FIIs listados na B3

    **8 -** Os usuários podem, enfim, consultar os dados disponibilizados através do [Athena](https://aws.amazon.com/pt/athena/) para os mais variados propósitos analíticos

## Quickstart

Agora que sabemos exatamente o que é o módulo pynvest-tools, vamos detalhar como utilizar e extrair o melhor de suas funcionalidades.

### Pré Requisitos

- ☁️ [Conta AWS](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) disponível para uso
- 🔑 [Acesso programático](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) à conta com chaves de acesso
- ⛏ [Terraform](https://www.terraform.io/) instalado

### Chamando o Módulo Terraform

Uma vez cumprido os pré requisitos, o usuário poderá obter todos os insumos já detalhados através de uma [chamada de módulo Terraform](https://developer.hashicorp.com/terraform/language/modules/syntax) no seguinte formato:

```python
# Chamada de módulo pynvest-tools em arquivo main.tf
module "pynvest-tools" {
  source = "git::https://github.com/ThiagoPanini/pynvest-tools?ref=main"

  bucket_names_map = {
    "sor" = "some-bucket-name-to-store-sor-data"
  }
}
```

Após isso, basta executar os seguintes comandos Terraform para implantar a infraestrutura relacionada:

- `terraform init` para inicialização do módulo
- `terraform plan` para validar o plano de implantação
- `terraform apply` para aplicar a implantação na conta AWS alvo

## Variáveis do Módulo

O módulo Terraform conta com algumas variáveis capazes de customizar a experiência de seus usuários. Para verificar quais variáveis estão atualmente disponíveis, basta acessar a [página de variáveis do módulo](./variaveis.md).

## Tabelas Disponíveis

A principal entrega de valor do *pynvest-tools* se materializa através da disponibilização de tabelas no Glue Data Catalog capazes de serem consumidas e analisadas pelos usuários para os mais variados propósitos. Até o momento, as seguintes tabelas se encontram disponíveis:

| **Camada** | **Database** | **Tabela** | **Descrição** |
| :-- | :-- | :-- | :-- |
| SoR | `db_pynvest_sor` | `tbl_fundamentus_indicadores_acoes` | Tabela contendo indicadores financeiros específicos de Ações listadas na B3 |
| SoR | `db_pynvest_sor` | `tbl_fundamentus_indicadores_fiis` | Tabela contendo indicadores financeiros específicos de FIIs listadas na B3 |

As tabelas são particionadas através da data de execução do processo (atributo `date_exec`) e seus dados são armazenados em buckets fornecidos pelo usuário através da variável *bucket_names_map* do módulo.

Para analisar a raíz dos indicadores financeiros consolidados nas tabelas, basta acessar a [página de indicadores](../indicadores/sobre-indicadores.md).

## Demonstração

Por fim, visando proporcionar uma experiência completa de prova de valor desta solução, a [página de demo](./demo.md) conta com demonstrações simplificadas de alguns elementos entregues pelo módulo e como análises específicas podem ser realizadas dentro desse propósito.