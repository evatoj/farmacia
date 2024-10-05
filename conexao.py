import mysql.connector


def conectar_banco():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#umdoistres",
        database="farmacia"
    )
    return db
