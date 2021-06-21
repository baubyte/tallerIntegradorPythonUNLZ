"""
Las funciones de orden superior son funciones que pueden recibir comoparámetro a otras funciones.
"""

#Funciones
def multiploDos(valor):
    if valor % 2 == 0:
        print('Es Múltiplo de 2')
    else:
        print('No es Múltiplo de 2')

def multiploTres(valor):
    if valor % 3 == 0:
        print('Es Múltiplo de 3')
    else:
        print('No es Múltiplo de 3')

#Funcion de Orden superior
def multiplos(value, callback):
    return callback(value)

multiplos(12, multiploDos)

multiplos(39, multiploTres)

multiplos(4, multiploTres)