"""
Cola.
Una cola es una lista de elementos en la que el primero en 
entrar es elprimero en salir.Para trabajar con colas, deberemos 
importar el módulo DEQUE:
"""
from collections import deque

cola = deque(['a','b','c','d'])
print(cola)
cola.append('e')
print(cola)
cola.popleft()
print(cola)