import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")

player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >= 280: # level success
        cars.level_up()
        score.plus_level()
        score.update_scoreboard()
        player.reset()
    cars.generate()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()