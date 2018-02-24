from datetime import datetime

from domain.Cliente import Cliente
from domain.Factura import Factura
from domain.Producto import Producto


def inicializarBDFalsa_inv():
    inventario = []
    inventario += [Producto(1,"Sardina del Mar",575, 10)]
    inventario += [Producto(2, "Choc Milan", 150, 3)]
    inventario += [Producto(3, "Flauta Pollo", 800, 20)]
    inventario += [Producto(4, "Flauta Carne", 800, 13)]
    inventario += [Producto(5, "Agua 350ml", 1100, 30)]
    return

def inicializarBDFalsa_cl():
    clientes = []
    clientes += [Cliente(2, 'Rosa', )]
    return

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