'''
Clase: FACTURA

ATRIBUTOS:
    numero de factura   int
    cliente             Cliente
    productos           []

'''

from domain.Cliente import Cliente


class Factura:
    numeroFactura = 0
    cliente= Cliente
    productos = []

    # constructor de la clase
    def __init__(self, pNumfactura, cliente):
        self.cliente = cliente
        self.numeroFactura = pNumfactura

    # obtiene el  numerod efactura de la clase
    def getNumeroFactura(self):
        return self.numeroFactura

    # obtiene los detalles del cliente
    def getDatosCliente(self):
        return self.cliente.toString()

    # asigna producto a la factura
    def setPorductoFactura(self, producto, cantidad):
        self.productos.append([producto, cantidad])

    # obtiene los detalles de la factura (lineas facturas)
    def getDetalleFactura(self):
        string ="CODIGO        NOMBRE PRODUCTO    PRECIO UNITARIO      CANTIDAD\n"
        listaProductos=self.productos
        for i in listaProductos:
            producto =i[0]
            string+=    str(producto.getCodigo()) +"             " + \
                        producto.getNombre() +"     "+ str(producto.getPrecio()) +"                 "+str(i[1])+"\n"
        return string
