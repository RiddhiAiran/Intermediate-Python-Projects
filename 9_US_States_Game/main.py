# Inspired by : https://www.sporcle.com/games/g/states
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = './9_US_States_Game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('./9_US_States_Game/50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter State:").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state,font=('Arial',10,'bold'))


# To generate your own coordinates for any other maps
# def get_mouseclick_cor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouseclick_cor)