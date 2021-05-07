"""
    Crea una función llamada modificar() que a partir de una lista de números realice las siguientes 
    tareas sin modificar la original:
        Borrar los elementos duplicados.
        Ordenar la lista de mayor a menor.
        Eliminar todos los números impares.
        Realizar una suma de todos los números que quedan.
        Añadir como primer elemento de la lista la suma realizada.
        Devolver la lista modificada.
    Una vez escrita la función, utilizarla y verificar que la el primer elemento de dicha lista, 
    coincide con la suma de los demás elementos.
"""
def modificar():
    #Lista con numero duplicados
    numeros = [1,2,3,3,4,4,5,5,6,6,7,8,9,9,0]
    numerosOrdenados = numeros.sort()
    numerosUnicos = set(numerosOrdenados)
    listaNumImpares = [numero for numero in numerosUnicos if numero % 2 == 1]
    
