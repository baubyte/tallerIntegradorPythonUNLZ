import random

inicio = 2000
fin = 5000
limite = 1000

numerosRand = [random.randrange(inicio, fin) for i in range(limite)]
print(numerosRand)