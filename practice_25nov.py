#gracie oxnam
#Ninja Turtles

import turtle

dona = turtle.Turtle()
#donatello’s color is purple
dona.pencolor('purple')
dona.fillcolor('purple')

leo = turtle.Turtle()
#leonardo’s color is blue
leo.pencolor('blue')
leo.fillcolor('blue')

raphael = turtle.Turtle()
#raphael’s color is red
raphael.pencolor('red')
raphael.fillcolor('red')

michel = turtle.Turtle()
#michelangelo’s color is orange
michel.pencolor('orange')
michel.fillcolor('orange')


#purple square
def square():
    for i in range(4):
        dona.forward(90)
        dona.right(90)

#orange hexagon (regular)
def hexagon_regular():
    #move so no overlap
    michel.left(90)
    michel.penup()
    michel.forward(100)
    michel.pendown()
    for i in range (6):
        michel.forward(70)
        michel.right(60)

#red hexagon (non-reg)
def hexagon_nonreg():
    #move so no overlap
    raphael.penup()
    raphael.backward(280)
    raphael.pendown()
    for i in range(2):
        raphael.forward(150)
        raphael.right(45)
        raphael.forward(80)
        raphael.right(90)
        raphael.forward(80)
        raphael.right(45)


#blue rectangle
def rectangle():
    #move so no overlap
    leo.penup()
    leo.backward(280)
    leo.left(90)
    leo.forward(100)
    leo.pendown()
    for i in range (2):
        leo.forward(90)
        leo.right(90)
        leo.forward(230)
        leo.right(90)

square()
hexagon_regular()
hexagon_nonreg()
rectangle()
