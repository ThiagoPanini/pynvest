# Primeiros Passos

O módulo `pynvest-tools` certamente poderá ajudar usuários a terem insumos extremamente interessantes para a aplicação dos mais variados processos de *analytics*. Para iniciar a jornada de utilização, é importante abordar alguns conceitos práticos.

## Pré Requisitos

- ☁️ [Conta AWS](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) disponível para uso
- 🔑 [Acesso programático](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) à conta com chaves de acesso
- ⛏ [Terraform](https://www.terraform.io/) instalado
- 🪣 [Buckets S3](https://aws.amazon.com/s3/) existentes na conta AWS para armazenamento de dados brutos (SoR), preparados (SoT) e especializados (Spec)

## Chamando o Módulo Terraform

Uma vez cumpridos os pré requisitos, o usuário poderá realizar uma [chamada de módulo Terraform](https://developer.hashicorp.com/terraform/language/modules/syntax) no seguinte formato:

```python
# Chamada de módulo pynvest-tools em arquivo main.tf
module "pynvest-tools" {
  source = "git::https://github.com/ThiagoPanini/pynvest-tools?ref=main"

  # Fornecendo nomes de buckets para armazenamento dos dados a serem gerados
  bucket_names_map = {
    "sor"  = "some-bucket-name-to-store-sor-data",
    "sot"  = "some-bucket-name-to-store-sot-data",
    "spec" = "some-bucket-name-to-store-spec-data"
  }
}
```

Após configurar a chamada ao módulo, basta executar os seguintes comandos Terraform para implantar a infraestrutura relacionada:

- `terraform init` para inicialização do módulo
- `terraform plan` para validar o plano de implantação
- `terraform apply` para aplicar a implantação na conta AWS alvo

Pronto! Você agora terá em sua conta AWS todo um conjunto de serviços para extrair, preparar e armazenar diariamente indicadores de Ações e Fundos Imobiliários da B3! Continue navegando nesta documentação para aprender mais detalhes sobre este incrível módulo!