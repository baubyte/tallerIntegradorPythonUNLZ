"""
    ingresar las notas de un alumno, se guardan en una lista.
    Se se la de la ejecución ingresando -1
    Se muestran todas las notas ingresadas
"""
#Lista
notas = []
#Contador
count = 0
print('***Ingrese todas las Notas del Alumno***\n ***Para terminar Ingrese \"-1\"***\n\n')
while True:
    nota = int(input('Ingrese una Nota: '))
    if nota == -1:
        break
    else:
        notas.append(nota)
#Mostar las Notas
cantidadNotas = len(notas)
promedio = sum(notas) / cantidadNotas
print("La cantidad de Notas ingresadas son:", cantidadNotas)
for nota in notas:
    count = count + 1
    print('La Nota ',count, 'es: ', nota)
print("El promedio de las Notas ingresadas es:", promedio)