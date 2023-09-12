from turtle import Turtle
import random


class Snake(Turtle):
    start_positions = [(0, 0), (-20, 0), (-40, 0)]
    pace = 20
    direction_right = 0
    direction_up = 90
    direction_left = 180
    direction_down = 270

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in self.start_positions:
            self.add_segment(position)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            if segment == 0:
                continue
            position = self.segments[segment - 1].position()
            self.segments[segment].goto(position)
        self.segments[0].forward(self.pace)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color(random.randint(50, 250), random.randint(50, 250), random.randint(50, 250))
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != self.direction_down:
            self.segments[0].setheading(self.direction_up)

    def down(self):
        if self.segments[0].heading() != self.direction_up:
            self.segments[0].setheading(self.direction_down)

    def right(self):
        if self.segments[0].heading() != self.direction_left:
            self.segments[0].setheading(self.direction_right)

    def left(self):
        if self.segments[0].heading() != self.direction_right:
            self.segments[0].setheading(self.direction_left)
