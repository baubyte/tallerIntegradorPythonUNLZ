"""
Ejercicio 3.2
Escribir una función para determinar si un número entero, ingresado por 
teclado es un número primo.
Un número primo es aquel que solo tiene como divisores enteros 
(resto igual a cero) al número 1 y a sí mismo, por ejemplo, el número 5.
"""

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

print("***Determina si el Numero Ingresado es Primo***")

numero = int(input("Ingrese un Número Mayor a Cero: "))

if numero > 0:
    print(f"El Numero {numero} es Primo") if esPrimo(numero) else print(f"El Numero {numero} no es Primo:")
else:
    print("El Numero Ingresado debe ser Mayor a Cero.")