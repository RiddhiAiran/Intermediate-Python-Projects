# scoreboard.py
from turtle import Turtle
from constants import SCORE_POSITION_Y, SCORE_POSITION_X

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self._write_score(-SCORE_POSITION_X, self.l_score)
        self._write_score(SCORE_POSITION_X, self.r_score)
        
    def _write_score(self, x_pos, score):
        """Helper method to write individual scores"""
        self.goto(x_pos, SCORE_POSITION_Y)
        self.write(score, align='center', font=('Courier', 80, 'normal'))
        
    def point(self, player):
        """Update score for specified player"""
        if player == 'left':
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        winner = "LEFT" if self.l_score > self.r_score else "RIGHT"
        self.write(f"GAME OVER! {winner} PLAYER WINS!", align='center', font=('Courier', 24, 'normal'))
