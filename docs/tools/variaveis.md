# Variáveis do Módulo

O módulo `pynvest-tools` foi inteiramente desenhado para fornecer a experiência mais **simplificada possível** para os usuários. Pensando nisso, grande parte das variáveis do módulo possuem valores *default* que funcionam estritamente bem dentro de uma dinâmica básica e eficiente de uso.

???+ warning "A única variável obrigatória do módulo"
    Em linhas gerais, a única variável obrigatória do módulo, ou seja, a única variável que os usuários necessariamente **precisam fornecer** é a `bucket_names_map`. Seu papel é fornecer informações relacionadas aos *buckets* pré existentes na conta AWS do usuário (vide [pré requisitos de uso](./quickstart.md#pré-requisitos)) para que os dados gerados pelos componentes implantados pelo módulo possam ser devidamente armazenados.

Por mais que a ideia seja facilitar a vida do usuário, as chamadas ao módulo `pynvest-tools` podem ser feitas de modo altamente customizado através das variáveis aceitas pelo módulo. Em casos mais avançados, os usuários podem, por exemplo, indicar para o módulo a utilização de *databases* próprios ao invés de permitir que o módulo crie seus próprios *databases*.

Para uma listagem completa de todas as variáveis, os usuários podem considerar as subseções abaixo:

## Variáveis do S3 e Glue Data Catalog

| **Variável** | **Tipo** | **Descrição** | **Default** |
| :-- | :-- | :-- | :-- |
| bucket_names_map | map(string) | Dicionário (map) contendo nomes dos buckets SoR, SoT e Spec da conta AWS alvo de implantação dos recursos. O objetivo desta variável e permitir que o usuário forneça seus próprios buckets para armazenamento dos arquivos gerados. O correto preenchimento desta variável exige que as referências de nomes sejam fornecidas dentro das chaves 'sor', 'sot' e 'spec'. O usuário também pode fornecer o mesmo nome de bucket para as três quebras, caso queira armazenar os dados das tabelas em um único bucket. | *Required* |
| flag_create_databases | bool | Flag para validar a criação de databases no Glue Data Catalog caso o usuário não tenha ou não queira utilizar databases já existentes para catalogação das tabelas geradas. | `true` |
| databases_names_map | map(string) | Dicionário (map) contendo os nomes dos databases no Glue Data Catalog para catalogação de tabelas SoR, SoT e Spec. O correto preenchimento desta variável exige que as referências de nomes sejam fornecidas dentro das chaves 'sor', 'sot' e 'spec'. O usuário também pode fornecer o mesmo nome de database para as três quebras, caso queira armazenar os dados das tabelas em um único database. | ```{"sor"  = "db_pynvest_sor", "sot"  = "db_pynvest_sot", "spec" = "db_pynvest_spec"}``` |


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

## Variáveis de Funções Lambda

| **Variável** | **Tipo** | **Descrição** | **Default** |
| :-- | :-- | :-- | :-- |
| functions_python_runtime | string | Definição do runtime (versão) da linguagem Python associada às funçõe | `"python3.10"` |
| functions_timeout | number | Timeout das funções Lambda | 900 |
| functions_memory_size | number | Quantidade de memória (MB) a ser alocada para as funções Lambda | 192 |
| sqs_lambda_trigger_batch_size | number | Número máximo de registros a serem enviados para a função em cada batch | 100 |
| sqs_lambda_trigger_batch_window | number | Valor máximo de tempo (em segundos) que a função irá aguardar para a coleta de registros antes da invocação | 10 |
| sqs_lambda_trigger_max_concurrency | number | Número máximo de funções concorrentes a serem invocadas pelo gatilho | 3 |