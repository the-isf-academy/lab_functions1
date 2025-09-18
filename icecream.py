# icecream.py

from turtle import *
from random import randint

def scoop(num_scoops, flavor, scoop_size):
    # draws a circle of any size
    if flavor == "chocolate":
        color = "brown"
    elif flavor == "strawberry":
        color = "pink"
    else:
        color = "moccasin"

    for i in range (num_scoops):
        begin_fill()
        fillcolor(color)
        circle(scoop_size)
        end_fill()
        penup()
        left(90)
        forward(scoop_size*3/4)
        right(90)
        pendown()

def cone(side_length, cone_color):
    # draws a triangle 
    begin_fill()
    fillcolor(cone_color)
   
    for i in range(3):
        forward(side_length)
        right(120)
    end_fill()

# print menu
print("--- Welcome to the ISF ice cream parlor ---")
print()
print("What flavor would you like?")
flavor = input("   > Select a flavor (chocolate, strawberry, vanilla): ")
print("How many scoops would you like?")
num_scoops = int(input("   > Select number of scoops (max 3): "))
print("Do you want sprinkles??")
sprinkles = input("   > Enter yes or no: ")

# 💻 Call the functions scoop() and cone() to draw an ice cream cone ⬇️ 

# draw cone
conesize = 100
cone(conesize, "sandy brown")

# go to position for scoop & draw scoop
penup()
forward(conesize/2)
right(90)
forward(conesize/3)
setheading(0)
pendown()
scoop(num_scoops, flavor, conesize/2)

penup()

# sprinkles
if sprinkles == "yes":
    x_coordinate = int(xcor())
    y_coordinate = int(ycor())
    for i in range (10):
        penup()
        goto(randint(int(x_coordinate)-50,int(x_coordinate)+50),randint(int(y_coordinate),int(y_coordinate)+50))
        setheading(randint(0,360))
        pendown()
        begin_fill()
        fillcolor("hot pink")
        for j in range (2):
            forward(7)
            right(90)
            forward(3)
            right(90)
        end_fill()

hideturtle()

print(" --- Enjoy your ice cream! Please come again! ---")
print()

input("[Press any key to exit]")
