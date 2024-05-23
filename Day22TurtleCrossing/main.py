import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()
    carManager.move_cars()

    # Detect car collision
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        else: pass

    # Detect end of level
    if player.ycor() > 270:
        player.goto(STARTING_POSITION)
        scoreboard.increase_score()
        scoreboard.update_score()
        carManager.increase_level()



screen.exitonclick()