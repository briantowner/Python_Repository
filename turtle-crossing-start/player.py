from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.color('black')
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def backwards(self):
        self.backward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
