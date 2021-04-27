"""
Diccionarios.
Este tipo de colección, al igual que los conjuntos, es muy utilizadas en 
Python.Son colecciones desordenadas.Los diccionarios tienen elementos definidos 
por una clave, que debe serúnica, y un valor.Podemos   crear   un   diccionario   
directamente,   sin   cargarle   elementosutilizando llaves
"""

# *** ¿Qué sucede  si colocamos dos pares de  elementos con la mismaclave?
diccionario = {'uno':'one', 'dos':'two', 'tres':'three', 'cuatro':'four'}
print(diccionario)
diccionario2 = {'cuatro':'four'}
diccionario.update(diccionario2)
print(diccionario)
# *** ¿Qué nos devuelve la función LEN aplicada a un diccionario?
print(len(diccionario))