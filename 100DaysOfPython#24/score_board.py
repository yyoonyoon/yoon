from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#24/score_data.txt",\
        mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,280)
        self.write("Current Score: {}, High Score: {}".format(self.score,self.high_score), move= False, align= 'center',\
            font=('Arial',15,'normal'))
    
    def get_point(self):
        self.clear()
        self.score += 1
        self.write("Current Score: {}, High Score: {}".format(self.score, self.high_score), move= False, align= 'center',\
            font=('Arial',15,'normal'))
    
    def reset_game(self):
        if (self.score > self.high_score):
            self.high_score = self.score
            with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#24/score_data.txt",\
            mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write("Current Score: {}, High Score: {}".format(self.score, self.high_score), move= False, align= 'center',\
        font=('Arial',15,'normal'))