"""
    Ejercicio 4.2
    Modificar el código del ejemplo de la página 15 del apunte de la clase 3 para que, además 
    de mostrar mediante una etiqueta el texto que ingresamos en la caja de texto, luego de hacerlo, 
    borre todo el contenido de dicha caja de texto, limpiando el formulario antes del próximo ingreso.
"""
#Modulo TkInter importar los principales con *
from tkinter import *
#Crea la ventana
ventana = Tk()
#Metedor de Configuración
ventana.configure(background='#003245')
#Titulo de la Ventana
ventana.title("Ejercicio 4.2")
#Desactiva el maximizar
ventana.resizable(0,0)
#Tamaño de la Ventana
ventana.geometry("600x400")

def click():
    mensaje = texto.get()
    etiquetaDos.config(text = mensaje)
    texto.delete(0,"end")

etiquetaUno = Label(ventana, text = 'Texto a Ingresar: ')
etiquetaUno.grid(row = 0, column = 0)

etiquetaDos = Label(ventana, text = 'Ingrese un Texto ')
etiquetaDos.grid(row = 1, column = 0)

texto = Entry(ventana, width = 30)
texto.grid(row = 0, column = 1)

btn = Button(ventana, text = 'Aceptar', command = click)
btn.grid(row = 0, column = 2)

ventana.mainloop()