
from chalice import Chalice, Response, CORSConfig

from chalicelib.client import postgres_database

app = Chalice(app_name='crud')

cors_config = CORSConfig(
    allow_origin='*',
    allow_headers=['*'],
    max_age=600,
    expose_headers=['*']
)


@app.route('/', methods=['POST'], cors=cors_config)
def auth():
    payload = app.current_request.json_body
    body = {'code': 200}
    headers = {"Content-Type": "application/json"}

    if not postgres_database().verify_email(payload):
        body = {"code": 404, "tag": "email"}
        return Response(body=body, status_code=200, headers=headers)

    if not postgres_database().verify_password(payload):
        body = {"code": 404, "tag": "senha"}
        return Response(body=body, status_code=200, headers=headers)

    return Response(body=body, status_code=200, headers=headers)


@app.route('/users', methods=['POST'])
def post_user():
    payload = app.current_request.json_body
    response = postgres_database().create_user(payload)
    return response


@app.route('/users', methods=['GET'])
def get_user():
    payload = app.current_request.json_body
    response = postgres_database().read_user(payload)
    return response


@app.route('/users', methods=['PUT'])
def put_user():
    payload = app.current_request.json_body
    response = postgres_database().update_user(payload)
    return response


@app.route('/users', methods=['DELETE'])
def delete_user():
    payload = app.current_request.json_body
    response = postgres_database().delete_user(payload)
    return response


@app.route('/files', methods=['POST'])
def post_file():
    payload = app.current_request.json_body
    response = postgres_database().create_file(payload)
    return response


@app.route('/files', methods=['GET'])
def get_file():
    payload = app.current_request.json_body
    response = postgres_database().read_file(payload)
    return response


@app.route('/files', methods=['PUT'])
def put_file():
    payload = app.current_request.json_body
    response = postgres_database().update_file(payload)
    return response


@app.route('/files', methods=['DELETE'])
def delete_file():
    payload = app.current_request.json_body
    response = postgres_database().delete_file(payload)
    return response
