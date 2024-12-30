from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

# The level and score board + Game over Sequence
# 5. Create a level board (write text, level addition)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-230,230)
        self.hideturtle()
        self.update_level()
    
    def update_level(self):
        self.write(f'Level: {self.level}', align = ALIGNMENT,font= FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align = ALIGNMENT,font= FONT)      
        
    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_level()
                
         
        