# Day 25 - US States Game
# Using pandas to create a game to study US states
# requirment: python pandas

import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_pen = turtle.Turtle()
state_pen.penup()
state_pen.hideturtle()

df = pandas.read_csv("50_states.csv")
score = 0
correct_guess = []
answer_state = screen.textinput(title=f"Guess the State", prompt="What's a state's name?").title()
while score < 50:
    if answer_state == "Exit":
        missed_states = df[~df.state.isin(correct_guess)].state
        missed_states.to_csv('missed_states.csv')
        break
    if answer_state in df.state.values and answer_state not in correct_guess:
        x_state = df[df.state == answer_state].x.item()
        y_state = df[df.state == answer_state].y.item()
        state_pen.goto(x_state, y_state)
        state_pen.write(answer_state,  align="center")
        score += 1
        correct_guess.append(answer_state)
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
