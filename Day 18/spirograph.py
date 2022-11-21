import turtle as t
import random

tuktuk = t.Turtle()
tuktuk.speed("fastest")


t.colormode(255)
t.bgcolor("black")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tuktuk.color(random_color())
        tuktuk.circle(100)
        tuktuk.setheading(tuktuk.heading() + size_of_gap)
                          
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

