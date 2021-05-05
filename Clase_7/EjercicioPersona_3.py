# Clase
class Persona:
    nombre = None
    apellido = None

    def __init__(self):
        self.nombre = input('Ingresa un Nombre: ')
        self.apellido = input('Ingresa un Apellido: ')
        print(f'Hola {self.nombre} {self.apellido} 🙂')


# Instanciamos la clase.
baubyte = Persona()
