import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        self.game_is_on = True
        self.setup_controls()

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.title("Turtle Crossing")
        self.screen.tracer(0)

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.player.go_up, "Up")

    def run_game(self):
        while self.game_is_on:
            time.sleep(0.1)
            self.screen.update()

            self.car_manager.create_car()
            self.car_manager.move_cars()

            # Detect collision with car
            for car in self.car_manager.all_cars:
                if car.distance(self.player) < 20:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    break

            # Detect successful crossing
            if self.player.is_at_finish_line():
                self.player.go_to_start()
                self.car_manager.level_up()
                self.scoreboard.increase_level()

        self.screen.exitonclick()

if __name__ == "__main__":
    game = Game()
    game.run_game()