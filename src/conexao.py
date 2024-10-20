import mysql.connector
from mysql.connector import Error


def conectar_banco():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#umdoistres",
            database="farmacia"
        )
        return db
    except Error as e:
        print(
            f"Não foi possível se conectar ao banco de dados, verifique se o serviço MySQL80 foi iniciado e tente novamente.\n {e}")
        return None
