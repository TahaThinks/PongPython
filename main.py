from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong by TahaLearns")


paddle = Turtle()
paddle.color("white")
paddle.shape('square')
paddle.penup()
paddle.shapesize(5,1)
paddle.goto(350, 0)



screen.exitonclick()