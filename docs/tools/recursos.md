# Recursos Provisionados pelo Módulo

Sendo um módulo Terraform, o `pynvest-tools` possui toda uma lógica de código baseada em IaC (*Infrastructure as Code*) para provisionar uma série de serviços AWS previamente configurados capazes de realizar todas as tarefas necessárias para proporcionar, ao usuário, uma experiência completa de análise de indicadores financeiros.

Conhecer os detalhes de cada um dos recursos provisionados é um passo importante para que os usuários compreendam, de fato, toda a mágia por trás da solução.

??? tip "Lembrete: arquitetura da solução"
    Expanda esse bloco sempre que precisar relembrar o desenho de arquitetura de solução.

    <small>
    :octicons-light-bulb-16:
    **Dica:** clique na imagem para uma melhor visualização dos elementos.
    </small>

    ![Arquitetura de Solução](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/docs/drawio/pynvest-tool-diagram-print.png?raw=true)

## Serviços AWS

Em linhas gerais, a última versão do módulo `pynvest-tools` considera o provisionamento dos seguintes recursos:

- :octicons-lock-16: :octicons-chevron-right-12: 9 *policies* e 7 *roles* no IAM para configuração das permissões das aplicações
- :octicons-database-16: :octicons-chevron-right-12: 3 databases e 5 tabelas no Glue Data Catalog para consultas analíticas nos indicadores financeiros processados
- :octicons-terminal-16: :octicons-chevron-right-12: 7 funções Lambda contendo todas as lógicas de processamento embarcadas
- :octicons-mail-16: :octicons-chevron-right-12: 2 filas SQS para armazenamento de *tickers* (códigos) de Ações e Fundos Imobiliários a terem seus respectivos indicadores processados
- :octicons-workflow-16: :octicons-chevron-right-12: 1 workflow no Step Functions para otimização do armazenamento dos dados
- :octicons-calendar-16: :octicons-chevron-right-12: 2 regras de agendamento no Eventbridge para execução dos processos

Cada serviço AWS contemplado no módulo `pynvest-tools` possui uma função representativa sobre como a solução, em geral, funciona. As subseções a seguir visam trazer um pouco mais de clareza sobre como cada um dos recursos acima listados atuam para gerar o valor esperado aos usuários.

### :octicons-lock-16: Policies e Roles IAM

As *policies* e *roles* IAM criadas pelo módulo `pynvest-tools` foram pensadas como elementos capazes de fornecer apenas as permissões necessárias para as aplicações e serviços de orquestração da solução.

Cada *policy* possui um contexto específico capaz de ser visualizado através da tabela abaixo:

??? info "Listagem de policies IAM presentes no módulo"
    | :octicons-lock-16: **Policy** | :octicons-pencil-16: **Descrição** | :octicons-link-16: **JSON** |
    | :-- | :-- | :-- |
    | pynvest-store-cloudwatch-logs | Concede permissões de escrita de logs no CloudWatch através de funções Lambda relacionadas ao módulo | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-store-cloudwatch-logs.json) |
    | pynvest-check-and-delete-partitions | Concede permissões de listagem e eliminação de objetos no S3 e de partições de tabelas no Glue Data Catalog | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-check-and-delete-partitions.json) |
    | pynvest-invoke-lambda-functions | Concede permissões de invocação de outras funções Lambda relacionadas ao módulo | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-invoke-lambda-functions.json) |
    | pynvest-invoke-state-machines | Concede permissões de inicialização de workflows do Step Function relacionados ao módulo | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-invoke-state-machines.json) |
    | pynvest-send-msgs-to-tickers-queues | Concede permissões para envio de mensagens para filas no SQS relacionadas ao módulo | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-send-msgs-to-tickers-queues.json) |
    | pynvest-share-sor-financial-data | Concede permissões de coleta de mensagens de filas SQS relacionadas ao módulo, além da escrita de objetos no S3 e atualização de partições em tabelas no Glue Data Catalog na camada SoR (dados brutos) | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-share-sor-financial-data.json) |
    | pynvest-share-sot-financial-data | Concede permissões de leitura de dados na camada SoR (dados brutos), além da escrita de objetos no S3 e atualização de partições em tabelas no Glue Data Catalog na camada SoT (dados preparados) | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-share-sot-financial-data.json) |
    | pynvest-share-spec-financial-data | Concede permissões de leitura de dados na camada SoT (dados preparados), além da escrita de objetos no S3 e atualização de partições em tabelas no Glue Data Catalog na camada Spec (dados especializados) | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-share-spec-financial-data.json) |
    | pynvest-dedup-financial-data | Concede permissões de leitura e escrita de dados nas camadas SoT e Spec, tanto no S3 quanto no Glue Data Catalog | [Link](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/infra/modules/iam/policy-templates/pynvest-dedup-financial-data.json) |

Já as *roles* são basicamente construções assumidas por aplicações/serviços e formadas por uma ou mais *policies* presentes no módulo.

??? info "Listagem de roles IAM presentes no módulo"
    | :octicons-lock-16: **Role** | :octicons-pencil-16: **Descrição** |
    | :-- | :-- |
    | pynvest-lambda-check-and-delete-partitions | Role assumida pela função Lambda responsável por verificar e eliminar dados relacionados à partição da data do processamento agendado |
    | pynvest-lambda-send-msgs-to-tickers-queues | Role assumida pela função Lambda responsável por coletar tickers de ativos e enviar mensagens para filas no SQS |
    | pynvest-lambda-share-sor-financial-data | Role assumida pela função Lambda responsável por extrair e armazenar dados brutos de indicadores financeiros na camada SoR |
    | pynvest-lambda-share-sot-financial-data | Role assumida pela função Lambda responsável por preparar e armazenar dados tratados de indicadores financeiros na camada SoT |
    | pynvest-lambda-share-spec-financial-data | Role assumida pela função Lambda responsável por especializar e armazenar dados consolidados de indicadores financeiros na camada Spec |
    | pynvest-lambda-dedup-financial-data | Role assumida por funções Lambda responsáveis por ler, remover registros duplicados e armazenar dados nas camadas SoT e Spec |
    | pynvest-sfn-invoke-lambda-functions | Role assumida pela máquina de estados no Step Functions para realização do processo de remoção de registros duplicados |

<small>
    :octicons-eye-16:
    **Observação:** todas as *policies* IAM presentes no módulo são criadas com base na prática de [least privileges](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html), ou seja, contemplam apenas as permissões estritamente necessárias para as aplicações. Isto é alcançado através de *templates* do Terraform onde variáveis específicas são definidas nos arquivos JSON das *policies* e substituídas em tempo de execução do módulo.
</small>


### :octicons-database-16: Databases e Tabelas no Data Catalog

O módulo `pynvest-tools` também contempla a criação de *databases* e tabelas previamente configuradas no Glue Data Catalog para que o usuário possa armazenar e analisar os dados financeiros obtidos em tempo de execução da solução.

??? info "Tabelas criadas pelo módulo"
    | :octicons-database-16: **Tabela** | :octicons-database-16: **Database** | :octicons-pencil-16: **Descrição** |
    | :-- | :-- | :-- |
    | tbsor_fundamentus_indicadores_acoes_raw | SoR | Tabela para armazenamento de indicadores financeiros de **Ações** extraídos diretamente do portal Fundamentus e sem qualquer tipo de preparação (dados brutos) |
    | tbsor_fundamentus_indicadores_fiis_raw | SoR | Tabela para armazenamento de indicadores financeiros de **Fundos Imobiliários** extraídos diretamente do portal Fundamentus e sem qualquer tipo de preparação (dados brutos) |
    | tbsot_fundamentus_indicadores_acoes_prep | SoT | Tabela preparada de indicadores financeiros de **Ações** (considerando tipagem e transformações específicas em strings) |
    | tbsot_fundamentus_indicadores_acoes_prep | SoT | Tabela preparada de indicadores financeiros de **Fundos Imobiliários** (considerando tipagem e transformações específicas em strings) |
    | tbspec_fundamentus_cotacao_ativos | Spec | Tabela especializada contendo apenas informações relacionadas à cotações de ativos financeiros, considerando tanto **Ações** quanto **Fundos Imobiliários** |

As tabelas são, provavelmente, os ativos mais valiosos entregues pelo módulo `pynvest-tools`. Através delas, os usuários poderão realizar uma série de consultas e análises de indicadores financeiros de ações e fundos imobiliários.

<small>
    :octicons-eye-16:
    **Observação:** todas as tabelas criadas pelo módulo possuem atributos e indicadores bem definidos. Para consultar quais indicadores financeiros estão sendo contemplados em cada uma das tabelas, não deixe de navegar pela seção de [indicadores]().
</small>

### :octicons-terminal-16: Funções Lambda

Apesar de já proporcionar toda a lógica de criação e documentação das tabelas, sem **dados** não há análise. Dito isso, é preciso conhecer em detalhes as aplicações capazes de extrair, preparar e especializar os dados em todas as camadas da solução.

??? info "Funções Lambda responsáveis pela obtenção dos dados"
    | :octicons-terminal-16: **Função** | :octicons-database-16: **Descrição** |
    | :-- | :-- |
    | pynvest-lambda-check-and-delete-partitions | Função responsável por verificar se existem partições físicas e lógicas relacionadas ao dia de processamento dos dados e, em caso positivo, eliminá-las para evitar dados duplicados |
    | pynvest-lambda-get-tickers | Função responsável por coletar *tickers* (códigos) de ações e fundos imobiliários utilizando funcionalidades da biblioteca `pynvest` e armazenar os resultados como mensagens de filas SQS |
    | pynvest-lambda-get-financial-data-for-acoes | Função responsável por ler mensagens de fila SQS contendo *tickers* de ações, extrair os indicadores financeiros utilizando funcionalidades da biblioteca `pynvest` e, por fim, armazenar os resultados em tabela na camada SoR (S3 e Glue Data Catalog) |
    | pynvest-lambda-get-financial-data-for-fiis | Função responsável por ler mensagens de fila SQS contendo *tickers* de fundos imobiliários, extrair os indicadores financeiros utilizando funcionalidades da biblioteca `pynvest` e, por fim, armazenar os resultados em tabela na camada SoR (S3 e Glue Data Catalog) |
    | pynvest-lambda-prep-financial-data-for-acoes | Função responsável por ler dados brutos de indicadores de ações na camada SoR, preparar os tipos primitivos dos atributos e, por fim, armazenar os resultados em tabela na camada SoT (S3 e Glue Data Catalog) |
    | pynvest-lambda-prep-financial-data-for-fiis | Função responsável por ler dados brutos de indicadores de fundos imobiliários na camada SoR, preparar os tipos primitivos dos atributos e, por fim, armazenar os resultados em tabela na camada SoT (S3 e Glue Data Catalog) |
    | pynvest-lambda-specialize-financial-data | Função responsável por ler dados preparados da camada SoT contendo indicadores de ações e fundos imobiliários, extrair apenas atributos específicos e, por fim, armazenar os resultados em tabela na camada Spec (S3 e Glue Data Catalog) |
    | pynvest-lambda-dedup-financial-data-for-acoes | Função responsável por ler dados da tabela SoT de ações, remover registros duplicados e armazenar os resultados na mesma tabela/camada (overwrite partition) |
    | pynvest-lambda-dedup-financial-data-for-fiis | Função responsável por ler dados da tabela SoT de fundos imobiliários, remover registros duplicados e armazenar os resultados na mesma tabela/camada (overwrite partition) |
    | pynvest-lambda-dedup-financial-data-for-spec-ativos | Função responsável por ler dados da tabela Spec de ativos, remover registros duplicados e armazenar os resultados na mesma tabela/camada (overwrite partition) |

<small>
    :octicons-eye-16:
    **Observação:** as funções Lambda de deduplicação de registros (três últimas referências da tabela acima) são engatilhadas através de um *workflow* no Step Functions a ser detalhado nas próximas seções.
</small>

<small>
    :octicons-light-bulb-16:
    **Dica:** os códigos de todas as funções Lambda podem ser visualizados diretamente no [repositório do módulo no GitHub](https://github.com/ThiagoPanini/pynvest-tools/tree/v0.2.x/app/lambda/functions).
</small>
 
### :octicons-mail-16: Filas no SQS

Como mencionado na seção anterior onde todas as funções Lambda foram exemplificadas, em determinada etapa do processo, mensagens são escritas em filas SQS para um posterior processamento desacoplado. Detalhes sobre essas filas podem ser vistos logo abaixo:

??? info "Filas SQS presentes no processo"
    | :octicons-mail-16: **Nome da Fila** | :octicons-database-16: **Descrição** |
    | :-- | :-- |
    | pynvest-tickers-acoes-queue | Fila SQS responsável por armazenar mensagens contendo *tickers* (códigos) de Ações extraídos pela função `pynvest-lambda-get-tickers` |
    | pynvest-tickers-fiis-queue | Fila SQS responsável por armazenar mensagens contendo *tickers* (códigos) de Fundos Imobiliários extraídos pela função `pynvest-lambda-get-tickers` |

### :octicons-workflow-16: Workflow no Step Functions

Assim como mencionado na seção de detalhamento das funções Lambda, um *workflow* do Step Functions foi criado para orquestrar o processo de remoção de registros duplicados nas tabelas disponibilizadas nas camadas SoT e Spec.

??? info "Workflow do Step Functions provisionado"
    | :octicons-workflow-16: **Workflow** | :octicons-database-16: **Descrição** |
    | :-- | :-- |
    | pynvest-sfn-dedup-sot-spec-tables | Workflow criado com o intuito de coordenar a execução de funções Lambdas específicas para a remoção de registros duplicados em tabelas do módulo `pynvest-tools` presentes nas camadas SoT e Spec. Este workflow é engatilhado através de um agendamento no Eventbridge. |

<small>
    :octicons-eye-16:
    **Observação:** como a lógica implementada para processar e escrever dados nas camadas SoT e Spec contempla o engatilhamento automático e desacoplado de funções Lambda, o workflow de remoção de registros duplicados foi designado a ser executado 15 minutos após o gatilho inicial do processo diário de atualização dos dados.
</small>

### :octicons-calendar-16: Gatilhos no Eventbridge

Por fim, a arquitetura de solução contempla a existência de gatilhos no Eventbridge que coordenam a execução dos processos de atualização dos dados e remoção de registros duplicados.

??? info "Regras e gatilhos no Eventbridge para execução diária do processo"
    | :octicons-calendar-16: **Regra no Eventbridge** | :octicons-database-16: **Descrição** | :octicons-clock-16: **Horário**
    | :-- | :-- |
    | trigger-pynvest-lambda-check-and-delete-partitions | Gatilho responsável por executar a primeira função Lambda do processo (verificação e eliminação de partições do dia já existentes) | Todos os dias às 18:45 |
    | trigger-pynvest-sfn-dedup-sot-spec-tables | Gatilho responsável por executar *workflow* do Step Functions para remoção de registros duplicados em tabelas das camadas SoT e Spec | Todos os dias às 19:00 |

<small>
    :octicons-eye-16:
    **Observação:** pela característica da solução, o primeiro gatilho do Eventbridge necessita apenas executar a função de validação e eliminação de partições. Todos os demais componentes e funções da arquitetura são executados automaticamente de forma altamente desacoplada.
</small>

## Infraestrutura

Como um reforço importante, toda a lógica dos componentes de infraestrutura provisionados (e também dos códigos das aplicações) estão disponíveis no [repositório do módulo no GitHub](https://github.com/ThiagoPanini/pynvest-tools) e podem ser analisados para um entendimento mais aprofundado sobre os recursos.