from turtle import Screen, Turtle
from Day20Snake import Snake
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')


snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, key='Down')
screen.onkey(snake.left, key='Left')
screen.onkey(snake.right, key='Right')



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()









screen.exitonclick()