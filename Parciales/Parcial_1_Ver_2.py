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
def validatePassword(password):
    if 6 <= len(password) <= 12:
        if validateContainAZ(password) and validateContainaz(password):
            if validateContain1a9(password):
                return True
    return False

def validateContainAZ(password):
    for letra in password:
        if ord(letra) >= ord('a') and ord(letra)  <= ord('z'):
            return True
    return False

def validateContainaz(password):
    for letra in password:
        if ord(letra) >= ord('A') and ord(letra)  <= ord('Z'):
            return True
    return False

def validateContain1a9(password):
    for letra in password:
        if ord(letra) >= ord('0') and ord(letra)  <= ord('9'):
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
        print("La Contraseña no Cumple con los Parametros de Segurida")
        input("Presione Enter e Intente de Nuevo")