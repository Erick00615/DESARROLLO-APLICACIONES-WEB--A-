from conexion.conexion import obtener_conexion
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id_usuario, nombre, email, password):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password


def obtener_usuario_por_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return Usuario(user["id_usuario"], user["nombre"], user["email"], user["password"])
    return None


def obtener_usuario_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return Usuario(user["id_usuario"], user["nombre"], user["email"], user["password"])
    return None


def crear_usuario(nombre, email, password):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
        (nombre, email, password)
    )

    conn.commit()
    conn.close()
    



