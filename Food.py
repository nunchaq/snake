from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # zmniejszamy o polowe
        self.speed("fastest")
        self.random_location()  # wymiary ekranu 600 x 600

    def random_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
