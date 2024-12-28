from turtle import Turtle, Screen
import random

rangila = Turtle()
rangila.shape('turtle')
rangila.color('Indianred')
rangila.pensize(3)
rangila.speed('fast')

colors = [
   'red', 'orange',
   'turquoise', 'teal', 'coral', 'skyblue', 'seagreen',
   'pink', 'indianred','salmon', 'peru',
   '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD',
    'wheat', 'bisque', 'blanchedalmond', 'burlywood',
    'peachpuff', 'navajowhite', 'moccasin', 'rosybrown',
    '#FFE4C4', '#DEB887', '#D2B48C', '#BC8F8F', '#F5DEB3',
    'sienna', 'saddlebrown', 'chocolate', 
   'rosybrown', 'sandybrown', 'goldenrod', 'tan',
   '#8B4513', '#D2691E', '#CD853F', '#DEB887'
]

#Draw All Shapes from 3 to 10 Sides in single run 
for sides in range(3,11):
    angle = 360/sides # Angle According to the Shape
    rangila.color(random.choice(colors)) # Change Color
    for _ in range(sides):
        rangila.fd(100) # Move Forward
        rangila.left(angle) # Point Left with Shape's angle

# Create the screen and set it to close on click
screen = Screen()
screen.exitonclick()