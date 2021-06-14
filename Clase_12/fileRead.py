#Abrimos el archivo con permiso de lectura
txt = open('./Clase_12/texto_2.txt', 'r')
contendido = txt.read()
print(contendido)
txt.close()