from turtle import *
from math import sqrt
def draw_hexagram(d):
    penup()
    setposition(-1.5 * d, d * sqrt(3) / 2)
    pendown()
    color('red')
    for i in range(3):
        forward(d)
        penup()
        forward(d)
        pendown()
        forward(d)
        right(120)
    penup()
    setposition(0, d * sqrt(3))
    right(60)
    pendown()
    color('blue')
    for i in range(3):
        forward(d)
        penup()
        forward(d)
        pendown()
        forward(d)
        right(120)




if __name__ == '__main__':
    speed(5)
    draw_hexagram(100)
    done()
