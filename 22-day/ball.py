from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")

    def move(self):
        x_cor = self.xcor() + 10
        y_cor = self.ycor() + 10
        self.goto(x_cor, y_cor)
