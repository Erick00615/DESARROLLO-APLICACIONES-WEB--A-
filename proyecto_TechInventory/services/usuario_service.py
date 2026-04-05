from conexion.conexion import obtener_conexion

def obtener_usuario_por_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE mail = %s", (email,))
    usuario = cursor.fetchone()

    conn.close()
    return usuario


def crear_usuario(nombre, email, password):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, mail, password) VALUES (%s, %s, %s)",
        (nombre, email, password)
    )

    conn.commit()
    conn.close()
    
