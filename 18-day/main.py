# Day 18 - Hirst Paint Projects
# Using Python Turtle for further understanding of OOP and learning tuples

import random
import turtle as t

color_tup_list = [
    (199, 175, 117),
    (125, 36, 24),
    (187, 158, 51),
    (170, 104, 56),
    (5, 57, 83),
    (200, 216, 204),
    (108, 67, 85),
    (39, 36, 35),
    (86, 142, 59),
    (20, 122, 176),
    (110, 161, 175),
    (75, 39, 47),
    (9, 67, 47),
    (64, 153, 137),
    (133, 41, 43),
    (184, 98, 80),
    (179, 201, 186),
    (209, 200, 115),
    (179, 174, 177),
    (151, 176, 165),
    (93, 142, 156),
    (28, 80, 59),
]
pos_x = -228
pos_y = -225
screen = t.Screen()
screen.setup(500, 500)
t.colormode(255)

brush = t.Turtle()
brush.speed("fastest")
brush.penup()
brush.hideturtle()

def draw_row():
    for i in range(10):
        color = random.choice(color_tup_list)
        brush.dot(20, color)
        brush.forward(50)

for i in range(10):
    brush.teleport(pos_x, pos_y)
    pos_y += 50
    draw_row()


screen.exitonclick()
