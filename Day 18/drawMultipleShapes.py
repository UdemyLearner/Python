from turtle import Turtle as t ,Screen
import random

tuktuk = t()

colours = ["medium blue","magenta","light sea green","spring green","maroon","dark violet"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle  = 360/num_sides
        tuktuk.forward(100)
        tuktuk.right(angle)


for _ in range(3,11):
    tuktuk.color(random.choice(colours))
    draw_shape(_)
