from turtle import Screen, Turtle


POSITIONS_LEFT = [(-270, 20), (-270, 0), (-270, -20)]
POSITIONS_RIGHT = [(-270, 20), (-270, 0), (-270, -20)]


class Paddle(Turtle):

    def __init__(self, x_pos=350):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
