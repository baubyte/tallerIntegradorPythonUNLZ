"""
Podemos pedirle al usuario que ingrese valores alfanuméricos por tecladomediante la función TEXTINPUT.Los   parámetros   son   TITULO   (es   el   título   de   la   ventana   emergente)   yMENSAJE (texto que se muestra en la ventana para el usuario).El valor se deberá asignar a una variable para poder utilizarla.
De   similar   manera,   podemos   pedirle   al   usuario   valores   numéricosmediante la función NUMINPUT con algunos parámetros adicionales (título,mensaje, predeterminado, mínimo, máximo).

"""
from turtle import *
#setup(ancho, alto, x, y)
setup(600,300,10,50)
#title('nombre de la ventana')
title("Modulo Turtle")
#Area de Dibujo screensizealta, ancho)
screensize(300, 300)
#ocultar turtle / cursor
hideturtle()
ingreso = textinput('Titulo Ventana', 'Ingrese una Frase')
write(ingreso, False, 'center',('arial', 12, 'bold'))

ingresoNumeros = numinput('Titulo Ventana', 'Ingrese un Valor de 1 a 10',10,1,10)
penup()
left(-90)
forward(15)
pendown()
write(ingresoNumeros, False, 'center',('arial', 12, 'bold'))

exitonclick()