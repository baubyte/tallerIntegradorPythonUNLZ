"""
Ejercicio 1.3
Pedir al usuario que ingrese por teclado dos números reales y 
utilizarlos para realizar todas las operaciones aritméticas vistas 
(suma, resta, multiplicación, división, potencia, división entera y resto).
Mostrar todos los resultados por pantalla (un resultado por línea) con 
su respectiva leyenda aclarando de que operación se trata.
 """
print("**** Operaciones Aritméticas *****")
print("***** Se aplicaran diversas operaciones a los números. ******")
#Variables
numeroUno = int(input("Ingrese un Número: "))
numeroDos = int(input("Ingrese un Número: "))

if numeroUno != 0 or numeroDos != 0:
    resultadoSuma = numeroUno + numeroDos
    resultadoResta = numeroUno - numeroDos
    resultadoMutiplicacion = numeroUno * numeroDos
    resultadoDivEntera = numeroUno // numeroDos if numeroDos != 0 else "No se pude dividir por 0"
    resultadoDivDecimal = numeroUno / numeroDos if numeroDos != 0 else "No se pude dividir por 0"
    resultadoResto = numeroUno % numeroDos if numeroDos != 0 else "No se pude dividir por 0"
    resultadoPotencia = numeroUno ** numeroDos
    print("Resultado de Sumar ", numeroUno ," mas ", numeroDos ," es igual a: ", resultadoSuma)
    print("Resultado de Restar ", numeroUno ," menos ", numeroDos ," es igual a: ", resultadoResta)
    print("Resultado de Multiplicar ", numeroUno ," por ", numeroDos ," es igual a: ", resultadoMutiplicacion)
    print("Resultado de elevar", numeroUno ," por ", numeroDos ," es igual a: ", resultadoPotencia)
    print("Resultado de la Division Entera entre", numeroUno ," y ", numeroDos ," es igual a: ", resultadoDivEntera)
    print("Resultado de la Division entre", numeroUno ," y ", numeroDos ," es igual a: ", resultadoDivDecimal)
    print("El resto de la Division entre", numeroUno ," y ", numeroDos ," es igual a: ", resultadoResto)
else:
    print("¡Ups! Al Menos un Número debe ser Distinto a Cero\n para Realizar el Calculo")