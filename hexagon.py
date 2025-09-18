# hexagon.py

from turtle import *

# 💻 Write the definition for draw_hexagon() ⬇️ #
def draw_hexagon(side_length):
    # draws a hexagon

    for i in range(6):
        forward(side_length)
        right(60)

# 💻 Don't forget to call the function  ⬇️ #
draw_hexagon(100)

input()