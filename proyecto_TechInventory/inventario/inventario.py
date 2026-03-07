import json
import csv


def guardar_txt(producto):

    with open("inventario/data/datos.txt", "a") as archivo:
        archivo.write(
            f"{producto['nombre']},{producto['cantidad']},{producto['precio']}\n"
        )


def leer_txt():

    productos = []

    try:
        with open("inventario/data/datos.txt", "r") as archivo:

            for linea in archivo:

                nombre, cantidad, precio = linea.strip().split(",")

                productos.append({
                    "nombre": nombre,
                    "cantidad": cantidad,
                    "precio": precio
                })

    except:
        pass

    return productos


def guardar_json(producto):

    datos = []

    try:
        with open("inventario/data/datos.json", "r") as archivo:
            datos = json.load(archivo)

    except:
        datos = []

    datos.append(producto)

    with open("inventario/data/datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)


def leer_json():

    try:
        with open("inventario/data/datos.json", "r") as archivo:
            return json.load(archivo)

    except:
        return []


def guardar_csv(producto):

    with open("inventario/data/datos.csv", "a", newline="") as archivo:

        writer = csv.writer(archivo)

        writer.writerow([
            producto["nombre"],
            producto["cantidad"],
            producto["precio"]
        ])


def leer_csv():

    productos = []

    try:
        with open("inventario/data/datos.csv", "r") as archivo:

            reader = csv.reader(archivo)

            for fila in reader:

                productos.append({
                    "nombre": fila[0],
                    "cantidad": fila[1],
                    "precio": fila[2]
                })

    except:
        pass

    return productos

