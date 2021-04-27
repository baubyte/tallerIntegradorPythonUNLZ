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
#Etiquetas necesita a quien pertenece y el  texto
#Etiquetas 1
etiquetaUno = Label(ventana,text = 'Etiqueta Uno',font=("calibri",20), bg="black",fg='green')
#Mostramos la Etiqueta
etiquetaUno.grid(row = 0, column = 1)
#Etiqueta 2
etiquetaDos = Label(ventana,text = 'Etiqueta Dos')
#Mostramos la Etiqueta
etiquetaDos.grid(row = 1, column = 0)
#Etiqueta 3
etiquetaTres = Label(ventana,text = 'Etiqueta Tres')
#Mostramos la Etiqueta y posicionamos con place por coordenadas
etiquetaTres.place(x=100, y= 50)

#Botones necesita a quien pertenece y el  texto
#Boton Uno
btnUno = Button(ventana, text = 'Aceptar')
btnUno.grid(row = 4, column = 1)
#Boton Dos
btnDos = Button(ventana, text = 'Flat', relief=FLAT)
btnDos.grid(row = 4, column = 2)
#Boton Tres
btnTres = Button(ventana, text = 'Sunken',relief=SUNKEN)
btnTres.grid(row = 4, column = 3)
#Boton Cuatro
btnCuatro = Button(ventana, text = 'Ridge',relief=RIDGE)
btnCuatro.grid(row = 4, column = 4)
#Boton Cinco
btnCinco = Button(ventana, text = 'Solido',relief=SOLID)
btnCinco.grid(row = 4, column = 5)
ventana.mainloop()