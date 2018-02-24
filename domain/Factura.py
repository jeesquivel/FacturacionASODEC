'''
Created on Feb 24, 2018

@author: Jeison
'''

from domain import Cliente
from domain.Cliente import Cliente


class Factura:
    numeroFactura = 0
    cliente= Cliente
    productos = []

    def __init__(self, pNumfactura, cliente):
        self.cliente = cliente
        self.numeroFactura = pNumfactura

    def getNumeroFactura(self):
        return self.numeroFactura

    def getDatosCliente(self):
        return self.cliente.toString()

    def setPorductoFactura(self, producto, cantidad):
        self.productos.append([producto, cantidad])

    # def getDetalleFactura(self):
    #     string = ""
    #     lista = self.productos
    #     for i in lista:
    #         string += i[0].