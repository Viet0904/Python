from turtle import Turtle, Screen

tim = Turtle()
angle = 360 / 5
for _ in range(5):
    tim.forward(100)
    tim.right(angle)
    tim.forward(100)
    tim.left(2 * angle)


screen = Screen()
screen.exitonclick()
