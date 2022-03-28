# App Business Tech
Disertação sobre utilização da resolução de problemas da appbusiness (Empresa fictícia). Era necessário uma solução que suportasse grande quantidade e volume de dados. Considerando que também fosse necessário a disponibilidade deste sistema. Mesmo que aumentasse a demanda. Foi procurado resolver os problemas da forma mais simples possível sem perder a qualidade.

## Arquitetura
![Arquitetura](https://i.ibb.co/VMCd07M/techinical-test-drawio-2.png)

### 1 Servidores
Pra este tipo de arquitetura foi pensado a não utilização de servidores como uma maquina EC2/VPS etc. O fato de não sabermos a quantidade exata de requisições (e sabermos que pode haver um grande volume de dados) optou-se por criar pequenos serviço em lambda para garantir que o sistema sempre se mantenha online e não tenha o risco de cair caso haja uma grande massa de requisições instântaneas. Olhando pelo valor da EC2 e da Lambda Function, o Servless acaba sendo uma solução mais viável em relação a custo benefício para este tipo de serviço.

### 2 Microserviços
Foi definido dentro do sistema que seria utilizado a arquitetura de microserviços, com recomendação da AWS utilizando o lambda para pequenos serviços junto com a API Gateway.

#### 2.1. JWT
Para um ganho na segurança dos dados foi implementado uma autenticação via JWT no meio do caminho para aumentar a segurança na transmissão dos dados.

## 3 Databases
Dissertação relacionada aos tipo de usos de banco de dados para a solução.

## 3.1 Amazon Aurora - database_a
Para o banco de dados `database_b` foi selecionado a opção de utilizar Amazon Aurora por ter uma boa performançe e ser até 5 vezes mais rápido do que o MySql e três vezes mais rápido do que Postgress. Além de suportar grandes volumes de dados de até 128TB por instâcia e contar com até 15 réplicas de baixa latência. O response teremos:

Payload Envio:

```sh
curl --location --request GET 'ms-auth-jwt' \
--header 'Authorization: Bearer eyJhbEciOiJIJUzI1XiIsnR5cCI6IkpXVCJ'
```

Response: 

```json
{
    "documentNumber": "28227263638",
    "address": "Rua das cores, 130",
    "city": "São Paulo",
    "state": "SP",
    "debts": [
        {
            "date": "2022-01-10 15:29:00",
            "type": "loan",
            "amount": 10000,
            "installments": "24"
        },
        {
            "date": "2021-11-10 14:15:00",
            "type": "loan",
            "amount": 10000,
            "installments": "12"
        }
    ]
}
```

## 3.2 Amazon Aurora - database_b
Para o banco de dados `database_b` foi selecionado a opção de utilizar Amazon Aurora por ter uma boa performançe e ser até 5 vezes mais rápido do que o MySql e três vezes mais rápido do que Postgress. Além de suportar grandes volumes de dados de até 128TB por instâcia e contar com até 15 réplicas de baixa latência. O response teremos:

Payload Envio:

```sh
curl --location --request GET 'ms-auth-jwt' \
--header 'Authorization: Bearer eyJhbEciOiJIJUzI1XiIsnR5cCI6IkpXVCJ'
```

```json
{
    documentNumber: "88837363533",
    "age": 25,
    "listOfGoods": {
        "properties": [
            {
                "type": "house",
                "cost": 130000
            },
            {
                "type": "farm",
                "cost": 2500000
            }
        ],
        "vehicles": [
            {
                "type": "car",
                "cost": 130000
            }
        ]
    },
    "sourceOfIncome": "CLT"
}
```
## 3.3 DynamoDB - database_c

Para o banco de dados `database_c` foi selecionado a opção de utilizar DynamoDB para que a consulta pudesse ser extremamente rápido, algo que fique abaixo de 10ms.

Payload Envio:

```sh
curl --location --request GET 'ms-auth-jwt' \
--header 'Authorization: Bearer eyJhbEciOiJIJUzI1XiIsnR5cCI6IkpXVCJ'
```

Response:
```json
{
    "message": "Dados encontrados com sucesso!",
    "dataResponse": [
        {
            "Timestamp": "1648487994",
            "ClientDocumentNumber": "12882827272",
            "LastCheckInDocumentNumber": "2022-03-20 10:00:02",
            "FinancialHistory": [
                {
                    "date": "2022-01-10 15:29:00",
                    "type": "loan",
                    "amount": 10000
                },
                {
                    "date": "2021-11-10 14:15:00",
                    "type": "loan",
                    "amount": 10000
                }
            ],
            "lastBuyWithCreditCard": {
                    "date": "2022-01-28 15:29:00",
                    "amount": 103
                }
        }
    ]
}
```

## Tech

Para desenvolvimento em ambiente local foi utilizado o Serverless que simula o Lambda function da AWS.

- [serverless] - Do more with less.

## AWS Cli
Para utilizar os sistemas é preciso configurar a CLI da AWS em maquina local.

## Execução Serverless
Para execução do mesmo, pode ser encontrada de forma fácil em sua [documentação](https://www.serverless.com/framework/docs/getting-started) após tudo instalado, para execução local basta executar o código `serverless invoke local -f hello`.

[serverless]: <https://www.serverless.com/>
