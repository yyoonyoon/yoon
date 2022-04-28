from turtle import Turtle, Screen, width
import turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong Game")
player1 = Paddle(-350, 0)
player2 = Paddle(350, 0)
ball = Ball()
game_is_on = True
score = Score()

screen.listen()
screen.onkey(player1.up,"w")
screen.onkey(player1.down,"s")
screen.onkey(player2.up,"Up")
screen.onkey(player2.down,"Down")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if (ball.ycor() >= 280 or ball.ycor() <= -280): # is ball hit with the wall?
        ball.bounce_y()
    if (ball.distance(player2) < 50 and ball.xcor() > 330) or \
        (ball.distance(player1) < 50 and ball.xcor() < -330): # is ball hit with player?
        ball.bounce_x()
    if (ball.xcor() > 380 or ball.xcor() < -380):
        if ball.xcor() > 380:
            ball.reset_position()
            score.l_get_score()
        elif ball.xcor() < -380:
            ball.reset_position()
            score.r_get_score()

screen.exitonclick()