class Empleado():
    def __init__(self):
        self.nombre = input('¿Nombre?: ')
        self.apellido = input('¿Apellido?: ')

    def __str__(self):
        mensaje = self.apellido +', '+self.nombre
        return mensaje

empleado = Empleado()
#Comentar el método __str__ para ver la diferencia
print(empleado)