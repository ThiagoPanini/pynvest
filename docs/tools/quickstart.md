# Primeiros Passos

Agora que sabemos exatamente o que é o módulo pynvest-tools, vamos detalhar como utilizar e extrair o melhor de suas funcionalidades.

## Pré Requisitos

- ☁️ [Conta AWS](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) disponível para uso
- 🔑 [Acesso programático](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) à conta com chaves de acesso
- ⛏ [Terraform](https://www.terraform.io/) instalado
- 🪣 [Buckets S3](https://aws.amazon.com/s3/) existentes na conta AWS para armazenamento de dados brutos (SoR), preparados (SoT) e especializados (Spec)

## Chamando o Módulo Terraform

Uma vez cumprido os pré requisitos, o usuário poderá obter todos os insumos já detalhados através de uma [chamada de módulo Terraform](https://developer.hashicorp.com/terraform/language/modules/syntax) no seguinte formato:

```python
# Chamada de módulo pynvest-tools em arquivo main.tf
module "pynvest-tools" {
  source = "git::https://github.com/ThiagoPanini/pynvest-tools?ref=main"

  bucket_names_map = {
    "sor"  = "some-bucket-name-to-store-sor-data",
    "sot"  = "some-bucket-name-to-store-sot-data",
    "spec" = "some-bucket-name-to-store-spec-data"
  }
}
```

???+ question "Quais variáveis o usuário necessita passar para o módulo?"
    Como esperado, um módulo Terraform pode ser configurado através de variáveis que guiam regras específicas dentro da lógica embutida no módulo.

    No `pynvest-tools`, muitas das variáveis já tão fornecidas com um valor padrão, não exigindo qualquer tipo de ação por parte do usuário, exceto se o mesmo deseja configurar comportamentos específicos dos recursos provisionados.

    A exceção fica por conta da variável `bucket_names_map` que, essencialmente, tem a função de configurar toda a lógica de armazenamento dos dados obtidos nas aplicações criadas pelo módulo. Esta é a **única variável obrigatória** exigida pelo módulo e seu preenchimento deve ser feito através de um dicionário (map type, no Terraform) contendo as chaves "sor", "sot" e "spec", cujos valores devem representar nomes válidos para buckets S3 responsáveis por armazenar dados nessas três camadas.

Após configurar a chamada ao módulo, basta executar os seguintes comandos Terraform para implantar a infraestrutura relacionada:

- `terraform init` para inicialização do módulo
- `terraform plan` para validar o plano de implantação
- `terraform apply` para aplicar a implantação na conta AWS alvo

Pronto! Você agora terá em sua conta AWS todo um conjunto de serviços para extrair, preparar e armazenar diariamente indicadores de Ações e Fundos Imobiliários da B3! Para saber mais sobre os recursos disponibilizados, não deixe de chegar a página contendo os [detalhes da solução]()