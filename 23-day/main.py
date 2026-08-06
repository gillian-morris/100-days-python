# Day 23 - Turtle Crossing
# A turtle's take on the classic frogger game

import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_cars()
    car.move()
    if car.car_collision(player.position()):
        scoreboard.game_over()
        game_is_on = False

    if player.next_level():
        player.start_position()
        car.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
