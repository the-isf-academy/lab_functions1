# triangle.py

from turtle import *

def draw_triangle(side_length):
    # draws a triangle

    for i in range(3):
        forward(side_length)
        left(120)


# 💻 Experiment with changing the number in the brackets and rerunning the program ⬇️ #

draw_triangle(200)

input()