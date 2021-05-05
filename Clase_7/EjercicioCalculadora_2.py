#Clase Calculadora
class Calculadora:
    resultado = None
    operacion = None

    def calcular(self, numUno, numDos, calculo):
        self.operacion = calculo.upper()
        if (self.operacion == "SUMA"):
            self.resultado = (numUno + numDos)
        elif (self.operacion == "RESTA"):
            self.resultado = (numUno - numDos)
        elif (self.operacion == "PRODUCTO"):
            self.resultado = (numUno * numDos)
        if (self.resultado is None):
            print("Operacion no Disponible")
        else:
            print(f"El Resultado de la Operacion \"{self.operacion}\" es {self.resultado}")


#Instanciamos la calculadora
calculadora = Calculadora()
print('Operaciones Disponibles')
print("""Para Sumar Ingrese: \"SUMA\" 
Para Restar Ingrese: \"RESTA\" 
Para Multiplicar Ingrese: \"PRODUCTO\" 
""")
ingOperacion = input('Escriba Operacion a Realizar: ')
ingNumUno = int(input('Ingrese un Numero: '))
ingNumDos = int(input('Ingrese un Numero: '))
#Llamamos al metodo calcular
calculadora.calcular(ingNumUno,ingNumDos,ingOperacion)




