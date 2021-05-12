"""
    Escribir un programa que verifique la validez de la CLAVE ingresada siguiendo los 
    siguentes criterios:
        1.Debe contener una longitud mínima de 6 caracteres.
        2.Debe tener una longitud máxima de 12 caracteres.
        3.Debe contener al menos una letra entre [a-z]
        4.Debe contener al menos una letra entre [A-Z]
        5.Debe contener al menos un número [0-9]
"""

# Permite acceder a funcionalidades dependientes del Sistema Operativo
import os
# Permite utilizar expresiones regulares
import re

# Valida si la contraseña cumple con los requerimientos
# Retorna true en si cumple caso contrio false

def validatePassword(password):
    if 6 <= len(password) <= 12:
        if re.search('[a-z]', password) and re.search('[A-Z]', password):
            if re.search('[0-9]', password):
                return True
    return False


usuario = input('Escriba su Usuario: ')
while True:
    os.system("clear")
    print()
    clave = input('Escriba la contraseña: ')
    if validatePassword(clave):
        print("Registro exitoso")
        break
    else:
        print("La Contraseña no Cumple con los Parametros de Seguridad")
        input("Presione Enter e Intente de Nuevo")
