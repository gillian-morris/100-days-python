from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1,5)
        self.color("white")
        self.goto(starting_pos)
        self.setheading(90)


    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
