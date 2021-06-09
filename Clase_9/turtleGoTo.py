""" La función GOTO nos permite desplazar el cursor a un determinado puntodel   área   de   dibujo, a 
    medida   que   lo   vamos   desplazando,   entre   unaposición y la siguiente, se irá dibujando una línea
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


#goto(x,y)
goto(0,0)
goto(10,10)
goto(10,-30)
goto(-20,35)

exitonclick()