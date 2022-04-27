from turtle import Screen, Turtle, shapesize
import turtle
import time
from snake import Snake
from food import Food
from score_board import Score_board

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score_board()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.get_point()
        snake.add_tail()
    if (snake.head.xcor() > 295 or snake.head.xcor() < -300):
        game_is_on = False
        score_board.game_over()
    elif (snake.head.ycor() > 300 or snake.head.ycor() < -295):
        game_is_on = False
        score_board.game_over()
    for each_snake in snake.all_snakes[1:]:
        if snake.head.distance(each_snake) < 10:
            game_is_on = False
            score_board.game_over()

        

# def add_snake(num_of_snake):
#     for i in range(num_of_snake):
#         new_snake = Turtle(shape= "squre")
#         new_snake.penup()
#         new_snake.color("white")
#         all_snakes.append(new_snake)










screen.exitonclick()