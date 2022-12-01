from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.sety(255)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.ht()
        self.penup()
        self.sety(255)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("white")
        self.ht()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
