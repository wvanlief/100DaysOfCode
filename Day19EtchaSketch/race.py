from turtle import Turtle, Screen
from random import randint

#tim = Turtle()
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color: ")
colors = ["red", "orange", "yellow", "black", "blue", "green"]
all_turtles = []

if user_bet:
    is_race_on = True

#def new_turtles(colors):

x_start = -230
y_start = -100
i = 0

for _ in colors:
    new_t = Turtle(shape="turtle")
    new_t.color(_)
    new_t.speed(10)
    new_t.penup()
    new_t.goto(x=x_start, y=y_start)
    all_turtles.append(new_t)
    y_start += 40

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(f"{turtle.pencolor()} won!")
            if turtle.pencolor() == user_bet:
                print("You won!")
            else:
                print("You lost")
        r_dist = randint(0, 10)
        turtle.forward(r_dist)



screen.exitonclick()
