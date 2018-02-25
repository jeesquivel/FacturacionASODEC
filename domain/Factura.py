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
    cabecera = ""
    productos = []
    total=0

    # constructor de la clase
    def __init__(self, pNumfactura):
        self.numeroFactura = pNumfactura

    # obtiene el  numerod efactura de la clase
    def getNumeroFactura(self):
        return self.numeroFactura

    # obtiene los detalles del cliente
    def getDatosCliente(self):
        return self.cliente.toString()

    # asigna producto a la factura
    def setProductoFactura(self, producto, cantidad):
        self.productos.append([producto, cantidad])

    def getProductos(self):
        return self.productos

    # obtiene los detalles de la factura (lineas facturas)
    def getDetalleFactura(self):
        string ="CODIGO \t\t  NOMBRE PRODUCTO \t\t\tPRECIO UNITARIO      CANTIDAD\n"
        listaProductos=self.productos
        for i in listaProductos:
            producto =i[0]
            string+=    str(producto.getCodigo()) +"             " + \
                        producto.getNombre() +"\t\t\t"+ str(producto.getPrecio()) +"\t\t\t"+str(i[1])+"\n"
        return string

    def setTotalFactura(self,total):
        self.total=total
