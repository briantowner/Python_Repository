from turtle import Turtle
import random

STARTING_ANGLE = random.randint(0, 360)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(STARTING_ANGLE)

    def move(self):
        self.forward(20)

    def rebound(self):
        current_heading = self.heading()
        new_heading = -current_heading
        self.setheading(new_heading)

    def paddle(self):
        current_heading = self.heading()
        new_heading = current_heading+(180-90-current_heading)*2
        self.setheading(new_heading)



