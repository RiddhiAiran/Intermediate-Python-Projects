from turtle import Turtle, Screen

# Draw a Dashed Line 
pen = Turtle() 

for i in range(15): 
    pen.forward(10)
    pen.penup() 
    pen.forward(10)
    pen.pendown()

screen = Screen() 
screen.title("Dashline")
screen.exitonclick() 
