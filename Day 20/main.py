from turtle import Screen , Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]
segments = []
for i in range(0,3):
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(-20*i,0)
    segments.append(snake_body)
    

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)




screen.exitonclick()