import mysql.connector
from mysql.connector import Error
import os

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
            user=os.environ.get("MYSQL_USER", "root"),
            password=os.environ.get("MYSQL_PASSWORD", "123456"),
            database=os.environ.get("MYSQL_DB", "techinventory"),
            port=int(os.environ.get("MYSQL_PORT", 3307))  # 3307 local, 3306 en Render
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        # Muestra claramente el error en consola
        print(f"Error al conectar a MySQL: {e}")
        return None
        
