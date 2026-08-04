# Day 19 - Turtle Racing
# Practicing more turtle racing. Working with multple instances of an object.

import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
y_axis = -100
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-225, y=y_axis)
    y_axis += 40
    turtle_list.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

screen.exitonclick()
