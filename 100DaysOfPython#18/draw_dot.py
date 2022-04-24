###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
from turtle import Turtle, Screen
import turtle
import random
# rgb_colors = []

# colors = colorgram.extract('/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#17/image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tupled_color = (r,g,b)
#     rgb_colors.append(tupled_color)    

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
baby_turtle = Turtle()
turtle.colormode(255)
baby_turtle.penup()
baby_turtle.hideturtle()
baby_turtle.setheading(225)
baby_turtle.forward(300)
baby_turtle.setheading(0)
def move_one_line():
    for i in range(10):
        rand_color = color_list[random.randint(0,29)]
        baby_turtle.dot(20,rand_color)
        baby_turtle.forward(50)
def turn_left():
    baby_turtle.left(90)
    rand_color = color_list[random.randint(0,29)]
    baby_turtle.dot(20,rand_color)
    baby_turtle.forward(50)
    baby_turtle.left(90)
    
def turn_right():
    baby_turtle.right(90)
    rand_color = color_list[random.randint(0,29)]
    baby_turtle.dot(20,rand_color)
    baby_turtle.forward(50)
    baby_turtle.right(90)

for i in range(4):
    move_one_line()
    turn_left()
    move_one_line()
    turn_right()
move_one_line()
turn_left()
move_one_line() 
rand_color = color_list[random.randint(0,29)]
baby_turtle.dot(20,rand_color)

turtle.exitonclick()