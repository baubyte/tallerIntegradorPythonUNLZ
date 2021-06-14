
#Escribir Archivos

#Abrimos el archivo con permiso de escritura
txt = open('./Clase_12/texto.txt', 'w')
txt.write('Linea 1\n')
txt.write('Linea 2\n')
txt.write('Linea 3\n')
txt.close()