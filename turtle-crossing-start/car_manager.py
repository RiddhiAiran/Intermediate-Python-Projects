from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

# Generate all the random cars
class CarManager():
    def __init__(self):
        self.cars_collection = []
        self.carspeed = STARTING_MOVE_DISTANCE
    
    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-230,230)
            new_car.goto(300,random_y)
            self.cars_collection.append(new_car)
        
    def move_car(self):
        for car in self.cars_collection:
            car.backward(self.carspeed)
        
    def increase_speed(self):
        """Increase the speed of all cars"""
        self.carspeed += MOVE_INCREMENT
