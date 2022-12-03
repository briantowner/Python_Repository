import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.backwards, "Down")

refresh_time = .1
game_is_on = True

while game_is_on:
    time.sleep(refresh_time)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
    # Detect if player make it to other side
    if player.ycor() == 300:
        player.reset()
        scoreboard.refresh()
        refresh_time *= .5

scoreboard.game_over()
screen.exitonclick()
