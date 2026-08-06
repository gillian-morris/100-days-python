# Day 22 - Pong
# The classic Pong game programmed with Python

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.pace)
    ball.move()

    # Detect bounce off of wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # Detect bounce off of paddles
    if (
        ball.xcor() > 320
        and ball.distance(r_paddle) < 50
        or ball.xcor() < -320
        and ball.distance(l_paddle) < 50
    ):
        ball.bounce_x()
        ball.increase_speed()

    # Detect game point
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_posiion()
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_posiion()


screen.exitonclick()
