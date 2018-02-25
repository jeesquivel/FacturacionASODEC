

class Producto:
    codigo = ""
    nombre = ""
    precio = 0
    cantidad = 0

    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

