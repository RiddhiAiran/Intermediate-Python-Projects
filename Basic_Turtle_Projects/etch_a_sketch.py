from turtle import Turtle, Screen

brush = Turtle() # Turtle Object 

screen = Screen()# Screen Object to Control the Display Screen when we run the code.
screen.title("Etch A Sketch")


def move_forward():
    brush.fd(20)
    
def move_backward():
    brush.bk(20)
    
def anti_clockwise():
    brush.left(10)
    # Or
    # new_heading = brush.heading() + 10 
    # brush.setheading(new_heading)
    
def clockwise():
    brush.right(10)
    # Or
    # new_heading = brush.heading() - 10 
    # brush.setheading(new_heading)
    
def clear_screen():
    brush.reset()
    # Or 
    # brush.clear()
    # brush.penup()
    # brush.home()
    # brush.pendown() 

screen.listen() 
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=anti_clockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clear_screen)


screen.exitonclick()
