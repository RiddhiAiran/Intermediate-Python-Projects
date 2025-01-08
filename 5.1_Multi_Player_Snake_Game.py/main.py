# main.py
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def setup_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

def get_game_mode():
    while True:
        mode = screen.textinput("Game Mode", "Enter 1 for Single Player, 2 for Two Players:").strip()
        if mode in ['1', '2']:
            return int(mode)

def get_difficulty():
    while True:
        level = screen.textinput("Difficulty", "Choose difficulty (easy/medium/hard):").lower().strip()
        if level in ['easy', 'medium', 'hard']:
            return level

screen = setup_game()
game_mode = get_game_mode()
difficulty = get_difficulty()

# Set game speed based on difficulty
speed_dict = {'easy': 0.1, 'medium': 0.075, 'hard': 0.05}
game_speed = speed_dict[difficulty]

# Create game objects
snake1 = Snake(start_pos=(0, 0), color='white')
snake2 = Snake(start_pos=(0, -40), color='yellow') if game_mode == 2 else None
food = Food()
scoreboard = Scoreboard(game_mode)

# Set up controls
screen.listen()
# Player 1 controls (Arrow keys)
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")
screen.onkey(snake1.boost_speed, "space")  # Speed boost

# Player 2 controls (WASD)
if game_mode == 2:
    screen.onkey(snake2.up, "w")
    screen.onkey(snake2.down, "s")
    screen.onkey(snake2.left, "a")
    screen.onkey(snake2.right, "d")
    screen.onkey(snake2.boost_speed, "Shift_L")  # Left Shift key for boost

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(game_speed)
    
    # Move snakes
    snake1.move()
    if game_mode == 2:
        snake2.move()

    # Check food collision for both snakes
    for snake in [snake1, snake2] if game_mode == 2 else [snake1]:
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score(1 if snake == snake1 else 2)

        # Wall collision
        if (snake.head.xcor() > 290 or snake.head.xcor() < -295 or 
            snake.head.ycor() > 290 or snake.head.ycor() < -295):
            game_on = False
            scoreboard.game_over()

        # Self collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()

        # Snake collision in 2 player mode
        if game_mode == 2 and snake2:
            if snake1.head.distance(snake2.head) < 10:
                game_on = False
                scoreboard.game_over("Draw!")
            for segment in snake2.segments:
                if snake1.head.distance(segment) < 10:
                    game_on = False
                    scoreboard.game_over("Player 2 Wins!")
            for segment in snake1.segments:
                if snake2.head.distance(segment) < 10:
                    game_on = False
                    scoreboard.game_over("Player 1 Wins!")

screen.exitonclick()