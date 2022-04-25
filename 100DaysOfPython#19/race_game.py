from turtle import Turtle, Screen
import turtle
import random
tim = Turtle()
tim.hideturtle()
screen = Screen()
is_race_on = False
all_turtles = []
y_positions = [125, 75, 25, -25, -75, -125]
screen.setup(width= 500,height = 400)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0, 6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(6):
        all_turtles[i].forward(random.randint(0,10))

    for each_turtle in all_turtles:
        if (each_turtle.xcor() > 230):
            winner = each_turtle.pencolor()
            if winner == user_bet:
                print("The winner is {}!!! You've got money!!!".format(winner))
            else:
                print("The winner is {}!!! You've loose money!!!".format(winner))
            is_race_on = False
            break


screen.exitonclick()