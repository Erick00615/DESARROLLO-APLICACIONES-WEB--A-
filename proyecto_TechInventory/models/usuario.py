from flask_login import UserMixin
from conexion.conexion import obtener_conexion


class Usuario(UserMixin):

    def __init__(self, id_usuario, nombre, email, password):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password


def obtener_usuario_por_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE mail = %s", (email,))
    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        return Usuario(
            usuario["id_usuario"],
            usuario["nombre"],
            usuario["mail"],
            usuario["password"]
        )
    return None


def obtener_usuario_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id,))
    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        return Usuario(
            usuario["id_usuario"],
            usuario["nombre"],
            usuario["mail"],
            usuario["password"]
        )
    return None


def crear_usuario(nombre, email, password):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, mail, password) VALUES (%s, %s, %s)",
        (nombre, email, password)
    )

    conn.commit()
    conn.close()
    


