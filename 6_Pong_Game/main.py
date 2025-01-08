# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_DISTANCE,
    COLLISION_DISTANCE, WALL_BOUNDARY, MISS_BOUNDARY
)

class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.create_game_objects()
        self.setup_controls()
        self.game_is_on = True
        
    def setup_screen(self):
        self.screen.title("The Pong Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)
        
    def create_game_objects(self):
        self.r_paddle = Paddle((PADDLE_DISTANCE, 0))
        self.l_paddle = Paddle((-PADDLE_DISTANCE, 0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        
    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.r_paddle.up, 'Up')
        self.screen.onkey(self.r_paddle.down, 'Down')
        self.screen.onkey(self.l_paddle.up, 'w')
        self.screen.onkey(self.l_paddle.down, 's')
        self.screen.onkey(self.quit_game, 'q')
        
    def check_collisions(self):
        # Wall collisions
        if abs(self.ball.ycor()) > WALL_BOUNDARY:
            self.ball.bounce_y()
            
        # Paddle collisions
        if ((self.ball.distance(self.r_paddle) < COLLISION_DISTANCE and 
             self.ball.xcor() > PADDLE_DISTANCE - 20) or
            (self.ball.distance(self.l_paddle) < COLLISION_DISTANCE and 
             self.ball.xcor() < -PADDLE_DISTANCE + 20)):
            self.ball.bounce_x()
            
    def check_scoring(self):
        # Right paddle misses
        if self.ball.xcor() > MISS_BOUNDARY:
            self.ball.reset_position()
            self.scoreboard.point('left')
            
        # Left paddle misses
        elif self.ball.xcor() < -MISS_BOUNDARY:
            self.ball.reset_position()
            self.scoreboard.point('right')
            
    def quit_game(self):
        self.game_is_on = False
        self.scoreboard.game_over()
        
    def run(self):
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()
            self.check_collisions()
            self.check_scoring()
        
        self.screen.exitonclick()

if __name__ == "__main__":
    game = PongGame()
    game.run()