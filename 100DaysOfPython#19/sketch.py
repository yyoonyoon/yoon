from turtle import Turtle, Screen
import turtle
tim = Turtle()
screen = Screen()
def turn_left():
    tim.setheading(tim.heading() + 10)
def turn_right():
    tim.setheading(tim.heading() - 10)
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
turtle.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(tim.reset, "c")
screen.listen()






# Screen.clearscreen()
turtle.exitonclick()