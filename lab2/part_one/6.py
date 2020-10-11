import turtle

turtle.shape('turtle')

def do_spider():
    for i in range(12):
        turtle.forward(50)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(50)
        turtle.left(180)
        turtle.right(360/12)

do_spider()