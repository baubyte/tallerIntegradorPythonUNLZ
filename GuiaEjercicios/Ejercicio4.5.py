"""
Ejercicio 4.5
Pedir al usuario que ingrese una frase y luego le muestre la frase ingresada y
 la cantidad de veces que aparece cada vocal.
"""
#Lista Vocales
vocales = ['a','e','i','o','u']

fraseIngresada = input("Ingrese una Frase: ")
#Recorrecolos las vocales
for vocal in vocales:
    print(f"La vocal {vocal} se repite {fraseIngresada.lower().count(vocal)}")