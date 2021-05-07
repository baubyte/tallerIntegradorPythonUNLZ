"""
Ejercicio 4.1
Hacer un programa que contenga tres botones y cada uno de ellos muestre por 
pantalla (usando una etiqueta) un número al azar con el siguiente criterio:
    Botón 1: un número al azar entre 0 y 10.
    Botón 2: un número al azar entre 0 y 50.
    Botón 3: un número al azar entre 0 y 100.
"""
#Importamos las librerías
from tkinter import *
from tkinter import ttk, font
import random
#Crea la ventana
ventana = Tk()
# Genera Números al azar de 0 al 10
def getNumAzar0a10():
    numAzar = random.randint(0,10)
    setNumAzar(numAzar)
# Genera Números al azar de 0 al 50
def getNumAzar0a50():
    numAzar = random.randint(0,50)
    setNumAzar(numAzar)
# Genera Números al azar de 0 al 100
def getNumAzar0a100():
    numAzar = random.randint(0,100)
    setNumAzar(numAzar)
#Setea el numero al label
def setNumAzar(numero):
    lblMostrarNumAzar.config(text = str(numero))
#Defino la Fuente
fuente = font.Font(weight='bold')
#Titulo de la ventana
ventana.title('Ejercicio 4.1')
#Desactiva el maximizar
ventana.resizable(0,0)
#Tamaño de la Ventana
ventana.geometry("400x200")
#Etiquetas
lblTitulo = ttk.Label(ventana, text="Presiona alguno de los Botones", font=fuente)
lblNumAzar = ttk.Label(ventana, text="Tu Número es: ", font=fuente)
lblMostrarNumAzar = ttk.Label(ventana, text="0", font=fuente)
#Mostramos la Etiqueta
lblTitulo.grid(row = 0, column = 1)
lblNumAzar.grid(row = 2, column = 1)
lblMostrarNumAzar.grid(row = 2, column = 2)
#Botones
btnNumAzar0a10 = ttk.Button(ventana, text="Botón 1",command = getNumAzar0a10)
btnNumAzar0a50 = ttk.Button(ventana, text="Botón 2",command = getNumAzar0a50)
btnNumAzar0a100 = ttk.Button(ventana, text="Botón 3",command = getNumAzar0a100)
#Mostramos los Botones
btnNumAzar0a10.grid(row = 4, column = 0)
btnNumAzar0a50.grid(row = 4, column = 1)
btnNumAzar0a100.grid(row = 4, column = 2)
ventana.mainloop()
   