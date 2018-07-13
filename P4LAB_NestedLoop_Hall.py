#CTI-110
#P4LAB Nested Loops
#Kaiya Hall
#july 1,2018


import turtle
import random


wn = turtle.Screen()
wn.bgcolor("blue")
 


flake = turtle.Turtle()

colors = ['hotpink', 'white', 'yellow','green']


def snowflake(size, pensize, x, y):
    
    
    flake.penup()
    flake.goto(x, y)
    flake.forward(10*size)
    flake.left(45)
    flake.pendown()
    flake.color('yellow')

    for i in range(8):
        branch(size)
        flake.left(45)



def branch(size):
    for i in range(3):
        for i in range(3):
            flake.forward(10.0*size/3)
            flake.backward(10.0*size/3)
            flake.right(45)
        flake.left(90)
        flake.backward(10.0*size/3)
        flake.left(45)
    flake.right(90)
    flake.forward(10.0*size)

snowflake(8, 6, 0, 0)


wn.mainloop()
