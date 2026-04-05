from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from conexion.conexion import obtener_conexion
import os

# USUARIOS
from models.usuario import (
    obtener_usuario_por_email,
    obtener_usuario_por_id,
    crear_usuario
)

# INVENTARIO ARCHIVOS
from inventario.inventario import (
    guardar_txt,
    guardar_json,
    guardar_csv,
    leer_txt,
    leer_json,
    leer_csv
)

# PDF
from services.pdf_service import generar_pdf_productos


app = Flask(__name__)
app.secret_key = "supersecretkey"


# =========================
# CREAR TABLAS SQLITE
# =========================
def crear_tablas():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        cantidad INTEGER,
        precio REAL
    )
    """)

    conn.commit()
    conn.close()


crear_tablas()


# =========================
# LOGIN MANAGER
# =========================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return obtener_usuario_por_id(user_id)


# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        usuario = obtener_usuario_por_email(email)

        if usuario and usuario.password == password:
            login_user(usuario)
            return redirect("/productos")
        else:
            return "Credenciales incorrectas"

    return render_template("auth/login.html")


# =========================
# REGISTER
# =========================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]

        crear_usuario(nombre, email, password)

        return redirect("/login")

    return render_template("auth/register.html")


# =========================
# LOGOUT
# =========================
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


# =========================
# INICIO
# =========================
@app.route("/")
def index():
    return redirect("/login")


# =========================
# VER PRODUCTOS
# =========================
@app.route("/productos")
@login_required
def productos():

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    lista = cursor.fetchall()

    conn.close()

    return render_template("productos.html", productos=lista)


# =========================
# AGREGAR
# =========================
@app.route("/agregar", methods=["GET", "POST"])
@login_required
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

        conn = obtener_conexion()
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
@login_required
def eliminar(id):

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect("/productos")


# =========================
# EDITAR
# =========================
@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):

    conn = obtener_conexion()
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


# =========================
# DATOS ARCHIVOS
# =========================
@app.route("/datos")
@login_required
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
@login_required
def estadisticas():

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM productos")
    total_productos = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(cantidad) FROM productos")
    total_cantidad = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(cantidad * precio) FROM productos")
    valor_inventario = cursor.fetchone()[0]

    conn.close()

    total_cantidad = total_cantidad or 0
    valor_inventario = valor_inventario or 0

    return render_template(
        "estadisticas.html",
        total_productos=total_productos,
        total_cantidad=total_cantidad,
        valor_inventario=valor_inventario
    )


# =========================
# PDF
# =========================
@app.route("/reporte")
@login_required
def reporte():

    ruta = os.path.join(os.getcwd(), "reporte_productos.pdf")

    generar_pdf_productos(ruta)

    return send_file(ruta, as_attachment=True)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(debug=True)


    



    

