"""
Ejercicio 1.3
Pedir al usuario que ingrese por teclado dos números reales y 
utilizarlos para realizar todas las operaciones aritméticas vistas 
(suma, resta, multiplicación, división, potencia, división entera y resto).
Mostar todos los resultados por pantalla (un resultado por línea) con 
su respectiva leyenda aclarando de que operación se trata.
 """
#Variable
print("**** Operaciones Aritméticas *****")
print("***** Se aplicaran diversas operaciones a los números. ******")
numeroUno = float(input("Ingrese un Número: "))
numeroDos = float(input("Ingrese un Número: "))

if numeroUno != 0 or numeroDos != 0:
    resultadoSuma = numeroUno + numeroDos
    resultadoResta = numeroUno - numeroDos
    resultadoMuti = numeroUno * numeroDos
    resultadoDiv = numeroUno / numeroDos if numeroUno !=0 and numeroDos != 0 else 0
    print("Resultado de Sumar el Primer Numero mas el Segundo Numero Ingresado: ", resultadoSuma)
    print("Resultado de Restar el Primer Numero menos el Segundo Numero Ingresado: ", resultadoResta)
     print("Resultado de Multiplicar el Primer Numero por el Segundo Numero Ingresado: ", resultadoMuti)
else:
    print("¡Ups! Al Menos un Número ser Mayor a Cero\n para Realizar el Calculo")