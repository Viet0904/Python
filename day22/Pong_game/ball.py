from turtle import Turtle


class Ball(Turtle):
    def __init_(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.dot(size=20, color="white")
        self.penup()
        self.goto((0, 0))
