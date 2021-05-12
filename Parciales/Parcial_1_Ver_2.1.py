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

# Valida si la contraseña cumple con los requerimientos
# Retorna true en si cumple caso contrio false


def validatePassword(password):
    if validateLen(password):
        if validateContainAZ(password) and validateContainaz(password):
            if validateContain1a9(password):
                return True
    return False

# Comprueba si el tamaño de la cadena esta entre 6 y 12 carateres
# Retorna true en si cumple caso contrio false


def validateLen(password):
    if 6 <= len(password) <= 12:
        return True
    return False

# Comprueba si la cadena contiene al menos una letra minúscula [a-z]
# Retorna true en si cumple caso contrio false


def validateContainAZ(password):
    for letra in password:
        if ord('a') <= ord(letra) <= ord('z'):
            return True
    return False
# Comprueba si la cadena contiene al menos una letra mayúscula [A-Z]
# Retorna true en si cumple caso contrio false


def validateContainaz(password):
    for letra in password:
        if ord('A') <= ord(letra) <= ord('Z'):
            return True
    return False
# Comprueba si la cadena contiene al menos una un numero [1-9]
# Retorna true en si cumple caso contrio false


def validateContain1a9(password):
    for letra in password:
        if ord('0') <= ord(letra) <= ord('9'):
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
