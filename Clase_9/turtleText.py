"""
La función WRITE nos permite poner texto dentro de nuestros dibujos. Se le pueden pasar hasta cuatro parámetros. Estos parámetros son:
    * TEXTO: cadena de texto a mostrar. Comienza a escribirse dondeeste el cursor, salvo que le indiquemos otra cosa.
    * DESPLAZAMIENTO:   este   parámetro   puede   tomar   los   valoresTRUE o FALSE y lo que le indicamos a Python es si desplaza elcursor a la esquina inferior derecha del texto o no antes deseguir dibujando.
    * ALINEACIÓN:   indicamos   cómo   será   la   alineación   del   textorespecto a la posición actual del cursor. Puede ser LEFT, CENTER o RIGHT
    * FUENTE: es una tupla de hasta tres elementos que indica tipo deletra, tamaño y tipo.
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

circle(40)

end_fill()


# left(90)
# penup()
# forward(100)

# write("Esto es un Circulo",True)
# write("Esto es un Circulo",False)
# pendown()
# forward(70)

forward(100)
write("Esto es un Circulo",False, "left")

penup()
forward(-220)
pendown()
write("Esto es un Circulo",False, "right", ('arial', 15, 'italic'))
exitonclick()