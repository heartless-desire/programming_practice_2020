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
        act, dX, dY = movement.split()
        move(act, int(dX), int(dY))


t.penup()
t.backward(300)
t.pendown()

inp = open('input.txt', 'r')

for digit in inp:
    do_digit(digit.split(','))

inp.close()
turtle.done()
