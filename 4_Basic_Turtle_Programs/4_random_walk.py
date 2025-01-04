from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.title("Random Walk")
# Object Assignment and Qualitie
brush = Turtle()
brush.shape('turtle')
brush.color('green')
brush.pensize(10)
brush.speed('fastest')

turtle.colormode(255) # RGB Mode

directions = [0, 90, 180, 270]

#Random RGB Tuple Colors 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

#Draw a Square
for i in range(200):
    brush.color(random_color())
    brush.forward(30) # Moves Forward - 100 Points 
    brush.setheading(random.choice(directions)) # Point Right - 90 Degrees 

# Create the screen and set it to close on click

screen.exitonclick()