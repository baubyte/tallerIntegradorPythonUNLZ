"""
Ejercicio 2.3
Pedirle al usuario que ingrese dos números enteros por teclado y 
contar cuantos números pares hay entre ambos valores ingresados, 
verificando también los números ingresados por el usuario.
"""
#Variables
numerosParesEnc = []
listaNumerosIng = []
numeroUno = int(input("Ingrese un Número Entero: "))
numeroDos = int(input("Ingrese un Número Entero: "))

if numeroUno != 0 or numeroDos != 0:
    listaNumerosIng = [numeroUno,numeroDos]
    listaNumerosIng.sort()
    for numeroIng in range(listaNumerosIng[0],listaNumerosIng[1]+1):
        resto = numeroIng%2
        if resto == 0:
            numerosParesEnc.append(numeroIng)
    print("La Cantidad de Números Pares Encontrados entre ", listaNumerosIng, "son: ", len(numerosParesEnc))
else:
    print("¡Ups! Al Menos un Número debe ser Mayor a Cero")