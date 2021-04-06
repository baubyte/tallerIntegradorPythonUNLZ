#Lineas
linea1 = [1,2,3]
linea2 = [4,5,6]
linea3 = [7,8,9]
#Matriz de lineas
matriz = [linea1, linea2, linea3]
print(matriz)
print('Buscamos')
print(matriz[2][0])

#Recorrer matriz
filas = len(matriz)
columnas = len(matriz[0])
#Recorremos
for fila in range(0,filas):
    for columna in range(0,columnas):
        print(matriz[fila][columna], end=',')