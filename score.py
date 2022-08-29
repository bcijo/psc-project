from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.goto(0, 260)
        self.write("Scoreboard", align="center", font=("Algerian", 40, "normal"))
        self.goto(-100, 220)
        self.write(self.lscore, align="center", font=("Currier", 30, "normal"))
        self.goto(100, 220)
        self.write(self.rscore, align="center", font=("Currier", 30, "normal"))

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write("Scoreboard", align="center", font=("Algerian", 40, "normal"))
        self.goto(-100, 220)
        self.write(self.lscore, align="center", font=("Currier", 30, "normal"))
        self.goto(100, 220)
        self.write(self.rscore, align="center", font=("Currier", 30, "normal"))

