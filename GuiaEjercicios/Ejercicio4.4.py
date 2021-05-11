"""
Ejercicio 4.4.
Escribir un programa que genere 20 números al azar entre 1 y 5, los guarde en una lista,
 muestre la lista y luego muestre los dos números que más se repiten.
En caso de haber dos o mas números con la misma cantidad de apariciones, mostrarlos a todos. 
Por ejemplo, el número mas repetido es el 5, mostramos el 5, pero en segundo lugar aparecen los 
números 2 y 4 con la misma cantidad de repeticiones, mostrarlos a ambos, además de mostrar el 5.
"""
import random
import operator
diccionario = {}
#Genera 20 números al azar entre 1 y 5.
numerosAzar = [random.randint(1, 5) for _ in range(20) ]
#Se guardan los números únicos.
numerosUnicos = set(numerosAzar)
#Se agregan los nùmeros con la cantidad de repeticiones.
for numero in numerosUnicos:
    diccionario[numero] = numerosAzar.count(numero)
print(diccionario)

#Se ordena el diccionario por valores (se convierte en una lista de tuplas).
dicOrdenado = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
#Se crean las listas de claves y valores donde se van a almacenar los mas repetidos.
listKey = []
listValue = []
#Recorremos la lista de tuplas.
for contador in range(len(dicOrdenado)):
    #Si es el primero, guardamos en las listas de valores y claves.
    #Siempre se va a agregar, dado que por el orden siempre va a ser el mas repetido.
    if contador == 0:
        listKey.append(dicOrdenado[contador][0])
        listValue.append(dicOrdenado[contador][1])
    #Con el segundo valor se toma la misma condición del elemento anterior.
    elif contador == 1:
        listKey.append(dicOrdenado[contador][0])
        listValue.append(dicOrdenado[contador][1])
    #Si el valor actual se encuentra en la lista de valores, se agrega.
    elif dicOrdenado[contador][1] in listValue:
        listKey.append(dicOrdenado[contador][0])
        listValue.append(dicOrdenado[contador][1])
        
for i in range(len(listKey)):
    print(f"El número {listKey[i]} se repite {listValue[i]} veces")