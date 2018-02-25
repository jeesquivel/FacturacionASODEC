from datetime import datetime

from domain.Cliente import Cliente
from domain.Factura import Factura
from domain.Producto import Producto


def inicializarBDFalsa_inv():
    inventario = []

    inventario += [Producto(1,"Sardina del Mar",575, 10)]
    inventario += [Producto(2, "Chocolate Milan", 150, 3)]
    inventario += [Producto(3, "Flauta Pollo", 800, 20)]
    inventario += [Producto(4, "Flauta Carne", 800, 13)]
    inventario += [Producto(5, "Agua   350ml", 1100, 30)]

    return inventario

def inicializarBDFalsa_cl():
    clientes = []

    clientes += [Cliente(1, 'Rosa', True, 0)]
    clientes += [Cliente(2, 'Potter', True, 5000)]
    clientes += [Cliente(3, 'Jeison', False, 0)]

    return clientes

def imprimirInventario(inventario):
    string1="===================================================================\n"
    string=string1+"CODIGO\t\tNOMBRE PRODUCTO \t\tPRECIO \t\tCANT DISPONIBLE\n"+string1
    for i in inventario:
        string+=   "\t" +str(i.getCodigo())+"\t\t"+i.getNombre()+"\t\t\t"+str(i.getPrecio())+"\t\t\t\t"+str(i.getCantidad())+"\n"

    return string+string1

#crea la cabecera de la factura
def crearCabecera():
    cabecera = ""
    fecha = datetime.now().strftime("Fecha: %d/%m/%Y Hora: %H:%M:%S")
    cabecera += "         ASODEC - Ventas\n"
    cabecera += "      Campus ITCR, Cartago\n"
    cabecera += "         Telef.: 2550-2290\n"
    cabecera += "---------------------------------\n"
    cabecera += fecha + "\n"
    cabecera += "---------------------------------\n"
    return cabecera


#calcula el total a pagar de una factura
def calcularTotalFactura(factura):
    total=0
    productosFactura=factura.getProductos()
    for i in productosFactura:
        total+=i.getPrecio
    factura.setTotalFactura(total)

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

def enIventario(inventario, id):
    for producto in inventario:
        if producto.codigo == id:
            return True
    return False

def cantidadDisponible(inventario, id, ctd):
    for producto in inventario:
        if(producto.codigo == id and producto.cantidad >= ctd):
            return True
    return False

def retornarProducto(inventario, id):
    for producto in inventario:
        if producto.codigo == id:
            return producto
    return