"""
Ejercicio 2.7
Escribir un programa que le solicite al usuario ingresar 10 palabras, 
luego le pida ingresar una más y le diga si esa última palabra ingresada se encuentra entre 
las 10 palabras ingresadas anteriormente.
"""
#Lista
palabras = []

for count in range(10):
	palabras.append(input(f"{count+1}. Ingrese una Palabra: "))
if input("Ingrese una Palabra mas: ") in palabras:
	print("Esa Palabra ya la Ingreso Anteriomente")
else:
	print("Esa Palabra no la Ingreso Anteriomente")