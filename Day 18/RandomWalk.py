import turtle as t
import random
tuktuk = t.Turtle()
t.colormode(255)
t.bgcolor("black")
tuktuk.speed("fastest")
direction = [0,270,180,90]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_col = (r,g,b)
    return random_col




for _ in range(200):
    tuktuk.color(random_colour())
    tuktuk.pensize(10)
    tuktuk.forward(22)
    tuktuk.setheading(random.choice(direction))
    
    

    
    
screen = t.Screen()
screen.exitonclick()