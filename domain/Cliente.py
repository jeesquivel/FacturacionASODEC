class Cliente:
    numeroCedula =0
    nombreCompleto =""
    esEstudiante = False
    credito = 0

    #constructor de la clase
    def __init__(self, numCedula, nbrCliente, esEstudiante, credito):
        self.nombreCompleto = nbrCliente
        self.numeroCedula = numCedula
        self.esEstudiante = esEstudiante
        self.credito = credito

    # obtiene el nombre del cliente : string
    def getNombre(self):
        return self.nombreCompleto

    # obtiene el telefono del cliente : int
    def getTelefono(self):
        return self.telefono

    # obtiene la cedula  del cliente : int
    def getCedula(self):
        return self.numeroCedula

    # retorna los detalles de un cliente :string
    def toString(self):
        return "Cliente: " + str(self.nombreCompleto) + "\n" + "Cedula: " + str(
            self.numeroCedula) + "\n" + "Telefono: " + str(self.telefono)

