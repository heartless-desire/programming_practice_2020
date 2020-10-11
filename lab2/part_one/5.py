import turtle


def new_square(d):
    turtle.penup()
    for _ in range(2):
        turtle.right(90)
        turtle.forward(d)
    turtle.right(180)
    turtle.pendown()


turtle.shape('turtle')
global k
k = 10
d_adder = 5


for _ in range(1, k+1):
    for _ in range(4):
        turtle.forward(k)
        turtle.left(90)
    new_square(d_adder)
    k += d_adder * 2