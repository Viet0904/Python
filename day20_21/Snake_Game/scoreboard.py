from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game over", font=FONT, align=ALIGMENT)

    def update_score(self):
        self.write(f"Score = {self.score}", font=FONT, align=ALIGMENT)

    def Increase_Score(self):
        self.score += 1
        self.clear()
