from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", 'r') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} - High Score: {self.high_score}", False, align="center", font=("Impact", 15, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Impact", 35, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



