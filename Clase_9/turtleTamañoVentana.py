from turtle import *

#setup(ancho, alto, x, y)
setup(600,300,10,50)


def poligono(lado,n):
    for index in range(n):
        forward(lado)
        left(360/n)

poligono(50,9)

exitonclick()