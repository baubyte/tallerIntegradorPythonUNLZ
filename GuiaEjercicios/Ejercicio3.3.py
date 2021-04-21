"""
Ejercicio 3.3.
Escribir una función que encuentre los números primos comprendidos entre 
dos números enteros ingresados por teclado.
"""
#Listas Números Primos
primos = []
#Determina si el Numero es Primo
def esPrimo(numPrimo):
    if numPrimo < 1:
        return False
    elif numPrimo == 2:
        return True
    else:
        for numero in range(2, numPrimo):
            if numPrimo % numero == 0:
                return False
            return True

#Agrega los Numero primos que se encuentra entre}
#los números que le pasemos

def primosAdd(numUno, numDos):
    numeros = [numUno, numDos]
    numeros.sort()
    for i in range(numeros[0], numeros[1]):
        if esPrimo(i) == True:
            primos.append(i)


print("***Determina los Numero Primos entre los Números Ingresados***")

numeroUno = int(input("Ingrese un Número Mayor a Cero: "))
numeroDos = int(input("Ingrese un Número Mayor a Cero: "))

if numeroUno > 0 or numeroDos > 0:
    primosAdd(numeroUno, numeroDos)
    print(f"Los Numero Primos Encontrados son: {primos}")
else:
    print("Alguno de los Numero deben ser Mayor a Cero.")