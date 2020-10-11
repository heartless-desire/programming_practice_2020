import turtle


def rect(n, d):
    a = 360 // n
    b = 90 + a / 2
    t.left(b)
    for _ in range(n):
        t.forward(d)
        t.left(360/n)
    t.penup()
    t.right(b)
    t.forward(d/8)
    t.pendown()


t = turtle.Turtle()
t.shape('turtle')
s = 30

for i in range(3, 14):
    rect(i, s)
    s += s/i**2.5

