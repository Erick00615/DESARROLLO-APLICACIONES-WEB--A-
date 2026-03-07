class Producto:

    def __init__(self, nombre, cantidad, precio):

        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):

        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }
    