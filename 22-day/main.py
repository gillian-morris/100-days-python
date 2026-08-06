# Day 22 - Pong
# The classic Pong game programmed with Python

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()


screen.exitonclick()
