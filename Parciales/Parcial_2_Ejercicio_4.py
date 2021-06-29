import random
class Numeros():
    valores = []

    def __init__(self):
        while True:
            cantNumAzar = int(input('Ingrese la Cantidad de Números al Azar: '))
            minNum = int(input('Ingrese el inicio del rango o el numero minimo para arrancar: '))
            maxNum = int(input('Ingrese el final del rango o el numero maximo para finalizar: '))
            if cantNumAzar < 0:
                print("El Numero debe se mayor a cero.")
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

print(numeros.valores)
print(numeros.candidato())