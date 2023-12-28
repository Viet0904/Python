import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape(name="turtle")
tim.pensize(15)
direction = [0, 90, 180, 270, 360]


def random_color():
    list = []
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


def random_walk(steps):
    for turtle_speed in range(steps):
        tim.speed(turtle_speed)
        tim.color(random_color())
        tim.forward(random.randint(20, 50))
        tim.right(random.choice(direction))

    tim.done()


random_walk(100)
