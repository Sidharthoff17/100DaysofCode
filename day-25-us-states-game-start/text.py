from turtle import Turtle

class Text(Turtle):
    def __init__(self, text:str, x_cor:int, y_cor: int):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.text = text
        self.x_cor= x_cor
        self.y_cor = y_cor
        self.display()

    def display(self):
        self.goto(self.x_cor, self.y_cor)
        self.write(self.text, align="center", font=("Courier", 15, "normal"))


