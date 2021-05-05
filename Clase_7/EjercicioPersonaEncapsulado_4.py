class Persona:
    __nombre = 'Atributo Privado'

    def __saludar(self):
        print('Método Privado')

    def getNombre(self):
        return self.__nombre

    def getSaludar(self):
        return self.__saludar()

    def setNombre(self, nombre):
        self.__nombre = nombre


baubyte = Persona()
print(baubyte.getNombre())
baubyte.getSaludar()
baubyte.setNombre('Martin')
print("Nombre Modificado 1: ", baubyte.getNombre())
baubyte.setNombre('Jose')
print("Nombre Modificado 2: ", baubyte.getNombre())
