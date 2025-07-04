from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import time


screen = Screen()
ball = Ball()
score_board = Scoreboard()
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
    time.sleep(0.0001)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.move()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.move()

    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_score()



screen.exitonclick()