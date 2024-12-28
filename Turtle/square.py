from turtle import Turtle, Screen

rangila = Turtle()
rangila.shape('turtle')
rangila.color('Indianred')

#Draw a Square
for i in range(4):
    rangila.forward(100) # Moves Forward - 100 Points 
    rangila.right(90) # Point Right - 90 Degrees 

# Create the screen and set it to close on click
screen = Screen()
screen.exitonclick()
