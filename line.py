from turtle import Turtle

LINE_WIDTH = 5
LINE_LENGTH = 10
LINE_GAP = 10
PEN_COLOUR = "White"


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(LINE_WIDTH)
        self.pencolor(PEN_COLOUR)
        self.speed(0)

    def draw_line(self):
        self.goto(0, 300)
        while self.ycor() > -280:
            self.setheading(270)
            self.forward(LINE_GAP)
            self.pendown()
            self.forward(LINE_LENGTH)
            self.penup()
