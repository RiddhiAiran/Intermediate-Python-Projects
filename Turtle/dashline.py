from turtle import Turtle, Screen

# Draw a Dashed Line 
pen = Turtle() 
pen.color('black') 
pen.pensize(2)

for i in range(15): 
    pen.forward(10)
    pen.penup() 
    pen.forward(10)
    pen.pendown()

screen = Screen() 
screen.exitonclick() 