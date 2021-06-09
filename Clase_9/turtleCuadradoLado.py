"""
    1. Escribir una función que reciba el lado del cuadrado y lo dibuje
"""

from turtle import *

def cuadrado(lado):
    for index in range(4):
        forward(lado)
        left(90)

cuadrado(200)
exitonclick()