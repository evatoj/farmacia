import mysql.connector
from mysql.connector import Error


def conectar_banco():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="batatadoce123",
            database="farmacia",
            auth_plugin='mysql_native_password'
        )
        return db
    except Error as e:
        print(f"Não foi possível se conectar ao banco de dados: {e}")
        return None
