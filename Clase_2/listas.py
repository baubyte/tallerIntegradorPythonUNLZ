#Listas
lista1 = [1,2,3,"Hola Mundo",4,5,6]
lista2 = ['a','b','c','d','e']
lista3 = [lista1, lista2]
lista4 = [1,1,1,2,3,4,5,5,6,7]
lista5 = [1,2,3,4,5,6,7,8,9,10]
lista6 = [120,10,5,150,6]
print(lista3)
print(lista3[1][0])
#Cantidad de elementos de una lista
print('Cantidad de elementos de una lista1')
print(len(lista1))
#Tipo de elemento
print('Tipo de elemento lista2')
print(type(lista2))
#Metodos
nombre = ['Martin', 'Jose']
print('Lista nombre')
print(nombre)
#Agregar Elementos
print('Lista nombre aplicando append')
nombre.append('BAUBYTE')
print(nombre)
#Contar elementos
print('El Número 1 se repite:', lista4.count(1), 'veces')
#Buscar y un elemento devuelve el indice
print('El Número 5 se encuentra en:', lista4.index(5))
#Elemento pop devuelve el ultimo elemento de una lista y lo borra
print('Elementos lista4:', lista4)
ultimoIndex = lista4.pop()
print('Elementos lista4 aplicando pop:', lista4, 'el ultimo elemento fue:', ultimoIndex)
#Remove elimina la primer aparición del elemento
lista4.remove(5)
print(lista4)
#Cambiar el orden de una lista
print('Lista Original:', lista5)
lista5.reverse()
print('Lista Aplicando reverse', lista5)
#Ordena los elementos de una lista de mayor a menor
print('Lista Original:', lista6)
lista6.sort()
print('Lista Aplicando sort:', lista6)
#Ordena los elementos de una lista de menor a mayor
print('Lista Original:', lista6)
lista6.sort(reverse=True)
print('Lista Aplicando sort reverse=True:', lista6)