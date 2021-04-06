#While
"""contador = 1
while contador <= 10:
    print(contador)
    contador= contador + 1
print('Fin de Ciclo:', contador)"""

contador = 0
while True:
    contador = contador + 1
    print(contador)
    if contador == 11:
        break
print('Fin de Ciclo:', contador)
