# main.py
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def setup_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

def main():
    screen = setup_game()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    # Set up controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.toggle_pause, "space")  # Added pause functionality
    
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(snake.speed)
        snake.move()
        
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        
        # Detect collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 
            or snake.head.ycor() > 290 or snake.head.ycor() < -290):
            scoreboard.game_over()
            time.sleep(2)
            scoreboard.reset()
            snake.reset()
        
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                time.sleep(2)
                scoreboard.reset()
                snake.reset()
    
    screen.exitonclick()

if __name__ == "__main__":
    main()