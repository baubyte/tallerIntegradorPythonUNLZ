print("crea la funcion 1")
#crea la funcion 1 (no la ejecuta)
def funcion1():
    print("ejecuta la funcion 1")
 
print("crea la funcion 2")
#crea la funcion 2 (no la ejecuta)
def funcion2():
    print("ejecuta la funcion 2")
 
print("antes de comprobar __name__")
#como es el programa principal
if __name__ == '__main__':
#por tanto, ejecuta ambas funciones
    funcion1()
    funcion2()
print("despues del bloque __name__")