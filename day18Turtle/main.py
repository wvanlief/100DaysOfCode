from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

# timmy.forward(30)
# timmy.right(90)
# timmy.forward(30)
# timmy.right(180)
# timmy.forward(30)
# timmy.right(270)
# timmy.forward(30)
# timmy.right(360)
# timmy.forward(30)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# angle = 360
#
# for side in range(3, 12):
#     for _ in range(side):
#         timmy.forward(100)
#         timmy.left(angle/side)

timmy.speed(0)
timmy.width(5)
# for i in range(150):
#     timmy.color(random.choice(["red","black","blue","orange","brown"]))
#     timmy.setheading(random.choice([0,90,180,270]))
#     timmy.forward(30)

for i in range(35):
    timmy.color(random.choice(["red", "black", "blue", "orange", "brown"]))
    timmy.circle(100)
    timmy.right(360-5*i)





















screen = Screen()
screen.exitonclick()
