from random import randint
import turtle

t = turtle.Turtle()

for _ in range(100):
    t.left(randint(0, 360))
    t.forward(randint(15, 60))
