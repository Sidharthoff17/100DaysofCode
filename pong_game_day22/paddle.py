from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position: tuple[int,int]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.penup()
        self.goto(position[0],position[1])

    def go_up(self):

        new_y = self.ycor() + 20
        if new_y > 260:
            new_y = 260


        self.goto(self.xcor(), new_y)


    def go_down(self):

        new_y = self.ycor() - 20
        if new_y < -260:
            new_y = -260
        self.goto(self.xcor(), new_y)


