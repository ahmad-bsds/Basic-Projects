from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.x = random.randint(-230, 230)
        self.y = random.randint(-180, 150)
        self.food()

    def food(self):
        self.shape('circle')
        self.pensize(0)
        self.pencolor('green')
        self.fillcolor('green')
        self.penup()
        self.goto(x=self.x, y=self.y)

    def refresh(self):
        x = random.randint(-230, 230)
        y = random.randint(-180, 180)
        self.hideturtle()
        self.goto(x=x, y=y)
        self.showturtle()
        # Hide and show turtle because , food animation shows without it(hide/show), every time it goes from one to
        # another place.
