""" Las   funciones   SETX   y   SETY   nos   permiten   desplazar   el   cursor   a   unadeterminada posición del área de dibujo modificando un solo componentede la coordenada (X o Y) manteniendo el otro fijo.
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


#setx() sety()
forward(100)
sety(-100)

exitonclick()