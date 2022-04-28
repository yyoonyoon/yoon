from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_position, y_position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x_position, y_position)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        if self.ycor() > 270:
            self.goto(self.xcor(), 270)
    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
        if self.ycor() < -270:
            self.goto(self.xcor(), -270)