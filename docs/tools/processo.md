# Etapas do Processamento

A solução `pynvest-tools` abrange a implantação de uma série de recursos AWS que, juntos, comportam uma série de atividades previamente definidas e designadas para um propósito único: disponibilizar dados confiáveis e recorrentemente atualizados contendo indicadores financeiros de ações e fundos imobiliários.

Para que isso seja possível, um total de **6 macro etapas** foram desenhadas de modo pontual. Nesta seção, o usuário poderá encontrar detalhes sobre cada uma das etapas de processamento dos recursos do módulo.

??? tip "Lembrete: arquitetura da solução"
    Expanda esse bloco sempre que precisar relembrar o desenho de arquitetura de solução.

    <small>
    :octicons-light-bulb-16:
    **Dica:** clique na imagem para uma melhor visualização dos elementos.
    </small>

    ![Arquitetura de Solução](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/docs/drawio/pynvest-tool-diagram-print.png?raw=true)

<small>
  :octicons-light-bulb-16:
  **Dica:** visando facilitar o detalhamento das etapas, cada ação a ser exemplificada está identificada, nas imagens de arquitetura disponibilizadas, com índices que se referem à macro etapa. Por exemplo, a etapa 1 definida como "eliminação de partições do dia" contemplam os passos 1.1, 1.2 e 1.3. Cada um desses passos será detalhado para o usuário.
</small>

## Etapa 1: Eliminação das Partições do Dia

![Desenho de arquitetura contendo apenas a primeira etapa do processamento](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/docs/imgs/arquitetura-etapas/etapa-01.png?raw=true)

O primeiro passo

## Etapa 2: Envio de Códigos de Ativos para Fila SQS

![Desenho de arquitetura contendo apenas a segunda etapa do processamento](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/docs/imgs/arquitetura-etapas/etapa-02.png?raw=true)


## Etapa 3: Processamento de Tabelas SoR


## Etapa 4: Processamento de Tabelas SoT


## Etapa 5: Processamento de Tabela Spec


## Etapa 6: Deduplicação de Registros