from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_count = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level_count}", align="center", font=FONT)

    def update_level(self):
        self.level_count += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


