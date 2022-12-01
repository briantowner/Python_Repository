from colorgram import extract
import turtle
import random


tim = turtle.Turtle()

colors = color_extract = extract('image.jpg', 10)


def new_line():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb.append(new_color)


tim.ht()
tim.penup()
tim.setposition(x=-200, y=- 200)
tim.shape("circle")
tim.speed("fastest")
turtle.colormode(255)

for _ in range(10):
    for _ in range(10):
        rand_color = random.choice(rgb)
        tim.color(rand_color)
        tim.stamp()
        tim.forward(50)
    new_line()

turtle.exitonclick()
