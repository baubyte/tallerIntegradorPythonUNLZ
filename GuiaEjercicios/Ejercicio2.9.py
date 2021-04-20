"""
Ejercicio 2.9
Hacer un menú de cuatro opciones, que le permita al usuario navegar 
por cuatro módulos diferentes del programa. Mostrar en cada módulo un 
título diferente para verificar que funciona correctamente
"""
while True:
    print()
    print("""Elija alguna de las Opciones Disponibles
            1. Modulo Uno
            2. Modulo Dos
            3. Modulo Tres
            4. Modulo Cuatro
            5. Salir""")
    opcion = int(input("Ingrese una Opción: "))
    print()
    if opcion == 1:
        print("Ingresaste al Modulo Uno")
        print()
    if opcion == 2:
        print("Ingresaste al Modulo Dos")
        print()
    if opcion == 3:
        print("Ingresaste al Modulo Tres")
        print()
    if opcion == 4:
        print("Ingresaste al Modulo Cuatro")
        print()
    if opcion == 5:
        print("Saliste del Programa ")
        break
    if opcion < 1 or opcion > 5:
        print("La Opción Ingresada no es correcta")