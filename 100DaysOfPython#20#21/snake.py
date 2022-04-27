from tkinter import LEFT, RIGHT
from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]
        
    def create_snake(self):
        for i in range(3):
            new_snake = Turtle(shape= "square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(STARTING_POSITIONS[i])
            self.all_snakes.append(new_snake)
    
    def move(self):
        for num in range(len(self.all_snakes)-1, 0, -1):
            new_x = self.all_snakes[num -1].xcor()
            new_y = self.all_snakes[num -1].ycor()
            self.all_snakes[num].goto(new_x, new_y)
        self.all_snakes[0].forward(MOVE_DISTANCES)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_tail(self):
        new_snake = Turtle(shape= "square")
        new_snake.color("white")
        new_snake.penup()
        xposition_of_tail = self.all_snakes[len(self.all_snakes)-1].xcor()
        yposition_of_tail = self.all_snakes[len(self.all_snakes)-1].ycor()
        new_snake.goto(xposition_of_tail, yposition_of_tail)
        self.all_snakes.append(new_snake)