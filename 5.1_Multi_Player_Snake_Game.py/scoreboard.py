# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, game_mode=1):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.game_mode = game_mode
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        if self.game_mode == 1:
            self.goto(0, 270)
            self.write(f'Score: {self.score1}', align='center', font=('Arial', 24, 'bold'))
        else:
            self.goto(-200, 270)
            self.write(f'P1: {self.score1}', align='center', font=('Arial', 24, 'bold'))
            self.goto(200, 270)
            self.write(f'P2: {self.score2}', align='center', font=('Arial', 24, 'bold'))
        
    def game_over(self, message="Game Over"):
        self.goto(0, 0)
        self.write(message, align='center', font=('Arial', 24, 'bold'))      
        
    def increase_score(self, player=1):
        if player == 1:
            self.score1 += 1
        else:
            self.score2 += 1
        self.update_scoreboard()