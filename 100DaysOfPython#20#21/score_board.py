from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,280)
        self.write("Current Score: {}".format(self.score), move= False, align= 'center',\
            font=('Arial',15,'normal'))
    
    def get_point(self):
        self.clear()
        self.score += 1
        self.write("Current Score: {}".format(self.score), move= False, align= 'center',\
            font=('Arial',15,'normal'))
    
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.write("GAME OVER", move= False, align= 'center',\
            font=('Arial',30,'normal'))