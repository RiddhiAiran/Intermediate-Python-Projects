from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Steps for the Snake Game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# 1. Create a Snake Body (creating 3 squares on the screen next to each other)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Control the Snake (Control the direction of the snake - Up, Down, Left, Right Arrow keys)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


# 2. Move the Snake (Continue to move forward)
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    ## Detect collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        # Extend the snake Body
        snake.extend()
        # 5. Create a Score board (write text, score addition)
        scoreboard.increase_score()
        
    # 6. Detect Collion with wall (Detect the collision, show game over text, no movement of snake)
    if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()
    
    # 7. Detect Collion with the Tail (head hit any part of the body of the snake, then again game over)
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()