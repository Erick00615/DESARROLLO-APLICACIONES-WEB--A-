import os
import json
import csv

# =========================
# CREAR CARPETA SI NO EXISTE
# =========================
os.makedirs("inventario/data", exist_ok=True)


# =========================
# GUARDAR EN TXT
# =========================
def guardar_txt(producto):

    with open("inventario/data/datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{producto['nombre']},{producto['cantidad']},{producto['precio']}\n"
        )


# =========================
# LEER TXT
# =========================
def leer_txt():

    productos = []

    try:
        with open("inventario/data/datos.txt", "r", encoding="utf-8") as archivo:

            for linea in archivo:

                nombre, cantidad, precio = linea.strip().split(",")

                productos.append({
                    "nombre": nombre,
                    "cantidad": cantidad,
                    "precio": precio
                })

    except Exception:
        pass

    return productos


# =========================
# GUARDAR JSON
# =========================
def guardar_json(producto):

    datos = []

    try:
        with open("inventario/data/datos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except Exception:
        datos = []

    datos.append(producto)

    with open("inventario/data/datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)


# =========================
# LEER JSON
# =========================
def leer_json():

    try:
        with open("inventario/data/datos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except Exception:
        return []


# =========================
# GUARDAR CSV
# =========================
def guardar_csv(producto):

    archivo_existe = os.path.isfile("inventario/data/datos.csv")

    with open("inventario/data/datos.csv", "a", newline="", encoding="utf-8") as archivo:

        writer = csv.writer(archivo)

        if not archivo_existe:
            writer.writerow(["nombre", "cantidad", "precio"])

        writer.writerow([
            producto["nombre"],
            producto["cantidad"],
            producto["precio"]
        ])


# =========================
# LEER CSV
# =========================
def leer_csv():

    productos = []

    try:
        with open("inventario/data/datos.csv", "r", encoding="utf-8") as archivo:

            reader = csv.reader(archivo)

            next(reader, None)  # saltar encabezado

            for fila in reader:

                productos.append({
                    "nombre": fila[0],
                    "cantidad": fila[1],
                    "precio": fila[2]
                })

    except Exception:
        pass

    return productos


