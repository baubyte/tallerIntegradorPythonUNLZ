# Importo el randomizer
import random

# Declaro las variables del inicio, fin y limite de numeros por lista
Start = 2000
Stop = 5000
limit = 1000

# Ejercicio 2.1
## Lista de 1000 numeros en el rango de 2000 a 5000
randomNumbersList = [random.randrange(Start, Stop) for iter in range(limit)]
print("Lista de 1000 números entre 2000 a 5000: ")
print()
print(randomNumbersList)

# Ejercicio 2.2
evenNumbers = list(filter(lambda x : x%2==0 ,randomNumbersList))
print()
print("Filtro solo los pares de la lista anterior usando una lambda: ")
print()
print(evenNumbers)