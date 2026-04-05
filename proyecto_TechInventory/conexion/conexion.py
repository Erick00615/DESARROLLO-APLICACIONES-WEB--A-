import mysql.connector
import os


def obtener_conexion():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "123456"),
        database=os.getenv("MYSQL_DB", "techinventory"),
        port=int(os.getenv("MYSQL_PORT", 3307))
    )


