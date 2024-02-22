from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong by TahaLearns")

def go_up():
    print("Up")
def go_down():
    print("Down")

paddle = Turtle()
paddle.color("white")
paddle.shape('square')
paddle.penup()
paddle.shapesize(5,1)
paddle.goto(350, 0)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

screen.exitonclick()