import turtle

t = turtle.Turtle()


def move(pen, dx, dy):
    if pen == 'draw':
        t.pendown()
    elif pen == 'jump':
        t.penup()
    x, y = t.pos()
    t.goto(x + dx, y + dy)


def do_digit(movements: list):
    for movement in movements:
        act, dX, dY = movement
        move(act, dX, dY)


ZERO = [('draw', 0, 80), ('draw', 40, 0), ('draw', 0, -80), ('draw', -40, 0), ('jump', 60, 0)]
ONE = [('jump', 0, 40), ('draw', 40, 40), ('draw', 0, -80), ('jump', 20, 0)]
FOUR = [('jump', 0, 80), ('draw', 0, -40), ('draw', 40, 0), ('draw', 0, 40), ('draw', 0, -80), ('jump', 20, 0)]
SEVEN = [('draw', 0, 40), ('draw', 40, 40), ('draw', -40, 0), ('jump', 60, -80)]

digits = [ONE, FOUR, ONE, SEVEN, ZERO, ZERO]

t.penup()
t.backward(300)
t.pendown()

for digit in digits:
    do_digit(digit)

turtle.done()
