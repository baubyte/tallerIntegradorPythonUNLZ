"""
Ejercicio 2.8
Crear una lista con 10 números enteros y mostrarlos por pantalla.
Luego reemplazar todos los números pares por la palabra PAR y 
volver a mostrar la lista por pantalla.
"""
#Para obtener números al azar
import random
#Lista
numerosEnteros = [random.randint(1,101) for _ in range(10)]

print(f"Números en la Lista {numerosEnteros}")

for index in range(len(numerosEnteros)):
    if numerosEnteros[index]%2 == 0:
        numerosEnteros[index] = "PAR"
print(f"Números en la Lista sin los Pares {numerosEnteros}")