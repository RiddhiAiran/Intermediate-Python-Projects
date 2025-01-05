# scoreboard.py
from turtle import Turtle
import json
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        # Create a separate turtle for game over message
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.penup()
        self.game_over_turtle.color("white")
        self.update_scoreboard()
        
    def load_highscore(self):
        try:
            with open("highscore.json", "r") as file:
                return json.load(file)["highscore"]
        except:
            return 0
            
    def save_highscore(self):
        with open("highscore.json", "w") as file:
            json.dump({"highscore": self.highscore}, file)
            
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)  # Ensure score stays at top
        self.write(f"Score: {self.score} High Score: {self.highscore}", 
                  align="center", font=("Courier", 24, "normal"))
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.game_over_turtle.clear()  # Clear game over message
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.game_over_turtle.goto(0, 0)
        self.game_over_turtle.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
