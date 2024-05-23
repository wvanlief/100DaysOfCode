from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.write(f"Level = {self.score}", False, align="center", font=("Impact", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Impact", 35, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
