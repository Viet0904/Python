from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
# Thiết lập độ rộng và cao màn hình
screen.setup(width=800, height=600)
# Đặt màu nền
screen.bgcolor("black")
# Đặt tiêu đề
screen.title("Pong Game")
#  Tắt hoạt ảnh
screen.tracer(0)
#  Lắng nghe
screen.listen()

# Tạo các đối tượng
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
# ball = Ball()

# Lắng nghe sự kiện
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()
