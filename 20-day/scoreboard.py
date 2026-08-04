from turtle import Turtle

ALIGNMENNT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE)
        )

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
