class Empleado():
    def __init__(self):
        self.nombre = input('¿Nombre?: ')
        self.apellido = input('¿Apellido?: ')

#Heredamos de Empleado       
class Gerente(Empleado):
    pass

#empleado = Empleado()
gerente = Gerente()