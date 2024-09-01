# icecream.py

from turtle import *
from random import randint

speed(0)

def scoop(scoop_size, scoop_color):
    # draws a circle of any size
    
    fillcolor(scoop_color)
    begin_fill()
    circle(scoop_size)
    end_fill()

def cone(side_length, cone_color):
    # draws a triangle 
   
    fillcolor(cone_color)
    begin_fill()
    forward(side_length/2)
    right(120)
    forward(side_length)
    right(120)
    forward(side_length)
    right(120)
    forward(side_length/2)
    end_fill()
 
def sprinkles():
  pensize(3)
  pencolor('pale turquoise')
  for i in range(10):
    penup()
    goto(randint(-65,65),randint(20,100))
    setheading(randint(0,360))
    pendown()
    forward(5)
  # print(pos())

# 💻 Call the functions scoop() and cone() to draw an ice cream cone ⬇️ 

# scoop_color = input('what flavor of ice cream? ')
cone(100, 'sandy brown')
penup()
goto(0,-20)
pendown()
begin_fill()
scoop(75, 'light salmon')
end_fill()
sprinkles()


hideturtle()
input()
