from turtle import Turtle, Screen
import random
tim = Turtle()
color = [
    "light cyan",
]


def draw_shape(number_side):
    angle = 360 / number_side
    for _ in range(number_side):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(5, 11):
    tim.color( "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)]))
    draw_shape(shape_side_n)
draw_shape(5)
screen = Screen()
screen.exitonclick()
