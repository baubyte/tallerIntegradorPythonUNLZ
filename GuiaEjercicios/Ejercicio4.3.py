"""
Ejercicio 4.3.
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
    #Lista con números duplicados
    numeros = [10,12,14,5,8,9,3,1,2,3,3,4,4,5,5,6,6,7,8,9,9,0]
    #Se eliminan los repetidos
    numerosUnicos = set(numeros)
    #Se eliminan los impares
    sinNumImpares = [numero for numero in numerosUnicos if numero % 2 == 0]
    nuevaLista = [sum(sinNumImpares)]
    nuevaLista.extend(sinNumImpares) 
    return nuevaLista

otraLista = modificar()
if sum(otraLista[1:]) == otraLista[0]:
    print("Suma: ", otraLista[0])
    print("Resto de la lista: ", otraLista[1:])
    print("Lista completa: ", otraLista)
    print("Son iguales")
else:
    print("No son iguales")
    print("Lista completa: ", otraLista)
