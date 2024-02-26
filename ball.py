from turtle import Turtle
import random

MOVEMENT_SPEED = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("White")
        self.bounces = 0
        self.x_move = MOVEMENT_SPEED
        self.y_move = MOVEMENT_SPEED

    def move(self):
        print(self.bounces)
        print(self.x_move)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.bounces += 1
        new_speed = MOVEMENT_SPEED + (self.bounces * 2)
        if self.x_move > 0:
            print("ok")
            self.x_move = -new_speed
        else:
            self.x_move = new_speed

    def reset_position(self):
        random_y = random.randint(-160, 160)
        self.goto(0, random_y)
        self.bounces = 0
        if self.x_move > 0:
            self.x_move = -MOVEMENT_SPEED
        else:
            self.x_move = MOVEMENT_SPEED
