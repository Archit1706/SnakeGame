from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.create_border()

    def create_border(self):
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-300, 300)
        self.color("saddle brown")
        self.pensize(20)
        self.pendown()
        for _ in range(4):
            self.forward(600)
            self.right(90)
