import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="techinventory",
        port=3307
    )
    return conexion
