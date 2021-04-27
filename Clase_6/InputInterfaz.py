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
caja = Entry(ventana)
caja.grid(row=0,column=0)

ventana.mainloop()

