#################################
# Unit 0 Lab 6
# Author: Your Name
#################################

from turtle import *

def setup(x, y):
    '''Sets up the turtle, ready to draw,
    at the given coordinates'''
    penup()
    goto(x, y)
    pendown()
    setheading(0)

def square(square_size):
    '''Draws a square using `square_size` as the length'''
    #YOUR CODE GOES HERE

    

def line_of_squares(square_size,gap_size):
    '''Draws a line of squares. 
    Uses `square_size` for the size of the square
    and `gap_size` for the size of the gap inbetween each square.
    Uses the function setup() to set the placement of the scoops.'''



def grid(square_size, gap_size):
    '''Draws a grid of squares. 
    Uses `square_size` for the size of the square
    and `gap_size` for the size of the gap inbetween each square.
    Uses the function setup() to set the placement of the scoops.'''


#Keeps the drawing window open until key press  
input("Press return to end drawing...")