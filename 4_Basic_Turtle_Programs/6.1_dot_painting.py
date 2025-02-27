# Based on : Damien Hirst Art Work

import random
import turtle
from turtle import Turtle, Screen

# Refer colorgram.py
rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
           (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), 
           (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
           (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
           (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
           (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), 
           (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), 
           (178, 198, 202), (112, 139, 141), (254, 194, 0)]

screen = Screen()
screen.title("Dot Painting")
screen.setup(width=1000,height=1000)

# Setup the turtle object
turtle.colormode(255)  # Set color mode to RGB
brush = Turtle()
brush.speed('fastest')  # Set turtle speed to fastest
brush.hideturtle()
brush.penup()

# with Experimenting
brush.goto(-250, -250)  # Move the turtle to a specific coordinate (bottom-left corner)

# Number of dots to draw
num_dots = 100
dot_size = 20
distance_between_dots = 50

# Draw the grid of dots
for count in range(1, num_dots + 1):
    brush.dot(dot_size, random.choice(rgb_colors))  # Draw a dot with a random color
    brush.forward(distance_between_dots)  # Move forward to the next dot
    
    # Move to the next row after every 10th dot
    if count % 10 == 0:
        brush.setheading(90)  # Point upwards
        brush.forward(distance_between_dots)  # Move to the next row
        brush.setheading(180)  # Point left
        brush.forward(distance_between_dots * 10)  # Move back to the start of the row
        brush.setheading(0)  # Point right

screen.exitonclick()
