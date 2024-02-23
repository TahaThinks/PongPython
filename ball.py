from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.__init_subclass__()
        self.shape('ball')
        self.color('white')
