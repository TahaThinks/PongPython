from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

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
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
# Movement of the Right Paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Movement of the Left Paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Ball Movement
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        print("Made Contact to Right Paddle")
        ball.bounce_x()
    # Detect Collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made Contacnt to Left Paddle")
        ball.bounce_x()

    # Detect if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point() 

    # Detect if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point() 


screen.exitonclick()

