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
    total = 0
    descuento = 0
    metodoPago = ""
    efectivo = 0
    cambio = 0

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
        string1="==========================================================================\n"
        string =string1+"CODIGO \t\t  NOMBRE PRODUCTO \t\t\tPRECIO UNITARIO    CANTIDAD\n" +string1
        listaProductos=self.productos
        for i in listaProductos:
            producto =i[0]
            string+=    str(producto.getCodigo()) +"             " + \
                        producto.getNombre() +"\t\t\t"+ str(producto.getPrecio()) +"\t\t\t\t\t"+str(i[1])+"\n"
        string+=string1
        string+="DETALLES  DEL PAGO\n"+string1
        string+="METODO PAGO\t\t\t\t"+self.metodoPago +"\n"
        string+="CONTADO\t\t\t\t\t"+str(self.total)+"\n"
        string+="DESCUENTO\t\t\t\t" + str(self.descuento) + "\n"
        string+="EFECTIVO\t\t\t\t"+str(self.efectivo)+"\n"
        string+="VUELTO\t\t\t\t\t"+str(self.cambio)+"\n"
        return string

    def setTotalFactura(self,total):
        self.total=total
