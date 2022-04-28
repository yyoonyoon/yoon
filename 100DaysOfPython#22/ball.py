from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if (new_x > 350 and new_y > 250):
            self.goto(350,250)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def bounce_y(self):
        self.y_move *= -1
    
    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1
        self.move_speed = 0.1