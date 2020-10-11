import turtle

t = turtle.Turtle()


def circle(rad, arc=None):
    if arc is not None:
        iterat = 18
        fi = -10
    else:
        iterat = 36
        fi = 10
    for i in range(iterat):
        t.left(fi)
        t.forward(rad)


t.begin_fill()
circle(20)
t.color('yellow')
t.end_fill()
t.color('black')
t.penup()
# right eye
t.goto(50, 140)
t.pendown()
t.begin_fill()
circle(5)
t.color('blue')
t.end_fill()
t.color('black')
t.penup()
# left eye
t.goto(-55, 140)
t.pendown()
t.begin_fill()
circle(5)
t.color('blue')
t.end_fill()
t.color('black')
t.penup()
# nose
t.goto(0, 120)
t.pendown()
t.width(5)
t.right(90)
t.forward(20)
t.penup()
# smile
t.goto(65, 90)
t.color('red')
t.pendown()
circle(12, arc='Yes')

