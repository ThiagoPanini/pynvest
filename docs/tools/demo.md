# Demonstração pynvest-tools

Para demonstrar as funcionalidades do pynvest-tools, vídeos foram gravados e transformados em GIFs para contemplar a jornada **completa** de utilização da solução, desde a chamada do módulo Terraform até a execução de *queries* no Athena com as tabelas geradas pelo processo. Navegue por essa decomentação e sane todas as suas dúvidas.

## Implantação dos Recursos

O primeiro passo a ser demonstrado é a chamada ao [módulo Terraform pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools) para implantarmos, em uma conta AWS alvo, todos os recursos e serviços necessários por fazer a magia acontecer. Para isso, realizaremos:

- A utilização do [Visual Studio Code](https://code.visualstudio.com/) como IDE
- A execução dos comandos Terraform para criação dos recursos:
    - `terraform init`
    - `terraform plan`
    - `terraform apply`


??? example "📽️ Inicialização do módulo pynvest-tools via `terraform init`"
    [![Um GIF mostrando a execução do comando terraform init para inicialização do módulo pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-terraform-init-edited.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-terraform-init-edited.gif?raw=true)

Uma vez inicializado o módulo, podemos validar o plano de implantação dos recursos da seguinte maneira:

??? example "📽️ Visualizando o plano de implantação via `terraform plan`"
    [![Um GIF mostrando a execução do comando terraform plan para visualização de plano de implantação de recursos do módulo pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-terraform-plan.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-terraform-plan.gif?raw=true)

Agora que sabemos a quantidade de recursos que serão adicionados em nosso ambiente AWS, podemos realizar a implanatação definitiva.

??? example "📽️ Implantando os recursos via `terraform apply`"
    [![Um GIF mostrando a execução do comando terraform apply para implantação de recursos do módulo pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-terraform-apply-edited.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-terraform-apply-edited.gif?raw=true)


## Visualizando os Recursos Implantados

Após a correta chamada do módulo Terraform, teremos, em nosso ambiente AWS, todos os recursos contemplados dentro da lógica interna do módulo. De forma simplificada, podemos resumir tais recursos em:

- **IAM** onde teremos *policies* e *roles* previamente definidas
- **Eventbridge** onde teremos um gatilho inicial de execução do processo de geração e atualização das tabelas
- **Lambda** onde teremos funções específicas para validar e processar os dados solicitados
- **Glue Data Catalog** onde teremos os *databases* e as tabelas devidamente catalogadas
- **Athena** onde teremos a possibilidade de consultar e analisar os dados gerados

Para cada um destes cenários, vídeos de demonstração trarão a visão pós chamada do módulo com o intuito de dar uma maior clareza sobre tudo aquilo que está contemplado na solução.

??? info "Relembrando a arquitetura do projeto"
    ![[](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/drawio/pynvest-tool-diagram.png?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/docs/drawio/pynvest-tool-diagram.png?raw=true)

### IAM

Como forma de garantir que as aplicações tenham as permissões necessárias para obter, processar e atualizar os dados referentes aos indicadores financeiros, uma série de *policies* e *roles* [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) são automaticamente entregues aos usuários. Uma listagem completa de todos os elementos IAM contemplados pode ser visualizada abaixo:

??? info "Lista de todas as policies IAM presentes no pynvest-tools"

    *Policies*

    | **Nome da policy** | **Descrição** |
    | :-- | :-- |
    | [pynvest-cloudwatch-logs](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-cloudwatch-logs.json) | Permite criação de *log groups* e escrita de *log streams* no CloudWatch |
    | [pynvest-lambda-invoke-functions](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-lambda-invoke-functions.json) | Permite a invocação de outras funções Lambda criadas no projeto |
    | [pynvest-sqs-send-msgs-to-tickers-queues](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-sqs-send-msgs-to-tickers-queues.json) | Permite o envio de mensagens para filas SQS criadas no projeto |
    | [pynvest-sqs-poll-msgs-from-tickers-queues](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-sqs-poll-msgs-from-tickers-queues.json) | Permite o *poll* de mensagens das filas SQS criadas no projeto |
    | [pynvest-s3-manage-sor-data](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-s3-manage-sor-data.json) | Permite listagem, leitura, escrita e deleção de objetos em bucket e prefixos restritos para dados SoR processados no projeto |
    | [pynvest-gluedatacatalog-check-partitions-sor-tables](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-gluedatacatalog-check-partitions-sor-tables.json) | Permite a validação e eventual deleção de partições em tabelas SoR criadas pelo projeto |
    | [pynvest-gluedatacatalog-manage-sor-tables](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.1/iam/policy-templates/pynvest-gluedatacatalog-manage-sor-tables.json) | Permite a criação e atualização de tabelas SoR criadas no projeto, além da atualização de partições processadas |

Agora que sabemos mais a respeito de tudo o que está consolidado no âmbito de identidade de acesso no projeto pynvest-tools, vamos visualizar os elementos já criados em nosso ambiente AWS alvo após a [implantação dos recursos](./demo.md#implantação-dos-recursos).

??? example "📽️ Visualizando policies e roles IAM criadas pelo projeto"
    [![Um GIF mostrando a presença de policies e roles IAM implantadas pelo módulo pynvest-tools](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-iam.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-iam.gif?raw=true)


### Eventbridge

Agora que visualizamos a presença das *policies* e *roles* IAM necessárias para conceder todas as permissões necessárias para os recursos do módulo pynvest-tools, vamos verificar a existência do gatilho de inicialização do processo de obtenção e atualização dos dados de indicadores financeiros (Lambda *trigger*). Faremos isso através da validação da existência de uma regra no [Eventbridge](https://aws.amazon.com/pt/eventbridge/).

??? example "📽️ Visualizando regra de agendamento de execução de processos"
    [![Um GIF mostrando a presença de uma regra no eventbridge](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-eventbridge.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-eventbridge.gif?raw=true)

### Lambda

Com a regra de agendamento devidamente implementada, podemos navegar no serviço [Lambda](https://aws.amazon.com/pt/lambda/) e validar se as funções foram criadas com sucesso. Em essência, tais funções são as aplicações responsáveis por consolidar toda a lógica de coleta, tratamento e atualização dos dados de indicadores financeiros de ativos da B3. Algumas funções possuem integrações com serviços específicos, como o [SQS](https://aws.amazon.com/sqs/), o [S3](https://aws.amazon.com/s3/) e o [Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html).

??? example "📽️ Visualizando funções Lambda para obtenção e processamento dos dados"
    [![Um GIF mostrando a presença de funções Lambda](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-lambda.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-lambda.gif?raw=true)

### SQS

Em uma das etapas de obtenção dos dados de indicadores financeiros, *tickers* de ativos são posicionados em filas SQS para posterior processamento.

??? example "📽️ Visualizando filas SQS para facilitar o processamento dos dados"
    [![Um GIF mostrando a presença de filas SQS](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-sqs.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-sqs.gif?raw=true)


### S3

Na dinâmica de atualização de dados, funções Lambda são engatilhadas por filas SQS para obter e escrever arquivos PARQUET em um bucket no S3 (por exemplo, o bucket SoR informado pelo usuário no parâmetro `bucket_names_map` exigido pelo módulo pynvest-tools). Simulando essa dinâmica de processamento, uma vez obtidos os dados, espera-se que novos prefixos de tabela surjam no S3 apontado com os respectivos arquivos PARQUET processados.

??? example "📽️ Visualizando dados atualizados no S3 após a execução agendada das Lambdas"
    [![Um GIF mostrando a presença de dados processados no S3](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-s3.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-s3.gif?raw=true)

Neste momento, é importante reforçar que o gatilho do Eventbridge é o início de tudo. Por padrão, o módulo pynvest-tools considera uma execução diária com início às 19h. Em outras palavras, novos dados irão chegar no bucket alvo todos os dias após às 19h.

### Glue Data Catalog

E assim, em conjunto com a escrita de arquivos PARQUET em bucket do S3, há também a catalogação dos dados em tabelas do Glue Data Catalog. Ao acessar a página do serviço, será possível visualizar novos *databases* e tabelas criadas pelos processos internos disponibilizados pelo módulo pynvest-tools.

??? example "📽️ Visualizando databases e tabelas disponibilizadas no Glue Data Catalog"
    [![Um GIF mostrando a presença de databases e tabelas disponibilizadas no Glue Data Catalog](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-glue-data-catalog.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-glue-data-catalog.gif?raw=true)


### Athena

Por fim, uma vez atualizados os indicadores financeiros através das tabelas disponibilizadas, os usuários poderão realizar as mais variadas análises em seu ambiente de nuvem AWS. Uma das possibilidades é, por exemplo, a execução de *queries* analíticas no Athena.

??? example "📽️ Executando queries no Athena para realização de análise de dados"
    [![Um GIF mostrando a execução de queries no Athena para realização de análise de dados](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-athena.gif?raw=true)](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.0.x/docs/gifs/pynvest-tools-athena.gif?raw=true)

