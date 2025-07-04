from turtle import Turtle, Screen
from paddle import Paddle
import time


screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME:")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))



screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_commence = True
while game_commence:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()