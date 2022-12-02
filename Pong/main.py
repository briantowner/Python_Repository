from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Towner's Pong Masterpiece")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
sleep_time = .1
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle()
        sleep_time *= .9

    if ball.xcor() > 400:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.goto(0, 0)
        ball.paddle()
        sleep_time = .1

    if ball.xcor() < -400:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.goto(0, 0)
        ball.paddle()
        sleep_time = .1


screen.exitonclick()

