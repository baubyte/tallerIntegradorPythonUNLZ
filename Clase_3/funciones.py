#Funciones
def potencia(valor):
    resultado = valor ** 2
    print('El número', valor, 'Elevado al Cuadrado es:', resultado)
potencia(3)
def potenciaVerDos(valor):
    resultado = valor ** 2
    return(resultado)
print('El número Elevado al Cuadrado es:', potenciaVerDos(4))

#Lambda
otraFuncion = potencia
otraFuncion(4)
#Tipos
print(type(potencia))
print(type(otraFuncion))

def resta(a,b):
    resultado = a - b
    print('El resultado de la resta:', resultado)
resta(12,4)

#Recibe definimos a cual valor le corresponde 
resta(b=4,a=12)
def restaVerDos(a=None,b=None):
    if a == None or b == None:
        print('Tenes que pasar los valores para la resta')
        return
    resultado = a - b
    print('El resultado de la resta:', resultado)

restaVerDos()
#Recibe cualquier argumento
def lista(argumentos):
    print(argumentos)

valores = [1,2,3,4,'BAUBYTE']
lista(valores)
