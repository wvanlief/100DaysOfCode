from turtle import Screen, Turtle
import time

POSITIONS = [(0, 0), (0, -20), (0, -40)]


class Snake:
    def __init__(self):
        self.snakes = []
        self.length = 3
        self.x_start = 0
        self.y_start = 0
        self.create_snake()
        self.move_dist = 20
        self.head = self.snakes[0]

    def create_snake(self, length=3, x_start=0, y_start=0):
        for pos in POSITIONS:
            self.add_segment(pos)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.snakes.append(new_segment)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            self.snakes[snake_num].goto(self.snakes[snake_num - 1].xcor(), self.snakes[snake_num - 1].ycor())
        self.snakes[0].forward(self.move_dist)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)
        else:
            pass

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)
        else:
            pass

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)
        else:
            pass

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)
        else:
            pass
