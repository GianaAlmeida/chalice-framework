Publicando essa layer e atualizando o serviço de banco de dados que utiliza ela:

#### 1. Buildando o docker e criando o folder que o AWS Lambda precisa
```bash
$ bash build.sh
$ zip -r layer.zip layer
```

#### 2. Publicando a layer na AWS
```bash
$ aws lambda publish-layer-version \
--layer-name psycopg2 \
--description "Python + Postgres" \
--zip-file fileb://psycopg2.zip \
--compatible-runtimes "python3.8"
```

#### 3. Incorporando essa layer no AWS Lambda
```bash
$ aws lambda update-function-configuration \
--layers $AWS_ARN:VERSION_NUMBER_HERE \
--function-name $AWS_ARN
```
