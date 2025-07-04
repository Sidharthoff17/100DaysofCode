from turtle import Turtle, Screen
import csv
import pandas as pd
from text import Text

data = pd.read_csv("50_states.csv")
data_dict = data.to_dict()

states = data_dict["state"]
x_coordinate = data_dict["x"]
y_coordinate = data_dict["y"]



# setting the background image to the US map

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(width=800, height=600)
screen.title("USA States Game:")
screen.tracer(0)

#read through the csv file

counter = 0
score = 0

guessed_states = []

while counter < 50:
    screen.update()
    guess = screen.textinput(f"{str(score)}/50 states correct", "Enter a state:").lower()
    for key, state in states.items():
        if (guess == state.lower()) and (guess not in guessed_states):
            guessed_states.append(guess)
            display_state = Text(state, x_coordinate[key], y_coordinate[key])
            score += 1

    counter += 1
final_score = Text(f"FINAL SCORE: {str(score)}/50", 0, 250)

screen.exitonclick()