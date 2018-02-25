from datetime import datetime

from domain.Cliente import Cliente
from domain.Factura import Factura
from domain.Producto import Producto

# Crea un inventario de productos en una lista
def inicializarBDFalsa_inv():
    inventario = []

    inventario += [Producto(1,"Sardina del Mar",575, 10)]
    inventario += [Producto(2, "Chocolate Milan", 150, 3)]
    inventario += [Producto(3, "Flauta Pollo", 800, 20)]
    inventario += [Producto(4, "Flauta Carne", 800, 13)]
    inventario += [Producto(5, "Agua   350ml", 1100, 30)]

    return inventario

# Crea una lista de clientes con sus respectivos datos
def inicializarBDFalsa_cl():
    clientes = []

    clientes += [Cliente(1, 'Rosa', True, 0)]
    clientes += [Cliente(2, 'Potter', True, -1000)]
    clientes += [Cliente(3, 'Jeison', False, 0)]

    return clientes

# Arma un string con la tabla del inventario de productos
def imprimirInventario(inventario):
    string1="===================================================================\n"
    string=string1+"CODIGO\t\tNOMBRE PRODUCTO \t\tPRECIO \t\tCANT DISPONIBLE\n"+string1
    for i in inventario:
        string +=   "\t" +str(i.getCodigo())+"\t\t"+i.getNombre()+"\t\t\t"+str(i.getPrecio())+"\t\t\t\t"+str(i.getCantidad())+"\n"

    return string+string1

#crea la cabecera de la factura
def crearCabecera():
    cabecera = "=========================================================================\n"
    spacios=5*"\t"
    fecha = datetime.now().strftime("Fecha: %d/%m/%Y Hora: %H:%M:%S")
    cabecera +=spacios+ "         ASODEC - Ventas\n"
    cabecera +=spacios+ "      Campus ITCR, Cartago\n"
    cabecera +=spacios+ "         Telef.: 2550-2290\n"
    cabecera +=spacios+ "---------------------------------\n"
    cabecera +=spacios+ fecha + "\n"
    cabecera += spacios+ "---------------------------------\n"
    return cabecera


#calcula el total a pagar de una factura

def calcularTotalFactura(factura):
    total = 0
    productosFactura = factura.productos
    for i in productosFactura:
        producto = i[0]
        total += producto.getPrecio()*i[1]
    factura.setTotalFactura(total)

# Crea las lineas de la factura con los productos y sus cantidades
def crearDetalle(factura, inventario):
    print(imprimirInventario(inventario))

    while(True):
        idProd = int(input("Ingrese el código del producto:\n"))
        if not enIventario(inventario, idProd):
            print("Ese producto no se encuentra disponible.\n")
            continue

        ctdProd = int(input("Ingrese la cantidad del producto:\n"))
        if not cantidadDisponible(inventario, idProd, ctdProd):
            print("La cantidad solicitada de ese producto no esta disponible\n")
            continue

        factura.setProductoFactura(retornarProducto(inventario, idProd), ctdProd)

        continuar = input("¿Desea seguir ingresando productos (s/n)? \n")
        if continuar == "n":
            break
        else:
            print(imprimirInventario(inventario))

    return factura

# Solicita todos los datos necesarios para establecer el pago de los productos
def iniciarPago(clientes, factura, descuento):
    idCliente = int(input("Ingrese el ID del cliente, si este no posee ID digite -1:\n"))

    if (idCliente != -1 and esEstudiante(clientes, idCliente)):
        factura.descuento = -1 * factura.total * descuento
        factura.total = factura.total * (1 - descuento)

        esCredito = input("¿El estudiante pagara a credito (s/n):\n")
        if esCredito == "s":
            actualizarCreditoEstudiante(clientes, idCliente, factura.total)
            factura.metodoPago = "Credito"
            return

    metodoPago = input("Ingrese el metodo de pago: (Efectivo | Tarjeta [E|T]):\n")
    if metodoPago == "E":
        factura.efectivo = int(input("Ingrese el monto de efectivo dado por el cliente:\n"))
        factura.cambio = factura.efectivo - factura.total
        factura.metodoPago = "Efectivo"
        return
    else:
        print("Inserte la tarjeta...")
        print("*SE UTILIZA UN ALGUN SISTEMA DE PAGO CON TARJETA CON EL HW CORRESPONDIENTE*")
        factura.metodoPago = "Tarjeta"
        return

# Actualiza la informacion de credito para el estudiante con el ID dado
def actualizarCreditoEstudiante(clientes, id, monto):
    for cliente in clientes:
        if cliente.numeroCedula == id:
            cliente.credito -= monto

# Determina si un cliente con el ID dado es un estudiante
def esEstudiante(clientes, id):
    for cliente in clientes:
        if (cliente.numeroCedula == id and cliente.esEstudiante):
            return True
    return False

# Determina si un producto con un ID dado esta en el inventario
def enIventario(inventario, id):
    for producto in inventario:
        if producto.codigo == id:
            return True
    return False

# Determina si la cantidad solicitada de un producto se encuentra disponible
def cantidadDisponible(inventario, id, ctd):
    for producto in inventario:
        if(producto.codigo == id and producto.cantidad >= ctd):
            return True
    return False

# Retorna el producto con el ID dado
def retornarProducto(inventario, id):
    for producto in inventario:
        if producto.codigo == id:
            return producto
    return

# Disminuye la cantidad de productos disponibles en el inventario con base en una factura
def actualizarInventario(factura,inventario):
    listaProductosFactura=factura.getProductos()
    for i in listaProductosFactura:
        producto=i[0]
        descontarCantidad(producto.getCodigo,inventario,i[1])

# Disminuye la cantidad de un producto dado por su codigo
def descontarCantidad(codigo,inventario,cantidad):
    for i in inventario:
        if i.getCodigo==codigo:
            i.setCantidad(cantidad)
