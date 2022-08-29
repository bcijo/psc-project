from turtle import Turtle


class Paddle:
    def __init__(self, side):
        self.side = side
        print(self.side)
        if self.side == "right":
            xcor = 360
        else:
            xcor = -366
        self.paddy = Turtle("square")
        self.paddy.shapesize(stretch_wid=5, stretch_len=1)
        self.paddy.color("blue")
        self.paddy.speed("slow")
        self.paddy.penup()
        self.paddy.setpos(x=xcor, y=0)

    def up(self):
        x = self.paddy.xcor()
        y = self.paddy.ycor()
        self.paddy.setpos(x=x, y=(y + 20))

    def down(self):
        x = self.paddy.xcor()
        y = self.paddy.ycor()
        self.paddy.goto(x=x, y=(y - 20))
