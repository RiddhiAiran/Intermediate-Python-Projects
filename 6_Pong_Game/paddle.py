# paddle.py
from turtle import Turtle
from constants import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=PADDLE_WIDTH, stretch_wid=PADDLE_HEIGHT)
        self.penup()
        self.goto(position)
        
    def move(self, direction):
        """Move paddle up or down"""
        new_y = self.ycor() + (PADDLE_SPEED * direction)
        # Prevent paddle from going off screen
        if abs(new_y) < (300 - PADDLE_HEIGHT * 10):
            self.goto(self.xcor(), new_y)
        
    def up(self):
        self.move(1)
        
    def down(self):
        self.move(-1)
