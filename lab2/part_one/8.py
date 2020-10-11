import turtle

step = 5
d_adder = 3
t = turtle.Turtle()
t.shape('turtle')


for i in range(40):
    t.forward(step)
    t.left(90)
    step += d_adder
