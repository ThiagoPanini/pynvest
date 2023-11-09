# Variáveis do Módulo

Até o presente momento, a única variável obrigatória do módulo a ser explicitamente fornecida pelo usuário é a *bucket_names_map* e seu papel é configurar, de forma genérica, o nome de um bucket S3 da conta do usuário para armazenamento de dados das tabelas geradas durante o processo.

Existem, ainda, uma série de outras variáveis capazes de serem utilizadas pelos usuários para customizar os recursos implantados. Todas as demais variáveis (com execção da *bucket_names_map*) possuem valores padrão que não exigem uma configuração adicional caso os usuários não queiram efetivamente alterar parâmetros específicos de serviços.

Para uma lista completa de todas as variáveis disponíveis, os usuários podem utilizar a tabela abaixo como referência:

## Variáveis do S3 e Glue Data Catalog

| **Variável** | **Tipo** | **Descrição** | **Default** |
| :-- | :-- | :-- | :-- |
| bucket_names_map | map(string) | Dicionário (map) contendo nomes dos buckets SoR, SoT e Spec da conta AWS alvo de implantação dos recursos. O objetivo desta variável e permitir que o usuário forneça seus próprios buckets para armazenamento dos arquivos gerados. O correto preenchimento desta variável exige que as referências de nomes sejam fornecidas dentro das chaves 'sor', 'sot' e 'spec'. O usuário também pode fornecer o mesmo nome de bucket para as três quebras, caso queira armazenar os dados das tabelas em um único bucket. | *Required* |
| flag_create_databases | bool | Flag para validar a criação de databases no Glue Data Catalog caso o usuário não tenha ou não queira utilizar databases já existentes para catalogação das tabelas geradas. | `true` |
| databases_names_map | map(string) | Dicionário (map) contendo os nomes dos databases no Glue Data Catalog para catalogação de tabelas SoR, SoT e Spec. O correto preenchimento desta variável exige que as referências de nomes sejam fornecidas dentro das chaves 'sor', 'sot' e 'spec'. O usuário também pode fornecer o mesmo nome de database para as três quebras, caso queira armazenar os dados das tabelas em um único database. | ```{"sor"  = "db_pynvest_sor", "sot"  = "db_pynvest_sot", "spec" = "db_pynvest_spec"}``` |
| sor_acoes_table_name | string | Nome da tabela SoR gerada a partir do processamento de indicadores financeiros de Ações | `"tbl_fundamentus_indicadores_acoes"` |
| sor_fiis_table_name | string | Nome da tabela SoR gerada a partir do processamento de indicadores financeiros de Fundos Imobiliários | `"tbl_fundamentus_indicadores_fiis"` |

## Variáveis do Eventbridge

| **Variável** | **Tipo** | **Descrição** | **Default** |
| :-- | :-- | :-- | :-- |
| schedule_expression_to_initialize | string | Expressão cron responsável por engatilhar a primeira etapa do processo | `"cron(0 22 ? * MON-FRI *)"` |

## Variáveis de Filas SQS

| **Variável** | **Tipo** | **Descrição** | **Default** |
| :-- | :-- | :-- | :-- |
| sqs_tickers_acoes_queue_name | string | Nome da fila SQS responsável por receber as mensagens contendo informações dos tickers de Ações extraídos | `"pynvest-tickers-acoes-queue"` |
| sqs_tickers_fiis_queue_name | string | Nome da fila SQS responsável por receber as mensagens contendo informações dos tickers de FIIs extraídos | `"pynvest-tickers-fiis-queue"` |
| sqs_visibility_timeout_seconds | number | Tempo (em segundos) em que uma mensagem recebida por um consumidor ficará invisível para outros consumidores | `1080` |
| sqs_message_retention_seconds | number | Tempo (em segundos) em que uma mensagem não deletada continua armazenada. Após esse período, as mensagens da fila são deletadas | `3060` |
| sqs_max_message_size | number | Tamanho máximo (em bytes) das mensagens da fila | `131072` |
| sqs_delay_seconds | number | Delay em que novas mensagens chegam à fila caso os consumidores necessitem de mais tempo para processamento | `0` |
| sqs_receive_wait_time_seconds | number | Tempo máximo (em segundos) que processos de pooling irão aguardar por mensagens disponíveis (Short Pooling versus Long Pooling) | `0` |
| sqs_lambda_trigger_batch_size | number | Número máximo de registros a serem enviados para a função em cada batch | `10` |
| sqs_lambda_trigger_batch_window | number | Valor máximo de tempo (em segundos) que a função irá aguardar para a coleta de registros antes da invocação | `5` |
| sqs_lambda_trigger_max_concurrency | number | Número máximo de funções concorrentes a serem invocadas pelo gatilho | `10` |