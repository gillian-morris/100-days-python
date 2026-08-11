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
        self.h_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.get_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score: {self.score}     High Score: {self.h_score}",
            align=ALIGNMENT,
            font=(FONT, FONT_SIZE, FONT_TYPE),
        )

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.update_high_score()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def get_high_score(self):
        try:
            with open("high-score.txt", "r") as f:
                self.h_score = int(f.readline())
        except FileNotFoundError:
            pass

    def update_high_score(self):
        if self.h_score <= self.score:
            with open("high-score.txt", "w") as f:
                f.write(f"{self.score}")
