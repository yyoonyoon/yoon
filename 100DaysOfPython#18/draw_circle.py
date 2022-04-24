from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
baby_turtle = Turtle()
baby_turtle.speed(200)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

while 1:
    baby_turtle.color(rand_color())
    baby_turtle.circle(100)
    baby_turtle.left(3)

turtle.exitonclick()