# snake.py
from turtle import Turtle

class Snake:
    def __init__(self, start_pos=(0,0), color='white'):
        self.segments = []
        self.color = color
        self.start_pos = start_pos
        self.move_distance = 20
        self.create_snake()
        self.head = self.segments[0]
        self.is_boosting = False
        
    def create_snake(self):
        x, y = self.start_pos
        positions = [(x, y), (x-20, y), (x-40, y)]
        for position in positions:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        distance = self.move_distance * 1.5 if self.is_boosting else self.move_distance
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(distance)
        self.is_boosting = False
            
    def boost_speed(self):
        self.is_boosting = True

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
       
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)