class Persona:
    __nombre = 'Atributo Privado'

    def __saludar(self):
        print('Método privado')


# Si intentamos acceder el interprete dará error
baubyte = Persona()
print(baubyte.__nombre)
baubyte.__saludar()
