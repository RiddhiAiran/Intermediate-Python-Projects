# snake.py
from turtle import Turtle
import time

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0.1
        self.is_paused = False
        
    def create_snake(self):
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0.1
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        # Increase speed slightly with each food eaten
        self.speed = max(0.05, self.speed * 0.95)
        
    def move(self):
        if not self.is_paused:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(20)
            
    def toggle_pause(self):
        self.is_paused = not self.is_paused
        
    def up(self):
        if self.head.heading() != 270 and not self.is_paused:
            self.head.setheading(90)
            
    def down(self):
        if self.head.heading() != 90 and not self.is_paused:
            self.head.setheading(270)
            
    def left(self):
        if self.head.heading() != 0 and not self.is_paused:
            self.head.setheading(180)
            
    def right(self):
        if self.head.heading() != 180 and not self.is_paused:
            self.head.setheading(0)