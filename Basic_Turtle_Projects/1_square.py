from turtle import Turtle, Screen

screen = Screen()
screen.title('Square')

rangila = Turtle()
rangila.shape('turtle')
rangila.color('Red')

#Draw a Square
for i in range(4):
    rangila.forward(100) # Moves Forward - 100 Points 
    rangila.right(90) # Point Right - 90 Degrees 

# Create the screen and set it to close on click
screen.exitonclick()

