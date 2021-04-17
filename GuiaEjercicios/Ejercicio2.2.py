"""
Ejercicio 2.1
Escribir un programa que pida ingresar un número entero mayor que cero por teclado.
Verificar si el número ingresado es múltiplo de 2, 3, 4, 5, 6, 7,8 o 9.
Armar una lista con los números encontrados (por ejemplo, si el 
número ingresado es múltiplo de 3,6 y 7, armamos una lista que contenga estos tres números).
Mostrar la lista por pantalla, ordenada de mayor a menor.
En caso de que el número ingresado no sea múltiplo de estos números, 
mostrar por pantalla el mensaje “No se encontraron divisores exactos”.
"""
verificarMultiplos = [2, 3, 4, 5, 6, 7, 8, 9]
multiplos = []
print("***** Busca los Múltiplos del Numero Ingresado en una Lista. ******")
numero = int(input("Ingrese un Numero: "))
#Verificamos que Numero sea Mayor a 0
if numero > 0:
    for valorVerificar in verificarMultiplos:
        resto = numero%valorVerificar
        if resto == 0:
            multiplos.append(valorVerificar)
    if len(multiplos) > 0:
        print("El Número Ingresado es Múltiplo de: ", multiplos)
    else:
        print("No se encontraron divisores exactos")
else:
    print("El Numero Ingresado debe ser Mayor a Cero.")