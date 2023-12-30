from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
paddle_right = Paddle(0)
paddle_left = Paddle(1)
PongA = Turtle()
ball = Ball()
PongA.color("white")
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
while True:
    screen.update()
screen.exitonclick()
