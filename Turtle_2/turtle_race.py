from turtle import Turtle, Screen
import random 
import time 

screen = Screen() # Screen Object to Control the Display Screen when we run the code.
screen.setup(width=500, height=500)
screen.title("Turtle Race")
screen.bgcolor("Beige")
time.sleep(2)

colors = ['red', 'orange', 'black', 'green', 'blue', 'purple', 'brown']
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

# Create turtles and set their initial positions
for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[i])
    all_turtles.append(new_turtle)

user_choice = screen.textinput(title='Make your Bet', prompt="Which turtle will win the race? Enter a color:")
if user_choice:
    race = True 

# Create a Turtle object to display text
text_writer = Turtle()
text_writer.hideturtle()
text_writer.penup()

while race:
    for turtle in all_turtles:
        if turtle.xcor() >= 230 - 10: # adjust to the turtle's size
            race = False
            winner = turtle.pencolor()
            text_writer.goto(0, 0)  # Position the text in the center of the screen
            if winner == user_choice:
                text_writer.write(f"You won! {winner.title()} is the winner of the race.", align="center", font=("Arial", 16, "bold"))
            else:
                text_writer.write(f"You lose! {winner.title()} is the winner of the race.", align="center", font=("Arial", 16, "bold"))
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
