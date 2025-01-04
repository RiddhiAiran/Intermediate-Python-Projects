# from turtle import Turtle, Screen

# # Draw a Dashed Line 
# pen = Turtle() 
# pen.color('black') 
# pen.pensize(2)


# for i in range(15): 
#     pen.forward(10)
#     pen.penup() 
#     pen.forward(10)
#     pen.pendown()

# screen = Screen() 
# screen.title("Dashline")
# screen.exitonclick() 

from turtle import Turtle, Screen

rangila = Turtle()
screen = Screen()
screen.title('Draw a Dashed line')

for _ in range(15):
    rangila.forward(10)
    rangila.penup()
    rangila.forward(10)
    rangila.pendown()
	
screen.exitonclick()