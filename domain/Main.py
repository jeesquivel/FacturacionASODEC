#Instituto Tecnologico de Costa Rica
#Escuela de Ing. en Computacion

#Tarea 2 - Requerimientos de Software
#Autores:   * Jeison Esquivel Samudio (2013018688)
#           * David Valverde Garro (2016034774)

#SISTEMA FACTURA ASODEC

from domain.Funciones import *

#Datos
idFactura = 0
factura = Factura(idFactura)

#BASE DE DATOS FALSA
inventario = inicializarBDFalsa_inv()

#BASE DE DATOS FALSA varibles globales
global inventario
inventario=inicializarBDFalsa_inv()
global clientes
clientes = inicializarBDFalsa_cl()

# variable global
descuento = 0.4
global facturas
facturas=[]


while True:
    factura.cabecera = crearCabecera()
    factura = crearDetalle(factura, inventario)
    calcularTotalFactura(factura)
    iniciarPago(clientes, factura, descuento)
    actualizarInventario(factura, inventario)
    print(factura.cabecera)
    print(factura.getDetalleFactura())

    continuar = input("¿Desea crear otra factura (s/n)?\n")
    if continuar == "n":
        break
    idFactura += 1
    factura = Factura(idFactura)