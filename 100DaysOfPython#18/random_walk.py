from turtle import Turtle,Screen
import turtle
import random

baby = Turtle()
baby.shape("turtle")
heading = [0, 90, 180, 270]
baby.pensize(5)
baby.speed(10)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

while True:
    baby.color(random_color())
    baby.forward(10)
    baby.right(random.choice(heading))


turtle.exitonclick()