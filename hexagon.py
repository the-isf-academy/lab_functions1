from turtle import *



# 💻 WRITE draw_hexagon BELOW  💻 #


def hexagon(side_length):
   #Draws a hexagon
   for i in range(6):
       forward(side_length)
       right(360//6)

hexagon(100)
input()

# 💻 DON'T FORGET TO CALL THE FUNCTION HERE  💻 #
