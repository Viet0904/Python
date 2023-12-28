from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
print(user_bet)
colors = ["red", "green", "blue", "purple", "yellow", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[index])
    tim.goto(x=-230, y=y_position[index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

winner = ""
while is_race_on:
    for object in all_turtle:
        if object.xcor() > 230:
            is_race_on = False
            winner = object.pencolor()
            if winner == user_bet:
                print(f"You've won! the {winner} turtle is the winner!")
            else:
                print(f"You've lost! the {winner} turtle is the winner")
        random_dinstace = random.randint(0, 10)
        object.forward(random_dinstace)


screen.exitonclick()
