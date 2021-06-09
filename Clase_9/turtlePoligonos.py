"""
    Crear una función que dibuje polígonos regulares.
    Polígono   regular   (es   un polígono cuyos lados y ángulos interiores son iguales entre sí).
"""

from turtle import *

def poligono(lado,n):
    for index in range(n):
        forward(lado)
        left(360/n)


for index in range(3,15):
    poligono(50,index)
    
exitonclick()