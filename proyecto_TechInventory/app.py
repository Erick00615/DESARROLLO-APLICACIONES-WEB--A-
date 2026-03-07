from flask import Flask, render_template, request, redirect
from database import crear_tablas, conectar

from inventario.inventario import (
    guardar_txt,
    guardar_json,
    guardar_csv,
    leer_txt,
    leer_json,
    leer_csv
)

app = Flask(__name__)

crear_tablas()


# =========================
# INICIO
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# VER PRODUCTOS
# =========================
@app.route("/productos")
def productos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")

    lista = cursor.fetchall()

    conn.close()

    return render_template("productos.html", productos=lista)


# =========================
# AGREGAR PRODUCTO
# =========================
@app.route("/agregar", methods=["GET", "POST"])
def agregar():

    if request.method == "POST":

        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }

        guardar_txt(producto)
        guardar_json(producto)
        guardar_csv(producto)

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
            (nombre, cantidad, precio)
        )

        conn.commit()
        conn.close()

        return redirect("/productos")

    return render_template("agregar.html")


# =========================
# ELIMINAR
# =========================
@app.route("/eliminar/<int:id>")
def eliminar(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM productos WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/productos")


# =========================
# EDITAR
# =========================
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    conn = conectar()
    cursor = conn.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        cursor.execute("""
        UPDATE productos
        SET nombre = ?, cantidad = ?, precio = ?
        WHERE id = ?
        """, (nombre, cantidad, precio, id))

        conn.commit()
        conn.close()

        return redirect("/productos")

    cursor.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    )

    producto = cursor.fetchone()

    conn.close()

    return render_template("editar.html", producto=producto)


# =========================
# DATOS DE ARCHIVOS
# =========================
@app.route("/datos")
def datos():

    txt = leer_txt()
    json_data = leer_json()
    csv_data = leer_csv()

    return render_template(
        "datos.html",
        txt=txt,
        json=json_data,
        csv=csv_data
    )


# =========================
# ESTADISTICAS
# =========================
@app.route("/estadisticas")
def estadisticas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM productos")
    total_productos = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(cantidad) FROM productos")
    total_cantidad = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(cantidad * precio) FROM productos")
    valor_inventario = cursor.fetchone()[0]

    conn.close()

    if total_cantidad is None:
        total_cantidad = 0

    if valor_inventario is None:
        valor_inventario = 0

    return render_template(
        "estadisticas.html",
        total_productos=total_productos,
        total_cantidad=total_cantidad,
        valor_inventario=valor_inventario
    )


if __name__ == "__main__":
    app.run(debug=True)



    

