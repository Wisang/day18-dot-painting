import turtle
from turtle import Turtle, Screen, colormode
from colors import color_list
# import colorgram
import random
import colorgram

colors = colorgram.extract("spot_painting.jpg", 30)

t = Turtle()
turtle.colormode(255)
t.penup()
t.hideturtle()

for y in range(10):
    for x in range(10):
        t.goto(-100 + 20*x, -100 + 20*y)
        color = random.choice(color_list)
        t.pencolor(color)
        t.dot(10)


screen = Screen()
screen.screensize(2000, 3000)
screen.exitonclick()