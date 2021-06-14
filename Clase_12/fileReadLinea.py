#Abrimos el archivo con permiso de lectura
txt = open('./Clase_12/datosClientesV2.txt', 'r')
contentLine = txt.readline()
while contentLine !='':
    print(contentLine, end='')
    contentLine = txt.readline()
txt.close()