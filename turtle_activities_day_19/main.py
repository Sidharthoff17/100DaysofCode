from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Bet:", "What turtle do you bet to win the race?:")

race_on = False
colours = ["red", "blue", "green", "yellow", "orange", "purple"]
turtles = []

for i in range(6):
    tim = Turtle("turtle")
    tim.color(colours[i])
    tim.penup()
    tim.goto(x=-230, y=-100 + i * 40)
    turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for turtle_x in turtles:
        if turtle_x.xcor()>230:
            race_on = False
            #get winning colour
            winning_colour = turtle_x.pencolor()
            if winning_colour == user_bet.lower():
                print(f"You won! The {winning_colour} turtle is the race winner!")
            else:
                print(f"You lost! The {winning_colour} turtle is the race winner!")


        turtle_x.forward(random.randint(0,10))



screen.exitonclick()