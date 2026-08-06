import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        t = Turtle()
        t.shape("square")
        t.shapesize(1, 2)
        t.penup()
        t.setheading(180)
        car_color = random.choice(COLORS)
        t.color(car_color)
        y_axis = random.randint(-250, 250)
        t.goto(300, y_axis)
        self.cars.append(t)

    def generate_cars(self):
        car_gen = random.randint(1, 6)
        if car_gen == 1:
            self.generate_car()

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def car_collision(self, player_pos):
        for car in self.cars:
            if car.distance(player_pos) < 20:
                return True
