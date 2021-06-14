#Abrimos el archivo con permiso de lectura
txt = open('./Clase_12/datosClientesV2.txt', 'r')
lista = txt.readlines()
print('La Lista Tiene: ' +str(len(lista))+' elementos.')
for index in lista:
    print(index)
txt.close()