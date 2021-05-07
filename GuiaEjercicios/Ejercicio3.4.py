"""
Ejercicio 3.4.
Escribir un programa que pida al usuario, que ingrese una frase por teclado.
El programa deberá tener dos funciones, una que reciba la frase y devuelva solo 
las vocales de dicha frase y otra función que reciba la misma frase pero que devuelva 
solo las consonantes.
Mostrar por pantalla la frase original ingresada por el usuario, las vocales y 
las consonantes devueltas por sus respectivas funciones.
"""
#Lista Vocales
vocales = 'aeiouAEIOU'

#Devuelve todas las vocales de la frase
def getVocales(frase):
    return set([letra for letra in frase if letra in vocales])

#Devuelve todas las consonantes de la frase
def getConsonantes(frase):
    return set([letra for letra in frase if letra not in vocales])

fraseIngresada = input('Ingrese una Frase: ')

print("Las Vocales de la Frase Ingresa son: ", getVocales(fraseIngresada))
print("Las Consonantes de la Frase Ingresa son: ", getConsonantes(fraseIngresada))
print("Frase Ingresada:", fraseIngresada)