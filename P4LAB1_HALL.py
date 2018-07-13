import turtle
wn = turtle.Screen()
wn.title('Square & Triangle')

square = turtle.Turtle()

for x in range (4):
    square.forward(50)
    square.left(90)

triangle = turtle.Turtle()

for x in range (3):
    triangle.forward(100)
    triangle.left(120)


wn.mainloop()
