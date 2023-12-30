from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
game_is_on = True
screen.onkey(
    snake.up,
    "Up",
)
screen.onkey(
    snake.down,
    "Down",
)
screen.onkey(
    snake.left,
    "Left",
)
screen.onkey(snake.right, "Right")
food = Food()
score = ScoreBoard()

while game_is_on:
    score.update_score()
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Ktra ăn được thức ăn hay chưa
    if snake.head.distance(food) < 15:
        food.refesh()
        snake.extend()
        score.Increase_Score()
    # kiểm tra qua chạm với tường
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        score.game_over()
        game_is_on = False
    # Đầu chạm vào thânx
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False


screen.exitonclick()
