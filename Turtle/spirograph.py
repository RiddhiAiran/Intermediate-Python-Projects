from turtle import Turtle, Screen
import random
import turtle

rangila = Turtle()
rangila.speed('fastest')
turtle.colormode(255) # RGB Mode

#Random RGB Tuple Colors 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# Draw a SpiroGraph
size = 3
for i in range(360//size):
    rangila.color(random_color())
    rangila.circle(100)
    rangila.setheading(rangila.heading() + size)




# Create the screen and set it to close on click
screen = Screen()
screen.exitonclick()