import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write_turtle = Turtle()
write_turtle.penup()
write_turtle.color("black")
write_turtle.hideturtle()

data = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/us-states-game-start/50_states.csv")
# data_dict = data.to_dict()
state_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()
score = 0
correct_answers = []

while score < 50:
    user_answer = screen.textinput(title= f"{score}/50 States Correct",\
        prompt="What's another state's name?").title()
    if user_answer == "Exit":
        break
    if user_answer in state_list:
        score += 1
        correct_answers.append(user_answer)
        x_postition = x_list[state_list.index(user_answer)]
        y_postition = y_list[state_list.index(user_answer)]
        write_turtle.goto(x_postition,y_postition)
        write_turtle.write(f"{user_answer}",font=('Arial',10,'normal'))
    if score == 50:
        write_turtle.goto(0,0)
        write_turtle.write("You win!",align="center",font=('Arial',30,'normal'))
        break

with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/\
us-states-game-start/should_memorize.csv",mode='w') as should_mem:
    mem_list = [x for x in state_list if x not in correct_answers]
    new_data = pandas.DataFrame(mem_list)
    new_data.to_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/us-states-game-start/should_memorize.csv")