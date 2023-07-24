import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 287)
        self.hideturtle()
        self.update_score(self.score)

    def update_score(self, score):
        self.clear()
        self.write(f"score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score(self.score)

    def increase_score(self, score):
        self.score += 1
        self.update_score(self.score)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
