"""
Ejercicio propuesto: Escribir un programa que solicite el ingreso por
teclado de los datos de un cliente (DNI, apellido y nombre) y le pregunte
al usuario si desea seguir cargando datos (las opciones son s/n).
Una vez terminada la carga de datos, guardarlos en un archivo.
"""

opcion = 's'

#Abrimos el archivo con permiso de escritura
txt = open('./Clase_12/datosClientesV2.txt', 'w')
#sale si la opción es igual n
while opcion == 's':
    #gusradamos los datos ingresados
    dni = input('Ingrese el DNI: ')
    apellido = input('Ingrese el Apellido del Cliente: ')
    nombre = input('Ingrese el Nombre del Cliente: ')
    #escribimos los datos en el archivo
    txt.write(dni+','+apellido+','+nombre+'\n')
    print('\n')
    #preguntamos si quieres seguir ingresando datos
    opcion = input('¿Quiere Ingresar mas Datos? (s/n): ').lower()
    if opcion != 's':
        break
#cerrasmos el archivo
txt.close()