import random

inicio = 2000
fin = 5000
limite = 1000

# Ejercicio 2.2
numerosRand = [random.randrange(inicio, fin) for i in range(limite)]
print(numerosRand)



# Ejercicio 2.2
evenNumbers = list(filter(lambda x : x%2==0 ,numerosRand))
print()
print("Filtro solo los pares de la lista anterior usando una lambda: ")
print()
print(evenNumbers)

