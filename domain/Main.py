

from domain.Cliente import Cliente
from domain.Factura import  Factura
from domain.Producto import Producto


cliente = Cliente(1, "Jeison Esquivel", 1)

producto1=Producto(1,"sardina del mar",555)


factura1 = Factura(1, cliente)
factura1.setPorductoFactura(producto1, 1)

print(factura1.getNumeroFactura())
print(factura1.getDatosCliente())
