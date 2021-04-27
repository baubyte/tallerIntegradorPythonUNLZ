#Modulo TkInter importar los principales con *
from tkinter import *
#Crea la ventana
ventana = Tk()
#Metedor de Configuración
ventana.configure(background='#003245')
#Titulo de la Ventana
ventana.title("Clase 6 Python")
#Desactiva el maximizar
ventana.resizable(0,0)
#Tamaño de la Ventana
ventana.geometry("600x400")
def clickUno():
    lblUno.configure(text='Boton Uno')
def clickDos():
    lblUno.configure(text='Boton Dos')
#Boton Uno
btnUno = Button(ventana, text = 'Boton Uno', command=clickUno)
btnUno.grid(row = 4, column = 1)
#Boton Dos
btnDos = Button(ventana, text = 'Boton Dos', command=clickDos)
btnDos.grid(row = 4, column = 5)

lblUno = Label(ventana, text="Presione un Boton")
lblUno.grid(row = 15, column = 1)
ventana.mainloop()

