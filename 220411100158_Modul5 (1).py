import turtle

pen=turtle.Turtle()
window=turtle.Screen()

def fraktal(panjang, level):
    if level ==0:
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(180)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.end_fill()
    else:
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(180)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(180)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang)
        pen.right(90)
        pen.forward(panjang/2)
        pen.right(90)
        pen.up()
        pen.end_fill()
        pen.forward(panjang/4)
        pen.right(90)
        pen.down()
        pen.forward(panjang/4)
        pen.right(180)

        fraktal(panjang/2, level-1)


fraktal(500,3)