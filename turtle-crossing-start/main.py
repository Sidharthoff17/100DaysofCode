import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
player_turtle.setheading(90)

screen.listen()
screen.onkey(player_turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player_turtle.ycor() > FINISH_LINE_Y:
        player_turtle.reset_position()
        scoreboard.update_level()
        car_manager.increase_speed()
screen.exitonclick()