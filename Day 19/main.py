import random
import turtle as t


screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="make your bet ",
                            prompt="which turtle will win the race?")
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []
colour = ["red", "yellow", "green", "blue", "orange", "purple"]
for _ in range(0, 6):
    tuktuk = t.Turtle(shape="turtle")
    tuktuk.color(colour[_])
    tuktuk.penup()
    tuktuk.goto(x=-230, y=y_pos[_])
    all_turtles.append(tuktuk)

if user_bet:
    is_race_on = True
while is_race_on:
    for tuktuk in all_turtles:
        if tuktuk.xcor() > 210:
            is_race_on = False
            wining_color = tuktuk.pencolor()
            if wining_color == user_bet:
                print(f"you won, {wining_color} is the winner")
            else:
                print(f"you lost, {wining_color} is the winner")
        rand_dist = random.randint(3, 10)
        tuktuk.forward(rand_dist)


screen.exitonclick()
