class Producto:
    codigo = ""
    nombre = ""
    precio = 0

    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

