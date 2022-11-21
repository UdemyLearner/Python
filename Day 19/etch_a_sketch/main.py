import turtle as t
tuktuk = t.Turtle()
screen = t.Screen()


def move_forward():
    tuktuk.forward(10)


def move_backward():
    tuktuk.backward(10)


def turn_right():
    # new_heading = tuktuk.heading() - 10
    # tuktuk.heading(new_heading)
    tuktuk.right(10)


def turn_left():
    tuktuk.left(10)

def clear():
    tuktuk.clear()
    tuktuk.penup()
    tuktuk.home()
    tuktuk.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
