#Clase Calculadora
class Calculadora:
    resultado = None
    def sumar(self, numUno, numDos):
        self.resultado = (numUno + numDos)
        print('El Resultado de la Suma es', self.resultado)



ingNumUno = int(input('Ingrese un Numero: '))
ingNumDos = int(input('Ingrese un Numero: '))

calculadora = Calculadora()

calculadora.sumar(ingNumUno,ingNumDos)