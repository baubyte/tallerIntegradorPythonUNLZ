class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __del__(self):
        print('La persona', self.nombre, 'ha Sido Eliminada.')


baubyte = Persona('Martin')
print('El Nombre de la Persona Creada es:', baubyte.nombre)
del(baubyte)
