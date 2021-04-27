"""
Escribir un programa que le pida al usuario que ingrese un número por teclado, lo 
eleve al cubo y muestre el resultado por pantalla. El programa deberá seguir funcionando 
hasta que el usuario ingrese el número cero.
"""

def cuboNumero(numero):
    return numero**3

while True:
    print("Ingresa Cero para salir")
    numeroIngresado = int(input("Ingrese un Número: "))
    if numeroIngresado != 0:
        print("El Cubo del Numero Ingresado es: ", cuboNumero(numeroIngresado))
    else:
        break