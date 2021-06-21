#DNI a buscar
dniBuscado = '9876543'
#Abrimos el archivo con permiso de lectura
txt = open('./Clase_12/datosClientesV2.txt', 'r')
contentLines = txt.readlines()
for index in contentLines:
    if dniBuscado == index[:len(dniBuscado)]:
        datosLines = index
        break

datosLines = datosLines.split(sep=',')
print(datosLines)
print('DNI: ', datosLines[0])
print('Apellido: ', datosLines[1])
print('Nombre: ', datosLines[2])
txt.close()