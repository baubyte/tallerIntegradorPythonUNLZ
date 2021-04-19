"""
Ejercicio 2.5
Escribir un programa que llene una lista con 50 números al azar y 
muestre por pantalla el número (o números) que más se repite. 
"""
#Para obtener números al azar
import random
#Lista
numerosAzar = []
numerosRepetidos = []
#Una manera de hacerlo
# numerosAzar = [random.randint(1,50) for _ in range(50)]

#Recorremos para buscar los numeros que se repiten
for azar in range(50):
    numerosAzar.append(random.randint(1,50))
#Recorremos para buscar los numeros que se repiten
for numero in numerosAzar:
    if numerosAzar.count(numero) > 2:
        if numero not in numerosRepetidos:
            numerosRepetidos.append(numero)
            print(f"El Número {numero} se repite {numerosAzar.count(numero)} veces.")

