from turtle import Turtle,Screen
import turtle

baby = Turtle()
baby.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple", "black"]
# 점선그리기
# for i in range(10): 
#     baby.pendown()
#     baby.forward(10)
#     baby.penup()
#     baby.forward(10)
def cal_angle(num_of_sides):
    angle = 360 / int(num_of_sides)
    return angle

def figure(num_of_sides):
    baby.color(colors[num_of_sides-3])
    for i in range(num_of_sides):
        baby.forward(100)
        baby.right(cal_angle(num_of_sides))
    
for i in range(3,11):
    figure(i)

turtle.exitonclick()