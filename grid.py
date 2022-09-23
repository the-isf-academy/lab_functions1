#######################
# Unit 0 Lab 6
# grid.py
#######################

from turtle import *


def square(square_size):
    '''Draws a square using `square_size` as the length'''
    
    # 💻 YOUR CODE GOES HERE 💻 #
    for i in range(4):
        forward(square_size)
        right(90)


def line_of_squares(square_size,gap_size):
    '''Draws a line of squares. 
    Uses `square_size` for the size of the square
    and `gap_size` for the size of the gap inbetween each square.
    Uses the function setup() to set the placement of the scoops.'''

    # 💻 YOUR CODE GOES HERE 💻 #
    for i in range(4):
        square(square_size)
        penup()
        forward(square_size+gap_size)
        pendown()
    
    penup()
    home()
    pendown()

# line_of_squares(50,20)



def polygon(num_sides,num_size):
    for i in range(num_sides):
        forward(num_size)
        right(360//num_sides)

def line_of_polygons(num_sides, num_size,gap_size):
    '''Draws a line of squares. 
    Uses `square_size` for the size of the square
    and `gap_size` for the size of the gap inbetween each square.
    Uses the function setup() to set the placement of the scoops.'''

    # 💻 YOUR CODE GOES HERE 💻 #
    for i in range(4):
        polygon(num_sides,num_size)
        penup()
        forward(num_size+gap_size)
        pendown()
    
    penup()
    home()
    pendown()     

def grid(num_sides, num_size, gap_size):
    '''Draws a grid of squares. 
    Uses `square_size` for the size of the square
    and `gap_size` for the size of the gap inbetween each square.
    Uses the function setup() to set the placement of the scoops.'''

    # 💻 YOUR CODE GOES HERE 💻 #
    for i in range(1,5):
        
        # line_of_squares(square_size,gap_size)
        line_of_polygons(num_sides, num_size, gap_size)

        penup()
        home()
        right(90)
        forward((gap_size+num_size)*i)
        left(90)
        pendown()

speed(0)
grid(8,25,50)

# 💻 DON'T FORGET TO CALL A FUNCTION! 💻 #
###### BE SURE TO TEST EACH FUNCTION ONE AT A TIME ######



#Keeps the drawing window open until key press  
input("Press return to end drawing...")