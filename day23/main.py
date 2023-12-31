import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Tạo đối tượng rùa


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
turtle = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=turtle.go_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Kiểm tra rùa vi phạm với xe
    for car in car_manager.all_card:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Kiểm tra rùa đã tới đích chưa
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()
