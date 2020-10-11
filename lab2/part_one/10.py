import turtle

t = turtle.Turtle()


def circle(angle):
    for i in range(360):
        t.forward(1)
        t.left(angle)


for j in range(1, 3):
    for i in range(1, 3):
        circle((-1)**(i+1))
    t.left(120)