from turtle import Turtle
from turtle import Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Level: {}".format(self.level), align="left", font= FONT)

    def plus_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-60,0)
        self.write("GAME OVER", align="left", font= FONT)