import mysql.connector
import os

def obtener_conexion():
    conexion = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "123456"),
        database=os.environ.get("MYSQL_DB", "techinventory"),
        port=int(os.environ.get("MYSQL_PORT", 3307))  # <-- 3307 para local
    )
    return conexion

