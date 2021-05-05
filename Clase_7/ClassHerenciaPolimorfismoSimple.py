class Empleado():
    def __init__(self):
        self.nombre = input('¿Nombre?: ')
        self.apellido = input('¿Apellido?: ')

#Heredamos de Empleado       
class Gerente(Empleado):
    # Modificamos el constructor de la clase que heredamos
    # para que nos permita ingresar un atributo mas
    def __init__(self):
        #Heredamos el Constructor de la clase padre
        super().__init__()
        self.gerencia = input('Ingrese Gerencia: ')

empleado = Empleado()
gerente = Gerente()