class Persona:
    __nombre = 'Atributo Privado'

    def __saludar(self):
        print('Metodo Privado')

    def getNombre(self):
        return self.__nombre

    def getSaludar(self):
        return self.__saludar()


baubyte = Persona()
print(baubyte.getNombre())
baubyte.getSaludar()
