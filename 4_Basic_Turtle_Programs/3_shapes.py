from turtle import Turtle, Screen
import random

rangila = Turtle()
rangila.pensize(2)
rangila.speed('fast')
screen = Screen()
screen.title("Draw Shapes")

colors = ['red', 'orange','pink', 'teal', 'coral', 'skyblue', 'seagreen','pink', 'indianred','salmon','rosybrown', 'sienna', 'saddlebrown', 'chocolate', 'rosybrown', 'sandybrown', 'goldenrod', 'tan']

def draw_shapes(num_sides):
    angle = 360/num_sides # Angle According to the Shape
    for _ in range(num_sides):
        rangila.fd(100)
        rangila.left(angle) # Point Left with Shape's angle

#Draw All Shapes from 3 to 10 Sides in single run 
for sides in range(3,11): 
    rangila.color(random.choice(colors)) # Change Color
    draw_shapes(sides)

# Create the screen and set it to close on click
screen.exitonclick()