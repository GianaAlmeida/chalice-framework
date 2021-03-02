# Database

Este serviço controla o banco de dados da nossa API

## Testes
Você vai precisar trocar as credenciais no arquivo `./chalice/config.json` e o `run_tests.sh`. Após isso é só executar o seguinte comando:
```bash
$ bash run_tests.sh
```
Os testes são encapsulados, ou seja, tudo que ele cria, ao final ele deleta

### Testando na cloud
```bash
$ curl -X POST \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
-d \
'{
    "nome": "Linux",
    "telefone": "+001 010 101 010",
    "email": "name@linux.com",
    "senha": "ilovelinux"
}' \
BASE_URL/api/users
```

O retorno deve ser parecido com isso:
```json
{
  "code":201,
  "message":"criado!",
  "id":"b2241e96-7be5-4e07-bf81-5e5ec02b83b0"
}
```

## Deploy

Esse serviço depende de uma layer para funcionar, após o deploy deve-se aplicar-lhe ela:
```bash
$ AWS_DEFAULT_REGION="sa-east-1" chalice deploy --stage dev
$ aws lambda update-function-configuration --layers $arn:layer:psycopg2:2 --function-name arn:aws:lambda:sa-east-1:281705241216:function:Databases-dev
```

Estou usando a região de SP para o exemplo se manter dentro da LGPD.
Se for apenas um teste use a region `us-east-1`, ela é a mais barata e a com mais recursos.
