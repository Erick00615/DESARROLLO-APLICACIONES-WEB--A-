from conexion.conexion import obtener_conexion

def obtener_productos():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()

    conn.close()
    return datos


def insertar_producto(nombre, cantidad, precio):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)",
        (nombre, cantidad, precio)
    )

    conn.commit()
    conn.close()


def eliminar_producto(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
    conn.commit()
    conn.close()


def obtener_producto(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
    dato = cursor.fetchone()

    conn.close()
    return dato


def actualizar_producto(id, nombre, cantidad, precio):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE productos
        SET nombre=%s, cantidad=%s, precio=%s
        WHERE id=%s
    """, (nombre, cantidad, precio, id))

    conn.commit()
    conn.close()
    
