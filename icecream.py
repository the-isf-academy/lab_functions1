from turtle import *

def setup(x,y):
    # this function moves the turtle to a given x,y location

    penup()
    goto(x,y)
    pendown()
    setheading(0)


def scoop(num_scoops):
    # 💻 Complete edit the scoop() function below 💻 #

    circle(100)


def cone():
    # 💻 Complete and edit the cone() function below 💻 #

    forward(100)



def draw_icecream():
    # 💻 You may need to edit the code below 💻 #

    cone()
    setup(0,0)
    scoop(3)


draw_icecream()
input()

