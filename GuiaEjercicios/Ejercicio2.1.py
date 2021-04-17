"""
Ejercicio 2.1
Si creamos tres listas. La primera contiene 4 números, la segunda contiene 5 letras 
y en la tercera le cargamos como elementos las dos listas anteriores.
¿Cuántos elementos contendrá la tercera lista? Dos Elenetos tendra la sublista.
Demostrar mediante un breve código.
"""
#Listas
listaNumeros = [1,2,3,4]
listaLetras = ['a','b','c','d','e']
subLista = [listaNumeros,listaLetras]
print("La Cantidad de Elementos de la Sublista es: ",len(subLista))