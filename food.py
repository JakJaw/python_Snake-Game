from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomx = random.randint(-260, 260)
        randomy = random.randint(-260, 260)
        self.goto(randomx, randomy)
