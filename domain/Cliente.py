
class Cliente:
    numeroCedula =0
    nombreCompleto =""
    telefono = 0

    def __init__(self, numCedula, nbrCliente, telefono):
        self.nombreCompleto = nbrCliente
        self.numeroCedula = numCedula
        self.telefono = telefono

    def getNombre(self):
        return self.nombreCompleto

    def getTelefono(self):
        return self.telefono

    def getCedula(self):
        return self.numeroCedula

    def toString(self):
        return "Cliente: " + str(self.nombreCompleto) + "\n" + "Cedula: " + str(
            self.numeroCedula) + "\n" + "Telefono: " + str(self.telefono)

