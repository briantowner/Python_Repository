from turtle import Turtle

FONT = ("Courier", 24, "normal")
NEW_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.goto(x=-250, y=250)
        self.write(f"LEVEL: {self.level}", move=False, align='left', font=FONT)

    def refresh(self):
        self.clear()
        self.level += 1
        self.ht()
        self.penup()
        self.goto(x=-250, y=250)
        self.write(f"LEVEL: {self.level}", move=False, align='left', font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", move=False, align='center', font=NEW_FONT)