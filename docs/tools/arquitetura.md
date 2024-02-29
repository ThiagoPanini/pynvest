# Arquitetura de Solução

Agora que temos uma noção sobre o que é o módulo `pynvest-tools` e os principais benefícios atrelados ao seu uso, vamos iniciar um aprofundamento técnico sobre o que está por trás da solução.

Iniciando pela arquitetura, a imagem abaixo traz uma visão detalhada da solução contendo toda a dinâmica de serviços e integrações disponibilizadas para o usuário.

<small>
  :octicons-light-bulb-16:
  **Dica:** clique na imagem para uma melhor visualização dos elementos.
</small>

![Arquitetura de Solução](https://github.com/ThiagoPanini/pynvest-tools/blob/v0.2.x/docs/drawio/pynvest-tool-diagram-print.png?raw=true)

Em essência, o diagrama acima contempla todos os serviços AWS entregues pelo módulo Terraform e, além disso, traz a visão de todas as integrações entre os recursos.

Toda a dinâmica de implantação do módulo é baseada em **6 macro etapas** que, em linhas gerais, contemplam toda a lógica de extração, preparação e atualização agendada dos dados financeiros disponibilizados ao usuário em seu próprio ambiente AWS.

Ao longo desta seção de detalhamento, será possível observar todas as nuances e particularidades dos [recursos provisionados](./recursos.md) e das [etapas de processamento da solução](./processo.md). 

