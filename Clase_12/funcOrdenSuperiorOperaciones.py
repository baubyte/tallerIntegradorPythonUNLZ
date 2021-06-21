"""
Las funciones de orden superior son funciones que pueden recibir comoparámetro a otras funciones.
"""

#Funciones
def suma(valor, otroValor):
    print(f"El Resultado de la Suma entre {valor} y {otroValor} es: {valor + otroValor}")

def resta(valor, otroValor):
    print(f"El Resultado de la Resta entre {valor} y {otroValor} es: {valor - otroValor}")

def multiplicacion(valor, otroValor):
    print(f"El Resultado de la Multiplicacion entre {valor} y {otroValor} es: {valor * otroValor}")

def division(valor, otroValor):
    try:
        print(f"El Resultado de la Resta entre {valor} y {otroValor} es: {valor / otroValor}")
    except:
        print("No se Puede Dividir por cero")



#Funcion de Orden superior
def operador(value, otherValue, operacion):
    return operacion(value, otherValue)

operador(12,20, suma)

operador(50,20, resta)

operador(0,20, multiplicacion)

operador(0,20, division)

operador(20,0, division)