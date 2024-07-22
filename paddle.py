from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
