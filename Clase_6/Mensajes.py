#Modulo TkInter importar los principales con *
from tkinter import *
from tkinter import messagebox as MessageBox
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

def textoA():
    MessageBox.showinfo('Mensaje A', 'Martin')

def textoB():
    MessageBox.showinfo('Mensaje B', 'BAUBYTE')

btnUno = Button(ventana, text = 'Martin', command = textoA)
btnUno.grid(row = 0, column = 0)

btnDos = Button(ventana, text = 'BAUBYTE', command = textoB)
btnDos.grid(row = 1, column = 0)
ventana.mainloop()