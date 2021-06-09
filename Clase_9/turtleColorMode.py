from turtle import *
#setup(ancho, alto, x, y)
setup(600,300,10,50)
#title('nombre de la ventana')
title("Modulo Turtle")
#Area de Dibujo screensizealta, ancho)
screensize(300, 300)
#ocultar turtle / cursor
hideturtle()

#Tamaño de Lapiz
pensize(10)
colormode(1)
#Color de Lápiz
pencolor(1,0.6,0.9)
forward(100)

penup()
forward(50)
pendown()
colormode(255)
#Color de Lápiz
pencolor(124, 255, 36)

forward(100)
exitonclick()