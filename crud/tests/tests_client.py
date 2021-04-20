from unittest import TestCase

from chalicelib.client import postgres_database

class Test_Users(TestCase):
    def setUp(self):
        self.payload = {
            "nome": "Giana",
            "telefone": "+5511777555333",
            "email": "giana@datarudder.com",
            "senha": "senha"
        }

    def test_read_users(self):
        print("# READ ALL")
        response = postgres_database().read_users(self.payload)
        self.assertEqual(response['code'], 200)

    def test_crud_user(self):
        print("# CREATE")
        response = postgres_database().create_user(self.payload)
        self.payload['id'] = response['id']
        self.assertEqual(response['code'], 201)

        print("# READ")
        response = postgres_database().read_user(self.payload)
        self.assertEqual(response['code'], 200)

        print("# UPDATE")
        response = postgres_database().update_user(self.payload)
        self.assertEqual(response['code'], 200)

        print("# DELETE")
        response = postgres_database().delete_user(self.payload)
        self.assertEqual(response['code'], 200)


class Test_Files(TestCase):
    def setUp(self):
        self.payload = {
            "user_id": "d4e2d3cd-17e6-41c2-9539-2fdaa7c977ee",
            "arquivo": "teste_1.sql",
            "setor": "Comercial",
            "target":"Categoria",
            "objeto": "Preço",
            "nivel": "2",
            "data": "Data"
        }

    def test_read_files(self):
        print("# READ ALL")
        response = postgres_database().read_files(self.payload)
        self.assertEqual(response['code'], 200)

    def test_crud_file(self):
        print("# CREATE")
        response = postgres_database().create_file(self.payload)
        self.payload['id'] = response['file_id']
        self.assertEqual(response['code'], 201)

        print("# READ")
        response = postgres_database().read_file(self.payload)
        self.assertEqual(response['code'], 200)

        print("# UPDATE")
        response = postgres_database().update_file(self.payload)
        self.assertEqual(response['code'], 200)

        print("# DELETE")
        response = postgres_database().delete_file(self.payload)
        self.assertEqual(response['code'], 200)

