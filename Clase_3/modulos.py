#Para obtener números al azar
import random
print('Numero al azar entre 1 y 10: ', random.randrange(11))
print('Numero al azar entre 20 y 30: ', random.randrange(20,31))
print('Numero impar al azar entre 1 y 20: ', random.randrange(1,21,2))

#Tomar al azar de una lista
autos = ['Fiat','Ford','Peugeot']
print('La marca elegida es: ', random.choice(autos))

#Mezclar una lista y la devuelve
valores = [1,2,3,4,5,6]
print(valores)
random.shuffle(valores)
print(valores)
random.shuffle(valores)
print(valores)
random.shuffle(valores)
print(valores)