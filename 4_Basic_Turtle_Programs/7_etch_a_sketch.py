from turtle import Turtle, Screen

brush = Turtle() # Turtle Object 

screen = Screen() # Screen Object to Control the Display Screen when we run the code.
screen.title("Etch A Sketch")

def move_forward():
    brush.fd(20)
    
def move_backward():
    brush.bk(20)
    
def anti_clockwise():
    brush.left(10)
    
def clockwise():
    brush.right(10)
    
def clear_screen():
    brush.reset()

screen.listen() # Listen the keyboard Events
screen.onkey(key='w',fun=move_forward) # Bind keystrokes with Events
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=anti_clockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clear_screen)

screen.exitonclick()
