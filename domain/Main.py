

from domain.Cliente import Cliente
from domain.Factura import  Factura
from domain.Producto import Producto


cliente = Cliente(1, "Jeison Esquivel", 1)

producto1=Producto(1,"sardina del mar",555)
producto2=Producto(2,"condones durex",1800)
producto3=Producto(3,"Chocolates Milan",700)

factura1 = Factura(1, cliente)
factura1.setPorductoFactura(producto1, 1)
factura1.setPorductoFactura(producto2,2)
factura1.setPorductoFactura(producto2,1)
factura1.setPorductoFactura(producto3,1)

print("\n")


print (factura1.getDetalleFactura())


