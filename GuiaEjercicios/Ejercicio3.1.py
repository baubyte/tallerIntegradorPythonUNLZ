"""
Ejercicio 3.1
Escribir una función en Python para calcular el factorial de un número entero positivo.
Basarse en la siguiente definición:
El factorial de un número entero positivo n, se define como el producto de 
todos los números enteros positivos menores o iguales a n. 
El factorial de cero es 1.
Por ejemplo, el factorial de 4 será 4x3x2x1 = 24.
"""
#Permite acceder a funcionalidades dependientes del Sistema Operativo
import os
#Funcion calcula el factorial de un numero
def factorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial 

numero = int(input("Ingrese un Número Mayor o Igual a Cero: "))

if numero >= 0:
    print(f"El Factorial del Numero {numero} es: {factorial(numero)}")
else:
    print("El Numero Ingresado debe ser Mayor o Igual a Cero.")