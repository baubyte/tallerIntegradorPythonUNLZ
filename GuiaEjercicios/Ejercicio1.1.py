"""
Ejercicio 1.1

Solicitar por teclado el ingreso de un número entero.
Asignar dicho número a una variable, transformarla 
a coma flotante y mostrarla por pantalla (valor y tipo de variable).
 """
#Variable
numero = int(input("Ingrese un Número entero Mayor a Cero: "))
numero = float(numero)
print("Tipo de Variable", type(numero))
print("Numero ingresado covertido:", numero)