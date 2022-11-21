import turtle as t

tuktuk = t.Turtle()
screen = t.Screen()

def move_forward():
    tuktuk.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()