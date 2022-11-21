from turtle import *

tuktuk = Turtle()

tuktuk.shape("turtle")
tuktuk.color("blue")

def rectangle():
    tuktuk.forward(100)
    tuktuk.left(90)


for _ in range(4):
    rectangle()


t = Turtle()

def dashLine():
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

for _ in range(15):
    dashLine()


screen = Screen()
screen.exitonclick()