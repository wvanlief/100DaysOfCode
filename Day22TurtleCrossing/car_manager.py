from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 1
        self.max_chance = 6

    def create_car(self):
        random_chance = randint(1, self.max_chance)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            new_car.setheading(180)
            new_car.speed(self.car_speed)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)

    def increase_level(self):
        self.car_speed += 1
        self.max_chance -= randint(0, 1)




