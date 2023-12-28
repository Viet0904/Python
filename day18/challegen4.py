import turtle as t
import random

tim = t.Turtle()
tim.shape(name="turtle")
tim.pensize(15)
direction = [0, 90, 180, 270, 360]
########### Challenge 4 - Random Walk ########
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
        tim.color(random.choice(colours))
        # Di chuyển về phía trước một khoảng cách ngẫu nhiên
        tim.forward(random.randint(20, 50))
        # Quay một góc ngẫu nhiên từ -180 đến 180 độ
        tim.right(random.choice(direction))

    tim.done()


# Gọi hàm để thực hiện random walk với số bước là 100
random_walk(100)
