# Ejercicio 3

# importo functools
import functools

numero = input("Ingrese un Numero: ")
factorial = (functools.reduce(lambda x,y:x*y,list(range(2,int(numero)+1))))
print()
print(f"El factorial es: {factorial}")