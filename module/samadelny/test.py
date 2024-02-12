# from mod import *
#
# print(ariif(10))
#
# print(num(2))
#
# print(i(10, 15))
#
# print(p(0, 10))
#
# print(k(10, 10))
import turtle

t = turtle.Turtle()


t.shape("turtle")
t.color("red")
t.pensize(2)


t.begin_fill()
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()
