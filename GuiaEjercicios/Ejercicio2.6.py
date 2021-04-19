"""
Ejercicio 2.6
Escribir un programa que le pregunte al usuario cuantas palabras desea 
ingresar, luego le permita ingresarlas todas y finalmente mostrarlas por pantalla.
"""
#Lista
palabras = []
cantPalabras = int(input("Ingrese la Cantidad de Palabras a Guardar: "))
for count in range(cantPalabras):
    palabras.append(input(f"Ingrese la Palabra {count+1}: "))

print("Las Palabras Ingresadas Fueron:")
for palabra in palabras:
    print(palabra)