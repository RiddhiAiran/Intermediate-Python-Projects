# ball.py
from turtle import Turtle
from constants import BALL_SPEED, INITIAL_MOVE_SPEED, SPEED_INCREMENT

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.reset_position()
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        """Bounce the ball vertically"""
        self.y_move *= -1 
        
    def bounce_x(self):
        """Bounce the ball horizontally and increase speed"""
        self.x_move *= -1 
        self.move_speed *= SPEED_INCREMENT
    
    def reset_position(self):
        """Reset ball to center with initial settings"""
        self.goto(0, 0)
        self.move_speed = INITIAL_MOVE_SPEED
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED