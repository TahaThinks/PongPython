from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong by TahaLearns")
screen.tracer(0)

r_position = (350,0)
l_position = (-350,0)

r_paddle = Paddle(r_position)
l_paddle = Paddle(l_position)

game_is_on = True

while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")


screen.exitonclick()