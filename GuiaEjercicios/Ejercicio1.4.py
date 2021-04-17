"""
Ejercicio 1.4
Escribir un programa que le pida dos números al usuario y 
muestre por pantalla todos los números pares que hay entre ambos números, 
incluyendo, en caso de ser pares, los números que ingresó el usuario.
 """
#Variables
numeroMayor = 0
numeroMenor = 0
numeroUno = int(input("Ingrese un Número: "))
numeroDos = int(input("Ingrese un Número: "))

if numeroUno == numeroDos:
    resto = numeroUno%2
    print("Ambos Números Ingresados son Iguales y son Pares") if resto == 0 else print("Ambos Números Ingresados son Iguales y no son Pares")
    pass
elif numeroUno > numeroDos:
    numeroMayor = numeroUno
    numeroMenor = numeroDos
else:
    numeroMayor = numeroDos
    numeroMenor = numeroUno
if numeroMayor > 0:
    print("Los Números Pares Entre: ", numeroMenor, " y ", numeroMayor, "son:")
    for valor in range(numeroMenor,numeroMayor+1):
        resto = valor%2
        if resto == 0:
            print(valor) 