from database import conectar

# ==============================
# CLASE PRODUCTO (POO)
# ==============================
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# ==============================
# CLASE INVENTARIO (USA DICCIONARIO)
# ==============================
class Inventario:
    def __init__(self):
        self.productos = {}  # colección tipo diccionario

    def cargar_productos(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()

        for row in rows:
            producto = Producto(
                row["id"],
                row["nombre"],
                row["cantidad"],
                row["precio"]
            )
            self.productos[producto.id] = producto

        conn.close()

    def obtener_todos(self):
        return list(self.productos.values())

    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.nombre.lower()
        ]
        