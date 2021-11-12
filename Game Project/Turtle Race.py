import turtle
import random
from random import randint
from turtle import *

speed(0)
penup()
goto(-140, 140)

for i in range(0,16):
    turtle.write(i, align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()
for turn in range(100):
    ada.forward(randint(1,5))

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()
for turn in range(100):
    bob.forward(randint(1,5))

woo = Turtle()
woo.color('green')
woo.shape('turtle')
woo.penup()
woo.goto(-160, 40)
woo.pendown()
for turn in range(100):
    woo.forward(randint(1,5))

yee = Turtle()
yee.color('yellow')
yee.shape('turtle')
yee.penup()
yee.goto(-160, 10)
yee.pendown()
for turn in range(100):
    yee.forward(randint(1,5))

turtle.done()