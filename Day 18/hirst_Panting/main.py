import random
import turtle as t

tuktuk = t.Turtle()
t.colormode(255)
tuktuk.speed("fastest")
tuktuk.penup()
tuktuk.hideturtle()

var = [(239, 230, 221), (230, 154, 83), (120, 171, 202), (39, 111, 159), (240, 199, 80), (160, 59, 84), (199, 83, 111),
       (215, 133, 160), (23, 137, 102), (223, 83, 61), (119, 189, 154), (156, 164, 49), (188, 212, 222),
       (244, 156, 174), (230, 197, 214), (47, 171, 134), (29, 164, 195), (197, 220, 211), (160, 74, 53), (9, 102, 78),
       (242, 164, 153), (115, 43, 56), (108, 115, 171), (151, 214, 194), (148, 208, 225), (19, 14, 13), (178, 181, 215),
       (43, 62, 99), (101, 48, 47), (32, 62, 78)]

tuktuk.setheading(225)
tuktuk.forward(250)
tuktuk.setheading(0)

no_of_dots = 100
for _ in range(1, no_of_dots + 1):
    tuktuk.dot(20, random.choice(var))
    tuktuk.forward(50)

    if _ % 10 == 0:
        tuktuk.setheading(90)
        tuktuk.forward(50)
        tuktuk.setheading(180)
        tuktuk.forward(500)
        tuktuk.setheading(0)



screen = t.Screen()
screen.exitonclick()

""" Colour Extracted From the .jpeg File And Stored in var variable above """
# import colorgram
#
# rgb_colours = []
#
# colors = colorgram.extract("a.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)
