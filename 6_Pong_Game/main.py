from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("The Pong Game")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up',fun=r_paddle.up)
screen.onkey(key='Down',fun=r_paddle.down)
screen.onkey(key='w',fun=l_paddle.up)
screen.onkey(key='s',fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounch_y()
        
    # Detect the collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounch_x()
    
    # Detect R paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect L paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()