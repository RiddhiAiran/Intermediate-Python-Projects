from turtle import Turtle, Screen
import random
import turtle
screen = Screen()
screen.title("Spirograph")

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
def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        rangila.color(random_color())
        rangila.circle(100)
        rangila.setheading(rangila.heading() + size_of_gap)

draw_spirograph(3)

# Set it to close on click
screen.exitonclick()