"""
Ejercicio propuesto: Escribir un programa que solicite el ingreso por
teclado de los datos de un cliente (DNI, apellido y nombre) y le pregunte
al usuario si desea seguir cargando datos (las opciones son s/n).
Una vez terminada la carga de datos, guardarlos en un archivo.
"""

#Datos
datosClientes = []
opcion = 's'

#sale si la opción es igual n
while opcion == 's':
    #gusradamos los datos ingresados
    dni = input('Ingrese el DNI: ')
    apellido = input('Ingrese el Apellido del Cliente: ')
    nombre = input('Ingrese el Nombre del Cliente: ')
    datosClientes.append(dni)
    datosClientes.append(apellido)
    datosClientes.append(nombre)
    print('\n')
    #preguntamos si quieres seguir ingresando datos
    opcion = input('¿Quiere Ingresar mas Datos? (s/n): ')
    if opcion.lower() != 's':
        break

#escribimos los datos en el archivo

#Abrimos el archivo con permiso de escritura
txt = open('./Clase_12/datosClientes.txt', 'w')
txt.write(str(datosClientes))
txt.close()