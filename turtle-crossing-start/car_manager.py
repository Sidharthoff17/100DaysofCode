from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid= 1, stretch_len= 2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.set_start_position()

    def set_start_position(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_chance = 10


    def create_car(self):
        #create a car 1/6th of the time
        number = random.randint(1,self.spawn_chance)
        if number == 1:
            new_car = Car()
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

        if self.spawn_chance > 1:
            self.spawn_chance -= 1
