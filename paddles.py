from turtle import Turtle

MOVEMENT_SPEED = 20


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xcor, ycor)
        self.showturtle()

    def up_movement(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def down_movement(self):
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)
