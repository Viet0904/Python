from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positon):
        super().__init__()
        self.create_paddle(positon)

    def create_paddle(self, position):
        self = Turtle(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
