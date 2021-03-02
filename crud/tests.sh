export "db_host"="api-database-instance.cuta6wjh6fcg.sa-east-1.rds.amazonaws.com"
export "db_name"="api_database"
export "db_username"="postgres"
export "db_password"=""
export "table_name_1"="public.users"
export "table_name_2"="public.files"

python3 -m venv env
source venv/bin/activate
pip install -r requirements-dev.txt -q
python -m unittest tests/*.py

sudo rm -r env
