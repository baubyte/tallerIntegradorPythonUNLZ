"""
Modificar el siguiente código para que no de error al recibir un 
argumento que no es del tipo Lista.
def lista(argumentos):
    print(argumentos)
    print(len(argumentos))
lista([1,'Hola',['a','b','c']])
"""
def lista(argumentos):
    print(argumentos)
    if type(argumentos) == list:
        print(len(argumentos))
    else:
        print("El Argumento no es de Tipo Lista")

lista([1,'Hola',['a','b','c']])
lista("a")

