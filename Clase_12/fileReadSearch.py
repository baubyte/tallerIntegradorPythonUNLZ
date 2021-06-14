#Abrimos el archivo con permiso de lectura
txt = open('./Clase_12/datosClientesV2.txt', 'r')
contentLine = txt.readline()
while contentLine !='':
    #Buscamos el dni 1234568
    dni = contentLine[0:7]
    dniSearch = input('Ingrese DNI a Buscar: ')
    if dni == dniSearch:
        print(contentLine)
        break
    else:
        print('El Numero de DNI no se encontró')
        break
    contentLine = txt.readline()
txt.close()