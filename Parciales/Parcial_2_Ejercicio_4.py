import random
class Numeros():
    valores = []

    def __init__(self):
        while True:
            cantNumAzar = int(input('Ingrese la cantidad de números al azar: '))
            minNum = int(input('Ingrese el inicio del rango o el numero minimo para arrancar: '))
            maxNum = int(input('Ingrese el final del rango o el numero maximo para finalizar: '))
            if cantNumAzar < 0:
                print("El Numero debe ser mayor a cero.")
            else:
                self.valores = [random.randint(minNum,maxNum) for _ in range(cantNumAzar)]

                break

    def candidato(self):
        count = 0
        for i in self.valores:
            frecuencia = self.valores.count(i)
            if(frecuencia > count):
                count = frecuencia
                num = i
        return num
        

numeros = Numeros()

print()
print("Valores creados al azar: ")
print(numeros.valores)
print()
print("Numero candidato de la lista: ")
print(numeros.candidato())
