"""
La función BEGIN_FILL le indica al programa que, a partir de ahí, todas lasfiguras que se hagan, deben ir rellenas hasta que le indiquemos que dejede hacerlo mediante la función END_FILL
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

begin_fill()
fillcolor()

left(90)
forward(100)
right(135)
forward(200)
left(135)
forward(100)
left(135)
forward(200)
end_fill()

exitonclick()