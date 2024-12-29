from turtle import Turtle, Screen
import time

# Steps for the Snake Game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


# 1. Create a Snake Body (creating 3 squares on the screen next to each other)

positions = [(0,0),(-20,0),(-40,0)]

snake = []
for position in positions:
    segment = Turtle("square")
    segment.color('white')
    segment.penup()
    segment.goto(position)
    snake.append(segment)
    
screen.update()



# Method 2 
# snake1 = Turtle(shape="square")
# snake1.color('white')

# snake2 = Turtle(shape="square")
# snake2.color('white')
# snake2.goto(-20,0)

# snake3 = Turtle(shape="square")
# snake3.color('white')
# snake3.goto(-40,0)

# Method - 3 (Best)
# snake1 = [Turtle('square') for _ in range(0,3)]
# for i, segment in enumerate(snake1):
#     segment.color('white')
#     segment.penup()
#     segment.goto(positions[i])

# 2. Move the Snake (Continue to move forward)
game = True
while game:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(snake)-1,0,-1):
        new_x = snake[seg-1].xcor()
        new_y = snake[seg-1].ycor()
        snake[seg].goto(new_x,new_y)
    snake[0].forward(20)

    

    
# 3. Control the Snake (Control the direction of the snake - Up, Down, Left, Right Arrow keys)



# 4. Detect Collision with food (Put the ranadom food on the screen and detect the food contact , new food creation , add snake length)

# 5. Create a Score board (write text, score addition)

# 6. Detect Collion with wall (Detect the collision, show game over text, no movement of snake)

# 7. Detect Collion with the Tail (head hit any part of the body of the snake, then again game over)




screen.exitonclick()