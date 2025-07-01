from turtle import Turtle, Screen
import heroes
import random
t = Turtle()
t.shape("arrow")


colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]

"""Draw shapes from side number 3 to 10"""
# for i in list(range(3,11)):
#     t.color(random.choice(colours))
#     for _ in range(i):
#         t.forward(100)
#         t.right(360/i)

directions = [0,90,180,270]
t.pensize(15)
t.speed("fastest")

for _ in range(200):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
