import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
color_list = [
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209),
]
tim.speed("fastest")
x = tim.xcor()
y = tim.ycor()
print(x)
print(y)
for i in range(10):
    tim.setpos((x, y))
    tim.pendown()
    for j in range(10):
        tim.color(random.choice(color_list))
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
        y += 5


screen = Screen()
screen.exitonclick()
