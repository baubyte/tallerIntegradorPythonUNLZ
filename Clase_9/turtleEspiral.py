"""
    Dibujar un espiral
"""

from turtle import *

def poligono(lado,n):
    for index in range(n):
        forward(lado)
        left(360/n)


for index in range(20,200,5):
    poligono(index,3)
    right(10)
    
exitonclick()