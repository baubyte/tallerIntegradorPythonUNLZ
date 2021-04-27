"""
Conjuntos.Los conjuntos son listas desordenadas de elementos únicos (no repetidos).
Se   los   suele   utilizar   para   eliminar   duplicados,   verificar   pertenencia   
y soportan operaciones matemáticas complejas.
"""

# *** ¿Qué sucederá si añadimos el número cero?
conjunto = {1, 2, 3, 4}
print(conjunto)
conjunto.add(5)
print(conjunto)
conjunto.add(0)
print(conjunto)
# *** ¿Qué longitud tiene nuestro conjunto?
conjunto2 = {2, 2, 4, 4}
print(conjunto2)
print(len(conjunto2))
# ** ¿Qué pasa si hacemos esto mismo con una cadena de caracteres o 
# con una lista de letras?
lista = ['a','a','b', 'b','c']
print(lista)
lista = list(set(lista))
print(lista)