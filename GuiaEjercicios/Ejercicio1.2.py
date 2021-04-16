"""
Ejercicio 1.2

Desarrollar un programa que solicite al usuario los lados de un rectángulo y 
calcule su perímetro y su superficie.
Informar ambos resultados por pantalla.
 """

print("**** Calculo de la Superficie de un Rectángulo y su Perimetro *****")
altura = float(input("Ingrese la Altura del Rectángulo: "))
base = float(input("Ingrese la Base del Rectángulo: "))
if altura > 0 and base > 0:
    superficie = base * altura
    perimetro = (base * 2) + (altura * 2)
    print("La Superficie del Rectángulo es: ", superficie)
    print("El Perimetro del Rectángulo es: ", perimetro)
else:
    print("¡Ups! Tanto la Altura como la Base deben ser Mayor a Cero\n para Realizar el Calculo")