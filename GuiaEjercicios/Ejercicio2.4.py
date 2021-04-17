"""
Ejercicio 2.3
Escribir un programa que permita al usuario ingresar por teclado tantos números 
enteros como desee. Cuando no quiera ingresar más números, deberá ingresar el cero.
A continuación, determinar cuál de los números ingresados es el mayor y cuál es el menor. 
Mostrar ambos por pantalla.
"""
#Listas
numeros = []
numeroMayor = None
numeroMenor = None
print('*** Ingrese tanto Números Enteros como Desee ***\n ***Para terminar Ingrese \"0\"***\n\n')
while True:
    numero = int(input('Ingrese un Número: '))
    if numero == 0:
        numeros.sort(reverse=True)
        print("El Mayor Número Ingresado es: ", numeros.pop())
        print("El Menor Número Ingresado es: ", numeros[0])
        break
    else:
        numeros.append(numero)