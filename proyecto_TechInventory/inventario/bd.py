import sqlite3


def conectar_bd():

    conexion = sqlite3.connect("inventory.db")

    return conexion
