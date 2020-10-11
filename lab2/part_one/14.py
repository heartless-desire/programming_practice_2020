import turtle

t = turtle.Turtle()
n = int(input())


def do_star(k):
    t.left(180 - (180 / k))
    t.forward(200)


for i in range(n):
    do_star(n)

