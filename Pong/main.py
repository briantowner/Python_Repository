from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Towner's Pong Masterpiece")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound()
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 60) or (ball.distance(l_paddle) < 60 and ball.xcor() < -340):
        ball.paddle()
        print(ball.heading())

screen.exitonclick()

