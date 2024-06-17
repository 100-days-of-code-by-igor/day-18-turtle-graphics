#####Turtle Intro######

import turtle
import random

t = turtle.Turtle()

t.shape("turtle")
t.color("black")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


######## Challenge 1 - Draw a Square ############
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

### Challenge 2 - dashed line
# for _ in range(10):
#     t.forward(5)
#     t.penup()
#     t.forward(5)
#     t.pendown()
#
# screen = Screen()
# screen.exitonclick()

### Challenge 3 - drawing figures


### Challenge 3 - drawing figures
#
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "gold",
    "cyan",
    "magenta",
    "lime green",
    "dark khaki",
    "navy"
]
#
# angles = range(3,11)
# for angle in angles:
#     t.color(random.choice(colors))
#     degree = 360/angle
#     degree_sum = degree
#     for _ in range(angle):
#         t.forward(100)
#         t.setheading(degree_sum)
#         degree_sum += degree
#
# screen = Screen()
# screen.exitonclick()

# Challenge 4 - Random Walk

t.pensize(1)
t.shape()
t.speed(10000000)

# current_position = 0
# number_of_steps = 100
# directions = [0, 90, 180, 270]
# for _ in range(number_of_steps):
#     t.color(random_color())
#     t.setheading(random.choice(directions))
#     t.forward(30)
#
# screen = turtle.Screen()
# screen.exitonclick()

for _ in range(1000):
    t.color(random_color())
    t.circle(100)
    t.left(10)

screen = turtle.Screen()
screen.exitonclick()