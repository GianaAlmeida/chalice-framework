import os

import psycopg2

class postgres_database():
    host        = os.environ['db_host']
    name        = os.environ['db_name']
    username    = os.environ['db_username']
    password    = os.environ['db_password']
    table_users = os.environ['table_name_1']
    table_files = os.environ['table_name_2']

    def __verify_inputs(self):
        return True

    def __execute_sql(self, sql):
        con = psycopg2.connect(host=self.host, database=self.name, user=self.username, password=self.password)
        con.cursor().execute(sql)
        con.commit()
        con.close()
        return True

    def __execute_sql_and_fetchall(self, sql):
        con = psycopg2.connect(host=self.host, database=self.name, user=self.username, password=self.password)
        cur = con.cursor()
        cur.execute(sql)
        response = cur.fetchall()
        con.close()
        print(response)
        return response

    def __execute_sql_and_fetchone(self, sql):
        con = psycopg2.connect(host=self.host, database=self.name, user=self.username, password=self.password)
        cur = con.cursor()
        cur.execute(sql)
        response = cur.fetchone()
        con.close()
        print(response)
        return response

    def __sql_to_list(self, sql_response):
        lista = []
        for r in sql_response:
            lista.append(r)
        if len(lista) == 1:
            return {"files": lista[0]}
        return {"files": lista}

    def create_user(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"INSERT INTO {self.table_users}(nome, telefone, email, senha) VALUES ('{payload['nome']}', '{payload['telefone']}', '{payload['email']}', '{payload['senha']}');"
        self.__execute_sql(sql)

        sql = f"SELECT id FROM {self.table_users} WHERE email = '{payload['email']}' ORDER BY criado_em DESC;"
        user_id = self.__execute_sql_and_fetchone(sql)
        return {"code": 201, "message": "criado!", "id": user_id[0]}

    def verify_email(self, payload):
        try:
            sql = f"SELECT nome FROM {self.table_users} WHERE email = '{payload['email']}';"
            response = self.__execute_sql_and_fetchone(sql)
            print("## EMAIL VERIFICADO")
            if response != None:
                return True
        except Exception as e:
            print(f"Erro: {str(e)}")
        return False

    def verify_password(self, payload):
        try:
            sql = f"SELECT nome FROM {self.table_users} WHERE senha = '{payload['senha']}' and email = '{payload['email']}';"
            response = self.__execute_sql_and_fetchone(sql)
            print("## SENHA VERIFICADA")
            if response != None:
                return True
        except Exception as e:
            print(f"Erro: {str(e)}")
        return False

    def read_user(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"SELECT * FROM {self.table_users} WHERE id = '{payload['id']}';"
        response = self.__execute_sql_and_fetchall(sql)
        return {"code": 200, "your_personal_data": self.__sql_to_list(response)}

    def read_users(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"SELECT * FROM {self.table_users};"
        response = self.__execute_sql_and_fetchall(sql)
        return {"code": 200, "all_users": self.__sql_to_list(response)}

    def update_user(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"UPDATE {self.table_users} SET nome='{payload['nome']}', telefone='{payload['telefone']}', email='{payload['email']}', senha='{payload['senha']}' WHERE id = '{payload['id']}';"
        self.__execute_sql(sql)
        return {"code":200, "message": "updated"}

    def delete_user(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"DELETE FROM {self.table_users} WHERE id = '{payload['id']}';"
        self.__execute_sql(sql)
        return {"code": 200, "message": "deleted"}

    def create_file(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"INSERT INTO {self.table_files}(user_id, arquivo, var_setor, var_target, var_objeto, var_nivel, var_date) VALUES ('{payload['user_id']}', '{payload['arquivo']}', '{payload['setor']}', '{payload['objeto']}', '{payload['target']}', '{payload['nivel']}', '{payload['data']}');"
        self.__execute_sql(sql)

        sql = f"SELECT id FROM {self.table_files} WHERE user_id = '{payload['user_id']}' ORDER BY criado_em DESC;"
        file_id = self.__execute_sql_and_fetchone(sql)
        return {"code": 201, "message": "criado!", "file_id": file_id[0]}

    def read_file(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"SELECT * FROM {self.table_files} WHERE user_id = '{payload['user_id']}' AND id = '{payload['id']}';"
        response = self.__execute_sql_and_fetchall(sql)
        return {"code": 200, "file": self.__sql_to_list(response)}

    def read_files(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"SELECT * FROM {self.table_files} WHERE user_id = '{payload['user_id']}';"
        response = self.__execute_sql_and_fetchall(sql)
        return {"code": 200, "files": self.__sql_to_list(response)}

    def update_file(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"UPDATE {self.table_files} SET arquivo='{payload['arquivo']}', var_setor='{payload['setor']}', var_target='{payload['target']}', var_objeto='{payload['objeto']}', var_nivel='{payload['nivel']}', var_date='{payload['data']}' WHERE user_id = '{payload['user_id']}' AND id = '{payload['id']}';"
        self.__execute_sql(sql)
        return {"code":200, "message": "updated"}

    def delete_file(self, payload):
        if not self.__verify_inputs():
            return {"Error": "Você esqueceu de no enviar alguns dados"}
        sql = f"DELETE FROM {self.table_files} WHERE user_id = '{payload['user_id']}' AND id = '{payload['id']}';"
        self.__execute_sql(sql)
        return {"code": 200, "message": "deleted"}
