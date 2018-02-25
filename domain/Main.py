from domain.Cliente import Cliente
from domain.Factura import Factura
from domain.Producto import Producto
from domain.Funciones import *

#Datos
factura = Factura(0)

#BASE DE DATOS FALSA
inventario = inicializarBDFalsa_inv()
#BASE DE DATOS FALSA varibles globales
global inventario
inventario=inicializarBDFalsa_inv()
global clientes
clientes = inicializarBDFalsa_cl()

# variable global
global facturas
facturas=[]


factura.cabecera = crearCabecera()
factura = crearDetalle(factura, inventario)

print(factura.cabecera)
print(factura.getDetalleFactura())


'''import time

print( time.strftime("%a, %d %b %Y %I:%M:%S", time.localtime(10.5)))

print(imprimirInventario(inventario))'''




