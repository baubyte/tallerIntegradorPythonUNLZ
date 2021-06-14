#Escribir Archivos

#Abrimos el archivo con permiso de escritura
txt = open('./Clase_12/texto_2.txt', 'w')
ListaUno = str([1,2,3,4,5])+'\n'
ListaDos = str([6,7,8,9,10])+'\n'
ListaTres = str([11,12,13,14,15])+'\n'
txt.write(ListaUno)
txt.write(ListaDos)
txt.write(ListaTres)
txt.close()