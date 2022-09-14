from turtle import *

def draw_triangle(side_length):
    #This function draws a triangle

    for i in range(3):
        forward(side_length)
        left(120)


# 💻 EXPERIMENT WITH CHANGING THE NUMBER IN THE BRACKETS BELOW  💻 #
draw_triangle(200)

input()