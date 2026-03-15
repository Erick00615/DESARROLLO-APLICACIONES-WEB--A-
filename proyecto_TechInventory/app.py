from flask import Flask, render_template, request, redirect, flash, url_for
from conexion.conexion import obtener_conexion

from inventario.inventario import (
    guardar_txt,
    guardar_json,
    guardar_csv,
    leer_txt,
    leer_json,
    leer_csv
)

app = Flask(__name__)
app.secret_key = "clave_secreta"  # necesario para flash messages

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
    conn = obtener_conexion()
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
        try:
            # Capturamos datos del formulario
            nombre = request.form["nombre"].strip()
            cantidad = request.form["cantidad"].strip()
            precio = request.form["precio"].strip()

            # Validamos campos vacíos
            if not nombre or not cantidad or not precio:
                flash("Todos los campos son obligatorios", "warning")
                return redirect(url_for("agregar"))

            # Convertimos tipos
            try:
                cantidad = int(cantidad)
                precio = float(precio)
            except ValueError:
                flash("Cantidad debe ser un número entero y precio un número decimal", "warning")
                return redirect(url_for("agregar"))

            # Guardar en archivos
            producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
            guardar_txt(producto)
            guardar_json(producto)
            guardar_csv(producto)

            # Guardar en base de datos
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)",
                (nombre, cantidad, precio)
            )
            conn.commit()
            cursor.close()
            conn.close()

            flash("Producto agregado correctamente", "success")
            return redirect(url_for("productos"))

        except Exception as e:
            print("Error al agregar producto:", e)
            flash(f"Error al agregar producto: {e}", "danger")
            return redirect(url_for("agregar"))

    return render_template("agregar.html")

# =========================
# ELIMINAR
# =========================
@app.route("/eliminar/<int:id>")
def eliminar(id):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Producto eliminado correctamente", "success")
    except Exception as e:
        print("Error al eliminar producto:", e)
        flash(f"Error al eliminar producto: {e}", "danger")
    return redirect(url_for("productos"))

# =========================
# EDITAR
# =========================
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    if request.method == "POST":
        try:
            nombre = request.form["nombre"].strip()
            cantidad = int(request.form["cantidad"].strip())
            precio = float(request.form["precio"].strip())

            cursor.execute("""
                UPDATE productos
                SET nombre = %s, cantidad = %s, precio = %s
                WHERE id = %s
            """, (nombre, cantidad, precio, id))
            conn.commit()
            flash("Producto actualizado correctamente", "success")
            return redirect(url_for("productos"))

        except Exception as e:
            print("Error al editar producto:", e)
            flash(f"Error al editar producto: {e}", "danger")
            return redirect(url_for("editar", id=id))
        finally:
            cursor.close()
            conn.close()

    cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
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
    return render_template("datos.html", txt=txt, json=json_data, csv=csv_data)

# =========================
# ESTADISTICAS
# =========================
@app.route("/estadisticas")
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

if __name__ == "__main__":
    app.run(debug=True)
    



    

