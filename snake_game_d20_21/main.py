from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME:")

starting_positions = [(0,0), (-20,0),(-40,0)]

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)

screen.exitonclick()