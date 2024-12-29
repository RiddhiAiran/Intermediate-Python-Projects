from turtle import Turtle, Screen
import random

rangila = Turtle()
rangila.shape('classic')
rangila.pensize(2)
rangila.speed('fast')
screen = Screen()
screen.title("Random Shapes")

colors = [
   'red', 'orange','pink'
   ,'turquoise', 'teal', 'coral', 'skyblue', 'seagreen',
   'pink', 'indianred','salmon', 'peru',
    'bisque', 'blanchedalmond', 'burlywood',
    'moccasin', 'rosybrown', 'sienna', 'saddlebrown', 'chocolate', 
   'rosybrown', 'sandybrown', 'goldenrod', 'tan',
]

#Draw All Shapes from 3 to 10 Sides in single run 
for sides in range(3,11):
    angle = 360/sides # Angle According to the Shape
    rangila.color(random.choice(colors)) # Change Color
    for _ in range(sides):
        rangila.fd(100) # Move Forward
        rangila.left(angle) # Point Left with Shape's angle

# Create the screen and set it to close on click

screen.exitonclick()