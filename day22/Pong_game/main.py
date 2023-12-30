from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

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
ball = Ball()
score = ScoreBoard()
speed = 1
# Lắng nghe sự kiện
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Bật ngược lại khi bóng chạm tường
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Kiểm tra chạm với paddle phải, trái
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or (
        ball.distance(paddle_left) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()
    # Kiểm tra bóng không va chạm với paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
