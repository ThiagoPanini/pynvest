# Obtenha Indicadores Financeiros em seu Próprio Ambiente AWS

Você já imaginou ter todo um conjunto de serviços AWS implantados em seu ambiente pessoal para extrair, armazenar e atualizar recorrentemente **indicadores financeiros** de ativos da B3?

Se sim, você precisa conhecer o [pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools) como um módulo Terraform capaz de implantar recursos AWS estrategicamente desenvolvidos com o intuito de permitir com que seus usuários obtenham e analisem dados financeiros.

<div align="center">
    <br><img src="https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/docs/imgs/logo/logo.png?raw=true" width=250 alt="pynvest-logo">
</div>

<div align="center">

  <a href="https://www.terraform.io/">
    <img src="https://img.shields.io/badge/terraform-grey?style=for-the-badge&logo=terraform&logoColor=B252D0">
  </a>

  <a href="https://www.mkdocs.org/">
    <img src="https://img.shields.io/badge/mkdocs-grey?style=for-the-badge&logo=markdown&logoColor=B252D0">
  </a>

  <a href="https://readthedocs.org/">
    <img src="https://img.shields.io/badge/readthedocs-grey?style=for-the-badge&logo=readthedocs&logoColor=B252D0">
  </a>

  <a href="https://github.com/">
    <img src="https://img.shields.io/badge/github-grey?style=for-the-badge&logo=github&logoColor=B252D0">
  </a>

</div>


## Visão Geral

Dado o contexto introdutório fornecido acima, os usuários que decidirem utilizar o `pynvest-tools` em seus respectivos ambientes AWS, poderão obter, entre outros benefícios:

- 🎯 Um processo agendado via [Eventbridge](https://aws.amazon.com/pt/eventbridge/) para obtenção e atualização diária de indicadores financeiros
- 📖 Tabelas previamente definidas no [Glue Data Catalog](https://docs.aws.amazon.com/pt_br/glue/latest/dg/start-data-catalog.html) para consultas em ferramentas analíticas
- 🧲 Arquitetura *serverless* e altamente desacoplada utilizando funções [Lambda](https://aws.amazon.com/pt/lambda/) e filas no [SQS](https://aws.amazon.com/sqs/)
- 📊 Possibilidade de utilizar serviços como [Glue](https://aws.amazon.com/pt/glue/), [Athena](https://aws.amazon.com/pt/athena/) e [QuickSight](https://aws.amazon.com/quicksight/) para as mais variadas análises em dados financeiros

## Saiba Mais

Navegue pelos tópicos desta seção para descobrir, de uma vez por todas, como o módulo Terraform `pynvest-tools` pode te ajudar a unir elementos do mundo financeiro em um ambiente totalmente *cloud native*.

- Visite a página de [primeiros passos](./quickstart.md) para aprender como chamar o módulo em seu projeto Terraform
- Em [variáveis do módulo](./variaveis.md), você poderá visualizar todas as diferentes formas de customizar os recursos provisionados
- Para compreender todos os detalhes técnicos por trás da solução, navegue até as páginas de [arquitetura](./arquitetura.md), [recursos provisionados](./recursos.md) e [etapas do processo](./processo.md)
- Há, ainda, diversos [exemplos de análises](./queries.md) no Athena disponíveis para o usuário destravar todo o potencial do módulo

<small>
  :octicons-history-16:
  **Não perca tempo** e comece agora mesmo a criar **seu próprio Data Lake** com dados financeiros atualizados diariamente.
</small>
