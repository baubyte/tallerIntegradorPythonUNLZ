"""
Ejercicio 2.9
Hacer un menú de cuatro opciones, que le permita al usuario navegar 
por cuatro módulos diferentes del programa. Mostrar en cada módulo un 
título diferente para verificar que funciona correctamente
"""
#Permite acceder a funcionalidades dependientes del Sistema Operativo
import os
while True:
    os.system ("clear") 
    print()
    print("""Elija alguna de las Opciones Disponibles
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Salir""")
    opcion = int(input("Ingrese una Opción: "))
    print()
    if opcion == 1:
        print("Estas en la Opción Sumar")
        numeroUno = int(input("Ingrese un Numero: "))
        numeroDos = int(input("Ingrese otro Numero: "))
        print()
        print(f"El Resultado de la Suma es: {numeroUno + numeroDos}")
        input("Presione Enter para Continuar...")
    if opcion == 2:
        print("Estas en la Opción Restar")
        numeroUno = int(input("Ingrese un Numero: "))
        numeroDos = int(input("Ingrese otro Numero: "))
        print()
        print(f"El Resultado de la Resta es: {numeroUno - numeroDos}")
        input("Presione Enter para Continuar...")
    if opcion == 3:
        print("Estas en la Opción Multiplicar")
        numeroUno = int(input("Ingrese un Numero: "))
        numeroDos = int(input("Ingrese otro Numero: "))
        print()
        print(f"El Resultado de la Multiplicación es: {numeroUno * numeroDos}")
        input("Presione Enter para Continuar...") 
    if opcion == 4:
        print("Estas en la Opción Dividir")
        numeroUno = int(input("Ingrese un Numero: "))
        numeroDos = int(input("Ingrese otro Numero: "))
        print()
        divisionEntera = numeroUno // numeroDos if numeroDos != 0 else "No se pude dividir por 0"
        divisionDecimal = numeroUno / numeroDos if numeroDos != 0 else "No se pude dividir por 0"
        print(f"El Resultado de la Division Entera es: {divisionEntera}")
        print(f"El Resultado de la Division Decimal es: {divisionDecimal}")
        input("Presione Enter para Continuar...") 
    if opcion == 5:
        print("Saliste del Programa ")
        break
    if opcion < 1 or opcion > 5:
        print("La Opción Ingresada no es correcta")
        input("Presione Enter para Continuar...")