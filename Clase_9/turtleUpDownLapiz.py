"""Podemos movernos de un lado al otro del área de dibujo sin dibujar la línea con la función PENUP (y con la función PENDOWN volvemos a bajarel lápiz).
"""

from turtle import *
#setup(ancho, alto, x, y)
setup(600,300,10,50)
#title('nombre de la ventana')
title("Modulo Turtle")
#Area de Dibujo screensizealta, ancho)
screensize(300, 300)
#ocultar turtle / cursor
#hideturtle()


#penup() pendown()
forward(100)
penup()
back(50)
pendown()
left(45)
forward(100)
exitonclick()