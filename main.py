from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong by TahaLearns")
screen.tracer(0)

r_position = (350,0)
l_position = (-350,0)

r_paddle = Paddle(r_position)
l_paddle = Paddle(l_position)

ball = Ball()

game_is_on = True

screen.listen()
# Movement of the Right Paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Movement of the Left Paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    # Ball Movement
    ball.move()


screen.exitonclick()