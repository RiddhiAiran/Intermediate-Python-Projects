from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars[:]:  # Create a copy of the list for iteration
            car.backward(self.car_speed)
            # Remove cars that are off screen
            if car.xcor() < -320:
                self.all_cars.remove(car)
                car.hideturtle()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def clear_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
