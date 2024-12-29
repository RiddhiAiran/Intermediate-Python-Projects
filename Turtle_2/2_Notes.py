from turtle import Turtle, Screen

brush = Turtle() # Turtle Object 


screen = Screen() # Screen Object to Control the Display Screen when we run the code.

def move_forward():
    brush.fd(20)

    

screen.listen() # Start Listening the Events. 
# Now We need to bind (function) that will be triggered when a particular Key is pressed.
# 1. Bind a Key with an event in the code (Event Listener) using screen.onkey(key,function)
# Function as an input so do not use paranthesis
screen.onkey(key='w',fun=move_forward)

screen.exitonclick()
