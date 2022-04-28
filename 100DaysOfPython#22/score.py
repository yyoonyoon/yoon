from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-100,200)
        self.write(self.l_score,\
            move= False, align= 'center', font=('Courier',80,'normal'))
        self.goto(100,200)
        self.write(self.r_score,\
            move= False, align= 'center', font=('Courier',80,'normal'))

    def l_get_score(self):
        self.clear()
        self.l_score += 1
        self.update_score()
    def r_get_score(self):
        self.clear()
        self.r_score += 1
        self.update_score()