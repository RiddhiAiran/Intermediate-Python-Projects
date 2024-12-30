import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up',fun=player.move_up)

time.sleep(3)

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    cars.generate_car()
    cars.move_car()
    # Detect collision
    for car in cars.cars_collection:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()
    
    cars.cars_collection = [car for car in cars.cars_collection if car.xcor() > -320]
    
    # Detect crossing of turtle without hitting any car
    if player.finish_line():
        player.to_start()
        cars.increase_speed()
        scoreboard.increase_score()
    
screen.exitonclick()