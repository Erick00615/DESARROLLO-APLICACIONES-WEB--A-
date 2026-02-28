from flask import Flask, render_template, request, redirect
from database import crear_tablas, conectar
from models import Inventario

app = Flask(__name__)

# Crear tabla automáticamente
crear_tablas()

# =========================
# INICIO
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# MOSTRAR PRODUCTOS
# =========================
@app.route("/productos")
def productos():
    inventario = Inventario()
    inventario.cargar_productos()
    lista = inventario.obtener_todos()
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
# ELIMINAR PRODUCTO
# =========================
@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/productos")


# =========================
# EDITAR PRODUCTO
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

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    conn.close()

    return render_template("editar.html", producto=producto)


if __name__ == "__main__":
    app.run(debug=True)
    
    

