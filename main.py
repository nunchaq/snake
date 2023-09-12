from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.random_location()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() < -290 or \
            snake.segments[0].xcor() > 280 or \
            snake.segments[0].ycor() < -290 or \
            snake.segments[0].ycor() > 280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]: # wszystko z listy bez pierwszego
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
